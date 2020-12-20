from fitness_function import FitnessFunction
from program_tree import PT
import unittest

class TestFitnessFunction(unittest.TestCase):
    def setUp(self):
        self.terminals = set([1,2,3,4,5,6])
        self.Fitness = FitnessFunction([1,2,3,4,5,6], self.terminals)

    
    def test_is_prime(self):
        self.assertTrue(self.Fitness.is_prime(2))
        self.assertTrue(self.Fitness.is_prime(13))
        self.assertTrue(self.Fitness.is_prime(13))
        self.assertTrue(self.Fitness.is_prime(3))
        self.assertFalse(self.Fitness.is_prime(4))
        self.assertFalse(self.Fitness.is_prime(16))
        self.assertFalse(self.Fitness.is_prime(49))
        
    def test_get_fitness(self):
        self.assertEquals(0, self.Fitness.get_fitness(PT(4)))
        self.assertEquals(0, self.Fitness.get_fitness(PT(3)))
        self.assertEquals(0, self.Fitness.get_fitness(PT("x")))







if __name__ == '__main__': 
    unittest.main() 