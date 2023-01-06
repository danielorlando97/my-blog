class CustomMetaclass(type):
    def __init__(cls, *args, **kwds):
        print('initialize CustomMetaclass')
        return super().__init__(*args, **kwds)

    def __call__(self, *args, **kwds):
        print('CustomMetaclass.__call__')
        return super().__call__(*args, **kwds)


class MyClass(metaclass=CustomMetaclass):

    def __init__(self, *args, **kwds):
        print('MyClass.__init__')

    def __new__(cls, *args, **kwds):
        print('MyClass.__new__')
        return super().__new__(cls, *args, **kwds)


print('init example')
my_class = MyClass()


class Singleton(type):
    _instances = None

    def __call__(cls, *args, **kwargs):
        if cls._instances is None:
            cls._instances = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances


class Counter(metaclass=Singleton):
    def __init__(self) -> None:
        print('initialize Counter')
        self.n = 0

    def __str__(self) -> str:
        self.n += 1
        return f'You have looked at me {self.n} times'


print(Counter())
print(Counter())
print(Counter())
print(Counter())
print(Counter())
print(Counter())
print(Counter())
