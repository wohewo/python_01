"""

1. 输入a,b,c,d4个整数，计算a+b-c*d的结果
a = input(输入整数)
b = input(输入整数)
c = input(输入整数)
d = input(输入整数) 

2. 打印1~100内被3整除的所有数的和 。
sum = 0
for x in range(1,101)
if x % 3 == 0
sum += x
print(sum)
3. 使用range()输出1~10内的所有奇数 。
for x in range(1,11,2)
print(x)
4. 打印1~100所有偶数的和 减去 所有奇数的和 的值
5. 求1+2+3+...+100的和
6. 判断一个数n能同时被3和5整除
7. 定义一个整数变量，判断该变量值是否是1-100内的某个数，如果是打印出来
8. 输入三个整数x,y,z，请把这三个数由小到大输出。备注：输入方法：input()
9. 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，
60分以下的用C表示。备注：需要使用input()方法
10. 将一个列表的数据复制到另一个列表中。
11. 输出 9*9 乘法口诀表。

12. 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
13. 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个
数相加)，几个数相加由键盘控制。
14. 题目：打印出如下图案（菱形）:
"""""

clst = ['red','blue','yellow']
blst = ['数',1,1.2]
clst.append('black')
print(clst)
clst.extend(blst)
print(clst)

clst.reverse()
print(clst)

print(clst.count(1))
print(clst.index('blue'))
clst.insert(2,'大')
print(clst)
clst.pop(6)
print(clst)
clst.remove('red')

dlst = ['ac','sd','ds','bbb','z']
dlst.sort()
print(dlst)

blst.clear()
print(blst)

blst = clst.copy()
print(blst)

print(blst.count(1))
blst.extend(['red','good'])
print(blst)

print(blst.index('good'))

blst.pop(7)
print(blst)

tp1 = (1)
print(tp1)

d1 = {}
d2 = {"上海":1,"北京":2}
print(d1)
print(d2)

print(d2["北京"])
d2["重庆"] = 3
print(d2)

d = {'zhangsan': 23, 'lisi': 35}
print(d)

print(d.get('zhangsan'))

print(d.keys())
print(d.values())

print(d.items())
dd = {'shanghai':1,'wuhan':2}
print(dd)

d.update(dd)
print(d)
bb = dd.copy()
print(bb)
bb.clear()
print(bb)

print('shanghai' in dd)
print(dd.keys())
for x in dd.keys():
    print(x)
#
print(dd.values())
for y in dd.values():
    print(y)

print(dd.items())
for x,y in dd.items():
    print(x,"====:", y)
d3 = d.fromkeys('a','b')
print(d3)

print(dd.setdefault('wuha'))

dd.pop('shanghai')
print(dd)
dd.popitem()
print(dd)

print("=====")

# 使用range()输出1~10内的所有奇数
for x in range(1,10,2):
    print(x)

# 5. 求1+2+3+...+100的和
sum = 0
a = 1
while  a<= 100:
    a+=1
    sum+=a
print(sum)

for x in ("abcdef"):
    print(x)

print("====")

app = 1
acc = 0
while app <= 100:
    app += 1
    acc += app
    print(acc)


for x in range(60,91):
    if x >= 90:
        continue
    print(x)











