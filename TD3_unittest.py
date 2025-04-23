from TD3 import T
import unittest

class Test_T(unittest.TestCase):

    def __init__(self,*kwargs):
        super().__init__(*kwargs)
        self.a = T("a")
        self.b = T("b")
        self.f = T("f")
        self.f_ab = T(self.f, self.a, self.b)

    def test_is_leaf(self):
        self.assertFalse(self.f_ab.is_leaf())


if __name__=="__main__":
    unittest.main()