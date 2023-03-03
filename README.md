

# 系统性能监控器

### 使用python绘制系统性能图像，从AIDA64获取数据

依赖

```
winreg
matplotlib
```

运行

```
python performance-monitor.py
```

#### 运行截图

![](https://github.com/iron0rca/performance-monitor/blob/master/image/1.jpg)

#### 必要设置

![](https://github.com/iron0rca/performance-monitor/blob/master/image/2.jpg)

打开aida64中将监测数据写入注册表
读取注册表中的数据并用matplotlib绘制图像
保持程序运行,即可实时监测系统性能
