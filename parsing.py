from bs4 import BeautifulSoup

# Открываем файл для чтения (rb)
htmlfile = open("skillbox.html", "rb")
# Читаем файл в переменную
code = htmlfile.read()
htmlfile.close()
# Разбираем содержимое файла на HTML-элементы
soup = BeautifulSoup(code,"html.parser")

# Находим все ссылки
links = soup.findAll('a')
# Для каждой ссылки в списке ссылок (links) вывести текст
print([item.string.strip() for item in links])
