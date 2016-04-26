'''
Created on 2016. 4. 16.

@author: Hwajung Lee
'''

from calculator.server.CalculatorSocketHelper import CalculatorSocketHelper

if __name__ == '__main__':
    helper = CalculatorSocketHelper()
    helper.runSocket()
    helper.closeSocket()