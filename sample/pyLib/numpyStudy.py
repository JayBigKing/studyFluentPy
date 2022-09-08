import numpy

def testDim():
    a = numpy.arange(12)
    print(a)
    print(type(a))
    print(a.shape)

    a.shape = (3,4)                 #改变行列
    print(a)
    print(a[2])
    print(a[:, 1])                  #所有行的第一个元素（从0开始数）
    print(a[2, 1])
    print(a[..., 2])                #...相当于n个:,n是剩下的维数

    a = a.transpose()               #转置
    print(a)

def testFile():
    floats = numpy.loadtxt('floats-in-line.txt')
    print(floats)
    floats *= .5
    print(floats)
    print(floats[-2:])                              #从后往前数第二个开始

    numpy.save('float-2', floats)
    floats = numpy.load('float-2.npy')
    print(floats)

def testTimeCounter():
    from time import perf_counter as pc
    from random import random
    floats = numpy.array([random() for i in range(10**6)], dtype=float)
    t0 = pc()                               #计时器当前时间
    floats /= 3
    print(pc() - t0)                        #时间间隔

def main():
    testDim()
    # testFile()
    # testTimeCounter()

if __name__ == '__main__':
    main()