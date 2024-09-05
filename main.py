import requests
from send_email import send_email

api_key ="39d7a7b933854bbdb602605d14d17ba3"

url="https://newsapi.org/v2/everything?q=tesla&\
from=2024-08-05&sortBy=publishedAt&\
apiKey=39d7a7b933854bbdb602605d14d17ba3"

response = requests.get(url)

content = response.json()

body = "subject :Today's new \n\n"

for article in content['articles'][:20]:
    if article['title']is not None and article['description'] is not None:
        body = body + article['title'] + "\n" \
            + article ['description']\
            + "\n" + article['url'] + 2 * "\n"

body = body.encode('utf-8')
send_email(message=body)