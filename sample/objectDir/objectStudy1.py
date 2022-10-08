import numbers
import reprlib
from array import array

class Vector_v2:
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def hello(self):
        print(self.typecode)
        print(self._components)

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        cls = type(self)

        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))

    def __str__(self):
        return str(tuple(self))

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'vector({})'.format(components)

def func1(func):
    func()

v7 = Vector_v2(range(7))
def test1():
    print(v7[-1])
    print(v7[1:5])
    print(repr(v7))

def test2():
    func1(v7.hello)

def test3():
    l1 = [1, 2, 3, 4, 5]
    t1 = type(l1)
    l2 = t1([3, 4, 5, 6, 7])
    print(l2)

def test4():
    pass

def main():
    test3()

if __name__ == "__main__":
    main()