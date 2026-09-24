def gen1():
    yield 1
    yield 2
    yield 3
    yield 4
def gen2(gen1):
    yield  from gen1()
    yield 4
    yield 5
    yield 6
def gen3(gen2):
    yield from gen2
    yield 10
    yield 20
    yield 30
    yield 40
g1=gen2(gen1)
g2 =gen2(gen3)
for numero in g1: 
    print(numero)
for numero in g2:
    print(numero)