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