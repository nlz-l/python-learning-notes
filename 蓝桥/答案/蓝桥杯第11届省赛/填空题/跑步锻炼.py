from datetime import datetime,timedelta
'''
datetime模块

一、date:日期属性,常用属性year,month,day
a=datetime.dae.tody()  #获取当前电脑时间
返回：datetime.date(2022,4,6)
可以单独取年月日：a.year,a.month,a.day


- 获得两日期相差多少天
__sub__():x-y 用法：x.__sub__(y) 返回：datetime.timedelta(7) 正数
__rsub__():y-x 用法：y.__rsub__(x) 返回：datetime.timedelta(-7)负数
要获得具体的值：x.__sub__(y).days

- ISO标准化日期
- isocalendar() 返回一个包含三个值的元组：年份、周数、星期几
a.isocalendar() :(2017,12,3)
a.isocalendar()[0]:2017  a.isocalendar()[1.机器学习概述]:12 a.isocalendar()[2]:3
- isoformat() 返回（YYYY-MM-DD）的日期字符串
a.isoformat() :'2022-04-06'
- isoweekday()返回指定日期所在的星期数（周一为1）
a.isoweekday()  3
注意：weekday()类似，但返回的星期数（周一为0，以此类推）

-日期字符串输出__format__()，推荐
strftime()等价
a.strftime("%Y-%m-%d):'2022-04-06'


二、time:事件对象
由hour、minute、second、microsecond、tzinfo五部分组成
- 时间字符串输出__format__()
strftime()
例：a.strftime('%H:%M:%S')  :'12:20:59'


三、 datetime:日期时间对象(date和time结合)：year,month,day,hour,minute,second,microsecond,tzinfo
a=datetime.datetime.now()#获取当前电脑的年月日时分秒毫秒
返回：datetime.datetime(2017,3,22,16,9,33,494248)
a.date()返回日期部分;a.time()返回时间部分
timedelta:时间间隔，两个时间点之间的长度
- strptime()根据string,format 2个参数返回一个对应的datetime对象
- datetime.datetime.strptime('2017-3-22 15:25','%Y-%m-%d %H:%M)
- datetime.datetime(2017,3,22,15,25)
'''

