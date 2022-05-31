sum = 0
for x in range(1,101):
    sum += x
print(sum)


sum1 = 0
for x in range(1,101):

     if x % 3 == 0:
        sum1 += x
print(sum1)
# #
# a = input("请输入整数")
# b = input("请输入整数")
# c = input("请输入整数")
# d = input("请输入整数")
#
# print(int(a) + int(b) - int(c) * int(d))
#
# for x in range(1,10):
#     for y in range(1,x+1):
#         print(x,' * ',y, ' = ', x * y ,end= ' ')
#     print()

# print("我的名字叫%s" %"张三")
# print("张三今年%d岁"%23)
# print("苹果%f块钱"%1.22)
# print("保留3位数字->'%.3f'" % 659)
# print("返回的数字宽度是8位，小数后两位，默认右对齐->'%8.2f'" %659)
# print("我是位置参数：{0} {1}".format('hello','python'))
# print("位置参数和关键字参数综合应用:{0} {x}".format('hello',x='python'))





# 字符串格式化 %s
my_str = "my name is %s" %('张三')
print(my_str)

# 格式化整数 %d
my_str1 = "张三今年%d岁" %(23)
print(my_str1)

# 格式化浮点数 %f
my_str2 = '一斤苹果%f钱'%(1.3)
print(my_str2)

# 指令  m.n m最小总宽度，n，显示小数点后的保留位数
my_str3 = '一斤苹果%5.2f钱'%(1.355)
print(my_str3)

# 显示左对齐 ： -
my_str4 = '一斤苹果%-5.2f钱'%(5.355)
print(my_str4)

# 在数字前面显示： +
my_str5 = '一斤苹果%+7.3f钱'%(5.35555)
print(my_str5)

# 加空格
my_str6 = '一斤苹果% 7.3f钱'%(5.35555)
print(my_str6)

# 前面显示0
my_str7 = '一斤苹果%012.3f钱'%(5.3555)
print(my_str7)

# 使用format方法进行字符串格式化 “{}”.format("传入的字符串")
my_str8 = "张三今年{}岁".format(44)
print(my_str8)

# format格式化两个参数，"{},{}".format(参数1，参数2)
my_str9 = "今天星期{}，张三买了{}斤苹果".format('二','5')
print(my_str9)

# format位置参数："{0}{1}{2}".format('1','5')
my_str10 = "今天星期{1}，张三买了{0}斤苹果".format('二','5')
print(my_str10)

# format关键字参数 "{}{}".format(x ='hello',y = 'good')
my_str11 = "今天星期{x}，张三买了{y}斤苹果".format(y = 9,x = '二')
print(my_str11)

#   位置参数和关键字参数可以结合起来使用，位置参数必须放在关键字前面
my_str12 = "今天星期{0}，张三买了{x}斤苹果".format('三',x = '9')
print(my_str12)

# 字符串方法
#1. 连接字符串：join(seq)
s1 = '+'
s2 =  s1.join('hello')
print(s2)

#2. 截取字符串 ： sqlity(str='')
s3 = "helloworldgoodnice"
s4 = s3.split("o")
print(s4)

# 3.查找字符串find(substr),找到返回最小索引，找不到返回-1
ss1 = "helloworld"
print(ss1.find("l"))
print(ss1.find("x"))
print(ss1.index("l"))

# 4.查找xxx结尾 endswith('xxx')
ss2 = "协商报告.doc"
if ss2.endswith('.doc'):
    print("hello")

# 5.查找xxx开头 startswith('xxx')
ss3 = "协商报告.doc"
if ss3.startswith('协商报告'):
    print("xieshang")

# 6.替换字符串 :replace(old.value,new.value)
ss4 = "good nice"
ss5 = ss4.replace("nice","bang")
print(ss5)

# 7.循环列表中的索引的值
lst8 = ['red', 'yellow', 'cream', 'blue', 'gunmetal']
for index,vls in enumerate(lst8):
    print(index,'====',vls)

# 列表推导式  [ expB for x in iterable expA ] [表达式2，循环体 表达式1]
# 1.生成一个1-10的列表
bb = []
for x in range(1,11):
    bb.append(x)
print(bb)
b1 = [x for x in range(1,11) ]
print(b1)

# 2.生成一个1-10的奇数列表
b2 = [x for x in range(1,11) if x % 2 !=0 ]
print(b2)

# 3.生成一个1-10的奇数列表，生成的值加10
b3 = [ x + 10 for x in range(1,11) if x % 2 !=0 ]
print(b3)

# q1 = "我的名字叫%s"%"钢铁侠"
# print(q1)
# q2 = "今天星期%d" %2
# print(q2)
# q3 = "苹果%f块一斤" %2.53
# print(q3)
#
# q4 = "苹果%10.3f块一斤" %2.5323
# print(q4)
# q5 = "苹果%+10.3f块一斤" %2.5323
# print(q5)


# def add(x,y):
#     z = x + y
#     return z
# print(add(3,4))
