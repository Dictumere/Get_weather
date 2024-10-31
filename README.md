# Weather Determination Script

This Python script retrieves weather information for a list of cities by interacting with the [wttr.in](https://wttr.in) weather service. It outputs the weather data for specified locations in Russian.

## Installation
1. Ensure Python 3 is installed.
2. Install Poetry (if not already installed). Use:
```bash
pip install poetry
```
3. Install dependencies from ```pyproject.toml``` using:
```bash
poetry install
```
4. Activate the virtual environment:
```bash
poetry shell
```
5. Alternative: If you need to install dependencies in requirements.txt without using Poetry, use:
```bash
pip install -r requirements.txt
```
## Usage

Run the script by executing:
```bash
python main.py
```
This will output the weather information for the cities specified in `locations`, including:
- Лондон
- svo (Moscow Sheremetyevo Airport)
- Череповец

### Code Structure
- `determine_weather(location)`: Fetches weather details for the given location.
- Main block iterates over a list of cities to print their weather information.

## Project Goals

This code was developed for educational purposes as part of the web developer course on [dvmn.org](https://dvmn.org).
