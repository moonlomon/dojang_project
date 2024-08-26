start, end = map(int, input().split())

# 방법1
for i in range(start, end+1):
    if i%5==0 and i%7==0:
        print('FizzBuzz')
    elif i%5==0:
        print('Fizz')
    elif i%7==0:
        print('Buzz')
    else:
        print(i)

# # 방법2
for i in range(start, end+1):
    if i%35==0:
        print('FizzBuzz')
    elif i%5==0:
        print('Fizz')
    elif i%7==0:
        print('Buzz')
    else:
        print(i)

# # 방법3
for i in range(start, end+1):
    print('Fizz'*(i%5==0)+'Buzz'*(i%7==0) or i)