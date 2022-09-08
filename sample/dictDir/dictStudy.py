import collections


def testDerivation():
    DIAL_CODES = [
        (86, "a"),
        (100, "b"),
        (200, "c"),
        (72, "ads")
    ]
    countryCode = {country : code for code, country in DIAL_CODES}

    print(countryCode)

def testSetDefault():
    DIAL_CODES = [
        (86, "a"),
        (100, "b"),
        (200, "c"),
        (72, "ads")
    ]
    countryCode = {country : code for code, country in DIAL_CODES}
    countryCode.setdefault("ui", []).append(900)
    print(countryCode)

def testInDict():
    DIAL_CODES = [
        (86, "a"),
        (100, "b"),
        (200, "c"),
        (72, "ads")
    ]
    countryCode = {country : code for code, country in DIAL_CODES}
    print(countryCode["a"])
    print(countryCode.get("d"))
    print(("d" in countryCode))

def testDefaultDict():
    DIAL_CODES = [
        (86, "a"),
        (100, "b"),
        (200, "c"),
        (72, "ads")
    ]
    countryCodeDict = {country : code for code, country in DIAL_CODES}
    countryCode = collections.defaultdict(int)
    countryCode.update(countryCodeDict)
    print(countryCode["a"])
    print(countryCode["d"])



def main():
    # testDerivation()
    testSetDefault()
    # testInDict()
    # testDefaultDict()

if __name__ == "__main__":
    main()