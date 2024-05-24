from multiprocessing import Queue

queue = Queue()

def calculate(operator, operand1, operand2):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2
    
while True:

    operator, operand1, operand2 = queue.get()
    result = calculate(operator, operand1, operand2)

    print(f'Result: {result}')