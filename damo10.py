
# 通过from ... import 导入
from hanshu import add

print(add(5,8))

from python_02.daamo05list import blst

def add(x,y,*args):
    z = x + y + sum(args)
    return z
print(add(1,2,1,2,1,4,14))

# 实例: 创建学生类，要求有属性：姓名和年级 ; 方法有：学习的方法，打印学生的上课情况
class Student():
    # name = ''
    # grade =0

    def __init__(self,name,grade):
        self.name = name
        self.grade = grade

    def syudy(self):

        print("{}是{}年纪的学生".format(self.name,self.grade))

s = Student('zhansan',2)
print(s.syudy())
