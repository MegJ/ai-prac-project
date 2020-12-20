from random import random, sample
from copy import deepcopy


class PT():
    
    """
    creates a new program

    arguments:
    op: a string representing either the operation to be performed 
        or a terminal
    left: the program on the left side of the operation, 
        left is None if self.op is a terminal
    right: the program on the right side of the operation, 
        right is None if self.op is a terminal
    """
    def __init__(self, op, left=None, right=None):
        self.nodes = []
        self.op = op
        self.left = left
        self.right = right
        self.max_directon = None
        max_size = 0
        if self.left:
            self.nodes.append(self.left.nodes)
            max_size = self.left.size
            self.max_directon = "Left"
        if self.right:
            self.nodes.append(self.right.nodes)
            max_size = max(max_size, self.right.size)
            self.max_direction = "Right"
        self.nodes.append(self)
        self.size = 1 + max_size
    
    def add_right(self, right):
        self.nodes = self.nodes + right.nodes
        self.right = right
        if right.size >= self.size or self.max_direction == "Right":
            self.size = right.size + 1
            self.max_direction = "Right"
    
    def add_left(self, left):
        self.nodes = self.nodes + left.nodes
        self.left = left
        if left.size >= self.size or self.max_direction == "Left":
            self.size = left.size + 1
            self.max_direction = "Left"
    
    """
    evaluates the PT for the given value of x
    """
    def eval(self, terminals, x = None):
        if self.op == "x":
            if x == None:
                raise Exception("no value of x provided")
            return x
        if self.op in terminals:
            return self.op
        left = self.left.eval(terminals, x) if self.left else None
        right = self.right.eval(terminals, x) if self.right else None
            
        if left is None:
            left = 0
        if right is None:
            right = 0
        if self.op == "+":
            return left + right
        
        if self.op == "*":
            return left * right
        raise Exception("Program tree invalid: " + str(self.op) + " is not a valid operator")
    
    """
    return a subtree.  Each node has a probability
    p of being selected.  If no subtree is selected, return None
    """
    def get_subtree(self):
        return sample(self.nodes, 1)[0]

    def replace_subtree(self, replacement_tree, terminals, operations):
        tree = sample(self.nodes, 1)[0]
        tree.op = replacement_tree.op
        tree.nodes = replacement_tree.nodes
        tree.left = deepcopy(replacement_tree.left)
        tree.right = deepcopy(replacement_tree.right)

    def crossover(self, replacement_tree, terminals, operations):
        return self.replace_subtree(replacement_tree, terminals, operations)
    
    def PTCI(self, depth, depth_bound, terminals, operations, p_non_terminal):
        if depth == depth_bound:
            return PT(sample(terminals,1)[0])
        if random() < p_non_terminal:
            new_tree = PT(sample(operations, 1)[0])
            new_tree.left = (self.PTCI(depth + 1, depth_bound, terminals, operations, p_non_terminal))
            new_tree.right = (self.PTCI(depth + 1, depth_bound, terminals, operations, p_non_terminal))
            return new_tree
        return PT(sample(terminals,1)[0])
     
    def grow(self, p_mutation, terminals, operations):
        if random() < p_mutation:
            new_tree = self.PTCI(0, 6, terminals, operations, 0.6)
            print(new_tree.to_string())
            self.op = new_tree.op
            self.left = new_tree.left
            self.right = new_tree.right
            return self
        else:
            if self.left is not None:
                self.left = self.left.mutate(p_mutation, terminals, operations)
            if self.right is not None:
                self.right = self.right.mutate(p_mutation, terminals, operations)
        return self
    
    
    def swap(self, p_mutation, terminals, operations):
        if random() < p_mutation:
            
            if self.op in terminals:
                self.op = sample(terminals, 1)[0]
            elif self.op in operations:
                self.op = sample(operations, 1)[0]
        else:
            if self.left is not None:
                self.left = self.left.swap(p_mutation, terminals, operations)
            if self.right is not None:
                self.right = self.right.swap(p_mutation, terminals, operations)
        return self
        
    def mutate(self, p_mutation, terminals, operations):
        self.swap(p_mutation, terminals, operations)
        return(self)

        

    def to_string(self):
        s = str(self.op)
        if self.left != None or self.right != None:
            s = s + " ("
            if self.left is None:
                s = s + "None"
            else:
                s = s + self.left.to_string()
            s = s + " "
            if self.right is None:
                s = s + "None"
            else:
                s = s + self.right.to_string()
            s = s + ")"
        return s
        
    def __str__(self):
        return self.to_string()



        

        
        
        
            
    