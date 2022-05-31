
# 函数
# def 函数名(参数列表):
#     函数体

# 函数的定义(加法)
def add(x,y):
    z = x +y
    return z

def add1(x,y):
    z = x +y
    print(z)

print(add(3,7))
print(add1(6,5.5))
print(add('a','b'))
# 位置参数
def add(x,y):   #定义了两个位置，不能多或少
    return x + y
print(add(10,8))

# 关键字参数：调用时使用 key:vlaue形式调用    实现一个函数，参数特别多 ，调用时不需要记住位置
def student_lesson(grade,subject):
    z = "{}年级上{}课".format(grade,subject)
    return z

print(student_lesson(2,'自习'))         #位置参数，顺序不能颠倒
print(student_lesson(subject="语文",grade='三'))       #关键字参数，可以调换位置
print(student_lesson(5,subject='体育'))    #关键字参数和位置参数混合使用。 位置参数必须在前，关键字参数在后，否则会报错。

# 默认参数    默认值的参数放最后面
def study_language(name,language='python'):
    info = ("{}学习的是{}语言".format(name,language))
    return info
print(study_language('李四','java'))
print(study_language('李'))

# 可变化参数
def add(x,y,*args):
    z = x + y + sum(args)
    print(args)
    return z
print(add(5,6,7,8))   #传递多个参数

# 使用列表的方式进行调用
print(add(5,6, *[1,2,3,4,5]))   #传递列表

# 可变化参数-字典形式
def show_info(**kwargs):
    print(kwargs)
    return None

ddd = {'a':1,'b':2,'c':3}
print(show_info(a='hello',b='good'))
print(show_info(**ddd))    #传递字典


# 面向对象
#1，定义一个类  ： class
# 2，在类里面申明属性（数据）和方法（函数）
# 3，定义一个具体的对象，叫初始化对象，对象是一个实实在在的对象  初始化对象==》 对象名 = 类名（）
# 4，使用多选调用方法或属性  对象名.属性 / 对象名.方法
print("="*20)

class Elevator():
    button = '开/关'
    floor = 15
    peple_num = 8

    def star(self):
        print("打开电梯")

    def stop(self):
        print("关闭电梯")

    def run(self):
        print("电梯运行")

e = Elevator()
e.star()          #使用方法
e.stop()
e.run()
print(e.button)   #使用属性
print(e.floor)
print(e.peple_num)

# 使用函数实现
def star():
    print("函数--打开电梯")


def stop():
    print("函数--关闭电梯")


def run():
    print("函数--电梯运行")

star()
stop()
run()
print("="*20)

# 实例: 创建学生类，要求有属性：姓名和年级 ; 方法有：学习的方法，打印学生的上课情况
class Students():
    name =''
    great = ''

    def study(self):
        print("{}年纪的学生{}正在学习".format(self.great,self.name))

s1 = Students()
print(s1)
s1.name ='张三'
s1.great = 5
print(s1.study())

s2 = Students()
print(s2)
s2.name = '王五'
s2.great = 3
print(s2.study())

# 类的构造方法：每次调用类的时候会自动被调用 ，主要用来初始化数据
#语法格式：
# def __init__(self,...):
#    代码块
class Student1():
    def __init__(self,grade,name):
        self.name = name
        self.grade = grade

    def stduy(self):
        print("{}年纪的学生{}在玩泥巴".format(self.name,self.grade ))

s3 = Student1('张三',6)
s3.stduy()

print("="*20)

# 变量
class Students2():
    name ='张三'      #类变量
    great = '五'      #类变量

    def study(self):
        print("{}年纪的学生{}正在学习".format(self.great,self.name))

# 使用类名调用

print(Students2.name)
print(Students2.great)

print("====")
# 使用使用实例化对象调用
ss = Students2()
print(ss.name)
print(ss.great)


# 实例变量
class Students3():

    def __init__(self,name,grade):
        self.name = name       #实例变量
        self.grade = grade      #实例变量
         #score = 60      #局部变量
    def study(self):
        print("{}年纪的学生{}正在学习".format(self.grade,self.name))

a1 = Students3('王五',4)
print(a1.name)
print(a1.grade)

print("="*20)
# 1try ... except语句
# 格式：
# try:
# 可能出现异常的代码块
# except Exception as e:
# print(e)

def div(x,y):
    try:

        z = x / y
        return z
    except Exception as e:
        print("不能被零整除")
        print(e)
# if __name__ == '__main__':

    print(div(5,2))
    print(div(5,0))
    print(div(15,2))

# 2try...except...finally语句
try:
    f = open('a.txt','r')
    l = f.readline()
    print(2/0)

    for x in l:
        print(x)

except Exception as e:
    print(e)

finally:                      #有时候在执行代码的过程中，无论是否出现异常，部分代码都希望被执行，如数据库关闭操作，关闭文件操作
    print("运行到这")
    f.close()




# main 方法
# if __name__ == '__main__':
