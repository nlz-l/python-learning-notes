def check_login(fn_name):
    def fn_inner():
        print('校验登录')
        fn_name()
    return fn_inner
def check_code(fn_name):
    def fn_inner():
        print('校验验证码!')
        fn_name()
    return fn_inner

# @check_login
# @check_code
def comment():
    print("发表评论")

cc = check_code(comment)
cl = check_login(cc)
cl()
#comment()