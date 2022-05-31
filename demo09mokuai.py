
# 模块：导入：两种方式

# 1.全部导入 【import 模块名】
# import hanshu
#
# print(hanshu.add(15,15))

# 2.【from 模块名 import 成员名】，
from  hanshu import add

print(add(1,5,4))


import os      #os模块
print(os.listdir())     #返回当前路径下的所有文件和文件夹

print(os.getcwd())       #返回当前的工作目录

print(os.path.exists('\Python36-32\python.exe'))


