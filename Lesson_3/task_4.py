import requests


list_link = input("Enter links separated by space").split(" ")
for website in list_link:
    test = requests.get(website)
    if test.status_code == 200:
            print("OK")
    elif test.status_code == 302:
            print("Failed")