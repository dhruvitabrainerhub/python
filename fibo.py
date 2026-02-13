def fib(n):
    a,b = 0,1
    while a<n:
        print(a,end=" ")
        a,b = b,a+b
    print()
fib(200)

def fib2(f):
    result =[]
    a,b =0,1
    while a<f:
        result.append(a)
        a,b = b,a+b
    return result
print(fib2(300))

def fib3(m):
    a,b=1,2
    while a<m:
        print(a,'+',b, '=',end=" ")
        a,b = a+b,a
    print()
fib3(200)