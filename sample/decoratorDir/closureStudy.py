#闭包学习
def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        return sum(series) / len(series)

    return averager

def test1():
    avg = make_averager()
    print(avg(10.))
    print(avg(11.))
    print(avg(12.))

    print(avg.__code__.co_varnames)
    print(avg.__code__.co_freevars)
    print(avg.__closure__)
    print(avg.__closure__[0].cell_contents)

def main():
    test1()

if __name__ == "__main__":
    main()

