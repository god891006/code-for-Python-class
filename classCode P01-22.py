print('Hello world!!!')
print('Hello kitty!!!')
print('Hello baby!!!')

print('Sirius 你好：')
print('  请点击激活用户！')

print('Defined(define)')
print('syntaxError--语法错误')
print('nameError--名字错误')
print('Invalid;Character')
print('Built-in(bulitins)')
print('Module')

'''标识符(age  =  18);区分大小写；不能以数字开头；有字母,数字,下划线组成,特殊字符不支持
	#可以用中文，但是不建议
命名规则
	#驼峰式getName,payMoney,getElementsByName
	#类GetName
	#下划线式
	#get_name(Python推荐)
'''
money = 99.9
count = 5
person = 'Sirius'

print(person,'bought',count,'cups and each valued',money,type(money))
money = '9.9元'
count = 99	
person = 'Sirius'

print(person,'bought',count,'cups and each valued',money,type(money))

#列出Python关键词
import keyword
print(keyword.kwlist)

#print函数
print('可以打印',end  =  '')#end = '';默认end = '\n'，当end = ''时，会取消换行
#'可以打印\n'-->'可以打印'
print('字符串','变量',sep  =  ',')
'''sep = 默认分割
\n换行
'''

custom_name = 'Sirius'
print('亲爱的\'',custom_name,'\':\n',
	'\t请点击链接激活',custom_name,'：激活',custom_name)#转移字符：\n换行；\t制表符；\r回车；\"；\'；\''
'''Python支持单引号和双引号的嵌套-->"''";'""'
但是同时单引号和单引号嵌套需要转义字符
'''
print("乔治说：'想玩恐龙！！'")
print('乔治说："想睡觉！！"')
print('\'\'\n','\"\"','\\')

'''\n是newline开个新行
\r是carriage return，打印头回到行首
'''
print('Hello\nKetty')
print('hello\py\thon')
print(r'hello\py\thon')#r raw表示原样输出字符串

'''java final表示常量
#python 常年名为大写，表示常量
'''
NAME = 'Jack'
print('hello')#输出字符串
print(NAME)
print(NAME)

#字符串'' ""
message = "[淘宝正在使用验证码]\n请注意"
print(message)

'''三引号
1.固定格式输出
2.作为注释使用
3.#作为单行注释，三引号作为多行注释，看是否赋值
'''
message = '''
[淘宝]
你正在使用验证码登陆
验证码是：8906
涉及个人账户安全，请保密
'''
print(message)

person = '齐天大圣'
work = '西天取经'
time = '唐朝'
number = 5
#print('我们的英雄'+person+'和唐三藏在'+time+'一起'+work+'一共'+number+'个人')
print('我们的英雄'+person+'和唐三藏在'+time+'一起'+work)
'''
%s,%d,%f占位符，用于格式化输出；
%s，s为string的简写，起到str()的作用；
%d，d为digital的缩写，强制转为整型，起到int()的作用；
%f，f为float的缩写，保留位数输出；
加号为拼接符，只能用于相同类型字段拼接，字符串+字符串可以，字符串+整型会报错；
'''
print('我们的英雄%s和唐三藏在%s一起%s一共%s个人'%(person,time,work,number))
print('我们的英雄'+person+'和唐三藏在'+time+'一起'+work+'一共'+str(number)+'个人')
print(int(99.9))

salary = 8899.32765
print('今年是：%d' % salary)
print('今年是：%.2f' % salary)#保留两位，且四舍五入

#打印练习
#写法一
movie = 'Titanic'
ticket = 49.5
count = 28
print('''
约起来一起看电影！！
电影名称：%s
票价：%.1f 元
观看人数：%d
总票价：%.1f 元
'''
%(movie,ticket,count,ticket*count)
)
#写法二
movie = 'Titanic'
ticket = 49.5
count = 28
message = '''
约起来一起看电影！！
电影名称：%s
票价：%f 元
观看人数：%d
总票价：%.1f 元
'''%(movie,ticket,count,ticket*count)#注意占位符赋值位置

print(message)

'''
字符串格式化输出
方式：1.使用占位符 2.format
format函数注意一一对应
'''
age = 2
name = '春天花花'
message = '乔治说：我今年%d岁了，在%s幼儿园上学' %(age,name)
print(message)
message = '乔治说：我今年{}岁了，在{}幼儿园上学'.format(age,name)
print(message)

#输入input()函数，默认字符串类型
movie = input('请输入电影名称：')
ticket = input('请输入票价：')
ticket = float(ticket)
count = input('请输入人数：')
count = int(count)#可以通过format的形式避免出错
message = '''
约起来一起看电影！！
电影名称：%s
票价：%f 元
观看人数：%d
总票价：%.1f 元
'''%(movie,float(ticket),int(count),float(ticket*count))
print(message)


print('''
**************
捕鱼达人
**************
''')#将算术运算符部分
username = input('请输入用户名：')
password = input('请输入密码：')
print('%s请充值加入游戏' % username)
coins = input('充值金额：')
print(type(coins))
coins = int(coins)
print(type(coins))
print('%s充值成功！当前金额为：%d' %(username,coins))
equipment = input('装备名称：')
update_equipment = input('升级装备名称：')
equipment = update_equipment#赋值
coins = input('购买装备金额：')
print('{}购买了{}装备，充值{}'.format(username,equipment,coins))
print('升级装备名称：',update_equipment)

#运算符operator
name = 'admin'#内存中分配了地址给字符串'admin'，容器name指向该地址，容器中保存的是地址而不是字符串
print(name,id(name))#赋值运算符----> = 
name1 = name#将内存中容器name的地址同样赋给name1，但内存中只有字符串'admin'占有地址
print(name1,id(name1))
name2 = name#将内存中容器name的地址同样赋给name2，python通过这种形式节省内存空间
print(name2,id(name2))
name = 'admin1'#内存的数据池中没有'admin1'，因此在内存中新开辟一个地址赋给'admin1'，name所指向的地址发生改变
#当出现一个新的变量，内存中会增加一个地址赋给新的变量，并改变相关容器的相关指向

#算术运算符 +=  -=  *=  /=
num = 8
num += 5 # num=num+5，+是数学运算符
print(num)
a = 'abc'
a += 'de'
print(a)
a = 'abc'
a += '5'#运算符左右需要是同一类型对象，+号此处是连接符
print(a)
'''
a = 'abc'
a -= 'bc'
print(a)
-=，*=，/=只能用于数值类型的对象运算，不支持string
'''

print('*'*50)
print('\t捕鱼达人')
print('*'*50)

#扩展的算术运算符：**  //
a=9
b=2
result=a*b
print(result)
result=a**b#幂函数运算
print(result)
result=a//b#整除
print(result)
result=a%b#求余数
print(result)
'''
关系运算符
逻辑运算符
位运算符
'''











