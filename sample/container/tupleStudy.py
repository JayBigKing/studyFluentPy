from collections import namedtuple
def testNameTuple():
    City = namedtuple('City', 'name county pop')
    city1 = City('hh', 'vie', 1000)
    city2 = City('66', 'man', 800)
    print(str.format("{0}\r\n{1}",city1,city2))
    print(City._fields)
    city3 = City._make(('xx', 'thl', 1200))
    print(city3)
    print(city3._asdict())

def testTupleUnpack():
    a = 10
    b = 20
    print(str.format("a is {0}, b is {1}", a, b))

    a, b = b, a
    print(str.format("a is {0}, b is {1}", a, b))

    a, b, _, _ = (10, 11, 12, 13)
    print(str.format("a is {0}, b is {1}", a, b))

    rangeObj = (i for i in range(0, 10))
    a, b, *rect = rangeObj
    print(str.format("a is {0}, b is {1}, remain is {2}", a, b, rect))

def main():
    # testNameTuple()
    testTupleUnpack()

if __name__ == '__main__':
    main()