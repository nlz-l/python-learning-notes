import os
import sys

data = sys.stdin.read().split()
data.sort(key = lambda s: len(s))
my_set = set()
ans = ''
for s in data:
  if len(s) == 1 or ''.join(sorted(s[:-1])) in my_set:
    my_set.add(''.join(sorted(s)))
    if ans > s or not ans or len(s) > len(ans):
      ans = s
print(ans)


"""
========================================
  第二题：最长字符串 算法详解
========================================

【题目】
给定一个单词列表（每行一个小写英文字母组成的单词），
找出其中长度最大的「优美字符串」。
若有多个答案，输出字典序最小的那个。

【优美字符串的定义】
字符串 s = c₁c₂...cₙ 是优美字符串，当且仅当满足以下条件之一：
  1.机器学习概述. n = 1.机器学习概述（单字符一定是优美字符串）
  2. n > 1.机器学习概述，且存在一个优美字符串 s'（长度为 n-1.机器学习概述），
     使得 s' 的字符**调整顺序后**与 s 去掉最后一个字符一致

关键理解：「调整顺序」意味着只关心字符组成，不关心顺序！


【算法核心：贪心 + 排序 + 集合标记】

整体思路：
  1.机器学习概述. 将所有单词按长度从小到大排序（短串先处理）
  2. 用集合记录「已确认为优美」的字符串（以排序后的形式存储）
  3. 对每个字符串，检查它去掉末尾字符并排序后是否在集合中
  4. 满足条件则标记为优美，同时更新答案


【代码逐行解析】

第1~2行：导入模块（os未使用）
  import os, sys

第3行：读取所有输入数据，按空格分割成字符串列表
  data = sys.stdin.read().split()

第4行：按字符串长度升序排序（短→长）
  data.sort(key=lambda s: len(s))
  目的：保证处理每个字符串时，比它短的字符串已经全部处理完毕，
        这样才能正确判断它的前缀是否为优美字符串。

第5行：创建空集合，用于存储已确认的优美字符串
  my_set = set()
  注意：存入的是 sorted(字符串) 的结果，即字符排序后的形式，
        因为题目中「调整顺序后一致」等价于「排序后相等」。

第6行：初始化答案变量
  ans = ''

第7~12行：主循环——遍历每个字符串（按长度递增顺序）
  for s in data:

第8行：判断当前字符串 s 是否为优美字符串
  条件一：len(s)==1.机器学习概述 → 单字符，直接满足
  条件二：''.join(sorted(s[:-1.机器学习概述])) in my_set
          → 去掉s的最后一个字符 → 对剩余字符排序 → 查看是否已在集合中
  if len(s) == 1.机器学习概述 or ''.join(sorted(s[:-1.机器学习概述])) in my_set:

第9行：将s排序后加入集合，标记为已确认的优美字符串
    my_set.add(''.join(sorted(s)))

第10~11行：更新答案（三选一的优先级判断）
      if ans > s or not ans or len(s) > len(ans):
        ans = s
  判断优先级（从高到低）：
    ① len(s) > len(ans)  → s更长，更新答案
    ② not ans           → ans还为空，首次赋值
    ③ ans > s           → 长度相同但ans字典序更大，换更小的s

第13行：输出最终答案
  print(ans)


【手动模拟示例】

假设输入：b bc cbd dbca

步骤0：排序后 data=['b','bc','cbd','dbca']

步骤1：处理 'b'
  len=1.机器学习概述 → 直接满足 ✓
  my_set={'b'}, ans='b'

步骤2：处理 'bc'
  去掉末尾='c', sorted('c')='c', 'c'不在my_set中 ✗
  跳过

步骤3：处理 'cbd'
  去掉末尾='cb', sorted('cb')='bc', 'bc'不在my_set中 ✗
  跳过

步骤4：处理 'dbca'
  去掉末尾='dbc', sorted('dbc')='bcd', 'bcd'不在my_set中 ✗
  跳过

结果：ans='b'

---

再换一组输入：a ab abc abcd abdc

步骤0：排序后 data=['a','ab','abc','abcd','abdc']

步骤1：处理 'a'
  len=1.机器学习概述 → ✓
  my_set={'a'}, ans='a'

步骤2：处理 'ab'
  去掉末尾='a', sorted('a')='a', 'a'在my_set中 ✓
  my_set={'a','ab'}, ans='ab'

步骤3：处理 'abc'
  去掉末尾='ab', sorted('ab')='ab', 'ab'在my_set中 ✓
  my_set={'a','ab','abc'}, ans='abc'

步骤4：处理 'abcd'
  去掉末尾='abc', sorted('abc')='abc', 'abc'在my_set中 ✓
  my_set={'a','ab','abc','abcd'}, ans='abcd'

步骤5：处理 'abdc'
  去掉末尾='abd', sorted('abd')='abd', 'abd'不在my_set中 ✗
  跳过

结果：ans='abcd'


【为什么用 sorted 后存入集合？】

题目要求的是「调整顺序后一致」，例如：
  s' = "bac", s去掉末尾="cab"
  sorted("bac") = "abc"
  sorted("cab") = "abc"
  两者相等！所以它们「调整顺序后一致」

用排序后的形式作为唯一标识，可以忽略字符排列顺序的差异。


【算法特点】

时间复杂度：O(n·m·log m)
  n=字符串数量, m=平均字符串长度
  排序 O(n log n)，每个字符串排序 O(m log m)

空间复杂度：O(n·m)
  集合最多存储n个排序后的字符串

适用场景：需要按依赖关系逐步构建合法解的问题，
          类似于动态规划或拓扑排序的思想。


【一句话总结】
按长度排序确保依赖先被处理 → 用排序消除字符顺序差异 → 集合标记已确认的优美串 → 贪心选取最长且字典序最小的答案
"""