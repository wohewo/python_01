#  定义变量
# a = "hello world"
# b = 20
# c = 12.2
# d = True
# e = None
#
# 定义变量的其他方式
# f,g= "hello",2
# h = b+c


# print("hello world")
# print(1+1)
# print(2 == 2)
#
# print(type("hello world"))
# print(type(11))
# print(type(11.11))

# 算数运算符
# b,c = 30,6
# print(b+c)
# print(b-c)
# print(b*c)
# print(b/c)
# print(b//c)
# print(b%c)
# print(b**c)
# # 比较运算符
# print(b>c)
# print(b>=c)
# print(b<c)
# print(b<=c)
# print(b == c)
# print(b!= c)
# print(b is c)
# print(b is not c)
# # 赋值运算符
# a,b =50,5
# a+=b
# print(a)
# a-=b
# print(a)
# a*=b
# print(a)
# a/=b
# print(a)
# a%=b
# print(a)
# a**=b
# print(a)
# a//=b
# print(a)
#
# # 逻辑运算符
# print(a and b)
# print(a or b)
# print(not a)
#
# if 10 > 8:
#     print('good')

# 1. 输入a,b,c,d4个整数，计算a+b-c*d的结果
# a = input("请输入一个整数:")
# b = input("请输入一个整数:")
# c = input("请输入一个整数:")
# d = input("请输入一个整数:")
# print(int(a) + int(b) - int(c) * int(d))
# 2. 打印1~100内被3整除的所有数的和 。
sum = 0
for x in range(3,101,3):
    if x % 3 == 0:
        sum += x
print(sum)
# 3. 使用range()输出1~10内的所有奇数 。
for x in range(1,11,2):
    print(x)

# 4. 打印1~100所有偶数的和 减去 所有奇数的和 的值
sum1 = 0
sum2 = 0
for x in range(1,101,1):
    if x % 2 == 0:
        sum1 += x
    else:
        sum2 += x
print(sum1 - sum2)



# 5. 求1+2+3+...+100的和
sum3 = 0
for x in range(1,101,1):
    sum3 += x
print(sum3)

# 6. 判断一个数n能同时被3和5整除
# n = input("请输入一个整数")
# if int(n) % 3 == 0 and int(n) % 5 == 0:
#     print(n,"能被整除")
# else:
#     print("不能整除")

# 7. 定义一个整数变量，判断该变量值是否是1-100内的某个数，如果是打印出来
# i = 55
# if i < 100:
#     print(i)
#
# f = input("输入整数")
# if 1 < int(f) < 100:
#     print("在1-100内")
# else:
#     print("不在1-100内")
# 8. 输入三个整数x,y,z，请把这三个数由小到大输出。备注：输入方法：input()
# x = int(input("输入整数"))
# y = int(input("输入整数"))
# z = int(input("输入整数"))
# lss = [x,y,z]
# print(lss)
# lss.sort()
# print(lss)
# 9. 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，
# 60分以下的用C表示。备注：需要使用input()方法
# socre = input("输入分数")
# if int(socre) >= 90:
#     print("A")
# elif int(socre) > 60:
#     print("B")
# else:
#     print("c")
# 10. 将一个列表的数据复制到另一个列表中。
lol = [1,2,55]
lol1 =[555,99]
lol1.extend(lol)
print(lol1)

print("=====")
# 11. 输出 9*9 乘法口诀表。
for x in range(1,10):
    for y in range(1,x+1):
        print(x,"*",y," = ",x * y,end='  ')
    print()
# 12. 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
s11 = "dssadsaz4545d dsad#$%1515"
zf = 0
kg = 0
sz = 0
other = 0

for x in s11:
    if x.isalpha():
        zf += 1
    elif x.isspace():
        kg += 1
    elif x.isdigit():
        sz += 1
    else:
        other += 1
print('字符个数',zf)
print('空格个数',kg)
print('数字个数',sz)
print('其他个数',other)




# 13. 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个
# 数相加)，几个数相加由键盘控制。

# 14. 题目：打印出如下图案（菱形）:print(999)
num = 5    #总数
x = num - 1    #循环轮次

for n in range(1,num):
    spcae = " " * (x-n)
    star = "*" * (2 *(n-1) +1)
    print(spcae + star)

for n in range(1,4):
    spcae = n * " "
    star = (5 - (n - 1) * 2) * "*"
    print(spcae + star)