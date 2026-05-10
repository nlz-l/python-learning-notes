"""
案例:
    基于用户的 年收入 和 消费指数, 根据用户的 相似性 进行 聚类
"""
import os
os.environ['OMP_NUM_THREADS'] = '1'
# 导包
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.metrics import calinski_harabasz_score,silhouette_score
import pandas as pd

# 1. 定义函数, 找聚类的K值.
def dm01_find_k():

    # 1. 加载数据集.
    df = pd.read_csv('./data/customers.csv')
    #df.info()
    #print(df.head())

    # 2. 定义sse_list,sc_list,记录不同K值的评估效果
    sse_list = []
    sc_list = []
    # 抽取特征
    x = df.iloc[:, 3: 5]
    # 3. 定义for训练,测试不同k值的效果.
    for k in range(2, 20):
        # 3.1 创建KMean对象.
        estimator = KMeans(n_clusters=k, n_init=100, random_state=23)
        # 3.2 模型训练.
        estimator.fit(x)
        # 3.3 模型预测.
        y_pred = estimator.predict(x)
        # 3.4 获取sse值.
        sse_list.append(estimator.inertia_)
        # 3.5 获取sc值.
        sc_list.append(silhouette_score(x, y_pred))
    # 4. 绘制sse和sc的折线图
    plt.figure(figsize=(20, 10))
    plt.plot(range(2,20), sse_list, label='SSE')
    plt.show()
    plt.figure(figsize=(20, 10))
    plt.plot(range(2,20), sc_list, label='SC')
    plt.show()

    # 结论 : K = 5的时候模型效果最好
# 2. 定义函数, 实现: 模型训练, 模型预测, 模型评估
def dm02_train_predict_evaluate():
    # 1. 加载数据集.
    df = pd.read_csv('./data/customers.csv')
    # 2. 抽取特征.
    X = df.iloc[:, 3: 5]
    # 3. 创建KMean对象.
    estimator = KMeans(n_clusters=5, n_init=100, random_state=23)
    # 4. 模型训练.
    estimator.fit(X)
    # 5. 模型预测.
    y_pred = estimator.predict(X)
    # 6.绘制5个族的 样本点 -> 散点图
    plt.scatter(X.values[y_pred == 0, 0], X.values[y_pred == 0, 1], c='red', label='Standard')
    plt.scatter(X.values[y_pred == 1, 0], X.values[y_pred == 1, 1], c='blue', label='Traditional')
    plt.scatter(X.values[y_pred == 2, 0], X.values[y_pred == 2, 1], c='green', label='Normal')
    plt.scatter(X.values[y_pred == 3, 0], X.values[y_pred == 3, 1], c='cyan', label='Youth')
    plt.scatter(X.values[y_pred == 4, 0], X.values[y_pred == 4, 1], c='magenta', label='TA')
    # 7.绘制5个族的 质心 -> 散点图
    print(estimator.cluster_centers_)
    plt.scatter(estimator.cluster_centers_[:, 0],estimator.cluster_centers_[:, 1],c='black',label='Centroids')
    # 8 添加标题, 坐标轴标签, 显示
    plt.title('Clusters of customers')
    plt.xlabel('Annual Income (k$)')
    plt.ylabel('Spending Score (1-100)')
    plt.legend(loc='best')
    plt.show()
# 3. 测试
if __name__ == '__main__':
    # dm01_find_k()
    dm02_train_predict_evaluate()