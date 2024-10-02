import re

text = 'Hi, mi name is Sina. I`m a Programmer!'

xpersion = re.compile(r'i.')

output = xpersion.finditer(text)
print(list(output))


# ----------------------------



# for emails
t = r"^([\w\.\-\_]+)@([a-zA-Z]+)\.([a-zA-Z]{2,5})$"

# for hex for #fff
th = r"^#([a-f0-9]{6}|[a-f0-9]{3})"