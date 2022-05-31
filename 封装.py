
# 封装  当类中的部分数据不愿意被外界使用时，就可以把类的部分方法和属性隐藏掉，只给用户提供一些方法的接口，如我们电脑的鼠标和键盘 。

class Students():
    name = '张三'
    __score = "45"

    def set_score(self,score):

        self.__score = score

    def get_score(self):
        return self.__score

print(Students.name)
# print(Students.__score)
s = Students()
# s.set_score(15)
print(s.get_score())

# 类的继承
class People():
    age = 0

    def eat(self,people_type):
        print(people_type,"在吃饭")

class Student1(People):

    pass

class Teacher(People):

    pass

s1 = Student1()
s1.eat("学生")
Student1.age = 20
print(Student1.age)

t = Teacher()
t.eat("老师")
Teacher.age = 55
print(Teacher.age) 


