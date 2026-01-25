# no access specifier in python but we can mimic
class demo:
    def __init__(self):
        self.no1 = 10           # public
        self._no2 = 20          # protected. demo chi child can see
        self.__no3 = 30         # private --> 100% abstraction (even child not know it)

obj = demo