class DigitError(Exception):
    def __init__(self, *args: object, msg = 'Number Error!') -> None:
        super().__init__(*args)
        self.message = msg

    def __str__(self) -> str:
        return '*** Your Enter is Not a Number *** \nEnter a Number !'



def func(number):
    if not number.isdigit():
        raise DigitError()
    _list = []
    for i in number:
        _list.append(i)

    print(_list)


# or loke like this
try:
    func('09364733583jk')
except DigitError as e:
    print(e)
