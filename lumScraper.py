import requests, json
from bs4 import BeautifulSoup

f = open('/Users/kaushik/Documents/lumiere_index/lumIndices.json', 'w')

for i in range(49300,49400):
    page = requests.get("https://lumiere.berkeley.edu/students/items/"+str(i))
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(class_="page-title column span-24")
    if results.text.strip():
        data = [str(i), results.text.strip(),"https://lumiere.berkeley.edu/students/items/"+str(i)]
        json.dump(data, f)