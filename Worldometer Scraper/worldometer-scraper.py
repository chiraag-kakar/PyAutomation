import requests
from bs4 import BeautifulSoup

url = "https://www.worldometers.info/coronavirus/"
# To scrape data country specific url path need to be modified
# url = "https://www.worldometers.info/coronavirus/country/india"
req = requests.get(url)
bsObj = BeautifulSoup(req.text, "html.parser")
data = bsObj.find_all("div",class_ = "maincounter-number")

print("Total Cases: ", data[0].text.strip())
print("Total Deaths: ", data[1].text.strip())
print("Total Recovered: ", data[2].text.strip())
