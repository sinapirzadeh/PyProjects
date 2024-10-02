_list = []

while (name := int(input('Enter Your Number (0000 for exit) :'))) != '0000':
    try:
        _list.append(name)
    except TypeError as e:
        print(e.__class__.__name__)
    except ZeroDivisionError as z:
        print(z)
    finally:
        print('!!!')
