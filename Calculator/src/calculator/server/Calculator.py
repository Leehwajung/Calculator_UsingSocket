'''
Created on 2016. 4. 24.

@author: Hwajung Lee
'''

class Calculator(object):
    '''
    Simple Arithmetic Calculator
    '''
    memory = 0
    
    def __init__(self):
        '''
        Constructor
        '''
        self.memory = 0
    
    def calculate(self, formula):
        form = formula.split('=')[0]
        self.memory = eval(form)
        return self.memory
        
    def plus(self, num1, num2 = None):
        if num2 is None:
            self.memory += num1
        else:
            self.memory = num1 + num2
        return self.memory
    
    def sum(self, *nums):
        self.memory = 0
        for num in nums:
            self.memory += num
        return self.memory
    
    def minus(self, num1, num2 = None):
        if num2 is None:
            self.memory -= num1
        else:
            self.memory = num1 - num2
        return self.memory
    
    def multifly(self, num1, num2 = None):
        if num2 is None:
            self.memory *= num1
        else:
            self.memory = num1 * num2
        return self.memory
    
    def devide(self, num1, num2 = None):
        if num2 is None:
            self.memory /= num1
        else:
            self.memory = num1 / num2
        return self.memory
    
    def mod(self, num1, num2 = None):
        if num2 is None:
            self.memory %= num1
        else:
            self.memory = num1 % num2
        return self.memory
    
    def getMemory(self):
        return self.memory
    
    def setMemory(self, value):
        self.memory = value
    
    def resetMemory(self):
        self.memory = 0