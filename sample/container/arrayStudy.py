from array import array
from random import random


def test1():
    # 1000 万个这样的数在二进制文件里只占用 80 000 000 个字节（每个浮点数占用8 个字节，不需要任何额外空间），
    # 如果是文本文件的话，我们需要 181 515 739 个字节。
    floats = array('d', (random() for i in range(10 ** 7)))  # python提供的数字类
    print(floats[-1])

    fp = open('floats.bin', 'wb')  # 用二进制写打开文件
    floats.tofile(fp)  # 把array数据放到文件里
    fp.close()

    floats2 = array('d')
    fp = open('floats.bin', 'rb')  # 用二进制读打开文件
    floats2.fromfile(fp, 10 ** 7)  # 读array数据
    fp.close()
    print(floats2[-1])

    print(floats == floats2)  # 检查数据是否一样


def memoryviewTest():
    #memoryview就是类似类型转换
    numbers = array('h', [-2, -1, 0, 1, 2])     #h为有符号短整型
    memv = memoryview(numbers)                  #得到一个内存视图
    print(len(memv))
    print(memv[0])

    memv_oct = memv.cast('B')                   #类型转换为byte，但是起始位置没有变，内存长度是没有变的
    print(memv_oct.tolist())
    print(memv_oct[5])
    memv_oct[5] = 4
    print(numbers)


def main():
    test1()
#    memoryviewTest()

if __name__ == '__main__':
    main()
