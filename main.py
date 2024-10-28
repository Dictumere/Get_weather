import requests


def determine_weather(article_id, lang, use_params):
    url_template = 'https://wttr.in/{}?nTqu3%20HTTP/1.1'
    url = url_template.format(article_id)
    if use_params:
        payload = {'lang': lang, 'M': '', 'n': '', 'q': '', 'T': '', '3': ''}
    else:
        payload = {}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response.text


if __name__ == "__main__":
    articles_id = [('London', 'en', False),
                   ('svo', 'en', False),
                   ('Череповец', 'ru', True)]
    for article_id, lang, use_params in articles_id:
        weather = determine_weather(article_id, lang, use_params)
        print(weather)
