b =1
def fn_other():
    a = 100
    def fn_inner():
        global b
        nonlocal a
        a =a + 1
        b = b + 1
        print(f'a:{a}')
        print(f'b:{b}')
    return fn_inner

if __name__ == '__main__':
    f =fn_other()
    f() #101
    f() #102
    f() #103