# loops in python -->

names = ['person_name1','person_name2','person_name3','person_name4','person_name5'];

# for loop in python

c=1;

for print_names in names:
    print(f'{c}. list is {print_names}');
    c+=1;

# break is loop control statement you can use it if you want to break your loop. You can use it with condition or without condition.

for print_name in names:
    print(print_name);
    if print_name == 'person_name4':
     break;


# while loop in python

i = 1;

while i<8:
    print(i);
    i+=1;