# 条件表达式
# samll =  x if x < y else y

# 断言
# 程序自动崩溃，检测用
# assert 3 > 4

# range
# range([strat,] stop[, step=1])
# 配合for使用，rang生成从strat到stop的数字序列，不包括stop的数字
# range(5)/range(0,5)/rang(0,5,1)
##list(range(5))
##[0, 1, 2, 3, 4]

# break
##b = 'niubi'
##a = input('shuru:')
##
##while True:
##    if a == b:
##        break
##    a = input('zaicishuru:')
##
##print('tongguo')

# continue
##for i in range(10):
##    if i%2 != 0:
##        print(i)
##        continue
##    i += 2
##    print(i)
# 此算法可做偶数项上的操作 i += 2       '

##列表，元组，字符串 统称为序列
##都可以通过索引得到每一个元素
##默认索引值总是从0开始
##可以通过分片的方法得到一个范围内的元素的集合
##有很多共同的操作符（重复操作符，拼接操作符，成员关系操作符）

##list()把一个可迭代对象转换为列表
##tuple([iterable])把一个可迭代对象转换为元组
##len(sub) 返回sub列表长度
##max()返回序列或参数集合中的最大值
##min() 与上相反
##max,min 保证列表参数数据类型一致
##sum(iterable[,start=0])返回序列iterable和可选参数start的总和
##x = [1, 2, 3]
##y = [3, 4, 5, 6]
##sorted(x)
##list(reversed(x))
##list(enumerate(x))
##list(zip(x, y))

# 函数 对象 模块

##def Function(x):
##    'wendangshuxin'
##    # zhushi
##    print(x + 'Function!')
##
##Function('23')
##23Function!
##
##Function.__doc__
##'wendangshuxin'
### 函数的默认属性doc，系统属性用双下横线，help更好用一点

##收集参数 (*形式参数)
##def test(*params):
##    print('参数的长度是：', len(params))
##    print('第二个参数是：',params[1])
##
##    
##test(1, '123', 3.12, 5, 6, 7)
##参数的长度是： 6
##第二个参数是： 123

##使用定制参数时，使用关键字参数，不然默认为收集参数,最好先设置默认参数
##def test(*params, exp):
##    print('参数的长度是：', len(params), exp)
##    print('第二个参数是：',params[1])
##
##    
##test(1, '123', 3.12, 5, 6, 7, exp = 8)
##参数的长度是： 6 8
##第二个参数是： 123

# 局部变量 与 全局变量
##def dis(p, r):
##    final_p = p * r
##    return final_p
##
##old_p = float(input('shuruyuanjia:'))
##r = float(input('shuruzhekou:'))
##new_p = dis(old_p, r)
##print('zhehoujia:', new_p)
##
##shuruyuanjia:100
##shuruzhekou:0.8
##zhehoujia: 80.0

## 不要再函数中修改全局变量
##def dis(p, r):
##    final_p = p * r
##    old_p = 10
##    print('xiugaihoude old_p:', old_p)
##    return final_p
##
##old_p = float(input('shuruyuanjia:'))
##r = float(input('shuruzhekou:'))
##new_p = dis(old_p, r)
##print('xiugaihoude old_p:', old_p)
##print('zhehoujia:', new_p)
##
##shuruyuanjia:100
##shuruzhekou:0.8
##xiugaihoude old_p: 10 # 这里函数会自动创建一个同名的局部变量
##xiugaihoude old_p: 100.0 
##zhehoujia: 80.0

##count = 5
##def Fun():
##    count = 10
##    print(10)
##
##Fun()
##10
##print(count)
##5

##count = 5
##def Fun():
##    global count # 指定count为全局变量
##    count = 10
##
##Fun()
##10
##print(count)
##10

### x *= x 是函数内部的函数Fun2对其外部 x = 5 变量的修改，及
### 相对于改变了Fun2的全局变量，故会报错
##def Fun1():
##    x = 5
##    def Fun2():
##        x *= x
##        return x
##    return Fun2()
##
##Fun1()
### 错误
##Traceback (most recent call last):
##  File "<pyshell#13>", line 1, in <module>
##    Fun1()
##  File "<pyshell#12>", line 6, in Fun1
##    return Fun2()
##  File "<pyshell#12>", line 4, in Fun2
##    x *= x
##UnboundLocalError: local variable 'x' referenced before assignment
### 解决方法一，早版本以前，利用列表
##def Fun1():
##    x = [5]
##    def Fun2():
##        x[0] *= x[0]
##        return x[0]
##    return Fun2()
##
##Fun1()
##25
### 解决方法二，定义Fun2中的 x 变量强制声明为不是局部变量
##def Fun1():
##    x = 5
##    def Fun2():
##        nonlocal x
##        x *= x
##        return x
##    return Fun2()
##
##Fun1()
##25

### 简介的函数定义 lambda 前面参数 : 返回值
### 节省函数定义过程，不用起名字
##def ds(x):
##    return 2 * x + 1
##
##ds(5)
##11
##
##lambda x : 2 * x + 1
##<function <lambda> at 0x0000013F5BFCA5F0>
##g = lambda x : 2 * x + 1
##g(5)
##11

### filter 过滤函数（过滤真值，1， True）
##list(filter(None, [1, 0, False, True]))
##[1, True]
### 例1
##def odd(x):
##    return x % 2
##
##t = range(10)
##list(filter(odd, t))
##[1, 3, 5, 7, 9]
### 简化
##list(filter(lambda x : x % 2, range(10)))
##[1, 3, 5, 7, 9]

### map 将后面的各项带入到前面一项中
##list(map(lambda x : x % 2, range(10)))
##[0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
##list(map(lambda x : x * 2, range(10)))
##[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


# {}是映射类型 字典

##b = ['1','2','3']
##s = ['a','b','c']
##print('1: ',s[b.index('3')])
##1:  c
##dict1 = {'1':'2', '3':'4', '5':'6'}
##print('1后面是：', dict1['1'])
##1后面是： 2

##fromkeys() 创建并返回一个新的字典
##dict1 = {}
##dict1.fromkeys((1, 2, 3))
##{1: None, 2: None, 3: None}
##dict1.fromkeys((1, 2, 3),'Number')
##{1: 'Number', 2: 'Number', 3: 'Number'}
##dict1.fromkeys((1, 2, 3),('one', 'two', 'three'))
##{1: ('one', 'two', 'three'), 2: ('one', 'two', 'three'), 3: ('one', 'two', 'three')}

##dict1 = dict1.fromkeys(range(5),'niuwa')
##dict1
##{0: 'niuwa', 1: 'niuwa', 2: 'niuwa', 3: 'niuwa', 4: 'niuwa'}
##
##for eachKey in dict1.keys():
##    print(eachKey)
##
##    
##0
##1
##2
##3
##4
##for eachValue in dict1.values():
##    print(eachValue)
##
##    
##niuwa
##niuwa
##niuwa
##niuwa
##niuwa
##for eachItem in dict1.items():
##    print(eachItem)
##
##    
##(0, 'niuwa')
##(1, 'niuwa')
##(2, 'niuwa')
##(3, 'niuwa')
##(4, 'niuwa')
##
##print(dict1[4])
##niuwa
##print(dict1[5])
##Traceback (most recent call last):
##  File "<pyshell#22>", line 1, in <module>
##    print(dict1[5])
##KeyError: 5
##dict1.get(5)
##print(dict1.get(5))
##None
##
##4 in dict1
##True
##5 in dict1
##False

##dict1.clear()
##dict1
##{}

