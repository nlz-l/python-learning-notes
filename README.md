# Python 学习笔记

![Python](https://img.shields.io/badge/python-3.10+-blue)
![NumPy](https://img.shields.io/badge/NumPy-1.x-013243)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458)
![PyTorch](https://img.shields.io/badge/PyTorch-2.x-EE4C2C)
![Scikit--learn](https://img.shields.io/badge/scikit--learn-1.x-F7931E)
![Status](https://img.shields.io/badge/status-active-brightgreen)

系统化的 Python 数据科学全栈学习仓库，涵盖 Python 基础、数据分析、机器学习、深度学习、NLP、网络爬虫、蓝桥杯竞赛和 AI Agent 应用。

**作者**：刘文博 | **学校**：湖北文理学院 · 信息与计算科学 · 2023 级

## 目录结构

```text
python-learning-notes/
├── 1.pythonBasicsAndDataStructures/   # Python 基础与数据结构
│   ├── 1-面向对象/                     # OOP 核心概念
│   ├── 2-面向对象高级/                 # 高级 OOP 特性
│   ├── 3-闭包和装饰器/                 # 函数式编程
│   ├── 4-网编和多线程/                 # socket、threading
│   ├── 5-生成器与正则表达式/           # yield、re 模块
│   └── 6-数据结构与算法初步/           # 链表、树、排序、查找
├── 2.Data_Analysis/                   # 数据分析（Jupyter Notebook）
│   ├── NumPy/                          # 数组运算
│   ├── Pandas/                         # 数据读写、CRUD、高级语法
│   ├── Matplotlib/                     # 基础绑图
│   ├── Seaborn/                        # 统计图表
│   ├── 链家数据集练习/                 # 实战案例
│   └── RFM案例/                        # 客户价值分析
├── 3.MachineLearning/                  # 机器学习
│   ├── 1-概述/                         # ML 基础概念
│   ├── 2-KNN算法/                      # K 近邻
│   ├── 3-线性回归/                     # Linear Regression
│   ├── 4-逻辑回归/                     # Logistic Regression
│   ├── 5-决策树/                       # Decision Tree
│   ├── 6-集成学习/                     # Bagging、Boosting
│   ├── 7-KMeans/                       # 聚类
│   └── 8-电力负荷预测/                 # 综合案例
├── 4.DeepLearning/                     # 深度学习
│   ├── 1-PyTorch框架/                  # 张量、自动求导
│   ├── 2-ANN/                          # 人工神经网络
│   ├── 3-CNN/                          # 卷积神经网络
│   └── 4-RNN/                          # 循环神经网络
├── 5.NLP/                              # 自然语言处理
│   ├── text_preprocessing/             # 文本预处理
│   ├── RNN_variants/                   # RNN 变体
│   ├── Transformer/                    # Transformer 架构
│   ├── transferLearning/               # 迁移学习
│   └── NLP精选问题/                    # 专题讨论
├── 网络爬虫/                           # Web Scraping
│   ├── 实验二 ~ 实验六/               # 爬虫实验作业
│   ├── 报告作业/                       # 实验报告
│   ├── 期中/                           # 期中作业
│   └── source/                         # 数据源
├── 机器学习(作业)/                     # ML 课程作业
│   └── 实验五 ~ 实验十三/
├── 蓝桥/                               # 蓝桥杯竞赛
│   ├── 答案/                           # 第 4-12 届官方题解
│   └── 自练/                           # 第 11/12/15/16 届练习
├── 数据清洗/                           # 数据清洗专题
├── 求职Agent/                          # AI 求职助手应用
├── 网页展示/                           # 个人展示页面
├── test/                               # 测试脚本
├── CLAUDE.md                           # Claude Code 配置
└── README.md
```

## 环境配置

项目使用三个 conda 虚拟环境，按需激活：

| 环境名 | 用途 | Python 路径 |
|---|---|---|
| `env` | 通用（数据分析、机器学习、爬虫） | `C:/Users/nlz/.conda/envs/env/python.exe` |
| `nlpbase` | NLP（CPU） | `C:/Users/nlz/.conda/envs/nlpbase/python.exe` |
| `nlpbase2` | NLP（GPU） | `C:/Users/nlz/.conda/envs/nlpbase2/python.exe` |

```bash
# 激活环境
conda activate env         # 通用任务
conda activate nlpbase     # NLP CPU
conda activate nlpbase2    # NLP GPU（需要 CUDA）

# 安装依赖
pip install -r requirements.txt
```

### 常用依赖

```bash
pip install numpy pandas matplotlib seaborn scikit-learn \
            xgboost lightgbm jupyter requests beautifulsoup4 \
            openpyxl torch torchvision
```

## 模块详解

### 1. Python 基础与数据结构

6 个递进式学习模块，含 Python 二级考试内容：

| 模块 | 内容 | 产出 |
|---|---|---|
| 面向对象 | 类、对象、继承、多态 | `.py` 练习 + `.md` 笔记 |
| 面向对象高级 | `__slots__`、描述符、元类 | `.py` 练习 |
| 闭包和装饰器 | 高阶函数、`@decorator` | `.py` 练习 |
| 网编和多线程 | socket、threading、queue | `.py` 练习 |
| 生成器与正则 | yield、re、迭代器 | `.py` 练习 |
| 数据结构与算法 | 链表、二叉树、排序、查找 | `.py` 练习 |

### 2. 数据分析

Jupyter Notebook 交互式学习，涵盖：
- **NumPy**：ndarray 操作、广播、线性代数
- **Pandas**：DataFrame、数据读写（CSV/JSON/Excel）、CRUD、高级语法
- **Matplotlib / Seaborn**：基础图表与统计可视化
- **实战案例**：链家房源数据集探索、RFM 客户价值分析

### 3. 机器学习

9 个模块，从算法原理到综合案例：

```text
概述 → KNN → 线性回归 → 逻辑回归 → 决策树 → 集成学习 → KMeans → 电力负荷预测
```

每个模块包含算法实现、scikit-learn 调用和模型评估。

### 4. 深度学习

基于 PyTorch 框架：
- 张量运算与自动求导
- ANN / CNN / RNN 网络构建
- `data/` 和 `model/` 目录已加入 `.gitignore`

### 5. NLP

文本处理全流程：
- 分词、去停用词、词向量
- RNN / LSTM / GRU 序列模型
- Transformer / BERT 迁移学习
- NLP 精选问题讨论

### 网络爬虫

从入门到实战的爬虫实验：
- **实验二**：Requests 基础请求
- **实验三**：JSON 接口解析
- **实验四**：HTML 页面解析
- **实验六**：Selenium 动态渲染

### 蓝桥杯

- **答案/**：第 4-12 届省赛官方题解（Python）
- **自练/**：第 11、12、15、16 届个人刷题记录
- 涵盖枚举、递归、DP、日期处理、字符串、图论

### 求职 Agent

AI 驱动的求职助手应用：
- 简历解析与优化
- 职位爬取与匹配
- 自动投递与追踪

> 此目录未上传 GitHub（`.gitignore` 排除）

## 学习路线

```text
第一阶段          第二阶段          第三阶段          第四阶段
 Python 基础  ──→ 数据分析 ──→ 机器学习 ──→ 深度学习
                                │
                                ├──→ NLP
                                ├──→ 爬虫专项
                                └──→ 蓝桥杯算法
```

1. **打基础**：完成 `1.pythonBasicsAndDataStructures/` 全部模块
2. **学分析**：通过 `2.Data_Analysis/` 掌握 NumPy、Pandas、可视化
3. **上模型**：依次学习 `3.MachineLearning/` 中的算法
4. **深钻研**：选择 DL/NLP/爬虫/竞赛方向深入

## 运行方式

### Jupyter Notebook

```bash
jupyter notebook
# 在浏览器中打开对应 .ipynb 文件
```

### Python 脚本

```bash
# 先 cd 到脚本所在目录（部分脚本使用相对路径读取数据）
cd 3.MachineLearning/5-决策树/
python script.py
```

### 蓝桥杯题解

```bash
python 蓝桥/自练/15届/solution.py
```

## Git 忽略说明

| 忽略内容 | 原因 |
|---|---|
| `4.DeepLearning/*/data/`、`4.DeepLearning/*/model/` | 模型/数据文件过大 |
| `手写数字识别.csv`、`*.pkl` | 数据集和序列化文件 |
| `求职Agent/` | 个人项目，不公开 |
| `.ipynb_checkpoints/` | Jupyter 自动生成 |

## 相关链接

- R 语言学习：[R](../R/)
- Python 课程作业：[python课上作业](../python课上作业/)
- 求职 Agent 项目：[求职Agent/](求职Agent/)
