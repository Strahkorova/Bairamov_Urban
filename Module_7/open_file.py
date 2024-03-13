from pprint import pprint

file_name = 'poem.txt'
file = open(file_name, mode='r', encoding='utf8')
pprint(file.read())
file.close()
