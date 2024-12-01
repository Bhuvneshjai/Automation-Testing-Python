'''
In Python, *args and **kwargs are used in function definitions to allow a flexible number of arguments.

*args: Allows a function to accept any number of positional arguments, which are passed to the function as a tuple.
**kwargs: Allows a function to accept any number of keyword arguments, which are passed to the function as a dictionary.

Use Cases
Flexible Input: When you don’t know beforehand how many arguments will be passed.
Forwarding Arguments: Useful in decorators or functions that wrap other functions.

In programming, verbose generally refers to the degree of detail included in output or logs. When a program, function,
or command is run in "verbose mode," it provides more detailed information about what it's doing.
This can help with debugging, understanding the flow, or simply providing more insight into the process.

Real-World Example: Calculator
'''

def calculate(operation, *numbers, **options):
    result = 0 if operation == 'add' else 1
    for number in numbers:
        if operation == 'add':
            result += number
        elif operation == 'multiply':
            result *= number
    if options.get('verbose'):
        print(f"Operation: {operation}, Numbers: {numbers}, Result: {result}")
    return result

calculate('add',1,2,3,verbose=True)
print(calculate('multiply',2,3,4,verbose=False))