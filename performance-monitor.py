#-*-coding:utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import winreg 


def get_GPU1TDPP_value():     
    key = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER,r"Software\FinalWire\AIDA64\SensorValues")
    while 1:
        va = winreg.QueryValueEx(key, 'Value.PGPU1TDPP')
        TDPP = int(va[0])
        return TDPP
        

def genTDPP(t=0): #设置xy变量
    x = 0              
    y = 1
    while 1:   
        y = get_GPU1TDPP_value() 
        x += 1
        yield  x,y


def init1():
    ax1.set_xlim(0, 100)                     #设置初始x轴 0-100
    ax1.set_ylim(0, 100)                     #设置y轴 0-100
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,


def updateTDPP(data):    # 更新数据
    t, y = data
    xdata.append(t)
    ydata.append(y)
    xmin, xmax = ax1.get_xlim()

    if t >= xmax:                       #表格随数据移动
        ax1.set_xlim(xmin+10, xmax+10)
        ax1.figure.canvas.draw()
    line.set_data(xdata, ydata)

    return line,


#fig1, ax = plt.subplots() #建立一个fig对象，建立一个axis对象
fig1 = plt.figure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None, frameon=True)
fig1.suptitle('performance-monitor')  #图标题

#--------------第一幅图开始--------------------
ax1 = fig1.add_subplot(2,2,1)  #设置为2*2中左上角的子图
line, = ax1.plot([], [], lw=2)              #线像素比
ax1.set(xlabel='time (s)', ylabel='percentage',title='GPU1TDPP')
ax1.grid()
xdata, ydata = [], []
#--------------第一幅图结束--------------------


#--------------第二幅图开始--------------------
ax2 = fig1.add_subplot(2,2,2)  #设置为2*2中右上角的子图
ax2.set(title='ADD WHAT YOU WANT')
#--------------第二幅图结束----------------------



ani = animation.FuncAnimation(fig1, updateTDPP, genTDPP, blit=False, interval=1000,repeat=False, init_func=init1)
plt.show()