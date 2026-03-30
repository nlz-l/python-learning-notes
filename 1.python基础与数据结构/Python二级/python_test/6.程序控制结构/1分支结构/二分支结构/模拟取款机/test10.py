#模拟取款机

#余额
balance = 5000

#接收取款金额
money = int(input("请输入取款金额："))

if money <= balance and money % 100 == 0:
    print("正在准备中，请稍侯. . .")
else:
    print("余额不足或没有输入100的整数倍")
