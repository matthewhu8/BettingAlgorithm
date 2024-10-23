import requests as req
import pandas as pd

scoreboard_url = 'https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard'
params = {
    "dates": "20231022"  # Example parameter, adjust according to the endpoint
}

try:
    response = req.get(scoreboard_url)
    response.raise_for_status()  # Check if the request was successful
    data = response.json()  # Extract JSON data from the response
except req.exceptions.RequestException as e:
    print(f"Error: {e}")

game_count = 0
for game in data['events']:
    game_count += 1
    print(game_count)

