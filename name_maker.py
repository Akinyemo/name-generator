#Combines two  given strings into 1
def calc_name(x,y):
    if isinstance(x,str) == False:
        raise TypeError('First input is not a string')

    if isinstance(y,str) == False:
        raise TypeError('Second input is not a string')

    if len(x) < 1:
        raise ValueError('String 1 length less than 1')

    if len(y) < 1:
        raise ValueError('String 2 length less than 1')


    return(x + ' '+ y)
