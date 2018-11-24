def simple(x):
    for i in range(2,x):
        b = True
        for j in range(2,i):
            if i % j == 0:
                b = False
                break
        if b:
            print(i)

with open('input.txt') as f_in:
    text = int(f_in.read())
simple(text)
