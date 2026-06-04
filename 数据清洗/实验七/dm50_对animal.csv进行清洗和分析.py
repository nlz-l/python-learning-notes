import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

font_set = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf", size=12)
# 读取animal.csv，将'NA'和'NULL'都识别为缺失值
df = pd.read_csv("./python数据清数据/animal.csv", na_values=['NA', 'NULL'])
print("=== 原始数据 ===")
print(df)
print("\n")
# 查看数据基本信息
print("=== 数据信息 ===")
print(df.info())
print("\n")
# 查看描述性统计
print("=== 描述性统计 ===")
print(df.describe())
print("\n")
# 查看缺失值情况
print("=== 缺失值统计 ===")
print(df.isnull().sum())
print("\n")
# 用每列的均值填充缺失值
df_filled = df.fillna(df.mean(numeric_only=True))
print("=== 均值填充后 ===")
print(df_filled)
print("\n")
# 按动物种类分组统计各颜色均值
print("=== 各动物种类的颜色均值 ===")
print(df_filled.groupby('animal').mean())
print("\n")

# 添加总和列
df_filled['total'] = df_filled.iloc[:, :-1].sum(axis=1)
print("=== 添加总和列 ===")
print(df_filled)
print("\n")

# 找出总和最大的动物
print("=== 总和最大的动物 ===")
print(df_filled.loc[df_filled['total'].idxmax()])

# 绘制各动物颜色对比柱状图
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 子图1: 各动物颜色堆积对比
color_cols = ['white', 'red', 'blue', 'pink', 'black', 'green']
df_filled.set_index('animal')[color_cols].plot(kind='bar', ax=axes[0], rot=0)
axes[0].set_title('各动物颜色值对比', fontproperties=font_set)
axes[0].set_xlabel('动物', fontproperties=font_set)
axes[0].set_ylabel('颜色值', fontproperties=font_set)

# 子图2: 各动物颜色总分对比
df_filled.set_index('animal')['total'].plot(kind='bar', ax=axes[1], color='steelblue', rot=0)
axes[1].set_title('各动物颜色总分', fontproperties=font_set)
axes[1].set_xlabel('动物', fontproperties=font_set)
axes[1].set_ylabel('总分', fontproperties=font_set)

plt.tight_layout()
plt.show()