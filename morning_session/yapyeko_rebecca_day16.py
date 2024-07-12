# Web Scraping
# Libraries for web scraping
# Request, BeautifulSoup, lxml, scrapy Selenium
# API Keys
# Exercise, get data from openweathermap.org ,

 # Step 1: Import Libraries 
import requests
from bs4 import BeautifulSoup
import csv
import json
 
 # Step 2: Fetch the web pages
 
url = 'http://ryeko.org'
response = requests.get(url) 
# Web Scraping
# Libraries for web scraping
# Request, BeautifulSoup, lxml, scrapy Selenium
# API Keys
# Exercise, get data from openweathermap.org ,

 # Step 1: Import Libraries 
import requests
from bs4 import BeautifulSoup
import csv
import json
 
 # Step 2: Fetch the web pages
 
url = 'http://ryeko.org'
response = requests.get(url) 
# Web Scraping
# Libraries for web scraping
# Request, BeautifulSoup, lxml, scrapy Selenium
# API Keys
# Exercise, get data from openweathermap.org ,

 # Step 1: Import Libraries 
import requests
from bs4 import BeautifulSoup
import csv
import json
 
 # Step 2: Fetch the web pages
 
url = 'http://ryeko.org'
response = requests.get(url) 
html_content = response.text
# api_key = 'Ur API key' without this you cant scrape any data from a website

# Step 3: Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Step 4: Find the specific data
data = []

# for card in soup.findall('div', class_='card'):
#     name = card.find('h3', class_='card-title').text.strip()
#     description = card.find('p', class_='card-text').text.strip()
#     image_url = card.find('img', class_='card-img-top').text.strip()
for item in soup.find_all('a'):
    title = item.text.strip()
    link = item.get('href')
    data.append({'title': title, 'link': link})
# Step 5: Save the data to a CSV file
csv_file = 'scrapped_data.csv'
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['title', 'link'])
    writer.writeheader()
    for row in data:
        writer.writerow(row)
        
        
# Step 6: Save the data to a JSON file
json_file = 'scraped_data.json'
with open(json_file, mode='w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
    

# Step 7: Save successfully to csv and json format
print(f'Data saved successfully to {csv_file} and {json_file} format!') 

#Exercise scrape data using api key
# scrape data from the http://openweathermap.org
# Current weatherdata (is whats needed from the site)
# Step 1: Fetch the web pages
api_key = '336e6e8bd4820f250616b1c3d5529e08'  # Replace with your actual API key
city = 'Kampala'  # Replace with the city you want to get weather data for
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

response = requests.get(url)
weather_data = response.json()

# Step 2: Parse the JSON response
data = [{
    'city': weather_data['name'],
    'temperature': weather_data['main']['temp'],
    'weather': weather_data['weather'][0]['description'],
    'humidity': weather_data['main']['humidity'],
    'pressure': weather_data['main']['pressure'],
    'wind_speed': weather_data['wind']['speed']
}]
# Step 3: Save the data to a CSV file
csv_file = 'weather_data.csv'
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerow(data[0])

# Step 4: Save the data to a JSON file
json_file = 'weather_data.json'
with open(json_file, mode='w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

# Step 6: Save successfully to csv and json format
print(f'Data saved successfully to {csv_file} and {json_file} format!')