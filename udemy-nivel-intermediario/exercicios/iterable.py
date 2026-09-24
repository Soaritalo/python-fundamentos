
def generator(n=0):
    yield 1
    print('Continuando')
    yield 2 
    print('Continuando')
    yield 3 
    print('Continuando')
    
gen = generator(n=0)
print(next(gen))
print(next(gen))
print(next(gen))



def generator2(n=0, maximum=10):
    while True:
        yield n 
        n += 1

        if n > maximum:
            return

        


gen2 = generator2(maximum=100)
for n in gen2:
    print(n)