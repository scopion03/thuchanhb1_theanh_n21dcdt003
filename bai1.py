# Phuong thuc de quy
def fibonacci_recursion(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)
   
# Phuong thuc khong de quy
def fibonacci_non_recursion(n):
    fib = [0, 1]
    if n <= 1:
        return fib[n]
    else:
        for i in range(2, n+1):
            fib.append(fib[i-1] + fib[i-2])
        return fib[n]

n = int(input("Nhap so Fibonacci muon tinh: "))

if n <= 0:
    print("Nhap mot so nguyen duong:")
else:
    print("So Fibonacci tuong ung la:", fibonacci_non_recursion(n))