korean, english, math, science = map(int, input().split())

if not (0 <= korean <= 100 and 0 <= english <= 100 and 0 <= math <= 100 and 0 <= science <= 100):
    print('잘못된 점수')
else:
    if korean>=90 and english>=90 and math>=90 and science>=90:
        print('합격')
    else:
        print('불합격')
