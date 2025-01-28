import re

from bs4 import BeautifulSoup
with open("blank/index2.html", encoding="utf-8") as file:
    src = file.read()
# print(src)
soup = BeautifulSoup(src, "lxml")

# title = soup.title
#
# print(title.string)
# выводит первый элемент с таким тегом
# page_h1 = soup.find("h1")
# print(page_h1)
# # выводит все элементы с таким тегом
# page_all_h1 = soup.find_all("h1")
# for item in page_all_h1:
#     print(item)
# поиск определенного кода
# user_name = soup.find("div", class_="user__name")
# print(user_name.text.strip())

# user_name = soup.find("div", {"class": "user__name"}).find("span").text
# print(user_name)
#
# find_all_spans_in_user_info = soup.find(
#     class_="user__info").find_all("span")
# for item in find_all_spans_in_user_info:
#     print(item.text)

# social_link = soup.find(class_="social__networks").find("ul").find_all("a")
# for item in social_link:
#     print(item)
#
# all_a = soup.find_all("a")
# # print(all_a)
# for item in all_a:
#     item_irl = item.get("href")
#     item_text = item.text
#     print(f"{item_text}:{item_irl}")

#поиск "родителей"
# post_div = soup.find(class_="post__text").find_parent()
# print(post_div)

# post_div = soup.find(class_="post__text").find_parent("div","user__post")
# print(post_div)

#поднимается до самого верха

# post_div = soup.find(class_="post__text").find_parents("div","user__post")
# print(post_div)

# .next_element возращает следующий элемент в коде .previous_element предыдущий
# next_el = soup.find(class_="post__title").next_element.next_element первый вернет переход на следующую строку
# print(next_el)
# next_el = soup.find(class_="post__title").find_next # сразу возращает следующий элемент
# print(next_el)

# next_sib = soup.find(class_="post__title").find_next_sibling
# print(next_sib)
#
# prev_sib = soup.find(class_="post__date").find_previous_sibling
# print(prev_sib)

#поиск по тексту

find_all_clothes = soup.find_all(text=re.compile("[Оо]дежда"))
print(find_all_clothes)