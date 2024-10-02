import warnings

def func(x:int ,y:int):
    if not isinstance(x, int) or not isinstance(y, int):
        warnings.warn('you batter enter a Integer!', Exception)
    
    print( x + y)


func('s', 'a')

print('ok!')