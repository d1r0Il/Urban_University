def code(n):
    sit = ''
    for i in range (1, n):
        for j in range (i+1, n):
            if n % (i+j) == 0:
                sit += str(i) + str(j)
    return  sit
for n in range (3, 21):
    sit = code(n)
    print (f'{n} - {sit}')


