from program_tree import PT
import unittest

class TestPT(unittest.TestCase):
    def setUp(self):
        self.terminals = set([1,2,3,4])

    def testTerminals(self):
        t1 = PT(1)
        t2 = PT(2)
        self.assertEquals(1, t1.eval(self.terminals))
        self.assertEquals(1, t1.eval(self.terminals, 2))
        self.assertEquals(2, t2.eval(self.terminals))
    
    def testVariables(self):
        x = PT("x")
        self.assertEquals(5, x.eval(self.terminals, 5))
        self.assertEquals(3, x.eval(self.terminals, 3))

    def testEval(self):
        #test + operater
        t1 = PT(1)
        t4 = PT(4)
        x = PT("x")
        xplus1 = PT("+", x, t1)
        program = PT("+", xplus1, t4)
        self.assertEquals(3, xplus1.eval(self.terminals, 2))
        self.assertEqual(8, program.eval(self.terminals, 3))
        self.assertEquals(1, t1.size)
        self.assertEquals(3, xplus1.size)
        self.assertEquals(5, program.size)

        #test * operator
        xtimes4 = PT("*", x, t4)
        xsquared = PT("*", x, x)
        self.assertEqual(12, xtimes4.eval(self.terminals, 3))
        self.assertEqual(16, xsquared.eval(self.terminals, 4))


if __name__ == '__main__': 
    unittest.main() 





