
name = "Hello"
print(name[::-1])

lst = [1,2,3,4,5,6,7,8]
for i in lst:
    if i%2==0:
        print(i)

data = [
    ["Riya", 22, 40000],
    ["Aman", 17, 20000],
    ["Neha", 25, 50000]
]
def eligible(data):
    valid=[]
    for d in data:
        if d[1]>=21 and d[2]>=35000:
            valid.append(d[0])
        return valid
result = print(eligible(data))

for i in range(0,6):
    if i>=3:
        print(i)


input =[1,2,3,4]
sum = 0
for i in input:
    sum+=i
    print(sum)
    
a = 5
b = 2
c = a
a = b
b = c
print(a,b)


lst = [10, 20, 30, 40]
for i in lst:
    if i >= 40:
        print(i)

        
i = 1
while i<=10:
    print(i)
    i+=1

names ="A","B"
salary = 20000,40000
for n , s in zip(names,salary):
    print(n,s)

lst =["apple","banana","mango"]
for index,name in enumerate(lst):
    print(index,name)
    

s = "python"
rev = ""
for i in s:
    rev = i+rev
print(rev)


s = "education"
vowels ="aeiou"
count = 0
for ch in s:
    if ch in vowels:
        count+=1
print(count)

lst = [10, 20, 30, 40]
max_num = lst[0]

for i in lst:
    if i > max_num:
        max_num = i

print(max_num)

lst = [2, 4, 6, 8]
square =(l*l for l in lst )
for s in square:
    print(s)

square = (l*l for l in range(1,5))
for s in square:
    print(s)

def sum(a,b):
    return a+b
result = sum(200,300)
print(result)

student = {
    "name": "Riya",
    "age": 22,
    "marks": 85
}
for key,value in student.items():
    print(key,":",value)

for i in range(4):
    for j in range(5):
        print(i,j)

for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print()

for i in range(1,2):
    for j in range(1,11):
        print(i,"*",j ,"=", i*j)
    print()

t=(10,20,30,40)
lst = list(t)
print(lst)

a=3
b=5
a,b = b,a
print(a,b)

