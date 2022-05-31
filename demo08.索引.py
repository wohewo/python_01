
# 序列的通用操作
# 1.索引
lst = ['red',1,155,'good']
print(lst[2])     #列表第三个值
print(lst[-1])     #列表最后一个值


tp = ('good',55,26,11)
print(tp[3])   #列表第4个值
print(tp[-2])   #列表倒数第2个值

q = 'redbook'
print(q[3])

# 序列的切片 lst[start:end:step] 开始位置：结束位置：步长
lst2 = ['red','green',11,'blue','black',66,'gold','orange']
print(lst2[1:5:1])  #取2-5
print(lst2[1:6:2])   #取偶数

print(lst2[1::])  #省略结束位置和步长

print(lst2[1:5])   #省略结束位置（结束位置默认为列表的长度）

print(lst2[::2])  #省略开始位置和结束位置（开始位置默认为0，结束位置默认为列表的长度）

print(lst2[1::2])

print(lst2[:3:])   #省略开始位置和步长 （开始位置默认为0，步长默认为1）

# 序列的相加想乘 +  *
a1 = [1,2]
b1 = [3,4]
c1 = a1 + b1  #将a1的值和b1的值加起来等于c1
print(c1)

print(a1 *3)  #将a1的值乘以3倍
d1 = [None] * 3
print(d1)

# 检查元素
lst3 = ['red', 'yellow', 1 , 'cream', 2 , 'blue', 'gunmetal']
print('red' in lst3)
print(1 in lst3)

print(len(lst3))
print(max(lst3))