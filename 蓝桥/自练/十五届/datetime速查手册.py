"""
========================================
  Python datetime 模块速查手册
  （蓝桥杯/竞赛专用）
========================================

【一、模块导入】
"""
from datetime import datetime, timedelta, date

"""
【二、三个核心对象】

┌─────────────────────────────────────────────┐
│  对象          含义           示例          │
│─────────────────────────────────────────────│
│  datetime      具体时刻       2024-01-15 14:30:00 │
│  timedelta     时间段/时长    3天2小时30分钟       │
│  date          只有日期        2024-01-15         │
└─────────────────────────────────────────────┘
"""

# ============================================
# 【三、创建 datetime 对象】
# ============================================

# 方法1：直接指定年月日时分秒
t1 = datetime(2024, 1, 15, 14, 30, 0)
print(t1)   # 2024-01-15 14:30:00

# 方法2：获取当前时间
t2 = datetime.now()
print(t2)   # 当前时间

# 方法3：从时间戳创建（秒数→时间）
import time
t3 = datetime.fromtimestamp(1705312800)
print(t3)   # 2024-01-16 00:00:00

# ============================================
# 【四、字符串 ↔ 时间互转（最常用！）】
# ============================================

# 4.1.机器学习概述 字符串 → datetime（解析）strptime = string parse time
s = "2016-09-07 18:24:33"
t = datetime.strptime(s, '%Y-%m-%d %H:%M:%S')
print(t)    # 2016-09-07 18:24:33

# 4.2 datetime → 字符串（格式化）strftime = string format time
t = datetime(2024, 1, 15, 14, 30, 0)
s = t.strftime('%Y-%m-%d %H:%M:%S')
print(s)    # "2024-01-15 14:30:00"

# 4.3 格式符号表（必背！）

"""
┌──────┬──────────┬──────────┐
│ 符号  │ 含义      │ 范围/示例 │
├──────┼──────────┼──────────┤
│ %Y   │ 四位年份  │ 0001~9999│
│ %y   │ 两位年份  │ 00~99    │
│ %m   │ 月份      │ 01~12    │
│ %d   │ 日期      │ 01~31    │
│ %H   │ 小时(24制)│ 00~23    │
│ %I   │ 小时(12制)│ 01~12    │
│ %M   │ 分钟      │ 00~59    │
│ %S   │ 秒        │ 00~59    │
│ %A   │ 星期全名  │ Monday   │
│ %a   │ 星期缩写  │ Mon      │
│ %B   │ 月份全名  │ January  │
│ %b   │ 月份缩写  │ Jan      │
└──────┴──────────┴──────────┘

记忆口诀：
  Y大写=年(Year), m小写=月(month), d小写=日(day)
  H大写=时(Hour), M大写=分(Minute), S大写=秒(Second)

注意区分大小写！%M 是分钟，不是月份！
"""

# 常用格式示例：
datetime.strptime("2024-03-05", "%Y-%m-%d")         # 只有日期
datetime.strptime("14:30:00", "%H:%M:%S")            # 只有时间
datetime.strptime("2024/03/05", "%Y/%m/%d")          # 斜杠分隔
datetime.strptime("20240305", "%Y%m%d")              # 无分隔符

# ============================================
# 【五、时间加减 —— timedelta】
# ============================================

t = datetime(2024, 1, 15, 14, 30, 0)

# 往后推
t_plus = t + timedelta(days=3, hours=2, minutes=30)
print(t_plus)    # 2024-01-18 17:00:00

# 往前推
t_minus = t - timedelta(days=1, hours=30)
print(t_minus)   # 2024-01-14 08:30:00

# 只加一种
t + timedelta(days=7)       # 加一周
t + timedelta(hours=12)     # 加半天
t + timedelta(minutes=45)   # 加45分钟
t + timedelta(seconds=90)   # 加90秒
t + timedelta(weeks=2)      # 加两周

# ============================================
# 【六、时间相减 → 得到 timedelta】
# ============================================

t1 = datetime(2024, 12, 31, 23, 59, 59)
t2 = datetime(2024, 1, 1, 0, 0, 0)

delta = t1 - t2
print(delta)              # 364 days, 23:59:59
print(type(delta))        # <class 'datetime.timedelta'>

# 取出总时长
total_sec = delta.total_seconds()          # 总秒数（浮点数）
total_min = delta.total_seconds() // 60    # 总分钟数（整数）
total_hour = delta.total_seconds() // 3600 # 总小时数（整数）
days = delta.days                           # 天数部分

# ============================================
# 【七、取出时间的各部分】
# ============================================

t = datetime(2024, 1, 15, 14, 30, 25)

print(t.year)     # 2024   年
print(t.month)    # 1.机器学习概述      月
print(t.day)      # 15     日
print(t.hour)     # 14     时
print(t.minute)   # 30     分
print(t.second)   # 25     秒
print(t.weekday()) # 0=周一, 6=周日

# ============================================
# 【八、修改时间的某一部分】
# ============================================

t = datetime(2024, 1, 15, 14, 30, 25)

t1 = t.replace(second=0)     # 秒归零 → 2024-01-15 14:30:00
t2 = t.replace(hour=9)       # 改小时 → 2024-01-15 09:30:25
t3 = t.replace(year=2025)    # 改年份 → 2025-01-15 14:30:25

# ============================================
# 【九、比较大小】
# ============================================

t1 = datetime(2024, 1, 1)
t2 = datetime(2024, 12, 31)

print(t1 < t2)    # True
print(t2 - t1)    # 364 days, 0:00:00

# ============================================
# 【十、蓝桥杯实战模板】
# ============================================

"""
模板1：计算两个时间差（分钟）
"""
def diff_minutes(time_str1, time_str2):
    t1 = datetime.strptime(time_str1, '%Y-%m-%d %H:%M:%S')
    t2 = datetime.strptime(time_str2, '%Y-%m-%d %H:%M:%S')
    return int((t2 - t1).total_seconds() // 60)

"""
模板2：给定时间，往回推到最近的整点周期（B4题）
"""
def last_alarm(time_str, interval):
    t = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
    epoch = datetime(1970, 1, 1, 0, 0, 0)
    delta = t - epoch
    d = (delta.total_seconds() // 60) % interval
    result = t - timedelta(minutes=d)
    return result.replace(second=0)

"""
模板3：判断某年是否闰年
"""
def is_leap_year(year):
    import calendar
    return calendar.isleap(year)
    # 或者：(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

"""
模板4：获取某月有多少天
"""
def days_in_month(year, month):
    import calendar
    return calendar.monthrange(year, month)[1]

"""
模板5：日期+1天 / -1天
"""
t = datetime(2024, 1, 31)
next_day = t + timedelta(days=1)    # 2024-02-01（自动进位！）
prev_day = t - timedelta(days=1)    # 2024-01-30

# ============================================
# 【十一、常见错误】
# ============================================

"""
❌ 错误1：strptime 格式不匹配
  datetime.strptime("2024-1.机器学习概述-5", "%Y-%m-%d")
  → 输入是 1.机器学习概述 和 5（一位），格式要求 %m %d（两位）
  ✅ 改成：datetime.strptime("2024-01-05", "%Y-%m-%d")
     或：datetime.strptime("2024-1.机器学习概述-5", "%Y-%-m-%-d")

❌ 错误2：timedelta 参数拼写错误
  timedelta(day=3)        ❌ 应该是 days（复数）
  timedelta(minute=30)    ❌ 应该是 minutes（复数）

❌ 错误3：忘记 total_seconds()
  delta = t1 - t2
  print(delta / 60)       ❌ 不支持直接除
  ✅ print(delta.total_seconds() // 60)

❌ 错误4：replace 返回新对象
  t.replace(second=0)     # 没有改变 t 本身！
  print(t.second)         # 还是原来的值
  ✅ t = t.replace(second=0)  需要重新赋值

❌ 错误5：字符串和 datetime 直接拼接
  "今天是" + datetime.now()  ❌ TypeError
  ✅ "今天是" + str(datetime.now())
  ✅ f"今天是{datetime.now()}"
"""

# ============================================
# 【十二、快速参考卡】
# ============================================

"""
┌──────────────────────────────────────────────────────────┐
│                    一张图记住所有操作                      │
├──────────────────────────────────────────────────────────┤
│                                                          │
│   "2024-01-15 14:30:00"                                  │
│        ↓ strptime()                                      │
│   ┌─────────────────┐                                   │
│   │  datetime 对象   │ ← datetime(2024,1.机器学习概述,15,14,30,0)    │
│   └────────┬────────┘                                   │
│            │                                            │
│     ┌──────┴──────┐                                     │
│     ▼             ▼                                     │
│  strftime()   +/- timedelta                              │
│     │             │                                     │
│     ▼             ▼                                     │
│  "2024-01-15    新的 datetime                            │
│   14:30:00"     对象                                    │
│                                                          │
│   datetime - datetime = timedelta                        │
│   timedelta.total_seconds() = 总秒数                     │
│                                                          │
└──────────────────────────────────────────────────────────┘
"""

print("datetime 速查手册加载完成!")