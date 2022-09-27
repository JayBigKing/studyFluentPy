registry = []

def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func

def dec(func):
    return func

def helloWorld():
    print('hello world')
def dec2(func):
    return helloWorld



@register
def f1():
    print('running f1()')

@register
def f2():
    print('running f2()')

def f3():
    print('running f3()')

@dec
def f4():
    print('running f4()')

@dec2
def f5():
    print('running f5()')

def test1():
    print('running test1()')
    print('registry ->', registry)
    f1()
    f2()
    f3()

def test2():
    print('running test2()')

def test3():
    f5()

def main():
    test3()

if __name__ == '__main__':
    main()