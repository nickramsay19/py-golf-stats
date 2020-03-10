# Statistical Methods in One Line
> Created by Nicholas Ramsay

* Each method is indepedent and relies only on in-built Python3 methods. 
* The methods utilise python lambda notation to reduce the method from 2 lines to 1 as well as shortening the method via omitting the 'return' keyword.
* It is important to note that readability is not a concern in this project.

## Mean
```py
mean = lambda d : sum(n for n in d)/len(d)
```

## Standard Deviation
```py
sd = lambda d : (sum([(n - sum(d)/len(d))**2 for n in d])/(len(d)))**(1/2)
```

## Standardise
```py
standardise = lambda d : [(n - sum(n1 for n1 in d)/len(d))/(sum([(n2 - sum(d)/len(d))**2 for n2 in d])/(len(d)))**(1/2) for n in d]
```

This method can be substantially shortened via including the mean and sd functions above:
```py
standardise = lambda d : [(n - mean(d))/sd(d) for n in d]
```

## Sum
```py
s = lambda d : d[0] + s(d[1:]) if len(d) > 0 else 0
```
```py
s = lambda d : d[0]+(0,s(d[1:]))[bool(len(d))]
```

The sum function already exists in python, however creating one from scratch can still be interesting.

Also, via the functools module one can:
```py
import functools
s = lambda d : functools.reduce(lambda a, b : a + b, d)
```