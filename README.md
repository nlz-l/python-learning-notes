# Python 学习笔记

[![Python](https://img.shields.io/badge/python-3.10+-blue)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.x-013243)](https://numpy.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.x-150458)](https://pandas.pydata.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.x-EE4C2C)](https://pytorch.org/)
[![Scikit--learn](https://img.shields.io/badge/scikit--learn-1.x-F7931E)](https://scikit-learn.org/)

系统化的 Python 数据科学全栈学习仓库，涵盖基础语法、数据分析、机器学习、深度学习、NLP、网络爬虫和蓝桥杯竞赛。

**作者**：刘文博 | **学校**：湖北文理学院 · 信息与计算科学 · 2023 级

---

## 📂 目录结构

```text
python-learning-notes/
├── 1.pythonBasicsAndDataStructures/   # Python 基础与数据结构
│   ├── 1-面向对象/                     #   面向对象基础
│   ├── 2-面向对象高级/                 #   高级 OOP
│   ├── 3-闭包和装饰器/                 #   函数式编程
│   ├── 4-网编和多线程/                 #   socket、threading
│   ├── 5-生成器与正则表达式/           #   yield、re 模块
│   └── 6-数据结构与算法初步/           #   链表、树、排序、查找
├── 2.Data_Analysis/                   # 数据分析（Notebook）
│   ├── NumPy/                          #   数组运算
│   ├── Pandas/                         #   数据读写、CRUD、高级语法
│   ├── Matplotlib/                     #   基础绑图
│   ├── Seaborn/                        #   统计图表
│   ├── 链家数据集练习/                 #   实战案例
│   └── RFM案例/                        #   客户价值分析
├── 3.MachineLearning/                  # 机器学习
│   ├── 1-概述/                         #   ML 基础概念
│   ├── 2-KNN算法/                      #   K 近邻
│   ├── 3-线性回归/                     #   线性回归
│   ├── 4-逻辑回归/                     #   逻辑回归
│   ├── 5-决策树/                       #   决策树
│   ├── 6-集成学习/                     #   Bagging、Boosting
│   ├── 7-KMeans/                       #   聚类
│   └── 8-电力负荷预测/                 #   综合案例
├── 4.DeepLearning/                     # 深度学习
│   ├── 1-PyTorch框架/                  #   张量、自动求导
│   ├── 2-ANN/                          #   人工神经网络
│   ├── 3-CNN/                          #   卷积神经网络
│   └── 4-RNN/                          #   循环神经网络
├── 5.NLP/                              # 自然语言处理
│   ├── text_preprocessing/             #   文本预处理
│   ├── RNN_variants/                   #   RNN 变体
│   ├── Transformer/                    #   Transformer 架构
│   ├── transferLearning/               #   迁移学习
│   └── NLP精选问题/                    #   专题讨论
├── 网络爬虫/                           # 爬虫实验
├── 机器学习(作业)/                     # ML 课程作业
├── 蓝桥/                               # 蓝桥杯竞赛
│   ├── 答案/                           #   第 4-12 届官方题解
│   └── 自练/                           #   第 11/12/15/16 届练习
├── 数据清洗/                           # 数据清洗专题
└── 网页展示/                           # 个人展示页
```

---

## 🔧 环境配置

项目使用三个 conda 虚拟环境，按需激活：

| 环境名 | 用途 | Python 路径 |
|---|---|---|
| `env` | 通用（数据分析、机器学习、爬虫） | `C:/Users/nlz/.conda/envs/env/python.exe` |
| `nlpbase` | NLP（CPU） | `C:/Users/nlz/.conda/envs/nlpbase/python.exe` |
| `nlpbase2` | NLP（GPU，需要 CUDA） | `C:/Users/nlz/.conda/envs/nlpbase2/python.exe` |

```bash
conda activate env              # 通用
conda activate nlpbase          # NLP CPU
conda activate nlpbase2         # NLP GPU

pip install -r requirements.txt
```

---

## 📖 模块详解

### 1. Python 基础与数据结构

6 个递进模块，含 Python 二级考试内容：

| 模块 | 内容 |
|---|---|
| 面向对象 | 类、对象、继承、多态 |
| 面向对象高级 | `__slots__`、描述符、元类 |
| 闭包和装饰器 | 高阶函数、`@decorator` |
| 网编和多线程 | socket、threading、queue |
| 生成器与正则 | yield、re、迭代器 |
| 数据结构与算法 | 链表、二叉树、排序、查找 |

### 2. 数据分析

Jupyter Notebook 交互式学习：
- **NumPy**：ndarray 操作、广播、线性代数
- **Pandas**：DataFrame、CSV/JSON/Excel 读写、CRUD
- **Matplotlib / Seaborn**：基础图表与统计可视化
- **实战案例**：链家房源数据探索、RFM 客户价值分析

### 3. 机器学习

9 个模块从理论到实战：

```text
概述 → KNN → 线性回归 → 逻辑回归 → 决策树 → 集成学习 → KMeans → 电力负荷预测
```

### 4. 深度学习

基于 PyTorch 框架：
- 张量运算与自动求导
- ANN / CNN / RNN 网络构建

### 5. NLP

文本处理全流程：
- 分词、去停用词、词向量
- RNN / LSTM / GRU 序列模型
- Transformer / BERT 迁移学习

### 网络爬虫

Requests → JSON API → HTML 解析 → Selenium 动态渲染

### 蓝桥杯

官方题解（第 4-12 届）+ 个人练习（第 11、12、15、16 届），涵盖枚举、递归、DP、日期处理、字符串、图论。

---

## 🚀 运行方式

```bash
# Jupyter Notebook
jupyter notebook

# Python 脚本（先 cd 到脚本所在目录，部分脚本使用相对路径读取数据）
cd 3.MachineLearning/5-决策树/
python script.py

# 蓝桥杯题解
python 蓝桥/自练/15届/solution.py
```

---

## 🎯 学习路线

```text
第一阶段           第二阶段          第三阶段          第四阶段
Python 基础  →  数据分析  →  机器学习 / 深度学习  →  专项深入
                                ├── NLP            ├── 爬虫
                                ├── 蓝桥杯          └── 竞赛
                                └── 深度学习
```

---

## 🔗 相关项目

- **R 语言**：[R](../R/) — R 数据分析与可视化
- **课程作业**：[python课上作业](../python课上作业/) — Python 课程报告
- **AI 项目**：[lc-course](../lc-course/)、[Dify](../Dify/)
