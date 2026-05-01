'''
def main():
    greeting()


def greeting():
    customer = input(
        "Greet the bank teller: "
    )  # If the greeting starts with “hello”, output $0. f the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.
    customer=customer.strip().lower()
    if customer.startswith("hello"):
        print("$0")
    elif customer.startswith("h"):
        print("$20")
    else:
        print("$100")


main()


'''







description ='''
In a file called bank.py,
implement a program that prompts the user for a greeting. 
If the greeting starts with “hello”, output $0.
If the greeting starts with an “h” (but not “hello”), output $20. 
Otherwise, output $100.
Ignore any leading whitespace in the user’s greeting, 
and treat the user’s greeting case-insensitively.
'''
def main():
    greeting()
def greeting() :
    user_greeting = input('Greeting: ').strip().lower()
    if user_greeting.startswith('hello'):
        print('$0')
    elif user_greeting.startswith('h'):
        print('$20')
    else :
        print('$100')
        
        
main()











