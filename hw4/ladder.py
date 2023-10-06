def my_step(n):
    if n == 1:
        return '1 step '
    elif n == 2:
        return '2 steps '
    else:
        return my_step(n-1) + my_step(n-2)
print(my_step(5)) 

