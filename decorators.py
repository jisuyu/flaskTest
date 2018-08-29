def hello(f):
    def greeting():
        print("^__^")
        f()
        print("ㅠ__ㅠ")
    return greeting
    
@hello
def korean():
    print("안녕하세요")
    
@hello
def english():
    print("hello")

korean()
##데코레이터와 동일 의미
#a=hello(korean)
#a()
english()