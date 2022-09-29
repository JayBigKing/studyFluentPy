from copy import deepcopy

class TwilightBus:
    def __init__(self, passengers = None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

    def __deepcopy__(self, memodict=None):
        if memodict is None:
            memodict = {}
        tb = TwilightBus()
        for item in self.passengers:
            tb.passengers.append(item)

        return tb

tb0 = TwilightBus(["1", "2"])
print(tb0.passengers)
tb1 = deepcopy(tb0)
print(tb1.passengers)
