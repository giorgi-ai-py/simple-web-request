from bs4 import BeautifulSoup

url = "https://google.com"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

page_title = soup.title.text

print ("what would you like to see?")
print ("1. raw html data")
print ("or...")
print ("2. just the title")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
        print (response.text)
elif choice == "2":
        print ("the title of the website is...")
        time.sleep(3)
        print ("*insert drumroll sound effect*")
        time.sleep(3)
        print (page_title)
else:
        print ("just type 1 or 2")
        print ("its not that hard :/")
