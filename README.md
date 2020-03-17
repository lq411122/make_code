# make_code
url转二维码。前后端不分离。
python + web + qrcode + pillow + pyinstaller
打包步骤：
1. 项目根目录：pyinstaller -F -w code.py。（code.py为项目入口.py文件）生成build,dist,code.spec三个文件。
2. 将项目依赖的static,templates文件复制到exe文件所在的dist文件夹下。
3. 进入dist目录，执行start code.exe或./code.exe，启动程序。
4. 可能的报错：
  1. 缺少项目依赖包。将报名添加在code.spec中hiddenimports=[]
  2. exe添加图标。准备.ico格式图片，添加在code.spec中icon="路径"
  3. 找不到包的。在code.spec的pathex=["项目使用的虚拟环境存放安装包的绝对路径"]
  4. 项目其他.py文件添加到code.spec的Analysis(["code.py", "xx.py"],,,)
5. 修改完code.spec文件后在项目目录执行：pyinstaller -F -y code.spec
