# from bs4 import BeautifulSoup
#
# html = ''
# with open('index.html', 'r') as file:
#     html = file.read()
# soup = BeautifulSoup(html, 'html.parser')
#
# # title
# print(soup.title)
#
# # title name
# print(soup.title.name)
#
# # title string
# print(soup.title.string)
#
# # parent name
# print(soup.title.parent.name)
#
# # finds all elements
# print(soup.find_all('a'))
#
# # finds only first element
# print(soup.find('a'))
#
# for link in soup.find_all('a'):
#     print(link.get('href'))
#
# # get whole text from webpage
# print(soup.get_text().strip())
#
# tag = soup.p
# print(tag)
# if tag['class'][0] == 'title':
#     print('correct')
# # p - tag
# # class/id = attribute
#
# # whole tag: <p class="title"><b>The Dormouse's story</b></p>
#
# soup.p['id'] = 'unique id'
# print(soup.get('class'))
#
# print(soup.p.get_attribute_list('class'))
#
# print(soup.p.string.replace_with('Replaced Text'))
# print(soup.p.string)
# rel_soup = BeautifulSoup('<p rel="reltext">Back to the <a rel="index first">homepage</a></p>', 'html.parser')
# print(rel_soup.a['rel'])
# import time
#
import time

print(bin(0b0001+0b0010))
print(eval('0b11'))