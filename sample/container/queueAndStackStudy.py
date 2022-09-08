from collections import deque

def testRotatary():
    dq = deque(range(10), maxlen = 10)
    print(dq)
    dq.rotate(3)                            #从左向右循环移位
    print(dq)
    dq.rotate(-4)                           #从右向左循环移位
    print(dq)

def testAppend():
    #append 和 popleft 都是原子操作，不用担心资源锁的问题
    dq = deque(range(10), maxlen = 10)
    dq.append(-1)                           #满了以后，以先入先出的方式先删除一个元素
    print(dq)

    dq.pop()                                #pop相当于后入先出，删除一个元素
    dq.append(-2)
    print(dq)

    dq.popleft()
    dq.append(-2)
    print(dq)

    dq2 = deque(range(10), maxlen=30)
    dq2.extend([1, 2, 3])
    print(dq2)
    dq2.extendleft([0, 0, 0])
    print(dq2)

def main():
    # testRotatary()
    testAppend()

if __name__ == '__main__':
    main()
