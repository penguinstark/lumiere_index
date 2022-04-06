import requests
from bs4 import BeautifulSoup
for i in range(49290,49390):
    URL = "https://lumiere.berkeley.edu/students/items/"+str(i)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(class_="page-title column span-24")
    if results.text.strip():
        print(str(i)+results.text)