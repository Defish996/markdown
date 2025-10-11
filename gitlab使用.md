gitlab使用

## gitlab使用

环境准备,推荐使用wsl的Ubuntu22.04

---



## wsl下载

### 配置电脑选项

使用前打开对应选项

![C__Users_1_AppData_Roaming_com.codexu.NoteGen_article__assets_355bcf13-e710-44be-9c38-0e6781305063.png](https://cdn.jsdelivr.net/gh/Defish996/Pictrue-bed@main/d30d4605-485d-464b-b154-f13a4ecb95a7.png)

勾选 适用于Linux的Windows子系统

然后进行重启电脑

### 下载wsl

管理员方式打开cmd

执行
wsl --install -d Ubuntu-24.04

#### 在此步可能出现的错误

1. 若提示
   C:\Users\1>wsl --install -d Ubuntu-24.04
   正在安装: Ubuntu 24.04 LTS
   安装过程中出现错误。分发名称: 'Ubuntu 24.04 LTS' 错误代码: 0x800704cf

该错误下，先看看Microsoft store能不能打开，能打开但是ubuntu下载失败需要先更新对应的Windows到最新版本

若Microsoft store打不开，则需要进行关闭代理，有可能出现网络错误，此时需要关闭代理即可（如：calsh）

若关闭代理还是不行，则需要从系统进行代理的关闭

如图：

![C__Users_1_AppData_Roaming_com.codexu.NoteGen_article__assets_e3c56d86-a67d-4897-ad23-f39c9bc1dd74.png](https://cdn.jsdelivr.net/gh/Defish996/Pictrue-bed@main/9b8db1b3-2078-4ea4-ae71-067f059b6d74.png)

在最后将代理服务器的对勾取消，此时便能正常访问Microsoft store，这时也能正常进行wsl的下载

需要在下载完成之后重新勾选代理服务器的选项，否则clash无法使用

## gitlab下载

直接运行

wget --content-disposition https://packages.gitlab.com/gitlab/gitlab-ce/packages/ubuntu/xenial/gitlab-ce_12.1.4-ce.0_amd64.deb/download.deb

等待下载完成即可

下载完成之后进行解压安装

sudo dpkg -i gitlab-ce_12.1.4-ce.0_amd64.deb

该过程释放压缩包的内存较大，需要的时间可能有点久，所以耐心等待

---
