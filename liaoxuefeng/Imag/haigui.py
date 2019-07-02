'''
在1966年，Seymour Papert和Wally Feurzig发明了一种专门给儿童学习编程的语言——LOGO语言，它的特色就是通过编程指挥一个小海龟（turtle）在屏幕上绘图。
海龟绘图（Turtle Graphics）后来被移植到各种高级语言中，Python内置了turtle库，基本上100%复制了原始的Turtle Graphics的所有功能。
我们来看一个指挥小海龟绘制一个长方形的简单代码：
'''
# 导入turtle包的所有内容：
# from turtle import *
#
# # 设置笔刷宽度：
# width(4)
#
# pencolor('yellow')      # 如果你不写默认颜色是黑色
# # 前进:
# forward(200)
# # 右转90度:
# right(90)
#
# # 笔刷颜色:
# pencolor('red')
# forward(100)
# right(90)
#
# pencolor('green')
# forward(200)
# right(90)
#
# pencolor('blue')
# forward(100)
# right(90)
#
# # 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
# done()
# 调用width()函数可以设置笔刷宽度，调用pencolor()函数可以设置颜色。更多操作请参考turtle库的说明。
# 绘图完成后，记得调用done()函数，让窗口进入消息循环，等待被关闭。否则，由于Python进程会立刻结束，将导致窗口被立刻关闭。

# turtle包本身只是一个绘图库，但是配合Python代码，就可以绘制各种复杂的图形。例如，通过循环绘制5个五角星：
# from turtle import *
#
# def drawStar(x, y):
#     pu()
#     goto(x, y)
#     pd()
#     pencolor('red')     # 设置笔刷颜色
#     width(15)           # 设置笔刷大小
#     # set heading:0
#     seth(0)
#     for i in range(5):
#         fd(40)
#         rt(144)
#
# for x in range(0, 300, 50):     # 300/50等于6个5角星
#     drawStar(x, 0)
#
# done()

# 使用递归，可以绘制出非常复杂的图形。例如，下面的代码可以绘制一棵分型树：
from turtle import *

# 设置色彩模式是RGB：
colormode(255)

lt(90)

lv = 14
l = 120
s = 45

width(lv)

# 初始化RGB颜色：
r = 0
g = 0
b = 0
pencolor(r, g, b)

penup()
bk(1)
pendown()
fd(1)

def draw_tree(l, level):
    global r, g, b
    # save the current pen width
    w = width()

    # narrow the pen width
    width(w * 3.0 / 4.0)
    # set color:
    r = r + 1
    g = g + 2
    b = b + 3
    pencolor(r % 200, g % 200, b % 200)

    l = 3.0 / 4.0 * 1
    lt(s)
    fd(1)

    if level < lv:
        draw_tree(1, level + 1)

    bk(1)
    rt(2 * s)
    fd(1)

    if level < lv:
        draw_tree(1, level + 1)
    bk(1)
    lt(s)

    # restore the previous pen width
    width(w)

speed('fastest')

draw_tree(1, 4)

done()
