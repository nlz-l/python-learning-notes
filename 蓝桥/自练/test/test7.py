
def a(test:str) -> bool:
    return (
        test.isdigit()
        and len(test) == 5
        and test[0] != '0'
        and test == test[::-1]
        )
if __name__ == "__main__":
    test = input()
    if a(test):
        print("是回文数")
    else:
        print("不是回文数")
