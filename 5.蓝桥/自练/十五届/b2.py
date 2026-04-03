MOD = 10**9 + 7

def mod_pow(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = (exp >> 1)
        base = (base * base) % mod
    return result

def count_valid_strings(n):
    total = mod_pow(9, n, MOD)
    without_3 = mod_pow(8, n, MOD)
    without_7 = mod_pow(8, n, MOD)
    without_37 = mod_pow(7, n, MOD)
    without_37_inclusion = (without_3 + without_7 - without_37) % MOD
    valid_strings = (total - without_37_inclusion) % MOD
    return valid_strings

length = 10000
result = count_valid_strings(length)
print(result)

# print((9**10000 - 8**10000*2 + 7**10000)%(1000000000+7))
MOD = 10**9 + 7
def ks_m(base,pow,MOD):
    result = 1
    base = base % MOD
    while pow > 0:
        if pow % 2 == 1:
            result = (result * base) % MOD
        pow = (pow >> 1)
        base = (base * base) % MOD
    return result
print((ks_m(9,10000,MOD) -2*(ks_m(8,10000,MOD))+ks_m(7,10000,MOD)) % MOD)

"""
========================================
  第十五届第二题：数字串个数 算法详解
========================================

【题目】
构造一个长度为 10000 的数字字符串，满足：
  1. 不能出现数字 0（只能用 1~9）
  2. 必须包含数字 3 和 7（至少各出现一次）

问：满足条件的字符串有多少个？
答案对 10^9+7 取模。

【算法核心：容斥原理 + 快速幂】

思路：
  总方案数 - 不含3的 - 不含7的 + 不含3且不含7的（被多减了，加回来）

  总方案数：每个位置有9种选择(1~9)，共 9^10000 种
  不含3：   每个位置有8种选择(除3外)，共 8^10000 种
  不含7：   每个位置有8种选择(除7外)，共 8^10000 种
  不含3且7：每个位置有7种选择(除3和7外)，共 7^10000 种

  公式：9^n - 8^n - 8^n + 7^n


【代码逐行解析】

第1行：MOD = 10**9 + 7
  取模数，蓝桥杯填空题标准要求

第3~11行：mod_pow(base, exp, mod) —— 快速幂
  用「二分法」计算 (base^exp) % mod
  例：计算 2^13
    13 的二进制 = 1101
    2^13 = 2^8 × 2^4 × 2^1 （只取二进制为1的位）
    
    过程：
      exp=13(奇数): result=1×2=2,  exp→6, base→4
      exp=6(偶数):               exp→3, base→16
      exp=3(奇数):  result=2×16=32, exp→1, base→256
      exp=1(奇数):  result=32×256=8192 → 返回！

  时间复杂度：O(log exp) 而不是 O(exp)
  对于 exp=10000，只需要约14次循环！

第13~25行：count_valid_strings(n) —— 容斥原理计数
  
  第15行：total = mod_pow(9, n, MOD)
    总数：每位9种选择(1~9)
  
  第17行：without_3 = mod_pow(8, n, MOD)
    不含3：每位8种选择(1,2,4,5,6,7,8,9)
  
  第18行：without_7 = mod_pow(8, n, MOD)
    不含7：每位8种选择(1,2,3,4,5,6,8,9)
  
  第19行：without_37 = mod_pow(7, n, MOD)
    不含3也不含7：每位7种选择(1,2,4,5,6,8,9)
  
  第21行：without_37_inclusion = (without_3 + without_7 - without_37) % MOD
    「至少缺一个」的数量 = 缺3的 + 缺7的 - 同时缺3和7的
    （同时缺的被减了两次，要加回一次）
  
  第23行：valid_strings = (total - without_37_inclusion) % MOD
    有效字符串 = 总数 - 至少缺一个的
  
  容斥原理图解（韦恩图）：

        ┌─────────── 总数 9^n ───────────┐
        │                                  │
        │     ┌───── 不含3: 8^n ───┐      │
        │     │ ╲                  │      │
        │     │   ╲  同时缺: 7^n   │      │
        │     │     ╲              │      │
        │     └───────╲── 不含7: 8^n┘     │
        │              ╲                 │
        │         ✅ 有效区域             │
        └─────────────────────────────────┘

        有效 = 总数 - 不含3 - 不含7 + 同时缺
            = 9^n - 8^n - 8^n + 7^n

第28~30行：主程序
  length = 10000       # 字符串长度
  result = count_valid_strings(length)  # 计算
  print(result)        # 输出答案


【为什么需要快速幂？】

普通方法算 9^10000：
  需要做 9999 次乘法，数字大到无法存储！
  9^10000 有约 9549 位十进制数字...

快速幂的优势：
  只需约 log₂(10000) ≈ 14 次循环
  每步都取模，数字始终 < 10^9+7


【快速幂原理详解】（二进制拆分）

把指数拆成二进制的幂次之和：
  9^10000 = 9^(8192+1024+512+256+16)
          = 9^8192 × 9^1024 × 9^512 × 9^256 × 9^16

  程序通过不断平方(base×base)和右移(exp>>1)来生成这些幂次，
  当exp的最低位为1时，就把当前的base乘入result。


【取模运算注意点】

(a - b) % mod 可能为负数！Python中 (-3) % 7 = 4（结果正确）
但有些语言会得到负数，所以保险做法是 (a%mod - b%mod + mod) % mod


【算法特点】

时间复杂度：O(log n) × 常数次快速幂调用 ≈ O(log n)
空间复杂度：O(1)

核心考点：
  ✓ 快速幂（必考算法）
  ✓ 容斥原理（组合数学基础）
  ✓ 大数取模


【一句话总结】
用容斥原理：总数9^n 减去缺3的8^n、减去缺7的8^n、加回同时缺的7^n，
全部用快速幂取模计算。
"""