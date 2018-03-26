"""
P3. Implement singleton pattern using meta classes
"""

import unittest

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
            cls.x = 5
        return cls._instances[cls]

class MyClass(metaclass=Singleton):
    pass

class TestSingleton(unittest.TestCase):
    
    def test_the_singleton_instance(self):
        m = MyClass()
        v = MyClass()

        self.assertEqual(m.x, 5)
        m.x = 9
        self.assertEqual(v.x, 9)

if __name__ == "__main__":
    unittest.main()
