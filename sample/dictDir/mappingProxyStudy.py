from types import MappingProxyType
#数据视图，通过视图，只能看不能改

def testView():
    dict0 = {"a" : 1, "b" : 2}
    dictMP = MappingProxyType(dict0)
    print(dictMP)
    print(dictMP["a"])

def testChange():
    dict0 = dict({"a" : 1, "b" : 2})
    dictMP = MappingProxyType(dict0)
    dict0["a"] = 3
    print(dictMP)
    dictMP["a"] = 1
    print(dictMP)

def main():
    # testView()
    testChange()

if __name__ == "__main__":
    main()