# condition in python -->


a = 4;
b = 7;


# if else statement -->
# in if else statement discribe the condition and then basis of these condition you get end result
# for eg. we have two variable a and b then you give if else statement on a and b variable if a value is big the you get
# (a is greater then b) or in else statement if condition is false the you get (a is less then b)
if a<b:
    print("a is less then b");
else:
    print("a is greater then b");

# else if (elif) statement is python -->
# in elif statement you can give multiple condition
if a>b:
    print("a is greater then b");
elif a==b:
    print("a and b are equal");
elif a<b:
    print("a is less then b");
else:
    print("all condition are false");

# if else statement is one line -->
# you can write your if else logic in one line instead of multiple lines
print("a is less then b") if a<b else print("a is greater then b");
