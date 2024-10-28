import requests


def determine_weather(article_id):
    url_template = 'https://wttr.in/{}?nTqu3%20HTTP/1.1'
    url = url_template.format(article_id)
    payload = {'lang': 'ru', 'M': '', 'n': '', 'q': '', 'T': '', '3': ''}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response.text


if __name__ == "__main__":
    articles_id = [('Лондон'),
                   ('svo'),
                   ('Череповец')]
    for article_id in articles_id:
        weather = determine_weather(article_id)
        print(weather)