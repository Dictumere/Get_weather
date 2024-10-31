# Weather Determination Script

This Python script retrieves weather information for a list of cities by interacting with the [wttr.in](https://wttr.in) weather service. It outputs the weather data for specified locations in Russian.

## Installation Instructions
1. You can either clone the public repository or, download the [tarball](https://github.com/Dictumere/Get_weather.git):
```bash
git clone https://github.com/Dictumere/Get_weather.git
```
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```
## Example of Running the Scripts

To run the script and get weather information, execute the following command in your terminal::
```bash
python main.py
```
This will output the weather information for the cities specified in `locations`, including:
- Лондон
- svo (Moscow Sheremetyevo Airport)
- Череповец

## Example Expected Output
After running the script, you should see something like this in the console:
![Example_part_1](https://gist.github.com/user-attachments/assets/ed61903f-2f71-4c42-b0a4-698c15dcb1e7)
![Example_part_2](https://gist.github.com/user-attachments/assets/dd8b1639-5e9a-493a-a2e2-c6b155709cec)
![Example_part_3](https://gist.github.com/user-attachments/assets/54e0ed8a-b8a0-4f13-b424-601efccb44ee)

### Code Structure
- `determine_weather(location)`: Fetches weather details for the given location.
- Main block iterates over a list of cities to print their weather information.

## Project Goals

This code was developed for educational purposes as part of the web developer course on [dvmn.org](https://dvmn.org).
