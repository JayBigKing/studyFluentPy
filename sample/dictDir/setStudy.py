
def test1():
    set0 = set(["0", "1", "2"])
    set1 = {"1", "2", "3"}
    print(set0 | set1)
    print(set0 & set1)
    print(set0 - set1)
    print(set0 in set1)

def test2():
    list0 = [1, 2, 2, 3, 4, 4]
    set0 = set(list0)
    list1 = list(set0)
    print(list1)

def test3():
    set0 = {str(i) for i in range(10)}
    print(set0)
    set0.add(10)
    print(set0)

def test4():
    set0 = frozenset({"1", "2", "3"})
    print(set0)
    #没有add


def main():
    test4()

if __name__ == "__main__":
    main()