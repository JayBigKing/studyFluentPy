from random import choice
import bisect

def testListSort():
    list0 = [i for i in range(0, 20)]
    list1 = [choice(list0) for item in list0]
    print(list1)
    list2 = sorted(list1)
    print(list1)
    print(list2)
    list1.sort()
    print(list1)

def testListBisect():
    list0 = [i for i in range(0, 8)]
    print(list0)
    for i in range(5):
        j = choice(list0)
        print(str.format("val is {:}, pos is {:}, left pos is {:}",
                         j, bisect.bisect(list0, j),                                            #bisect可以看作是从1开始数的位置
                         bisect.bisect_left(list0, j)))                                         #bisect_left可以看作是从0开始数的位置



def main():
    # testListSort()
    testListBisect()

if __name__ == '__main__':
    main()