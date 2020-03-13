# -*- coding:utf-8 -*-


# 知识点：二维码生成，图片合成，图片处理，web前后端交互
import sys
import web
import qrcode
import PIL.Image as Image
import time


# 生成二维码函数，传入信息参数
def qc(info):
    # 创建qrcode对象
    qr = qrcode.QRCode(
        version=1,   # version为一个整数，范围1~40，作用表示二维码的大小
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        # error_correction容错率，挡出部分二维码还能识别，越高可以挡住部分越多，但数据量增加.四个等级：H,L,M,Q  Q最高，可以挡住25%
        box_size=10,  # box_size 每个格子里像素大小
        border=4,  # border 表示二维码距离图像外边框的距离
        )
    qr.add_data(info['url'])
    img = qr.make_image()  # 创建二维码图片
    img = img.convert("RGBA")  # 图片转换为RGBA格式
    img_w, img_h = img.size  # 返回二维码图片的大小
    logo = Image.open("static/images/logo.jpg")  # 打开logo
    logo_w = int(img_w/4)
    logo_h = int(img_h/4)
    logo = logo.resize((logo_w,logo_h), Image.ANTIALIAS)  # 改变大小,抗锯齿
    w = int((img_w-logo_w)/2)
    h = int((img_h-logo_h)/2)
    img.paste(logo, (w, h))
    path = "static/qrcode/%s.png" %time.time()
    img.save(path)  # 保存图片
    return path


urls = ('/', 'Index',)  # '/'为路径，index为类名

render = web.template.render('templates')  # 读取文件夹下的html代码


class Index:  # 页面处理类
    def GET(self):
        return render.index()

    def POST(self):  # 返回二维码图片地址
        i=web.input()  # 获取用户请求的参数和值
        return qc(i)


if __name__ == '__main__':
    # globals 函数返回一个全局变量的字典，包括所有导入的变量。
    web.application(urls,globals()).run()