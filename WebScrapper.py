import requests
from bs4 import BeautifulSoup
from csv import writer # allow us to write csv file

# link that you want to Scrap
response = requests.get('https://rohansinghkalhans.firebaseapp.com/')

soup = BeautifulSoup(response.text, "html.parser")

# this will find all the class with this name and give the data to you, change according you. 
posts = soup.find_all(class_="col-md-9 col-12")

# now we are creating a CSV file where we store all the data that we scrapping with name posts.csv
with open('posts.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    header = ['Title', 'Link', 'Date']   # title of rows in csv file
    csv_writer.writerow(header)
    # we are finding the class intro in the main class and scrapping it, but if we just scrap all it will give tags also, so we are using get_text to get only data/text and replacing all 'next line' with space.
    for post in posts:
        title = post.find(class_='intro').get_text().replace('\n', ' ')  # we are saving all in title heading, and replace space with nothing
        csv_writer.writerow([title])