
# 1.for循环
"""
for 循环变量 in 序列
代码块

"""
# 循环abcdef中的每个字符
for y in "abcdef":
    print(y)

print("=====")


#  while循环
# while 条件语句(condition)：
# 代码块(statements)…

# 打印1~5的所有数字
a = 1
while a <= 5:
    print(a)
    a+=1

# # 计算1~100内所有数的和
sum = 0
a = 1
while a <= 100:
    sum += a
    a += 1
print(sum)


print("=====")
# 开始位置为0.循环到10，步长为1
for x in range(0,10,1):
    print(x)

print("=====")
# 开始位置为1，循环到10，步长为1
for x in range(1,10,1):
    print(x)

print("=====")
# 开始位置为1，循环到10，步长为2
for x in range(1,10,2):
    print(x)

print("=====")
# break语句用例终止当前循环
for x in range(1,10,1):
    if x == 7:
        break
    print(x)

print("=====")
# continue语句主要用来跳过当前循环
for x in range(1,10,1):
    if x == 7:
        continue
    print(x)

print("=====")
