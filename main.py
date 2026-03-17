def add(a, b):
return a + b

if name == "main":
print(add(3, 4))

test_main.py
import unittest
from main import add

class TestAdd(unittest.TestCase):
def test_add(self):
self.assertEqual(add(2, 3), 5)
