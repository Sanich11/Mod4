import requests
from bs4 import BeautifulSoup


url = 'https://www.raexpert.ru/rankingtable/mfi/2022/tab02/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')


# Находим таблицу
table = soup.find('table', {'class': 'ranking_content'})


# Получаем заголовки столбцов
headers = table.find_all('th')[1:]


# Создаем пустой список для хранения данных
data = []


# Проходимся по каждому заголовку столбца
for header in headers:
    # Получаем значение ячейки
    value = header.find('td', {'class': 'raexpert-cell raexpert-cell__value'}).text
    

    # Добавляем данные в список
    data.append([value])


# Открываем файл Excel
with open('mfi_2022_tab02.xlsx', 'w', newline='') as file:
    for row in data:
        file.write(row + '\n')