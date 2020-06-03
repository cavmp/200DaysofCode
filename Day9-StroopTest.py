import random
import time
from colorama import init
from termcolor import colored

init(autoreset=True)
phase_time = 10

def main():
    numcorrect_in_controlled_phase=run_mulitple_testst(True)
    numcorrect_in_inverted_phase=run_mulitple_testst(False)
    print(numcorrect_in_controlled_phase,"Is the correct outputs in the controlled phase")
    print(numcorrect_in_inverted_phase,"Is the correct number of outputs in the inverted phase")

def run_mulitple_testst(is_correct):
    s0=time.time()
    count=0
    while(time.time()-s0<phase_time):
        if(run_single_test(is_correct)):
            count+=1
    return count
def run_single_test(is_phase):
    color_name = random_color_name()
    font_color = get_font_color(is_phase,color_name)
    print_in_color(color_name,font_color)
    user_answer = input("Please enter the font color \n")
    if(user_answer == font_color):
        return True
    print("Oops the correct color was", font_color)
    return False

def get_font_color (is_phase , color_name):
   if(is_phase==True):
       return color_name
   else:
       return random_color_name()

def random_color_name():
    '''
    Function: random color
    Returns a string (either red, blue or pink) with equal likelihood
    '''
    return random.choice(['red', 'blue', 'pink'])

def print_in_color(text, font_color):
    '''
    Function: print in color
    Just like "print" but this time, you can specify the font-color
    '''
    if font_color == 'pink': # magenta is a lot to type...
        font_color = 'magenta'
    print(colored(text, font_color, attrs=['bold']))

if __name__ == '__main__':
    main()
