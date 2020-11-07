from bs4 import BeautifulSoup
import requests
import os


input_image = input("請輸入要下載的圖片：")

response = requests.get(f"https://unsplash.com/s/photos/{input_image}")
soup = BeautifulSoup(response.text, "lxml")

results = soup.find_all("img", {"class": "_2zEKz"}, limit=5)

image_links = [result.get("src") for result in results]

for index, link in enumerate(image_links):

    if not os.path.exists("images"):
        os.mkdir("images")

    img = requests.get(link)
    with open("images\\" + input_image + str(index+1) + ".jpg", "wb") as file:
        file.write(img.content)
