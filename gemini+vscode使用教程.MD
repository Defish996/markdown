# VSCode + Gemini 3 Pro！绝配！整理了 4 种官方使用姿势（建议收藏）

原创 小4子 

[前端开发爱好者](javascript:void(0);)

 *2025年11月24日 08:33* *江苏*

从 **VSCode** 到 **3D** 场景，一行命令让 **AI** 替你干活

**谷歌**憋了个大招：**Gemini 3 Pro** 一上线就横扫各大榜单，连马斯克都点赞。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/kzFgl6ibibNKqRDTUhSKohsPrWoQicRGepWoKtWAuXpjibzpSCDrwbfbA1BPENGqI3YEmJjN0ILq8kA3kvcHNtO3NA/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

模型再强，用不起来也是白搭。

我把官方渠道全部实测一遍，挑出 **4** 个`最顺手`、`最实用`、最`不需要折腾`的入口。

如果你是开发者，建议直接上车 **Google Antigravity**！因为它完全就是 **VSCode** + **Gemini 3 Pro** + **Claude4** 的结合体，简直无敌！并且**免费**！

**非开发者**建议尝试剩下的**三种**方式！

## **前置条件：30 秒搞定“地区限制”**

- `kexue`上网，**建议挂漂亮国节点**（日本/新加坡偶尔能通，香港节点一律不行）

- 开 **Tun 模式**（全局代理），让谷歌域名全部走代理；浏览器开无痕，避免缓存翻车

- 还是提示`“not available in your country”？`

  **浏览器打开**：`https://policies.google.com/country-association-form`,检查账号关联地区是否是美国

  ![图片](https://cdn.jsdelivr.net/gh/Defish996/Picture-bed@main/202511260938987.webp)

  如果是 **香港**或者**其他不可用地区**，建议修改

![图片](https://cdn.jsdelivr.net/gh/Defish996/Picture-bed@main/202511260938990.webp)

把账号归属改成**美国** → **提交** → **等邮件**（平均 2 小时，最长 24 小时），通过之后**所有谷歌 AI 产品一路绿灯**

## **1️⃣ Google Antigravity（首推 · 开发者专用）**

#### ***\*VSCode\** + \**Gemini 3 Pro\** = \**无敌！\****

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/kzFgl6ibibNKqRDTUhSKohsPrWoQicRGepWlzj7zEvkxyCLtwW92toBbv5jvXLZgHGxt9REMDPPSRwQF3b5KAt24g/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

**一句话**：基于 **VSCode** 源码改的 `AI IDE`，内置 `Gemini 3 Pro/Claude 4.5`，前端/全栈开发效率 `×10`

### **为什么放在第一**

- 原生 `VSCode` 键盘映射、`插件市场`、`调试面板`，零学习成本
- 多 `Agent` 并发：一个写前端、一个写后端、一个跑测试，自动合并 PR 感
- 限时免费，速率用完还能切到自带 `Gemini 3 Pro` 120 次/天备用额度

### **3 步开玩**

- 浏览器访问 `https://antigravity.google` → `下载` → 用改好地区的`谷歌账号登录`
- 新建 `Workspace` → 选「Empty」或「React/Next/Vite」模板
- 右侧输入框直接扔需求：

```
 用 Next15 + TypeScript + Tailwind 做一张待办清单页，支持增删改查，数据用 localStorage，再写个测试用例
```

回车 → 看 **Agents** 自动拆 **Task**，左边代码实时生成，终端自动 `npm run dev` 给你跑起来

## **2️⃣ Gemini CLI（终端党的浪漫）**

![图片](https://cdn.jsdelivr.net/gh/Defish996/Picture-bed@main/202511260938984.webp)

**一句话**：不用离开命令行，就能让 `Gemini 3 Pro` 读代码、写脚本、跑 Shell

### **安装 & 登录**

```
# Node≥18 即可
npm i -g @google/gemini-cli
gemini auth          # 回车自动打开浏览器授权
```

### **常用姿势**

```
# 1. 直接对话
gemini chat "用 bash 写一段备份脚本，保留最近 7 天"

# 2. 读整个项目
gemini read ./src --summary

# 3. 边写边跑
gemini shell "找出当前目录下最大的 5 个文件并删除"
# 它会先给你看脚本，确认后自动执行

# 4. 连 MCP 服务器（内部工具）
gemini mcp --server http://localhost:9000 --prompt "把昨天的订单报表发邮件给老板"
```

### **额度 & 权限**

- **Ultra** 订阅默认开，**Pro/免费用户**填表（地址见文末）基本秒过
- 命令行里 `gemini config set model gemini-3-pro` 锁定模型，避免回落

## **3️⃣ Google AI Studio（百宝箱 · 免费不限次）**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/kzFgl6ibibNKqRDTUhSKohsPrWoQicRGepWER3Tpv1uXK0TTLbeWibmsOvQ1aryfbQjrbVeGKk8krXruqAnHiaEicMfQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

**一句话**：官方指定“游乐场”，**100** 万 **tokens** 随便玩，适合读论文、写长文、批处理

### **核心亮点**

- 上传 `1G` 视频、`500` 页 `PDF` 照样聊，不压缩
- 右侧`「Build」`模式：一句话生成可分享的小 `Web App`，支持嵌入 `Notion`、`Confluence`
- 温度、`Top-P`、`Thinking Level` 滑杆随便调，想保守想脑洞都行

### **快速上手指南**

- 访问 `https://aistudio.google.com` → 新建 `Project` → 模型选 `Gemini 3 Pro`
- 把需求直接粘进去：

```
 帮我把这份 2025 年 React 官方文档提炼成中文思维导图，输出成 markdown
```

- 点**「Build」**→ 选择「**Mindmap**」模板 → `30` 秒拿到可交互网页，链接甩群里

### **注意**

- 默认谷歌会用你的数据训模型，**敏感代码/隐私文件先关 Data 保存开关**
- 免费层暂无 **API** 额度，想调接口得绑卡（文末价格表）

## **4️⃣ Gemini 应用（手机 & 网页 · 5 次/天应急）**

![图片](https://cdn.jsdelivr.net/gh/Defish996/Picture-bed@main/202511260938460.webp)

**一句话**：每天免费 `5` 次，地铁里拍花识图、问菜谱够用，重度用户去前面三个渠道

### **打开方式**

- 网页：`https://gemini.google.com`（已全量 3 Pro）
- 手机：应用商店更新 `Gemini App` → 左上角确认模型显示**「Gemini 3 Pro」**

## **所有链接 3 秒收藏**

- **Google Antigravity**：`https://antigravity.google`
- **Gemini CLI 权限申请**：`https://docs.google.com/forms/d/e/1FAIpQLScQBMmnXxIYDnZhPtTP3xr5IwHNzKW4nLomuQ1tGOO-UldMdQ/viewform`
- **Google AI Studio**：`https://aistudio.google.com`
- **Gemini 网页版**：`https://gemini.google.com`
- **账号地区修改**：`https://policies.google.com/country-association-form`

开发者的时间应该花在创意，而不是复制粘贴。

**Gemini 3 Pro** 已经替你写好 `90%` 的代码，剩下 `10%`，你只管改变世界。