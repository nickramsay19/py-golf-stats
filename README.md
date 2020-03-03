# Statistical Methods in One Line
> Created by Nicholas Ramsay

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