import csv
import requests
from bs4 import BeautifulSoup

with open("population.csv", "w", encoding="UTF-8", newline="\n") as csvfile :
    population_writer = csv.writer(csvfile)
    population_writer.writerow(["Country","Population"])

    current_url = "https://en.wikipedia.org/wiki/Germany"
    r = requests.get(current_url)
    soup = BeautifulSoup(r.text, "html.parser")
    link = soup.find_all("a", string="Population")
    td = link[0].find_parent("tr").find_next_sibling("tr").find_all("td", {"class": "infobox-data"})
    value = td[0].text
    population_writer.writerow(["Germany",value])
    print("Germany : ",value)

    current_url = "https://en.wikipedia.org/wiki/France"
    r = requests.get(current_url)
    soup = BeautifulSoup(r.text, "html.parser")
    link = soup.find_all("a", string="Population")
    td = link[0].find_parent("tr").find_next_sibling("tr").find_all("td", {"class": "infobox-data"})
    value = td[0].text
    population_writer.writerow(["France",value])
    print("France : ",value)

    current_url = "https://en.wikipedia.org/wiki/Thailand"
    r = requests.get(current_url)
    soup = BeautifulSoup(r.text, "html.parser")
    link = soup.find_all("a", string="Population")
    td = link[0].find_parent("tr").find_next_sibling("tr").find_all("td", {"class": "infobox-data"})
    value = td[0].text
    population_writer.writerow(["Thailand",value])
    print("Thailand : ",value) 