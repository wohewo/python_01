
a = "我的名字叫%s"% '张三'
print(a)
a1 = "西瓜%d块钱一斤" %2
print(a1)
a2 = "黄瓜%f块钱一斤" %2.2525
print(a2)
a4 = "黄瓜%-10.2f块钱一斤" %2.2525
print(a4)
a5 = "今天星期{},西瓜{}钱一斤".format(3 , 2.22)
print(a5)
a11 = "今天星期{1},西瓜{0}钱一斤".format(3 , 2.22)
print(a11)
a12 = "今天星期{y},西瓜{x}钱一斤".format(x = '五' ,y = 2.22)
print(a12)
a13 = "今天星期{0},西瓜{x}钱一斤".format(3 , x =6)
print(a13)
a14 = '=='
a15 = a14.join("hello")
print(a15)
a16 = "doo sfsk sfj f z"
a17 = a16.split("f")
print(a17)
a18 = "hellogoodnoice"
print(a18.find("good"))
print(len(a18))
print(a18.endswith("ice"))
print(a18.startswith('he'))
a19 = "12314"
a20 = a19.replace("2","7")
print(a20)
print(a19.isdigit())

a21 = " sdsdfvzfmwizu "
print(max(a21))
print(min(a21))
print(a19.isdigit())

print(a21.strip())

ls = ['ee',12,'dof','ff']
print(ls[3])
print(ls[-2])
lst = ['red','green','blue','black','gold','orange', 2 , 25]
print(lst[1:5:1])
print(lst[::2])
print(lst[2:])
print(lst[:3:])
lst1 = [1,2,3,4,5,6,7,8,9,10]
lst2 = ['good',44]
print(lst1[::2])
lst3 = lst1 + lst2
print(lst3)
print(lst2 * 3)
print(11 not in lst1)
print(len(lst2))
print(max(lst1))
print(min(lst1))

lll = "我是钢铁侠"
print(list(lll))
print(str(lll))
lll1 = 1,2,4,5,68,6
print(sum(lll1))
print(sorted(lll1))
lol = ['a','b','c']
lol.reverse()
print(lol)
print(lol + ['red','good'])

lst8 = ['red', 'yellow', 'cream', 'blue', 'gunmetal']


def add(x,y):
    return x + y
print(add(15,8))


def student_lesson(grade,subject):
    z = '{}班的小朋友{}在玩泥巴'.format(grade,subject)
    return z
print(student_lesson(5,'wangba'))


def add1(x,y,z):
    sa = x + y
    sb = sa * z
    return sa,sb
print(add1(2,3,4))

def add2(a,b,*args):
    for x in args:
        sum = sum +x
    return a + b + sum

class Student():
    name = ""
    grade = ""

    def stady(self):
        print('{}班学生{}正在学习'.format(self.grade,self.name))
s1 = Student()
s1.name = '张三'
s1.grade = 2
print(s1.stady())





