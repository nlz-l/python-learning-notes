# Python 学习笔记

本项目整理了 Python 课程学习、数据分析、机器学习、深度学习、NLP、网络爬虫、蓝桥杯练习以及个人项目实验。内容覆盖基础语法到综合实践，适合作为阶段性学习资料库。

## 目录结构

```text
1.pythonBasicsAndDataStructures/  Python 基础与数据结构
2.Data_Analysis/                  NumPy、Pandas、Jupyter 等数据分析练习
3.MachineLearning/                机器学习算法、案例和实验项目
4.DeepLearning/                   深度学习相关练习
5.NLP/                            自然语言处理相关练习
网络爬虫/                         requests、HTML、JSON、网页数据采集
蓝桥/                             蓝桥杯省赛题解和个人练习
数据清洗/                         数据清洗专题练习
机器学习(作业)/                   机器学习课程作业
求职Agent/                        Agent 应用实验
网页展示/                         个人网页或 HTML 展示页面
test/                             临时测试代码
```

## 模块说明

### Python 基础与数据结构

包含面向对象、闭包、装饰器、网络编程、多线程、生成器、正则表达式、链表、二叉树、排序和查找等内容。适合按学习顺序逐个主题复习。

### 数据分析

主要使用 Jupyter Notebook 练习 NumPy、Pandas、CSV/JSON 读写、数据清洗、统计汇总和基础可视化。适合配合真实数据集完成探索式分析。

### 机器学习

包含算法实验和案例项目，例如集成学习对比、电力负荷预测等。部分项目会保存数据、模型、日志和工具函数，适合练习完整的建模流程。

### 网络爬虫

包含 requests 请求、JSON 接口解析、HTML 页面解析、Excel 保存等练习，适合学习从网页采集结构化数据的基本流程。

### 蓝桥杯

收录蓝桥杯省赛官方题解和个人练习题，重点训练枚举、递归、动态规划、日期处理、字符串、图形输出和常见算法模板。

## 推荐环境

- Python 3.10 或更高版本
- Jupyter Notebook / JupyterLab
- 常用依赖：

```bash
pip install numpy pandas matplotlib seaborn scikit-learn xgboost lightgbm jupyter requests beautifulsoup4 openpyxl
```

不同子目录的依赖可能不同，运行前请根据具体脚本补充安装。

## 运行方式

启动 Notebook：

```bash
jupyter notebook
```

运行普通 Python 脚本：

```bash
python 文件名.py
```

如果脚本依赖数据文件，建议先进入脚本所在目录，再执行命令，避免相对路径找不到数据。

## 学习建议

1. 先完成 Python 基础与数据结构，打牢语法和算法基础。
2. 再学习数据分析，掌握 Notebook、NumPy 和 Pandas。
3. 之后进入机器学习和深度学习项目，练习从数据到模型评估的完整流程。
4. 网络爬虫和蓝桥杯可以作为专项训练，用来提高工程实践和算法熟练度。
