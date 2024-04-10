

- **已知一个字符串为 “hello_world_yoyo”, 如何得到一个队列 [“hello”,”world”,”yoyo”]**

```python
test = 'hello_world_yoyo'
# 使用split函数，分割字符串，并且将数据转换成列表类型
print(test.split("_"))

结果：
['hello', 'world', 'yoyo']

Process finished with exit code 0
12345678
```

- **有个列表 [“hello”, “world”, “yoyo”]如何把把列表里面的字符串联起来，得到字符串 “hello_world_yoyo”**

```python
test = ["hello", "world", "yoyo"]
# 使用 join 函数将数据转换成字符串
print("_".join(test))

结果：
hello_world_yoyo

Process finished with exit code 0
12345678
```

这边如果不依赖python提供的join方法，我们还可以通过for循环，然后将[字符串](https://so.csdn.net/so/search?q=字符串&spm=1001.2101.3001.7020)拼接，但是在用"+"连接字符串时，结果会生成新的对象，
用join时结果只是将原列表中的元素拼接起来，所以join效率比较高

```python
test = ["hello", "world", "yoyo"]

# 定义一个空字符串
j = ''

# 通过 for 循环 打印出列表中的数据
for i in test:
    j = j + "_" + i

# 因为通过上面的字符串拼接，得到的数据是“_hello_world_yoyo”,前面会多一个下划线，所以我们下面把这个下划线去掉
print(j.lstrip("_"))
1234567891011
```

- **把字符串 s 中的每个空格替换成”%20”
  输入：s = “We are happy.”
  输出：”We%20are%20happy.”**

```python
s = 'We are happy.'

print(s.replace(' ', '%20'))

结果：
We%20are%20happy.

Process finished with exit code 0

123456789
```

- **打印99乘法表**

```python
for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j, i, i*j), end='')
    print()

结果：
1x1=1	
1x2=2	2x2=4	
1x3=3	2x3=6	3x3=9	
1x4=4	2x4=8	3x4=12	4x4=16	
1x5=5	2x5=10	3x5=15	4x5=20	5x5=25	
1x6=6	2x6=12	3x6=18	4x6=24	5x6=30	6x6=36	
1x7=7	2x7=14	3x7=21	4x7=28	5x7=35	6x7=42	7x7=49	
1x8=8	2x8=16	3x8=24	4x8=32	5x8=40	6x8=48	7x8=56	8x8=64	
1x9=9	2x9=18	3x9=27	4x9=36	5x9=45	6x9=54	7x9=63	8x9=72	9x9=81	

Process finished with exit code 0

123456789101112131415161718
```

下面是使用while循环实现

```python
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("%d*%d=%-2d"%(i,j,i*j),end = ' ')  # %d： 整数的占位符，'-2'代表靠左对齐，两个占位符
        j += 1
    print()
    i += 1
12345678
```

- **找出单词 “welcome” 在 字符串”Hello, welcome to my world.” 中出现的位置，找不到返回-1
  从下标0开始索引**

```python
def test():
    message = 'Hello, welcome to my world.'
    world = 'welcome'
    if world in message:
        return message.find(world)
    else:
        return -1


print(test())

结果：
7

Process finished with exit code 0
123456789101112131415
```

- **统计字符串“Hello, welcome to my world.” 中字母w出现的次数
  统计单词 my 出现的次数**

```python
def test():
    message = 'Hello, welcome to my world.'
    # 计数
    num = 0
    # for 循环message
    for i in message:
        # 判断如果 ‘w’ 字符串在 message中，则num +1
        if 'w' in i:
            num += 1
    return num


print(test())

1234567891011121314
```

- **题目:输入一个字符串str, 输出第m个只出现过n次的字符，如在字符串 gbgkkdehh 中,
  找出第2个只出现1 次的字符，输出结果：d**

```python
def test(str_test, num, counts):
    """
    :param str_test: 字符串
    :param num: 字符串出现的次数
    :param count: 字符串第几次出现的次数
    :return:
    """
    # 定义一个空数组，存放逻辑处理后的数据
    list = []

    # for循环字符串的数据
    for i in str_test:
        # 使用 count 函数，统计出所有字符串出现的次数
        count = str_test.count(i, 0, len(str_test))

        # 判断字符串出现的次数与设置的counts的次数相同，则将数据存放在list数组中
        if count == num:
            list.append(i)

    # 返回第n次出现的字符串
    return list[counts-1]


print(test('gbgkkdehh', 1, 2))

结果：
d

Process finished with exit code 0
1234567891011121314151617181920212223242526272829
```

- **判断字符串a=”welcome to my world” 是否包含单词b=”world”
  包含返回True，不包含返回 False**

```python
def test():
    message = 'welcome to my world'
    world = 'world'

    if world in message:
        return True
    return False


print(test())

结果：
True

Process finished with exit code 0
123456789101112131415
```

- **输出指定字符串A在字符串B中第一次出现的位置,如果B中不包含A,则输出-1
  从 0 开始计数
  A = “hello”
  B = “hi how are you hello world, hello yoyo !”**

```python
def test():
    message = 'hi how are you hello world, hello yoyo !'
    world = 'hello'

    return message.find(world)


print(test())

结果：
15

Process finished with exit code 0
12345678910111213
```

- **输出指定字符串A在字符串B中最后出现的位置,如果B中不包含A, 出-1从 0 开始计数
  A = “hello”
  B = “hi how are you hello world, hello yoyo !”**

```python
def test(string, str):
    # 定义 last_position 初始值为 -1
    last_position = -1
    while True:
        position = string.find(str, last_position+1)
        if position == -1:
            return last_position
        last_position = position


print(test('hi how are you hello world, hello yoyo !', 'hello'))

结果：
28

Process finished with exit code 0

1234567891011121314151617
```

- **给定一个数a，判断一个数字是否为奇数或偶数
  a1 = 13
  a2 = 10**

```python
while True:
    try:
        # 判断输入是否为整数
        num = int(input('输入一个整数：'))
    # 不是纯数字需要重新输入
    except ValueError: 
        print("输入的不是整数！")
        continue
    if num % 2 == 0:
        print('偶数')
    else:
        print('奇数')
    break

结果：
输入一个整数：100
偶数

Process finished with exit code 0
12345678910111213141516171819
```

- **输入一个姓名，判断是否姓王
  a = “王五”
  b = “老王”**

```python
def test():
    user_input = input("请输入您的姓名：")

    if user_input[0] == '王':
        return "用户姓王"

    return "用户不姓王"


print(test())

结果：
请输入您的姓名：王总
用户姓王

Process finished with exit code 0

123456789101112131415161718
```

- **如何判断一个字符串是不是纯数字组成
  a = “123456”
  b = “yoyo123”**

这个答案，其实有些取巧，利用python提供的类型转行，将用户输入的数据转换成浮点数类型，如果转换抛异常，则判断数字不是纯数字组成

```python
def test(num):
    try:
        return float(num)
    except ValueError:
        return "请输入数字"


print(test('133w3'))

123456789
```

- **将字符串 a = “This is string example….wow!” 全部转成大写
  字符串 b = “Welcome To My World” 全部转成小写**

```python
a = 'This is string example….wow!'
b = 'Welcome To My World'

print(a.upper())
print(b.lower())

123456
```

- **将字符串 a = “ welcome to my world “首尾空格去掉**

python提供了strip()方法，可以去除首尾空格
rstrip()去掉尾部空格
lstrip（）去掉首部空格
replace(" ", “”) 去掉全部空格

```python
a = '  welcome to my world   '
print(a.strip())
12
```

还可以通过递归的方式实现

```python
def trim(s):
    flag = 0
    if s[:1]==' ':
        s = s[1:]
        flag = 1
    if s[-1:] == ' ':
        s = s[:-1]
        flag = 1
    if flag==1:
        return    trim(s)
    else:
        return s
print(trim('  Hello world!  '))

1234567891011121314
```

通过while循环实现

```python
def trim(s):
    while(True):
        flag = 0
        if s[:1]==' ':
            s = s[1:]
            flag = 1
        if s[-1:] == ' ':
            s = s[:-1]
            flag = 1
        if flag==0:
            break
    return s
print(trim('  Hello world!  '))

1234567891011121314
```

- **s = “ajldjlajfdljfddd”，去重并从小到大排序输出”adfjl”**

```python
def test():
    s = 'ajldjlajfdljfddd'
    # 定义一个数组存放数据
    str_list = []
    # for循环s字符串中的数据，然后将数据加入数组中
    for i in s:
        # 判断如果数组中已经存在这个字符串，则将字符串移除，加入新的字符串
        if i in str_list:
            str_list.remove(i)

        str_list.append(i)
    # 使用 sorted 方法，对字母进行排序
    a = sorted(str_list)
    # sorted方法返回的是一个列表，这边将列表数据转换成字符串
    return "".join(a)


print(test())

结果：
adfjl

Process finished with exit code 0
1234567891011121314151617181920212223
```

- **题目 打印出如下图案（菱形）:**

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210519185708341.png)

```python
def test():
    n = 8
    for i in range(-int(n/2), int(n/2) + 1):
        print(" "*abs(i), "*"*abs(n-abs(i)*2))


print(test())

结果：
    **
   ****
  ******
 ********
  ******
   ****
    **
     

Process finished with exit code 0
1234567891011121314151617181920
```

1. **题目 给一个不多于5位的正整数，要求：
   一、求它是几位数，
   二、逆序打印出各位数字。
   a = 12345**

```python
class Test:

    # 计算数字的位数
    def test_num(self, num):

        try:

            # 定义一个 length 的变量，来计算数字的长度
            length = 0

            while num != 0:
                # 判断当 num 不为 0 的时候，则每次都除以10取整
                length += 1
                num = int(num) // 10

            if length > 5:
                return "请输入正确的数字"
            return length
        except ValueError:
            return "请输入正确的数字"

    # 逆序打印出个位数
    def test_sorted(self, num):
        if self.test_num(num) != "请输入正确的数字":
            
            # 逆序打印出数字
            sorted_num = num[::-1]
            
            # 返回逆序的个位数
            return sorted_num[-1]


print(Test().test_sorted('12346'))

结果：
1

Process finished with exit code 0

123456789101112131415161718192021222324252627282930313233343536373839
```

**如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。
例如：153 = 1^3 + 5^3 + 3^3，因此 153 就是一个水仙花数
那么问题来了，求1000以内的水仙花数（3位数）**

```python
def test():
    for num in range(100, 1000):
        i = num // 100
        j = num // 10 % 10
        k = num % 10
        if i ** 3 + j ** 3 + k ** 3 == num:
            print(str(num) + "是水仙花数")

test()
123456789
```

- **求1+2+3…+100和**

```python
i = 1

for j in range(101):
    i = j + i

print(i)

结果：
5051

Process finished with exit code 0
1234567891011
```

- **计算求1-2+3-4+5-…-100的值**

```python
def test(sum_to):
    
    # 定义一个初始值
    sum_all = 0
    # 循环想要计算的数据
    for i in range(1, sum_to + 1):
        sum_all += i * (-1) ** (1 + i)
    return sum_all


if __name__ == '__main__':
    result = test(sum_to=100)
    print(result)

-50

Process finished with exit code 0

123456789101112131415161718
```

**计算公式 13 + 23 + 33 + 43 + …….+ n3
实现要求：
输入 : n = 5
输出 : 225
对应的公式 : 13 + 23 + 33 + 43 + 53 = 225**

```python
def test(n):
    sum = 0
    for i in range(1, n+1):
        sum += i*i*i

    return sum

print(test(5))

结果：
225

Process finished with exit code 0
12345678910111213
```

- **已知 a的值为”hello”，b的值为”world”，如何交换a和b的值？
  得到a的值为”world”，b的值为”hello”**

```python
a = 'hello'
b = 'world'

c = a
a = b
b = c
print(a, b)
1234567
```

- **如何判断一个数组是对称数组：
  要求：判断数组元素是否对称。例如[1，2，0，2，1]，[1，2，3，3，2，1]这样的都是对称数组
  用Python代码判断，是对称数组打印True，不是打印False,如：
  x = [1, “a”, 0, “2”, 0, “a”, 1]**

```python
def test():

    x = [1, 'a', 0, '2', 0, 'a', 1]
    # 通过下标的形式，将字符串逆序进行比对
    if x == x[::-1]:
        return True
    return False

print(test())

结果：
True

Process finished with exit code 0

123456789101112131415
```

- **如果有一个列表a=[1,3,5,7,11]
  问题：1如何让它反转成[11,7,5,3,1]
  2.取到奇数位值的数字，如[1,5,11]**

```python
def test():

    a = [1, 3, 5, 7, 11]
    # 逆序打印数组中的数据
    print(a[::-1])

    # 定义一个计数的变量
    count = 0
    for i in a:
        # 判断每循环列表中的一个数据，则计数器中会 +1
        count += 1
        # 如果计数器为奇数，则打印出来
        if count % 2 != 0:
            print(i)


test()

结果：
[11, 7, 5, 3, 1]
1
5
11

Process finished with exit code 0

1234567891011121314151617181920212223242526
```

- **问题：对列表a 中的数字从小到大排序
  a = [1, 6, 8, 11, 9, 1, 8, 6, 8, 7, 8]**

```java
a = [1, 6, 8, 11, 9, 1, 8, 6, 8, 7, 8]
print(sorted(a))

结果：
[1, 1, 6, 6, 7, 8, 8, 8, 8, 9, 11]

Process finished with exit code 0
1234567
```

- **L1 = [1, 2, 3, 11, 2, 5, 3, 2, 5, 33, 88]
  找出列表中最大值和最小值**

```python
L1 = [1, 2, 3, 11, 2, 5, 3, 2, 5, 33, 88]
print(max(L1))
print(min(L1))

结果：
88
1

Process finished with exit code 0

12345678910
```

上面是通过python自带的函数，下面有可以自己写一个计算程序，贴代码：

```java
class Test(object):

    def __init__(self):
        # 测试的列表数据
        self.L1 = [1, 2, 3, 11, 2, 5, 3, 2, 5, 33, 88]

        # 从列表中取第一个值，对于数据大小比对
        self.num = self.L1[0]

    def test_small_num(self, count):
        """

        :param count: count为 1，则表示计算最大值，为 2 时，表示最小值
        :return:
        """
        # for 循环查询列表中的数据
        for i in self.L1:
            if count == 1:
                # 循环判断当数组中的数据比初始值小，则将初始值替换
                if i > self.num:
                    self.num = i
            
            elif count == 2:
                if i < self.num:
                    self.num = i
                    
            elif count != 1 or count != 2:
                return "请输入正确的数据"

        return self.num


print(Test().test_small_num(1))
print(Test().test_small_num(2))
结果：
88
1

Process finished with exit code 0

12345678910111213141516171819202122232425262728293031323334353637383940
```

- **a = [“hello”, “world”, “yoyo”, “congratulations”]
  找出列表中单词最长的一个**

```python
def test():
    a = ["hello", "world", "yoyo", "congratulations"]
    
    # 统计数组中第一个值的长度
    length = len(a[0])
    
    for i in a:
        # 循环数组中的数据，当数组中的数据比初始值length中的值长，则替换掉length的默认值
        if len(i) > length:
            length = i
    return length


print(test())

结果：
congratulations

Process finished with exit code 0
12345678910111213141516171819
```

- **取出列表中最大的三个值
  L1 = [1, 2, 3, 11, 2, 5, 3, 2, 5, 33, 88]**

```python
def test():
    L1 = [1, 2, 3, 11, 2, 5, 3, 2, 5, 33, 88]
    return sorted(L1)[:3]


print(test())

结果：
[1, 2, 2]

Process finished with exit code 0
1234567891011
```

- **a = [1, -6, 2, -5, 9, 4, 20, -3] 按列表中的数字绝对值从小到大排序**

```python
def test():
    a = [1, -6, 2, -5, 9, 4, 20, -3]
    # 定义一个数组，存放处理后的绝对值数据
    lists = []
    for i in a:
    	# 使用 abs() 方法处理绝对值
        lists.append(abs(i))
    return lists

print(test())

结果：
[1, 6, 2, 5, 9, 4, 20, 3]

Process finished with exit code 0
123456789101112131415
```

- **b = [“hello”, “helloworld”, “he”, “hao”, “good”]
  按list里面单词长度倒叙**

```python
def test():

    b = ["hello", "helloworld", "he", "hao", "good"]
    count = {}
    # 循环查看数组汇总每个字符串的长度
    for i in b:
        # 将数据统计称字典格式，字符串作为键，字符串长度作为值
        count[i] = len(i)
    
    # 按照字典的值，将字典数据从大到小排序
    message = sorted(count.items(), key=lambda x:x[1], reverse=True)

    lists = []
    for j in message:
        # 循环把处理后的数据，加入到新的数组中
        lists.append(j[0])

    print(lists)

test()

结果：
['helloworld', 'hello', 'good', 'hao', 'he']

Process finished with exit code 0

1234567891011121314151617181920212223242526
```

**L1 = [1, 2, 3, 11, 2, 5, 3, 2, 5, 33, 88]
如何用一行代码得出[1, 2, 3, 5, 11, 33, 88]**

```python
print(sorted(set(L1)))

结果：
[1, 2, 3, 5, 11, 33, 88]

Process finished with exit code 0
123456
```

- **将列表中的重复值取出(仅保留第一个)，要求保留原始列表顺序
  如a=[3, 2, 1, 4, 2, 6, 1] 输出[3, 2, 1, 4, 6]**

```python
a = [3, 2, 1, 4, 2, 6, 1]

lists = []
for i in a:
    if i not in lists:
        lists.append(i)
print(lists)

结果：
[3, 2, 1, 4, 6]

Process finished with exit code 0
123456789101112
```

- **a = [1, 3, 5, 7]
  b = [‘a’, ‘b’, ‘c’, ‘d’]
  如何得到[1, 3, 5, 7, ‘a’, ‘b’, ‘c’, ‘d’]**

```python
a = [1, 3, 5, 7]
b = ['a', 'b', 'c', 'd']

for i in b:
    a.append(i)

print(a)

结果：
[1, 3, 5, 7, 'a', 'b', 'c', 'd']

Process finished with exit code 0
123456789101112
```

- **用一行代码生成一个包含 1-10 之间所有偶数的列表**

```python
print([i for i in range(2, 11, 2) if i % 2 == 0])

结果：
[2, 4, 6, 8, 10]

Process finished with exit code 0
123456
```

- **列表a = [1,2,3,4,5], 计算列表成员的平方数，得到[1,4,9,16,25]**

```python
a = [1, 2, 3, 4, 5]
lists = []

for i in a:
    lists.append(i*i)

print(lists)

结果：
[1, 4, 9, 16, 25]

Process finished with exit code 0
123456789101112
```

- **使用列表推导式，将列表中a = [1, 3, -3, 4, -2, 8, -7, 6]
  找出大于0的数，重新生成一个新的列表**

```python
a = [1, 3, -3, 4, -2, 8, -7, 6]

print([i for i in a if i > 0])

结果：
[1, 3, 4, 8, 6]

Process finished with exit code 0
12345678
```

- **统计在一个队列中的数字，有多少个正数，多少个负数，如[1, 3, 5, 7, 0, -1, -9, -4, -5, 8]**

```python
def test():
    
    lists = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
    
    # 定义一个变量，计算正数
    positive_num = 0
    # 计算负数
    negative_num = 0

    for i in lists:
        # 判断循环数组中的数据大于0，则正数会+1
        if i > 0:
            negative_num += 1
        
        # 因为 0 既不是正数也不是负数，所以我们判断小于0为负数
        elif i < 0:
            positive_num += 1 

    return positive_num, negative_num


print(test())

结果：
(4, 5)

Process finished with exit code 0
12345678910111213141516171819202122232425262728
```

- **a = [“张三”,”张四”,”张五”,”王二”] 如何删除姓张的**

```python
def test():
    a = ["张三", "张四", "张五", "王二"]

    for i in a[:]:
        if i[0] == '张':
            a.remove(i)

    return a


print(test())

结果：
['王二']

Process finished with exit code 0

1234567891011121314151617
```

在实现这个需求的时候，踩到了一个坑，就是当我在for循环判断数组中的姓名第一个等于张的时候，当时的代码判断是这样写的

```powershell
 for i in a:
        if i[0] == '张':
12
```

然后打印出来的数据是 [‘张四’, ‘王二’]，我当时还有写疑惑，我的逻辑判断是对的，为什么‘张四’这个名称会被打印出来，于是我打了一个断点查看了一下。

发现当第一个‘张三’被删除之后，再次循环时，直接跳过了‘张三’，百度查了才知道，如图：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20210520212046649.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80Mzg2NTAwOA==,size_16,color_FFFFFF,t_70)
感兴趣的小伙伴，可以查看这篇文章：https://www.cnblogs.com/zhouziyuan/p/10137086.html

- **有个列表a = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8] 使用filter 函数过滤出大于0的数**

```python
a = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8]


def test(a):
    return a < 0


temlists = filter(test, a)
print(list(temlists))

结果：
[-1, -9, -4, -5]

Process finished with exit code 0
1234567891011121314
```

- **列表b = [“张三”, “张四”, “张五”, “王二”] 过滤掉姓张的姓名**

```python
b = ["张三", "张四", "张五", "王二"]


def test(b):
    return b[0] != '张'


print(list(filter(test, b)))

结果：
['王二']

Process finished with exit code 0

1234567891011121314
```

- **过滤掉列表中不及格的学生
  a = [
  {“name”: “张三”, “score”: 66},
  {“name”: “李四”, “score”: 88},
  {“name”: “王五”, “score”: 90},
  {“name”: “陈六”, “score”: 56},
  ]**

```python
a = [
       {"name": "张三", "score": 66},
       {"name": "李四", "score": 88},
       {"name": "王五", "score": 90},
       {"name": "陈六", "score": 56}
]


print(list(filter(lambda x: x.get("score") >= 60, a)))

返回：
[{'name': '张三', 'score': 66}, {'name': '李四', 'score': 88}, {'name': '王五', 'score': 90}]
12345678910111213
```

- 有**个列表 a = [1, 2, 3, 11, 2, 5, 88, 3, 2, 5, 33]
  找出列表中最大的数，出现的位置，下标从0开始**

```python
def test():

    a = [1, 2, 3, 11, 2, 5, 88, 3, 2, 5, 33]

    # 找到数组中最大的数字
    b = max(a)

    count = 0
    # 定义一个计数器，每次循环一个数字的时候，则计数器+1，用于记录数字的下标
    for i in a:
        count += 1
        # 判断当循环到最大的数字时，则退出
        if i == b:
            break

    return count -1


print(test())
结果：
6

Process finished with exit code 0
1234567891011121314151617181920212223
```

- **a = [
  ‘my’, ‘skills’, ‘are’, ‘poor’, ‘I’, ‘am’, ‘poor’, ‘I’,
  ‘need’, ‘skills’, ‘more’, ‘my’, ‘ability’, ‘are’,
  ‘so’, ‘poor’
  ]
- **找出列表中出现次数最多的元素**

```python
def test():

   a = [
      "my", "skills", "are", "poor", "I", "am", "poor", "I",
      "need", "skills", "more", "my", "ability", "are",
      "so", "poor"
   ]

   dicts = {}
   for i in a:

      # 统计数组中每个字符串出现的次数，将数据存入到字典中
      if i not in dicts.keys():
         dicts[i] = a.count(i)

   # 找到字典中最大的key
   return sorted(dicts.items(), key=lambda x: x[1], reverse=True)[0][0]


print(test())

结果：
poor

Process finished with exit code 0
1234567891011121314151617181920212223242526
```

- **给定一个整数数组A及它的大小n，同时给定要查找的元素val，
  请返回它在数组中的位置(从0开始)，若不存在该元素，返回-1。
  若该元素出现多次请返回第一个找到的位置
  如 A1=[1, “aa”, 2, “bb”, “val”, 33]
  或 A2 = [1, “aa”, 2, “bb”]**

```python
def test(lists, string):
   """
   
   :param lists: 数组
   :param string: 查找的字符串
   :return: 
   """

   # 判断字符串不再数组中，返回-1
   if string not in lists:
      return -1

   count = 0
   # 获取字符串当前所在的位置
   for i in lists:
      count += 1
      if i == string:
         return count - 1


print(test([1, "aa", "val",  2, "bb", "val", 33], 'val'))

结果：
2

Process finished with exit code 0
1234567891011121314151617181920212223242526
```

- **给定一个整数数组nums 和一个目标值target ，请你在该数组中找出和为目标值的那两个整数，并返回他
  们的数组下标。
  你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
  示例:
  给定nums=[2，7，11，15]，target=9
  因为nums[0] + nums[1] =2+7 = 9
  所以返回[0， 1]**

```python
def test(target=9):
    num = [2, 7, 11, 15]
    # 统计数组的长度
    length = len(num)
    dicts = {}

    for i in range(length):
        # 添加两个 for 循环，第二次for循环时，循环的位置会比第一次循环多一次
        for j in range(i + 1, length):
            
            # 将循环后的数据放在列表中，利用字典 key 唯一的属性处理数据
            dicts.update({num[i] + num[j]: {i, j}})
        
    # 打印出来的数据，是元素的格式，按照题目，将数据转行成字典
    lists = []
    for nums in dicts[target]:
        lists.append(nums)

    return lists


print(test())

结果：
[0, 1]

Process finished with exit code 0
123456789101112131415161718192021222324252627
```

- **a = [[1,2],[3,4],[5,6]] 如何一句代码得到 [1, 2, 3, 4, 5, 6]**

```python
a = [[1, 2], [3, 4], [5, 6]]

# 定义一个新数组存放数据
lists = []

for i in a:
    # 二次 for 循环，将数据存入到 lists 中
    for j in i:
        lists.append(j)

print(lists)

结果：
[1, 2, 3, 4, 5, 6]

Process finished with exit code 0
12345678910111213141516
```

- **二维数组取值(矩阵),有 a = [[“A”, 1], [“B”, 2]] ，如何取出 2**

```python
import numpy


a = [["A", 1], ["B", 2]]

x = numpy.array(a)
print(x[1, 1])

结果：
2

Process finished with exit code 0
123456789101112
```

- 列表转字符串，L = [1, 2, 3, 5, 6]，如何得出 ‘12356’？

```python
L = [1, 2, 3, 5, 6]
# 使用推导式，将数组中的数字转成 str 类型
lists = [str(i) for i in L]
print(''.join(lists))

结果：
12356

Process finished with exit code 0

12345678910
```

- **a = [“a”, “b”, “c”]
  b = [1, 2, 3]
  如何得到 {‘a’: 1, ‘b’: 2, ‘c’: 3}**

```python
a = ["a", "b", "c"]
b = [1, 2, 3]

c = {k: v for k, v in zip(a, b)}
print(c)

结果：
{'a': 1, 'b': 2, 'c': 3}
12345678
```

- **如下列表
  people = [
  {“name”:”yoyo”, “age”: 20},
  {“name”:”admin”, “age”: 28},
  {“name”:”zhangsan”, “age”: 25},
  ]
  按年龄age从小到大排序**

```python
people = [
   {"name": "yoyo", "age": 20},
   {"name": "admin", "age": 28},
   {"name": "zhangsan", "age": 25},
]


print(sorted(people, key=lambda x: x['age'], reverse=True))

结果：
[{'name': 'admin', 'age': 28}, {'name': 'zhangsan', 'age': 25}, {'name': 'yoyo', 'age': 20}]

Process finished with exit code 0

1234567891011121314
```

- **现有 nums=[2, 5, 7] ，如何在该数据最后插入一个数字 9 ，如何在2后面插入数字0**

```python
nums=[2, 5, 7]

nums.append(9)
nums.insert(1, 0)

print(nums)

结果：
[2, 0, 5, 7, 9]

Process finished with exit code 0

123456789101112
```

- **有个列表a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  如何打乱列表a的顺序,每次得到一个无序列表**

```python
import random

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

random.shuffle(a)

print(a)

结果：
[2, 7, 9, 4, 8, 1, 3, 5, 6]

Process finished with exit code 0
12345678910111213
```

- **输出1-100除3余1 的数，结果为tuple**

```python
tuples = ()
for i in range(1, 101):

    # 判断除以 3 余 1 的数
    if i % 3 == 1:
        # 将数据加入元祖中
        tuples += (i, )

print(tuples)

12345678910
```

- **将(‘a’, ‘b’, ‘c’, ‘d’, ‘e’) 和 (1,2, 3, 4, 5)两个tuple转成
  （1， 2， 3， 4， 5）为key, (‘a’, ‘b’, ‘c’, ‘d’, ‘e’) 为value的字典**

```python
def test():
    a = (1, 2, 3, 4, 5)
    b = ("a", "b", "c", "d", "e")

    # 使用 zip 函数将元素组合成多个元祖
    c = list(zip(a, b))
    dicts = {}

    # 将数据转换成字典类型
    for i in c:
        dicts[i[0]] = i[1]
    return dicts


print(test())
结果：
{1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

Process finished with exit code 0
12345678910111213141516171819
```

- **将字典里的值是数值型的转换为字符串，如a = {‘aa’: 11, ‘bb’: 222}
  得到{‘aa’: ‘11’, ‘bb’: ‘222’}**

```python
def test():
    a = {'a': 11, 'bb': 222}

    for i in a.items():
        a.update({i[0]: str(i[1])})

    return a

结果：
{'a': '11', 'bb': '222'}

Process finished with exit code 0

12345678910111213
```

- **a = [1,2,3] 和 b = [(1),(2),(3) ] 以及 c = [(1,),(2,),(3,) ] 的区别？**

```python
a = [1,2,3]正常的列表
b = [(1),(2),(3)] 虽然列表的每个元素加上了括号，但是当括号内只有一个元素并且没有逗号时，其数据类型是元素本身的数据类型
b = [(1,),(2,),(3,)]列表中的元素类型都是元组类型
123
```

- **map函数,有个列表a = [1, 2, 3, 4] 计算列表中每个数除以2 取出余数 得到 [1,0,1,0]**

```python
ef test():
    a = [1, 2, 3, 4]

    lists = []
    for i in a:
        lists.append(i % 2)
    return lists


print(test())

结果：
[1, 0, 1, 0]

Process finished with exit code 0

12345678910111213141516
```

- **map函数将列表 [1,2,3,4,5] 使用python方法转变成 [1,4,9,16,25]**

```python
def test():
    a = [1, 2, 3, 4, 5]

    new_list = []
    for i in a:
        new_list.append(i*i)
    return new_list


print(test())

结果：
[1, 4, 9, 16, 25]

Process finished with exit code 0
123456789101112131415
```

- **map函数对列表a=[1,3,5],b=[2,4,6]相乘得到[2,12,30]**

```python
a = [1, 3, 5]
b = [2, 4, 6]

print(list(map(lambda x, y: x*y, a, b)))

结果：
[2, 12, 30]

Process finished with exit code 0
123456789
```

- **reduce函数计算1-100的和**

```python
from functools import reduce


def test():
    lists = []
    
    # for 循环往列表中加入1-100的数据
    for i in range(1, 101):
        lists.append(i)
    
    # 实现数据相加
    return reduce(lambda x, y: x + y, lists)


print(test())

结果：
5050

Process finished with exit code 0
1234567891011121314151617181920
```

- **两个字典合并a={“A”:1,”B”:2},b={“C”:3,”D”:4}**

```python
a = {"A": 1, "B": 2}
b = {"C": 3, "D": 4}
b.update(a)
print(b)

结果：
{'C': 3, 'D': 4, 'A': 1, 'B': 2}

Process finished with exit code 0

12345678910
```

- **m1={‘a’:1,’b’:2,’c’:1} # 将同样的value的key集合在list里，输出{1:[‘a’,’c’],2:[‘b’]}**

```python
def test():
    m1={"a": 1, "b": 2, "c": 1}
    
    new_dict = {}
    
    # 循环 m1 字典中的数据
    for key, value in m1.items():
        
        # 判断如果 m1 字典中的值不在新定义的 new_dist 字典中
        if value not in new_dict:
            # 则往新字典中添加键值对
            new_dict[value] = [key]
        else:
            # 如果添加的键已经存在了，则直接添加值
            new_dict[value].append(key)
            
    return new_dict


print(test())

结果：
{1: ['a', 'c'], 2: ['b']}

Process finished with exit code 0

1234567891011121314151617181920212223242526
```

- **d={“name”:”zs”,”age”:18,”city”:”深圳”,”tel”:”1362626627”}
  字典根据键从小到大排序**

```python
def test():
    d = {"name": "zs", "age": 18, "city": "深圳", "tel": "1362626627"}
    # 将字典中的数据进行排序
    dict2 = sorted(d.items(), key=lambda d: d[0], reverse=False)

    # 排序之后的数据类型会变成列表类型，这里将数据重新转换成字典
    new_dict = {}
    for i in dict2:
        new_dict[i[0]] = i[1]

    return new_dict


print(test())

结果：
{'age': 18, 'city': '深圳', 'name': 'zs', 'tel': '1362626627'}

Process finished with exit code 0

1234567891011121314151617181920
```

- **a = [2, 3, 8, 4, 9, 5, 6]
  b = [2, 5, 6, 10, 17, 11]
  1.找出a和b中都包含了的元素
  2.a或b中包含的所有元素
  3.a中包含而集合b中不包含的元素**

```python
a = [2, 3, 8, 4, 9, 5, 6]
b = [2, 5, 6, 10, 17, 11]

# 并集
print(list(set(a).union(set(b))))

# 交集
print(list(set(a).intersection(set(b))))

# 差集
print(list(set(a) ^ set(b)))


结果：
[3, 4, 8, 9, 10, 11, 17]
[2, 3, 4, 5, 6, 8, 9, 10, 11, 17]
[2, 5, 6]

Process finished with exit code 0
12345678910111213141516171819
```

- **函数计算10！**

```python
def f(num):
    if num == 1 or num == 0:
        return 1

    else:
        # 利用递归方式实现
        return num * f(num - 1)

print(f((10)))
结果：
3628800

Process finished with exit code 0
12345678910111213
```

- **有1、2、3、4数字能组成多少互不相同无重复数的三位数?
  分别打印这些三位数的组合**

```python
l = ["1", "2", "3", "4"]

n = len(l)

for i in range(n):
    for j in range(n):
        for k in range(n):
            if i != k and k != j and i != j:
                print(l[i] + l[j] + l[k])
123456789
```

- **在以下文本中找出 每行中长度超过3的单词:**
  Call me Ishmael. Some years ago - never mind how long precisely - having
  little or no money in my purse, and nothing particular to interest me
  on shore, I thought I would sail about a little and see the watery part
  of the world. It is a way I have of driving off the spleen, and regulating
  the circulation. - Moby Dick

python的预期结果(尽量不超过3行搞定):
[[‘Call’, ‘Ishmael.’, ‘Some’, ‘years’, ‘never’, ‘mind’, ‘long’, ‘precisely’, ‘having’],
[‘little’, ‘money’, ‘purse,’, ‘nothing’, ‘particular’, ‘interest’],
[‘shore,’, ‘thought’, ‘would’, ‘sail’, ‘about’, ‘little’, ‘watery’, ‘part’],
[‘world.’, ‘have’, ‘driving’, ‘spleen,’, ‘regulating’],
[‘circulation.’, ‘Moby’, ‘Dick’]]]

```python
a='''Call me Ishmael. Some years ago - never mind how long precisely - having
little or no money in my purse, and nothing particular to interest me
on shore, I thought I would sail about a little and see the watery part
of the world. It is a way I have of driving off the spleen, and regulating
the circulation. - Moby Dick'''

list1=[[j for j in i.split(' ') if len(j)>3 ]for i in a.split('\n')]

print(list1)


结果：
[['Call', 'Ishmael.', 'Some', 'years', 'never', 'mind', 'long', 'precisely', 'having'], ['little', 'money', 'purse,', 'nothing', 'particular', 'interest'], ['shore,', 'thought', 'would', 'sail', 'about', 'little', 'watery', 'part'], ['world.', 'have', 'driving', 'spleen,', 'regulating'], ['circulation.', 'Moby', 'Dick']]

Process finished with exit code 0
123456789101112131415
```

- **a = [11, 2, 33, 1, 5, 88, 3]
  冒泡排序：
  依次比较两个相邻的元素，如果顺序（如从小到大、首字母从A到Z）
  错误就把他们交换过来**

```python
def bubbleSort(arr):
    n = len(arr)

    # 遍历所有数组元素
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [11, 2, 33, 1, 5, 88, 3]

bubbleSort(arr)
print(arr)

结果：
[1, 2, 3, 5, 11, 33, 88]

Process finished with exit code 0
12345678910111213141516171819202122
```

- **有一个数据list of dict如下
  a = [
  {“yoyo1”: “123456”},
  {“yoyo2”: “123456”},
  {“yoyo3”: “123456”},
  ]
  写入到本地一个txt文件，内容格式如下：
  yoyo1,123456
  yoyo2,123456
  yoyo3,123456**

```python
def test():
    a = [
        {"yoyo1": "123456"},
        {"yoyo2": "123456"},
        {"yoyo3": "123456"},
    ]

    # 打开一个名为 test.txt 的文件，如果文件不存在，则自动创建
    with open('test.txt', 'w') as f:

        for i in a:
            # 循环数组中的字典
            for key, value in i.items():
                # 将数据存入 txt 文件中
                f.write("{0},{1}\n".format(key, value))
                print("{0},{1}\n".format(key, value))
                

test()
1234567891011121314151617181920
```