def ave(li):
    return sum(li) / len(li)


setattr(ave, 'sina', '1331')
print(ave.__dict__)
# delattr(ave, 'sina')
print(ave.__dict__)
# or for delete attrebute you can use ' del '
del ave.sina
print(ave.__dict__)
