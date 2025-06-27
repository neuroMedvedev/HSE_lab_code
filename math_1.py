import random
correct = 0
incorrect = 0
a=1
b=0
c=0
g=0
t=0
r=0
count1 = 1
count2 = 1
while a==1:
    if r == 10001:
        break
    while count1 == 1:
        b = random.randint(1,200)
        c = random.randint(1,200)
        if b >= c:
            count1 += 1
        else:
            count1 = 1
    g = random.randint(1,2)
    count1 = 1
    if g == 1:
        t = b+c
        while count2 == 1:
            print (f"{b} + {c} = ", end = "")
            try:
                r = int(input())
            except:
                print ("Введено некорректное значение, попробуйте ещё раз:)")
                continue
            if r == t:
                correct += 1
            else:
                incorrect += 1
            break
    elif g==2:
        t = b-c
        while count2 == 1:
            print (f"{b} - {c} = ", end = "")
            try:
                r = int(input())
            except: 
                print ("Введено некорректное значение, попробуйте ещё раз:)")
                continue
            if r == t:
                correct += 1
            else:
                incorrect += 1
            break
print (f"Правильных:{correct}")
print (f"Неправильных:{incorrect-1}")