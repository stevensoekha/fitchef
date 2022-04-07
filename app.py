import pyperclip as pc
from lib.files import get_week_days
from lib.extract import add_ingredients_to_list

files = get_week_days()
data = dict()

# Extract from singles
for file in files.get('singles'):
    print('>> Extracting file as single ***', file)
    add_ingredients_to_list(file, data)

# Extract from doubles
for file in files.get('doubles'):
    print('>> Extracting file as single ***', file)
    add_ingredients_to_list(file, data)
    add_ingredients_to_list(file, data)

shoppinglist = ''

for key in data:
    item = data[key]
    shoppinglist = shoppinglist + f'{item["amount"]} {item["text"]}' + '\n'

pc.copy(shoppinglist)
print('\n***\nShoppinglist copied to clipboard!\n***\n')
