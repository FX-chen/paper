#jpg2eps by fxc
#data : 20220607

import os

list = []
num = 0
path = os.getcwd()
for q in os.listdir(path):
    (name,extension) = os.path.splitext(path + "\\" + q)
    print(extension)
    if extension == ".jpg":
        cmd = "bmeps -c " + q + " " +name + ".eps"
        jpg2eps = os.system(cmd)
        print(name + " is ok")
        num = num + 1
    if extension == ".png":
        cmd = "bmeps -c " + q + " " +name + ".eps"
        jpg2eps = os.system(cmd)
        print(name + " is ok")
        num = num + 1
print("共生成了" + str(num) + "张图")
