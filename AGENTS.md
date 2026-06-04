# AGENTS.md

始终使用中文进行对话交流。

This file provides guidance to Codex (Codex.ai/code) when working with code in this repository.

## 项目概述

湖北文理学院 · 信息与计算科学 · 2023 级 Python 学习笔记仓库。涵盖 Python 基础、数据分析、机器学习、深度学习、NLP、网络爬虫、蓝桥杯竞赛题解。

## 环境

项目共有三个 conda 虚拟环境，根据任务选择合适的：

| 环境名 | 用途 | Python 解释器路径 |
|--------|------|-------------------|
| `env` | 通用（数据分析、机器学习、爬虫） | `C:/Users/nlz/.conda/envs/env/python.exe` |
| `nlpbase` | NLP（CPU） | `C:/Users/nlz/.conda/envs/nlpbase/python.exe` |
| `nlpbase2` | NLP（GPU） | `C:/Users/nlz/.conda/envs/nlpbase2/python.exe` |

运行任何 Python 脚本或 Jupyter notebook 前先激活对应环境：

```bash
conda activate env        # 通用
conda activate nlpbase    # NLP CPU
conda activate nlpbase2   # NLP GPU
```

依赖安装：

```bash
pip install -r requirements.txt
```

## 目录结构要点

- `1.pythonBasicsAndDataStructures/` — 按学习顺序编号的 6 个模块（面向对象→面向对象高级→闭包和装饰器→网编和多线程→生成器与正则表达式→数据结构与算法初步），含 Python 二级内容，每个模块含 `.py` 文件和随堂 `.md` 笔记
- `2.Data_Analysis/` — Jupyter Notebook（NumPy、Pandas、Matplotlib、Seaborn），含链家数据集练习和 RFM 综合案例
- `3.MachineLearning/` — 9 个模块（概述→KNN→线性回归→逻辑回归→决策树→集成学习→KMeans→电力负荷预测案例）
- `4.DeepLearning/` — PyTorch 框架、ANN、CNN、RNN，部分子目录含 `data/` 和 `model/` 文件夹（被 gitignore 排除）
- `5.NLP/` — 文本预处理、RNN变体、Transformer、迁移学习、NLP精选问题，含 NLP 阶段大纲
- `网络爬虫/` — 实验作业（二、三、四、六）+ 报告作业 + 期中 + source（数据源），涉及 Requests、Selenium、JSON 爬取、HTML
- `机器学习(作业)/` — 实验作业（五至十一、十三），与机器学习课程配套
- `蓝桥/` — 答案（第4-12届官方题解）+ 自练（十一、十二、十五、十六届个人练习）
- `数据清洗/` — 数据清洗相关学习内容
- `test/` — 测试/练习脚本
- `求职Agent/` — 被 gitignore 排除，不上传 GitHub

## 注意事项

- 大部分代码为 Jupyter Notebook (`.ipynb`)，直接阅读或运行 `jupyter notebook` 启动
- `4.DeepLearning/*/data/` 和 `4.DeepLearning/*/model/` 目录内容不上传（已在 `.gitignore` 中排除）
- `手写数字识别.csv` 和 `*.pkl` 文件也不上传
