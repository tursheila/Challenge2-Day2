x = []
y = []
def fizzbuzz (x,y):

    x=input('enter list for x')
    y=input('enter for list y') 

    p=len(x)+len(y)


    if p%3==0 and p%5==0:
       return ("fizzbuzz")

    elif p%3==0:
       return ("fizz")
   
    elif p%5==0:
       return ("Buzz")

    else:
       return p

print (fizzbuzz(x,y))