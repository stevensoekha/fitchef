import re
from bs4 import BeautifulSoup


def get_ingredient_detail(ingredient):
    id = ''.join([i for i in ingredient if not i.isdigit()]
                 ).replace(',', '').replace(' ', '')
    text = ''.join(
        [i for i in ingredient if not i.isdigit()]).replace(',', '')
    amount = [int(float(s))
              for s in re.findall(r'-?\d+\.?\d*', ingredient)]

    return {"id": id, "text": text, "amount": amount[0] if len(amount) else 1}


def add_ingredients_to_list(path, data):
    html = BeautifulSoup(open(path, 'r').read(), 'lxml')

    for tag in html.find_all('ul', class_='meal-plan-day-ingredients'):
        items = tag.children

        for item in items:
            ingredient = get_ingredient_detail(item.text)

            if (ingredient['id'] in data.keys()):
                data[ingredient['id']] = {'text': ingredient['text'],
                                          'amount': data[ingredient['id']]['amount'] + ingredient['amount']}
            else:
                data[ingredient['id']] = {'text': ingredient['text'],
                                          'amount': ingredient['amount']}
