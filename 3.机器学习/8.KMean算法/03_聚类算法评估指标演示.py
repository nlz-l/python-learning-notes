"""

案例:
    演示聚类算法的评估指标, 即: SSE + 肘部法, SC轮廓系数法, CH轮廓系数法

聚类算法评估指标:
    思路1: SSE + 肘部法:
        SSE:
            概述:
                所有簇的 所有样本到该簇质心的 误差的平方和.
            特点:
                随着K值的增加, SSE值会逐渐减少
            目标:
                SSE越小, 代表族内样本越聚集, 内聚程度越高.
        肘部法:
            K值越大, SSE就会随之减小, 下降梯度陡然变缓的时候, 那个K值,就是我们要的最佳值
    思路2: SC轮廓系数:
        考虑簇内 -> 聚集程度, 越小越好
        考虑簇间 -> 分离程度, 越大越好
    思路3: CH轮廓系数:
        考虑簇内 -> 聚集程度, 越小越好
        考虑簇间 -> 分离程度, 越大越好
        考虑K值 -> K值越小,代表簇内样本越聚集, 内聚程度越高.
"""
import os
os.environ['OMP_NUM_THREADS'] = '4'
# 导包
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.metrics import calinski_harabasz_score,silhouette_score


# 1. 定义函数, 演示: SSE + 肘部法
def dm01_sse():
    # 1. 定义SSE列表, 记录每个K值对应的SSE值.
    sse_list = []
    # 2. 生成数据集.
    x, y = make_blobs(
        n_samples=1000,
        n_features=2,
        centers=[[-1,-1],[0,0],[1,1],[2,2]],
        cluster_std=[0.4,0.2,0.2,0.4],
        random_state=23)
    # 3. for训练遍历, 获取到每个K值, 计算其对应的 sse值, 并添加到 sse_list中.
    for k in range(1, 100):
        # 3.1 创建KMean对象.指定K值,最大迭代次数, 随机种子.
        estimator = KMeans(n_clusters=k, n_init=100, random_state=23)
        # 3.2 模型训练.
        estimator.fit(x)
        # 3.3 模型预测.
        # 3.4 获取每个簇的sse值.
        sse_value = estimator.inertia_
        # 3.5 添加到 sse_list中.
        sse_list.append(sse_value)
    # 4. 数据的可视化.
    # 4.1 创建画布.
    plt.figure(figsize=(20, 10))
    # 参1: K值, 参2: SSE值
    # 4.2 设置标题
    plt.title('SSE value')
    # 4.3 设置x的刻度
    plt.xticks(range(1, 100, 3))
    # 4.4 添加x轴,y轴的标签
    plt.xlabel('K')
    plt.ylabel('sse')
    # 4.5 绘制网格
    plt.grid()
    # 4.6 绘制折线图
    plt.plot(range(1, 100), sse_list)
    # 4.7 显示图形
    plt.show()
# 2. 定义函数, 演示: SC轮廓系数法
def dm02_sc():
        # 1. 定义SC轮廓系数列表, 记录每个K值对应的SC轮廓系数值.
    sc_list = []
    # 2. 生成数据集.
    x, y = make_blobs(
        n_samples=1000,
        n_features=2,
        centers=[[-1,-1],[0,0],[1,1],[2,2]],
        cluster_std=[0.4,0.2,0.2,0.4],
        random_state=23)
    # 3. for训练遍历, 获取到每个K值, 计算其对应的 sc轮廓系数值, 并添加到 sc_list中.
    for k in range(2, 100):
        # 3.1 创建KMean对象.指定K值,最大迭代次数, 随机种子.
        estimator = KMeans(n_clusters=k, n_init=10, random_state=23)
        # 3.2 模型训练.
        estimator.fit(x)
        # 3.3 模型预测.
        y_pred = estimator.predict(x)
        # 3.4 获取每个簇的sc轮廓系数值.
        sc_value = silhouette_score(x, y_pred)
        # 3.5 添加到 sc_list中.
        sc_list.append(sc_value)
    # 4. 数据的可视化.
    # 4.1 创建画布.
    plt.figure(figsize=(20, 10))
    # 参1: K值, 参2: SC值
    # 4.2 设置标题
    plt.title('SC value')
    # 4.3 设置x的刻度
    plt.xticks(range(1, 100, 3))
    # 4.4 添加x轴,y轴的标签
    plt.xlabel('K')
    plt.ylabel('sc')
    # 4.5 绘制网格
    plt.grid()
    # 4.6 绘制折线图
    plt.plot(range(2, 100), sc_list)
    # 4.7 显示图形
    plt.show()
# 3. 定义函数, 演示: CH轮廓系数法
def dm03_ch():

    # 1. 定义ch轮廓系数列表, 记录每个K值对应的ch轮廓系数值.
    ch_list = []
    # 2. 生成数据集.
    x, y = make_blobs(
        n_samples=1000,
        n_features=2,
        centers=[[-1, -1], [0, 0], [1, 1], [2, 2]],
        cluster_std=[0.4, 0.2, 0.2, 0.4],
        random_state=23)
    # 3. for训练遍历, 获取到每个K值, 计算其对应的 ch轮廓系数值, 并添加到 ch_list中.
    for k in range(2, 100):
        # 3.1 创建KMean对象.指定K值,最大迭代次数, 随机种子.
        estimator = KMeans(n_clusters=k, n_init=10, random_state=23)
        # 3.2 模型训练.
        estimator.fit(x)
        # 3.3 模型预测.
        y_pred = estimator.predict(x)
        # 3.4 获取每个簇的ch轮廓系数值.
        ch_value = calinski_harabasz_score(x, y_pred)
        # 3.5 添加到 ch_list中.
        ch_list.append(ch_value)
    # 4. 数据的可视化.
    # 4.1 创建画布.
    plt.figure(figsize=(20, 10))
    # 参1: K值, 参2: ch值
    # 4.2 设置标题
    plt.title('ch value')
    # 4.3 设置x的刻度
    plt.xticks(range(1, 100, 3))
    # 4.4 添加x轴,y轴的标签
    plt.xlabel('K')
    plt.ylabel('ch')
    # 4.5 绘制网格
    plt.grid()
    # 4.6 绘制折线图
    plt.plot(range(2, 100), ch_list)
    # 4.7 显示图形
    plt.show()
# 4. 测试
if __name__ == '__main__':
    # dm01_sse()
    # dm02_sc()
    dm03_ch()