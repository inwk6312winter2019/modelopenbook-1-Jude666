#This is Task3

with open('running-config') as in fin:
    a = f.read()
    b = a.split("!")
print(b)
