import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

font_set = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=12)

# 读取泰坦尼克号数据集
df = pd.read_csv("./python数据清数据/train.csv")
print("=== 原始数据前10行 ===")
print(df.head(10))
print("\n")
# 查看数据基本信息
print("=== 数据信息 ===")
print(df.info())
print("\n")
# 查看缺失值情况
print("=== 缺失值统计 ===")
print(df.isnull().sum())
print("\n")
# Age 用中位数填充
df['Age'] = df['Age'].fillna(df['Age'].median())
print("=== Age 缺失值用中位数填充后 ===")
print("Age 缺失值数量:", df['Age'].isnull().sum())
print("\n")
# Embarked 用众数填充
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
print("=== Embarked 缺失值用众数填充后 ===")
print("Embarked 缺失值数量:", df['Embarked'].isnull().sum())
print("\n")
# Cabin 缺失值太多(77%)，填充为'Unknown'
df['Cabin'] = df['Cabin'].fillna('Unknown')
print("=== Cabin 缺失值填充为 Unknown ===")
print("Cabin 缺失值数量:", df['Cabin'].isnull().sum())
print("\n")
# 确认所有缺失值已处理
print("=== 处理后缺失值统计 ===")
print(df.isnull().sum())
print("\n")
# 描述性统计
print("=== 描述性统计 ===")
print(df.describe())
print("\n")
# 按性别统计存活率
print("=== 按性别统计存活率 ===")
print(df.groupby('Sex')['Survived'].mean())
print("\n")
# 按船舱等级统计存活率
print("=== 按船舱等级(Pclass)统计存活率 ===")
print(df.groupby('Pclass')['Survived'].mean())
print("\n")
# 按登船港口统计存活率
print("=== 按登船港口(Embarked)统计存活率 ===")
print(df.groupby('Embarked')['Survived'].mean())

# 绘制存活率对比图
fig, axes = plt.subplots(1, 3, figsize=(14, 5))

# 子图1: 按性别统计存活率
surv_sex = df.groupby('Sex')['Survived'].mean()
axes[0].bar(surv_sex.index, surv_sex.values, color=['lightcoral', 'steelblue'])
axes[0].set_title('按性别存活率', fontproperties=font_set)
axes[0].set_xlabel('性别', fontproperties=font_set)
axes[0].set_ylabel('存活率', fontproperties=font_set)

# 子图2: 按船舱等级统计存活率
surv_pclass = df.groupby('Pclass')['Survived'].mean()
axes[1].bar(surv_pclass.index.astype(str), surv_pclass.values, color='steelblue')
axes[1].set_title('按船舱等级存活率', fontproperties=font_set)
axes[1].set_xlabel('舱位等级', fontproperties=font_set)
axes[1].set_ylabel('存活率', fontproperties=font_set)

# 子图3: 按登船港口统计存活率
surv_embarked = df.groupby('Embarked')['Survived'].mean()
axes[2].bar(surv_embarked.index, surv_embarked.values, color='steelblue')
axes[2].set_title('按登船港口存活率', fontproperties=font_set)
axes[2].set_xlabel('登船港口', fontproperties=font_set)
axes[2].set_ylabel('存活率', fontproperties=font_set)

plt.tight_layout()
plt.show()