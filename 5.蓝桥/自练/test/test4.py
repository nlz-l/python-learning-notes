def main():
    text = input("请输入一行字符:")
    alpha_count = sum(1 for ch in text if ch.isalpha())
    space_count = sum(1 for ch in text if ch.isspace())
    digit_count = sum(1 for ch in text if ch.isdigit())
    other_count = len(text) - alpha_count - space_count - digit_count
    print(f"字母数量:{alpha_count}")
    print(f"空格数量:{space_count}")
    print(f"数字数量:{digit_count}")
    print(f"其他数量:{other_count}")
if __name__ == "__main__":
    main()
