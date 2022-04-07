from files import get_week_days
from extract import add_ingredients_to_list

files = get_week_days()
data = dict()

# Extract from singles
for file in files.get('singles'):
    print('*** Extracting file as single ***', file)
    add_ingredients_to_list(file, data)

# Extract from doubles
for file in files.get('doubles'):
    print('*** Extracting file as single ***', file)
    add_ingredients_to_list(file, data)
    add_ingredients_to_list(file, data)

for key in data:
    item = data[key]
    print(item['amount'], item['text'])
