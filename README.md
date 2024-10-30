# Weather Determination Script

This Python script retrieves weather information for a list of cities by interacting with the [wttr.in](https://wttr.in) weather service. It outputs the weather data for specified locations in Russian.

## Installation

Ensure Python 3 is installed. Install required dependencies with the following command:
```bash
pip install -r requirements.txt
```

## Usage

Run the script by executing:
```bash
python <filename>.py
```
This will output the weather information for the cities specified in `articles_id`, including:
- Лондон
- svo (Moscow Sheremetyevo Airport)
- Череповец

### Code Structure
- `determine_weather(article_id)`: Fetches weather details for the given location.
- Main block iterates over a list of cities to print their weather information.

## Project Goals

This code was developed for educational purposes as part of the web developer course on [dvmn.org](https://dvmn.org).
