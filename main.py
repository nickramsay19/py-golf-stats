'''
    Statistical Methods in One Line
    Nicholas Ramsay
'''
mean = lambda d : sum(n for n in d)/len(d)
sd = lambda d : (sum([(n - sum(d)/len(d))**2 for n in d])/(len(d)))**(1/2)
standardise = lambda d : [(n - sum(n1 for n1 in d)/len(d))/(sum([(n2 - sum(d)/len(d))**2 for n2 in d])/(len(d)))**(1/2) for n in d]

print(standardise([0,0,1,2,5,6,8,15,23,25,38]))


