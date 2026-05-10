# 导包
import os
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from utils.log import Logger
from utils.common import data_preprocessing
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, mean_absolute_error, root_mean_squared_error, mean_absolute_percentage_error
import joblib


plt.rcParams['font.family'] = 'SimHei'
plt.rcParams['font.size'] = 15

# 1. 定义电力负荷模型类, 配置日志, 获取数据源
class PowerLoadModel:
    def __init__(self,file_path):
        # 1.2 拼接日志文件名.
        logfile_name = 'train'+pd.to_datetime(datetime.datetime.now()).strftime('%Y%m%d%H%M%S')
        # 1.3 创建日志对象.
        self.logfile = Logger('../', logfile_name).get_logger()
        # 测试写一条日志.
        self.logfile.info('开始创建 电力负荷模型类的 对象了')
        # 1.4 获取数据源.
        self.data_source = data_preprocessing(file_path)

# 2. 查看数据的整体分布情况
def ana_data(data): # analysis: 分析
    """
    1.查看数据整体情况
    2.负荷整体的分布情况
    3.各个小时的平均负荷趋势，看一下负荷在一天中的变化情况
    4.各个月份的平均负荷趋势，看一下负荷在一年中的变化情况
    5.工作日与周末的平均负荷情况，看一下工作日的负荷与周末的负荷是否有区别
    :param data: 数据源
    :return:
    """
    # 0. 为了防止会修改原数据,我们做一次拷贝
    ana_data= data.copy()
    # 1. 查看数据整体情况

    ana_data.info

    # 2. 负荷整体的分布情况, 直方图
    # 2.1 创建画布
    fig = plt.figure(figsize=(20, 40))
    # 2.2 创建子图
    ax1 = fig.add_subplot(411)
    ax1.hist(ana_data['power_load'],bins=100)  #负荷 直方图 20个区间
    ax1.set_title('负荷整体分布情况')
    ax1.set_xlabel('负荷')

    # 3.各个小时的平均负荷趋势，看一下负荷在一天中的变化情况
    # 3.1 新增一列, 充当小时
    ana_data['hour'] = ana_data['time'].str[11:13]
    # 3.2 根据小时分组, 计算平均值
    hour_load_mean = ana_data.groupby('hour',as_index=False)['power_load'].mean()
    # 3.3 绘制折线图
    ax2 = fig.add_subplot(412)
    ax2.plot(hour_load_mean['hour'],hour_load_mean['power_load'])
    ax2.set_title('各个小时的平均负荷趋势')
    ax2.set_xlabel('小时')

    # 4.各个月份的平均负荷趋势，看一下负荷在一年中的变化情况
    ana_data['month'] = ana_data['time'].str[5:7]
    month_load_mean = ana_data.groupby('month',as_index=False)['power_load'].mean()
    ax3 = fig.add_subplot(413)
    ax3.plot(month_load_mean['month'],month_load_mean['power_load'])
    ax3.set_title('各月份的平均负荷趋势')
    ax3.set_xlabel('月份')

    # 5.工作日与周末的平均负荷情况，看一下工作日的负荷与周末的负荷是否有区别
    ana_data['weekday'] = ana_data['time'].apply(lambda x: pd.to_datetime(x).weekday())
    ana_data['is_holiday'] = ana_data['weekday'].apply(lambda x: 1 if x in [5,6] else 0)
    week_load_mean =ana_data[ana_data['is_holiday']==0].power_load.mean()
    holiday_load_mean =ana_data[ana_data['is_holiday']==1].power_load.mean()
    ax4 = fig.add_subplot(414)
    ax4.bar(['工作日','周末'],[week_load_mean,holiday_load_mean])
    ax4.set_title('工作日与周末的平均负荷情况')
    ax4.set_xlabel('类别')
    plt.savefig('../data/fig/负荷整体的分布情况.png')
    plt.show()

# 3. 特征工程(重点)
def feature_engineering(data, logger):
    """
    对给定的数据源，进行特征工程处理，提取出关键的特征
    1.提取出时间特征：月份、小时
    2.提取出相近时间窗口中的负荷特征：step大小窗口的负荷
    3.提取昨日同时刻负荷特征
    4.剔除出现空值的样本
    5.整理时间特征，并返回
    :param data: 数据源
    :param logger: 日志
    :return:
    """
    # 1.提取出时间特征：月份、小时
    feature_data = data.copy()
    feature_data['hour'] = feature_data['time'].str[11:13]
    feature_data['month'] = feature_data['time'].str[5:7]
    # 热编码 one-hot处理 hour 和 month 字段.
    # feature_data = pd.get_dummies(feature_data,columns=['hour','month'])
    hour_month_data = pd.get_dummies(feature_data[['hour','month']])
    # print(hour_month_data.head())
    # print(hour_month_data.info())
    feature_data = pd.concat([feature_data,hour_month_data],axis=1)
    # print(feature_data.info())

    # 2.提取出相近时间窗口中的负荷特征：step大小窗口的负荷
    # 2.1 获取上一个小时的负荷
    load_1h_data = feature_data['power_load'].shift(1)
    # 2.2 获取两个小时的负荷
    load_2h_data = feature_data['power_load'].shift(2)
    # 2.3 获取三个小时的负荷
    load_3h_data = feature_data['power_load'].shift(3)
    # 2.4 拼接
    load_shift_data = pd.concat([load_1h_data,load_2h_data,load_3h_data],axis=1)
    # 2.5 修改列名
    load_shift_data.columns = ['前1小时','前2小时','前3小时']
    # 2.6 拼接
    feature_data = pd.concat([feature_data,load_shift_data],axis=1)
    # print(feature_data.info())

    # 3.提取昨日同时刻负荷特征
    # 3.1 给特征新增一列名, yesterday_time
    feature_data['yesterday_time'] = feature_data['time'].apply(lambda x:(pd.to_datetime(x) - datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S'))
    # 3.2 我们把所有的 日期 和 负荷 拼接成字典, 方便查找.
    time_load_dict = feature_data.set_index('time')['power_load'].to_dict()
    # print(time_load_dict)
    # 3.3 新增一列 yesterday_load 表示: 昨日相同时间点的负荷.
    feature_data['yesterday_load'] = feature_data['yesterday_time'].apply(lambda x:time_load_dict.get(x))
    # 4.剔除出现空值的样本
    feature_data = feature_data.dropna()
    # 5.整理时间特征，并返回
    feature_columns = list(hour_month_data.columns) + list(load_shift_data.columns) + ['yesterday_load']
    print(feature_columns) # ['hour_00', 'hour_01', 'hour_02', 'hour_03', 'hour_04', 'hour_05', 'hour_06', 'hour_07', 'hour_08', 'hour_09', 'hour_10', 'hour_11', 'hour_12', 'hour_13', 'hour_14', 'hour_15', 'hour_16', 'hour_17', 'hour_18', 'hour_19', 'hour_20', 'hour_21', 'hour_22', 'hour_23', 'month_01', 'month_02', 'month_03', 'month_04', 'month_05', 'month_06', 'month_07', 'month_08', 'month_09', 'month_10', 'month_11', 'month_12', '前1小时', '前2小时', '前3小时', 'yesterday_load']
    # 6. 返回结果.
    return feature_data, feature_columns

# 4. 模型训练, 评估, 保存
def model_train(data, features, logger):
    """
    1.数据集切分
    2.网格化搜索与交叉验证
    3.模型实例化
    4.模型训练
    5.模型评价
    6.模型保存
    :param data: 特征工程处理后的输入数据
    :param features: 特征名称
    :param logger: 日志对象
    :return:
    """
    # 1.数据集切分
    x = data[features]
    y = data['power_load']
    # print(x.shape,y.shape)
    # print(x.head(10))
    # print(y.head(10))
    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=23
                                                        )
    # 2.网格化搜索与交叉验证
    # logger.info('------ 网格搜索 + 交叉验证 寻找最优超参 ------')
    # logger.info(f'开始时间: {datetime.datetime.now()}')
    # # 2.1 定义参数字典
    # param_dict = {
    #     'n_estimators': [50, 100, 150, 200],
    #     'max_depth': [3, 5, 6, 7],
    #     'learning_rate': [0.01,0.1],
    # }
    # # 2.2 创建XGBoost 模型对象.(Extreme Gradient Boosting Tree, 极限梯度提升树)
    # estimator = XGBRegressor()
    # # 2.3 创建网格搜索对象
    # gs = GridSearchCV(estimator,param_grid=param_dict,cv=5)
    # # 2.4 模型训练
    # gs.fit(x_train,y_train)
    # # 2.5 打印最优参数组合
    # logger.info(f'最优参数组合: {gs.best_params_}')
    # logger.info(f'结束时间: {datetime.datetime.now()}')
    # 3.模型实例化
    estimator = XGBRegressor(n_estimators=100,max_depth=7,learning_rate=0.1)
    # 4.模型训练
    estimator.fit(x_train,y_train)
    y_pred = estimator.predict(x_test)
    # 5.模型评价
    print(f'均方误差: {mean_squared_error(y_test,y_pred)}')
    print(f'均方根误差: {root_mean_squared_error(y_test,y_pred)}')
    print(f'平均绝对误差: {mean_absolute_error(y_test,y_pred)}')
    # print(f'平均绝对百分比误差: {mean_absolute_percentage_error(y_test,y_pred)}')

    # 6.模型保存
    joblib.dump(estimator,'../model/xgb_20260503.pkl') # pickle文件 -> 后缀名一般是 .pkl, .hth .pickle
    logger.info(f'模型保存成功!保存路径为:{os.path.abspath('../model/xgb_20260503.pkl')}')
# 5. 测试
if __name__ == '__main__':
    # 5.1 创建电力负荷预测模型对象
    pm = PowerLoadModel('../data/train.csv')
    # 5.2 打印数据源.
    # print(pm.data_source)

    # 5.3 查看数据分布.
    # ana_data(pm.data_source)

    # 5.4 特征工程.
    feature_data, feature_columns = feature_engineering(pm.data_source,pm.logfile)

    # 5.5 模型训练.
    model_train(feature_data, feature_columns, pm.logfile)