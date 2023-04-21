from bs4 import BeautifulSoup

html = ''
with open('index.html', 'r') as file:
    html = file.read()
soup = BeautifulSoup(html, 'html.parser')

# title
print(soup.title)

# title name
print(soup.title.name)

# title string
print(soup.title.string)

# parent name
print(soup.title.parent.name)

# finds all elements
print(soup.find_all('a'))

# finds only first element
print(soup.find('a'))

for link in soup.find_all('a'):
    print(link.get('href'))

# get whole text from webpage
print(soup.get_text().strip())


print(soup)
