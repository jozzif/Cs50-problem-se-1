descrition = '''
In a file called interpreter.py, 
implement a program that prompts the user for
an arithmetic expression and then calculates and outputs the 
result as a floating-point value formatted to one decimal place.
Assume that the user’s input will be formatted as x y z, 
with one space between x and y and one space between y and z, wherein:

x is an integer
y is +, -, *, or /
z is an integer

'''
def main():
    math_interpreter()
    
def math_interpreter() :
    expression = input('')
    
    split_expression = expression.split(' ')
    x,y,z = split_expression
    x = int(x)
    z = int(z)
    
    if y == '+':
        print(f"{x + z:.1f}")
    elif y == '-':
        print(f"{x - z:.1f}")
    elif y == '*':
        print(f"{x * z:.1f}")
    elif y == '/':
        print(f"{x / z:.1f}")
    else:
        print('invalid input')
main()