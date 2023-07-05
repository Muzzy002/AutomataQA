import re

data = "position: relative; left: 80px; top: 48px;"

top = re.findall(r'\d[0-9]|\d', data.split(';')[1])

print(top)