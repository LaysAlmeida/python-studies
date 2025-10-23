# 1 - Fatorial de um número
def factorial(num):
    if num == 1:
        return 1
    else:
        return(num * factorial(num - 1))
    
print(factorial(5))

# 2 - Soma total de um número
def total_sum(num):
    if num == 1:
        return 1
    else:
        return(num + total_sum(num - 1))
    
print(total_sum(5))