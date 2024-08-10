import io
from pprint import pprint

def custom_write(file_name, strings):
    strings_positions = {}
    
    file_name = '7.2.txt'
    with open(file_name, 'w', encoding= 'utf-8') as file:
        for i in strings:
            position = file.tell()
            file.write(i + '\n')
            strings_positions  [(len(strings_positions) + 1, position)] = i 
        return strings_positions
    
   
   
    
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('7.2.txt', info)
for elem in result.items():
  print(elem)