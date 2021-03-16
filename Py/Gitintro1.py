def simple_interest(p,t,r):
    print('The Principle is', p)
    print('The time period is', t)
    print('The rate of interst is', r)
    si = (p*t*r)/100
    print('The Simple Interest is', si)
    return si
simple_interest(10000,1,4)
