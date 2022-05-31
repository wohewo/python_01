# 类的多肽
# 1.必须是继承关系
# 2.子类中的方法覆盖了父类的方法

# 区别
# 子类方法调用父类方法：继承
# 子类方法覆盖父类方法：多肽

class People():
    age = 0

    def eat(self,people_type):
        print(people_type,"在吃饭")

class Student1(People):

    def eat(self,grade):
        super().eat(grade)    #调用父类的方法
        print("{}在吃饭".format(grade))

class Teacher(People):

    def eat(self, sub,time):
        print("{}科目的来说在{}吃饭".format(sub,time))

s = Student1()
s.eat('2年级')

t = Teacher()
t.eat('语文','12:00')

# import lx
#
# print(lx.add(5,5))

for x in range(1,11):

    print(x)

