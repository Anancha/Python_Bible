import requests
from bs4 import BeautifulSoup

current_url = "https://en.wikipedia.org/wiki/Germany"
r = requests.get(current_url)
soup = BeautifulSoup(r.text, "html.parser")
link = soup.find_all("a", string="Population")
td = link[0].find_parent("tr").find_next_sibling("tr").find_all("td", {"class": "infobox-data"})
value = td[0].text
print("Germany : ",value)

current_url = "https://en.wikipedia.org/wiki/France"
r = requests.get(current_url)
soup = BeautifulSoup(r.text, "html.parser")
link = soup.find_all("a", string="Population")
td = link[0].find_parent("tr").find_next_sibling("tr").find_all("td", {"class": "infobox-data"})
value = td[0].text
print("France : ",value)

current_url = "https://en.wikipedia.org/wiki/Thailand"
r = requests.get(current_url)
soup = BeautifulSoup(r.text, "html.parser")
link = soup.find_all("a", string="Population")
td = link[0].find_parent("tr").find_next_sibling("tr").find_all("td", {"class": "infobox-data"})
value = td[0].text
print("Thailand : ",value)
