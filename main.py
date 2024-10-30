import requests


def determine_weather(location):
    url_template = 'https://wttr.in/{}?'
    url = url_template.format(location)
    payload = {'lang': 'ru', 'M': '', 'n': '', 'q': '', 'T': '', '3': ''}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response.text


if __name__ == "__main__":
    locations = [('Лондон'),
                 ('svo'),
                 ('Череповец')]
    for location in locations:
        weather = determine_weather(location)
        print(weather)
