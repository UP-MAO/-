#Tempconvert.py
Tempstr = input("请输入带有符号得温度数值:")
if Tempstr[-1]in ['F','f']:
    c = (eval(Tempstr[0:-1])-32)/1.8
    print("转换后的温度是{:.2f}c".format(c))
elif Tempstr[-1]in['C','c']:
    F=1.8*eval(Tempstr[0:-1])+32
    print("转换后的温度是{:.2f}C".format(C))
else:
    print("输入格式错误")
