# 1)
def a_function(a_parameter):
    a_variable = 15
    return a_parameter

a_function(10)
print(a_variable)    # Output : NAMEERROR

# 2)
i = 50
def foo():
    i = 100
    return i

foo()
print(i)    # Output 50

# 3)
def bar():
    my_variable = 9

    if 16 > 9:
        my_variable = 16

        print(my_variable)

bar()        # Output : 16