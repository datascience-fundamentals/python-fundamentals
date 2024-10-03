import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/questions"
resp = requests.get(url)
text = resp.text
soup = BeautifulSoup(text, "html.parser")
questions = soup.select(".s-post-summary")
for question in questions:
    title = question.select_one(".s-link").get_text()
    user = question.select_one(".s-user-card--link").get_text()
    print(title.strip())
    print(user.strip())

# reading attributes from label in html
data_post_type_id = questions[0]["data-post-type-id"]
print(data_post_type_id)
