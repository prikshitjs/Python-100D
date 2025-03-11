# functions in javascript

# tsk = create a function in python that get input from user and print on screen
import time;

def userDetails():
    name = input('Your name: ');
    age  = input('your age: ');
    email = input('your email (person@gmail.com): ');
    print('please wait!');
    
    time.sleep(3);
    print('your name - '+name);
    print('your age - '+age);
    print('your email - '+email);
    
userDetails();
