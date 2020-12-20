import program_tree
from random import sample

class FitnessFunction2():
    def __init__(self, seeds, terminals):
        self.seeds = seeds
        self.primes = set([2])
        self.not_prime = set()
        self.terminals = terminals
        
    
    def is_prime(self, n) : 
        if n in self.not_prime:
            return False
        if n <= 0:
            return False
        if n in self.primes:
            return True
        # Corner cases 
        if (n <= 1) : 
            return False
        if (n <= 3) : 
            return True

        # This is checked so that we can skip  
        # middle five numbers in below loop 
        if (n % 2 == 0 or n % 3 == 0) : 
            return False
        i = 5
        while(i * i <= n) : 
            if (n % i == 0 or n % (i + 2) == 0) : 
                self.not_prime.add(n)
                return False
            i = i + 6
        self.primes.add(n)
        return True
    
    def get_fitness(self, pt):
        if (pt.left == None) and (pt.right == None):
            return 0
        generated_numbers = set()
        fitness = 0
        sub_primes = 0
        for seed in self.seeds:
            n = pt.eval(self.terminals, seed)
            if (n > 0 and n not in generated_numbers) and (self.is_prime(n)):
                sub_primes += 1
                if sub_primes > fitness:
                    fitness = sub_primes
            else:
                sub_primes = 0                    
            generated_numbers.add(n)
        return fitness

class FitnessFunction():

    def __init__(self, seeds, terminals):
        self.seeds = seeds
        self.primes = set([2])
        self.not_prime = set()

        self.terminals = terminals
        
    
    def is_prime(self, n) : 
        if n in self.not_prime:
            return False
        if n <= 0:
            return False
        if n in self.primes:
            return True
        # Corner cases 
        if (n <= 1) : 
            return False
        if (n <= 3) : 
            return True

        # This is checked so that we can skip  
        # middle five numbers in below loop 
        if (n % 2 == 0 or n % 3 == 0) : 
            return False
        i = 5
        while(i * i <= n) : 
            if (n % i == 0 or n % (i + 2) == 0) : 
                self.not_prime.add(n)
                return False
            i = i + 6
        self.primes.add(n)
        return True

    def get_fitness(self, pt, seeds):
        if (pt.left == None) and (pt.right == None):
            return 0
        generated_numbers = set()
        fitness = 0
        for seed in seeds:
            n = pt.eval(self.terminals, seed)
            if (n > 0 and n not in generated_numbers) and (self.is_prime(n)):
                fitness += 1
            generated_numbers.add(n)
        return fitness

    def get_primes(self):
        return self.primes
