from functools import reduce

def fn(*args, **kwargs):
    print(args)
    print(kwargs)

def factorial(n):
    return 1 if n < 2 else n * factorial(n-1)

def myAdd(a,b):
    return a+b

def testAnnotation(a : str, b : 'int < 10') -> str:
    print('hh')
    return r'%s + %d = unknown' % (a, b)

def test1():
    '''
    测试可变参数函数
    '''
    fn(1,2,3,4, a= 10, b = 11)

def test2():
    '''
    测试map、fileter和reduce
    及其分别对应的替代用法
    '''
    testStr = ["map", "filter", "reduce", "all and any"]
    index = 0
    fact = factorial
    print("test %s" % testStr[index])
    l1 = list(map(fact,range(6)))
    print(l1)
    l1 = [fact(i) for i in range(6)]
    print(l1)
    print("test %s" % testStr[index])

    index += 1
    print("test %s" % testStr[index])
    l1 = list(map(fact, filter(lambda n : n % 2 , range(6))))
    print(l1)
    l1 = [fact(i) for i in range(6) if i % 2]
    print(l1)
    print("test %s" % testStr[index])

    index += 1
    print("test %s" % testStr[index])
    print(reduce(myAdd, range(100)))
    print(sum(range(100)))
    print("test %s" % testStr[index])

    index += 1
    l2 = [True if i % 2 else False for i in range(10) ]
    print(str.format("l2:{0:}", l2))
    print("test %s" % testStr[index])
    print("all : %s" % all(l2))
    print("any : %s" % any(l2))
    print("test %s" % testStr[index])

def test3():
    class Obj:
        def __init__(self):
            pass

        def __call__(self):
            print('hh')
    obj = Obj()
    obj()

def test4():
    print(dir(factorial))

def test5():
    '''
    测试函数注解
    '''
    from inspect import signature
    sig = signature(testAnnotation)
    print(str(sig))
    print(sig.return_annotation)
    print(sig.parameters)
    print(testAnnotation('张', 9))

def test6(choose = 0):
    if choose == 0:
        from operator import itemgetter
        list0 = [i for i in range(10)]
        ig0 = itemgetter(0)
        ig1 = itemgetter(0, 1)
        print(ig0(list0))
        print(ig1(list0))
    elif choose == 1:
        from collections import namedtuple
        from operator import attrgetter
        hhName = namedtuple("hhName", "a b c")
        ag0 = attrgetter("a")
        ag1 = attrgetter("a", "b")
        hh0 = hhName(0, "666", 2)
        print(ag0(hh0))
        print(ag1(hh0))
    elif choose == 2:
        from operator import methodcaller
        s = 'The time has come'
        upacase = methodcaller('upper')
        print(upacase(s))                   #s对象必须有这个方法才行哦
        hiphenate = methodcaller('replace', ' ', '-')
        print(hiphenate(s))
    else:
        from functools import partial
        from operator import mul
        triple = partial(mul, 3)
        list0 = [triple(i) for i in range(10)]
        print(list0)




def main():
    test6(3)

if __name__ == '__main__':
    main()