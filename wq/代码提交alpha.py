from main import *

import time
import requests
from requests.exceptions import RequestException

def submit_alpha(alpha_id: str):
    """
    提交 alpha，一直重试到成功或遇到不可恢复错误。
    所有 logger 已移除，仅用 print 做最小输出。
    """
    s = login()
    TOTAL_RETRY_COUNT = 100_000
    retry_count = 0

    while retry_count < TOTAL_RETRY_COUNT:
        try:
            url = f"https://api.worldquantbrain.com/alphas/{alpha_id}/submit"
            res = s.post(url)

            # 400 特殊处理：认为已提交过
            if res.status_code == 400 and "The plain HTTP request was sent to HTTPS port" in res.text:
                print("提交中...")
                res.headers["Retry-After"] = "1.0"

            # 轮询 retry-after
            while "retry-after" in res.headers:
                sleep_time = max(float(res.headers["Retry-After"]), 3)
                time.sleep(sleep_time)
                print(".", end="", flush=True)
                res = s.get(url)

            print(f"[{alpha_id}] submit response {res.status_code} {res.text[:200]}")

            # 各类状态码处理
            if res.status_code == 429:
                print("触发限流，sleep 60s")
                time.sleep(60)
                retry_count += 1
                continue

            if res.status_code == 401:
                print("401 未授权，重新登录")
                s = login()
                retry_count += 1
                continue

            if res.status_code == 404:
                print("404 超时，重试")
                retry_count += 1
                continue

            if res.status_code // 100 == 5:
                print("5xx 网关错误，5s 后重试")
                time.sleep(5)
                retry_count += 1
                continue

            if res.status_code == 403:
                print(f"{alpha_id} 提交失败：403")
                fail_checks = []
                try:
                    checks = res.json()["is"]["checks"]
                    fail_checks = [c for c in checks if c.get("result") == "FAIL"]
                except Exception as e:
                    print("解析 fail_checks 异常:", e)

                print("fail_checks=", fail_checks)
                if any(c["name"] in {"REGULAR_SUBMISSION", "SUPER_SUBMISSION"} for c in fail_checks):
                    print("SUBMISSION 超过限制，退出")
                return

            if res.status_code == 200:
                print(f"{alpha_id} 提交成功")
                return 200

            if res.status_code // 100 != 2:
                print(f"submit alpha 非 2xx {alpha_id} {res}")
                return

            return

        except RequestException as e:
            print(f"RequestException {alpha_id} retry={retry_count} {e}")
            retry_count += 1
            time.sleep(10)
            continue

        except Exception as e:
            print(f"Exception {alpha_id} {e}")
            return

submit_alpha("leOQrNR2")

