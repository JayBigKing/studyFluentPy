from functools import singledispatch
from collections import abc
import numbers

@singledispatch
def TenTimesPrinter(obj):
    pass

@TenTimesPrinter.register(numbers.Integral)
def _(n):
    print(n*10)

@TenTimesPrinter.register(str)
def _(text:str):
    print(int(text)*100)

@TenTimesPrinter.register(abc.MutableSequence)
def _(seq):
    return [TenTimesPrinter(item) for item in seq]

TenTimesPrinter(10)
TenTimesPrinter("100")
TenTimesPrinter([1, 2, 3])