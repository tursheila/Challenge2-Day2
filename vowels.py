def countvowels ():

    x = input('enter string:')

    y = ['a','e','i','o','u']
    
    z= ''
    for char in x:
        if char in y:
            z += str(char)
    print (z)
countvowels()