descrption = '''
            In deep.py,\n implement a program that\n 
            prompts the user for the answer to the Great Question of Life, the Universe and Everything,\n
            outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. \n
            Otherwise output No.
            '''


def main():
    prompt()
    
def prompt():
    user_input = input('What is the Answer to the Great Question of Life, the Universe, and Everything? ').strip().lower()
    if user_input == '42' or user_input == 'forty-two' or user_input == 'forty two' :
        print('Yes')
    else :
        print('No')
    
main()