# WeChat_Article    
爬取微信公众号文章    

> Bilibili视频演示：https://www.bilibili.com/video/BV1vN411D7Y3/

**注意，除非你要断点续传，否则删除目录下conf.ini和url.json再启动！！！！**

![image](https://user-images.githubusercontent.com/31002981/217465357-d0737b23-55ec-47d3-b12c-ee8973a04291.png)

## macOS使用方法：

### 1 使用EditThisCookie导出cookie

Chrome插件安装链接
https://chrome.google.com/webstore/detail/edit-this-cookie/fngmhnnpilhplaeedifhccceomclgfbg/reviews

Edge浏览器可以搜同名插件：EditThisCookie

### 2 获取token

进入微信公众号后台网页，打开Chrome浏览器控制台，勾选网络（Network），勾选Fetch/XHR，随便点击一个请求，点击载荷（Payload），里面就有`token: 829****43`参数，这个数字就是下一步需要的。

### 3 根目录新建cookie.json文件，内容示例如下：

```
[
  {
    "COOKIES": [
      {
        "domain": ".qq.com",
        "expirationDate": 1727226754,
        "hostOnly": false,
        "httpOnly": false,
        "name": "_clck",
        "path": "/",
        "sameSite": "unspecified",
        "secure": false,
        "session": false,
        "storeId": "0",
        "value": "12334441212|1|ffc|0",
        "id": 1
      },
      // 这里省略若干行
      {
        "domain": "mp.weixin.qq.com",
        "expirationDate": 1730207739.668822,
        "hostOnly": true,
        "httpOnly": true,
        "name": "xid",
        "path": "/",
        "sameSite": "unspecified",
        "secure": true,
        "session": false,
        "storeId": "0",
        "value": "8f43a3ae8f1e8abcdedd62645ec461c1",
        "id": 18
      }
    ],
    "TOKEN": "829****43"
  }
]
```

COOKIES冒号后面的就是EditThisCookie插件导出的cookie

### 4 安装依赖并运行项目

```bash
# 创建虚拟环境（仅首次）
python3 -m venv venv
# 进入虚拟环境（运行python3 main.py前执行一次即可）
source venv/bin/activate
# 安装依赖（仅首次）
pip install -r requirements.txt
# 运行项目
python3 main.py
```

如果出现了这个错误：Tkinter is required for pymsgbox 就使用homebrew安装python-tk：

```
brew install python-tk
```



## Windows使用方法：     

1、下载并解压[**Chrome.rar**](https://sxf1024.lanzouo.com/iJ2Rp0mwy50j)；    
2、运行**main.exe**；    
3、填入信息，点击“**启动**”即可。    
4、如果想修改UI，可以安装这个：[Qt Designer](https://build-system.fman.io/qt-designer-download)    
****************************************************************************************************    

## 背景知识:     
使用公众号写文章时支持搜索其他公众号的文章的方式，来实现爬取指定公众号所有文章的目的。    
****************************************************************************************************    

## 程序原理:     
通过selenium登录获取token和cookie，再自动爬取和下载   
* 使用前提：   
1、申请一个免费的微信公众号，个人订阅号即可(https://mp.weixin.qq.com)      
****************************************************************************************************    

## 更新记录：
1. 下载文章文字内容到txt
2. 下载文章图片
3. 保存HTML文件，并将图片链接指向本地  
4. 添加按时间范围下载  
5. 添加cookie登陆，不成功才selenium浏览器登陆  
6. 增加记住密码功能  
7. 修复一些问题，如requests卡死  
8. 添加按关键词下载  
9. 多线程优化下载速度  
10. 增加断点续传功能（可能存在bug，推荐不要用）  
11. 拟增加备用公众号功能（暂未完成）  
12. 下载PDF格式
13. 不需要再手动下载Chrome，启动时会自动下载    
**************************************************************************************************** 

## 使用说明：
创建虚拟环境
```bash
conda create -n wechat python=3.9 -y
```

进入虚拟环境
```bash
conda activate wechat
```

安装三方库
```bash
pip install -r requirements.txt
```
> 对于mac用户，安装pyqt5可能会报错，可以尝试：
> ```bash
> brew install pyqt@5
> cp -r   /opt/homebrew/Cellar/pyqt@5/5.15.7_2/lib/python3.9/site-packages/*   /Users/songxf/miniconda3/envs/wechat/lib/python3.9/site-packages/   
> ```
> 然后就可以导入了：
> ```bash
> import PyQt5
> ```

运行脚本
```bash
python main.py
```

打包exe(生成在dist下)
```bash
pyinstaller -F -w -i icon.ico main.py
```


## 其他说明：
- 爬取间隔太快，容易遇到“**访问频繁**”或“**freq_control**”，这时候可以删除**cookie.json**，再重新运行软件，**换个号**继续运行；
- Qt打包完实在是太大了，有大佬会转成Tkinter吗？


欢迎关注微信公众号：xfxuezhang

---
## 打赏    
如果这个项目帮助到了你，欢迎请我喝杯阔落👏🏻    
![yf](yf.png)

