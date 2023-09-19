class SingletonClass(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

a = SingletonClass()
b = SingletonClass()
print(a)
print(b)
print(a is b)
print(id(a) == id(b))

