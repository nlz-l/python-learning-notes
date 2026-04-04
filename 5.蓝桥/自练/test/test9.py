def a(b):
    c = (b - 32) *5/9
    return c

if __name__ == "__main__":
    try:
        b = float(input())
        c = a(b)
        print(f"华氏度:{b}")
        print(f"摄氏度:{c}")
    except ValueError:
        print("错误,请输入有效数字")
    except Exception as es:
        print("未知异常")
