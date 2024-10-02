# for Testing in python

def func(x:int ,y:int):
    assert not isinstance(x, int) or not isinstance(y, int)
    print( x + y)


func('s', 'a')

print('ok!')