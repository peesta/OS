from multiprocessing import Queue
import sys

queue = Queue()

def take_task():
    operator = input('Enter operator (+, -, *, /): ')
    if operator == 'exit':
        sys.exit(0)
    operand1 = input('Enter first operand: ')
    if operand1 == 'exit':
        sys.exit(0)
    else: operand1 = int(operand1)
    operand2 = input('Enter second operand: ')
    if operand2 == 'exit':
        sys.exit(0)
    else: operand2 = int(operand1)

    if not operator in ['+', '-', '*', '/']:
        print('Not supported operator')
        sys.exit(1)
    if operator == '/' and operand2 == 0:
        print(f'{operand1} can not divided by zero')
        sys.exit(1)

    return operator, operand1, operand2

while True:
    
    task = take_task()
    queue.put(task)

    

    

