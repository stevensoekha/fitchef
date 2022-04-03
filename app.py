from bs4 import BeautifulSoup
import re

file1 = open('./week/1.html', 'r')
content = file1.read()

parsed1 = BeautifulSoup(content, 'lxml')

file2 = open('./week/2.html', 'r')
content = file2.read()

parsed2 = BeautifulSoup(content, 'lxml')

file3 = open('./week/3.html', 'r')
content = file3.read()

parsed3 = BeautifulSoup(content, 'lxml')

file4 = open('./week/4.html', 'r')
content = file4.read()

parsed4 = BeautifulSoup(content, 'lxml')

data = dict()

week = [parsed1, parsed2, parsed3, parsed4]

for index, day in enumerate(week):
    for tag in day.find_all('ul', class_='meal-plan-day-ingredients'):
        list_items = tag.children

        for item in list_items:
            id = ''.join([i for i in item.text if not i.isdigit()]
                         ).replace(',', '').replace(' ', '')
            text = ''.join([i for i in item.text if not i.isdigit()]
                           ).replace(',', '')
            amount = [int(float(s))
                      for s in re.findall(r'-?\d+\.?\d*', item.text)]

            if (id in data.keys()):
                data[id] = {'text': text, 'amount': data[id]['amount']}
            else:
                data[id] = {'text': text, 'amount': 0}

            if (index == 3):
                data[id]['amount'] = data[id]['amount'] + \
                    (amount[0] if len(amount) else 1)
            else:
                data[id]['amount'] = data[id]['amount'] + \
                    (amount[0]*2 if len(amount) else 2)


for id in data:
    print(data[id]['amount'], data[id]['text'])
