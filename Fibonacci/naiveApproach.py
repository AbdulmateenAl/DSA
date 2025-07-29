# This method is simply the slowest with 0(2^n) time complexity
def fib(n):
    if n <= 2:
        result = 1
    else:
        result = fib(n-1) + fib(n-2)
    return result

print(fib(1000))

# It also won't work for large numbers because it recalculates some fibonacci numbers multiple times