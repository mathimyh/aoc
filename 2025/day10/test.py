listy = [57,33,24,22,68,47,40,42,35,32]

for i in range(2,20):
    divisible = True
    for elem in listy:
        if elem % i != 0:
            divisible = False
            break
    if divisible:
        print('ja: ', i)