#This is Task2

with open('running-config') as fin:
    secondtext = fin.read().replace('192', '10')
    secondtext = fin.read().replace('replace', '10')
with open('running-config') as fin:
fin.write(secondtext)
