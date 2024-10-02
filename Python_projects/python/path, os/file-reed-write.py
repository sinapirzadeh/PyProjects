import pandas
f = open(file='file.txt', mode='w')
print(f.write('programming is good job!\nsina\nfdsafsafsdafsdaf'))

# -------- open wite with

with open('file.txt', 'w') as file:
    if file.writable:
        w_file = file.write()
        print(w_file)


# json file


# csv files

df = pandas.read_csv('file.csv')
print(df.head(2))
