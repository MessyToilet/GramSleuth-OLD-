import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.instagram.com/accounts/login/")
html_content = response.text

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Extract specific information from the HTML using BeautifulSoup methods
# For example, to find all the <a> tags in the HTML:
a_tags = soup.find_all('a')

# Print the extracted information
for tag in a_tags:
    print(tag.text)
