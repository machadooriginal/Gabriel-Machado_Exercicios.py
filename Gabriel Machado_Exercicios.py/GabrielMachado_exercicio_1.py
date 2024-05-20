n= int(input('Digite um número: '))
c=n
f=1
while c !=1:
    f=f*c
    c-=1
    print ('{} x {} = {}'.format(n,c,f))
print ('O valor fatorial de {} é igual a {}!'.format(n,f))
