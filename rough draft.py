import requests
import json

# API URL with query parameters for event odds
sport = 'americanfootball_nfl'  # Specify the sport
xyz = 'a60ecb3c882d09f08b6e194e858aec42'
event_id = xyz
  # Your specified event ID

# Parameters
api_key = '56b1c1af71544f4f9a63799520c4d826'
regions = 'us'
markets = 'player_pass_yds'  # Market type as per your example
date_format = 'iso'  # Specify the date format you want
odds_format = 'american'

url = f'https://api.the-odds-api.com/v4/sports/{sport}/events/{event_id}/odds'

# Parameters from the URL
params = {
    'apiKey': api_key,
    'regions': regions,
    'markets': markets,
    'dateFormat': date_format,
    'oddsFormat': odds_format,
}

# Headers
headers = {
    'accept': 'application/json'
}

# Make the API request
response = requests.get(url, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data
    data = response.json()
    
    # Initialize a dictionary to hold the total points and counts for each player
    player_points = {}

    # Iterate through each bookmaker
    for bookmaker in data['bookmakers']:
        for market in bookmaker['markets']:
            for outcome in market['outcomes']:
                description = outcome['description']
                point = outcome['point']

                # Add points to the corresponding player
                if description not in player_points:
                    player_points[description] = {'total_points': 0, 'count': 0}
                
                player_points[description]['total_points'] += point
                player_points[description]['count'] += 1

    # Calculate average points for each player
    average_points = {player: (info['total_points'] / info['count']) for player, info in player_points.items()}

    # Create a dictionary to save
    dictionary_pass_yards = {
        'average_pass_yards': average_points
    }

else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")






# API URL with query parameters for event odds
sport = 'americanfootball_nfl'  # Specify the sport
 # Your specified event ID

# Parameters
api_key = '56b1c1af71544f4f9a63799520c4d826'
regions = 'us'
markets = 'player_rush_yds'  # Market type as per your example
date_format = 'iso'  # Specify the date format you want
odds_format = 'american'

url = f'https://api.the-odds-api.com/v4/sports/{sport}/events/{event_id}/odds'

# Parameters from the URL
params = {
    'apiKey': api_key,
    'regions': regions,
    'markets': markets,
    'dateFormat': date_format,
    'oddsFormat': odds_format,
}

# Headers
headers = {
    'accept': 'application/json'
}

# Make the API request
response = requests.get(url, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data
    data = response.json()
    
    # Initialize a dictionary to hold the total points and counts for each player
    player_points = {}

    # Iterate through each bookmaker
    for bookmaker in data['bookmakers']:
        for market in bookmaker['markets']:
            for outcome in market['outcomes']:
                description = outcome['description']
                point = outcome['point']

                # Add points to the corresponding player
                if description not in player_points:
                    player_points[description] = {'total_points': 0, 'count': 0}
                
                player_points[description]['total_points'] += point
                player_points[description]['count'] += 1

    # Calculate average points for each player
    average_points = {player: (info['total_points'] / info['count']) for player, info in player_points.items()}

    # Create a dictionary to save the data
    dictionary_rush_yards = {
        'average_rush_yards': average_points
    }




# API URL with query parameters for event odds
sport = 'americanfootball_nfl'  # Specify the sport
  # Your specified event ID

# Parameters
api_key = '56b1c1af71544f4f9a63799520c4d826'
regions = 'us'
markets = 'player_reception_yds'  # Market type as per your example
date_format = 'iso'  # Specify the date format you want
odds_format = 'american'

url = f'https://api.the-odds-api.com/v4/sports/{sport}/events/{event_id}/odds'

# Parameters from the URL
params = {
    'apiKey': api_key,
    'regions': regions,
    'markets': markets,
    'dateFormat': date_format,
    'oddsFormat': odds_format,
}

# Headers
headers = {
    'accept': 'application/json'
}

# Make the API request
response = requests.get(url, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data
    data = response.json()
    
    # Initialize a dictionary to hold the total points and counts for each player
    player_points = {}

    # Iterate through each bookmaker
    for bookmaker in data['bookmakers']:
        for market in bookmaker['markets']:
            for outcome in market['outcomes']:
                description = outcome['description']
                point = outcome['point']

                # Add points to the corresponding player
                if description not in player_points:
                    player_points[description] = {'total_points': 0, 'count': 0}
                
                player_points[description]['total_points'] += point
                player_points[description]['count'] += 1

    # Calculate average points for each player
    average_points = {player: (info['total_points'] / info['count']) for player, info in player_points.items()}

    # Create a dictionary to save the data
    dictionary_reception_yards = {
        'average_reception_yards': average_points
    }





# API URL with query parameters for event odds
sport = 'americanfootball_nfl'  # Specify the sport
  # Your specified event ID

# Parameters
api_key = '56b1c1af71544f4f9a63799520c4d826'
regions = 'us'
markets = 'player_receptions'  # Changed market type to 'player_receptions'
date_format = 'iso'  # Specify the date format you want
odds_format = 'american'

url = f'https://api.the-odds-api.com/v4/sports/{sport}/events/{event_id}/odds'

# Parameters from the URL
params = {
    'apiKey': api_key,
    'regions': regions,
    'markets': markets,
    'dateFormat': date_format,
    'oddsFormat': odds_format,
}

# Headers
headers = {
    'accept': 'application/json'
}

# Function to convert American odds to implied probability
def american_to_implied_probability(odds):
    if odds > 0:
        return 100 / (odds + 100)
    else:
        return -odds / (-odds + 100)

# Function to calculate no-vig probabilities ensuring they sum to 100%
def calculate_no_vig(over_prob, under_prob):
    total = over_prob + under_prob
    no_vig_over = over_prob / total
    no_vig_under = under_prob / total
    return no_vig_over, no_vig_under

# Make the API request
response = requests.get(url, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data
    data = response.json()
    
    # Dictionary to store no-vig over probabilities for each player
    player_no_vig_over_probs = {}

    # Loop through bookmakers and calculate no-vig probabilities
    for bookmaker in data['bookmakers']:
        for market in bookmaker['markets']:
            if market['key'] == 'player_receptions':  # Adjusted to check for 'player_receptions' market
                outcomes = market['outcomes']
                
                # Separate over and under for each player
                player_outcomes = {}
                for outcome in outcomes:
                    player_name = outcome['description']
                    outcome_type = outcome['name']  # "Over" or "Under"
                    if player_name not in player_outcomes:
                        player_outcomes[player_name] = {}
                    player_outcomes[player_name][outcome_type] = american_to_implied_probability(outcome['price'])
                
                # Calculate no-vig probabilities for each player
                for player, probs in player_outcomes.items():
                    if 'Over' in probs and 'Under' in probs:
                        no_vig_over, no_vig_under = calculate_no_vig(probs['Over'], probs['Under'])
                        
                        # Collect the no-vig over probability for consensus averaging
                        if player not in player_no_vig_over_probs:
                            player_no_vig_over_probs[player] = []
                        player_no_vig_over_probs[player].append(no_vig_over)

    # Calculate and save consensus no-vig probability averages for each player
    consensus_reception_probs = {}
    
    for player, over_probs in player_no_vig_over_probs.items():
        avg_no_vig_over = sum(over_probs) / len(over_probs)
        consensus_reception_probs[player] = avg_no_vig_over

    # Create a dictionary to save the data
    dictionary_receptions = {
        'average_pass_receptions': consensus_reception_probs
    }






# API URL with query parameters for event odds
sport = 'americanfootball_nfl'  # Specify the sport
  # Your specified event ID

# Parameters
api_key = '56b1c1af71544f4f9a63799520c4d826'
regions = 'us'
markets = 'player_pass_tds'  # Market type
date_format = 'iso'  # Specify the date format you want
odds_format = 'american'

url = f'https://api.the-odds-api.com/v4/sports/{sport}/events/{event_id}/odds'

# Parameters from the URL
params = {
    'apiKey': api_key,
    'regions': regions,
    'markets': markets,
    'dateFormat': date_format,
    'oddsFormat': odds_format,
}

# Function to convert American odds to implied probability
def american_to_implied_probability(odds):
    return 100 / (odds + 100) if odds > 0 else -odds / (-odds + 100)

# Function to calculate no-vig probabilities ensuring they sum to 100%
def calculate_no_vig(over_prob, under_prob):
    total = over_prob + under_prob
    return over_prob / total, under_prob / total

# Make the API request
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data
    data = response.json()
    
    # Dictionary to store no-vig over probabilities for each player
    player_no_vig_over_probs = {}

    # Loop through bookmakers and calculate no-vig probabilities
    for bookmaker in data['bookmakers']:
        for market in bookmaker['markets']:
            if market['key'] == 'player_pass_tds':
                outcomes = market['outcomes']
                
                # Separate over and under for each player
                player_outcomes = {}
                for outcome in outcomes:
                    player_name = outcome['description']
                    outcome_type = outcome['name']  # "Over" or "Under"
                    
                    if player_name not in player_outcomes:
                        player_outcomes[player_name] = {}
                    player_outcomes[player_name][outcome_type] = american_to_implied_probability(outcome['price'])
                
                # Calculate no-vig probabilities for each player
                for player, probs in player_outcomes.items():
                    if 'Over' in probs and 'Under' in probs:
                        no_vig_over, _ = calculate_no_vig(probs['Over'], probs['Under'])
                        if player not in player_no_vig_over_probs:
                            player_no_vig_over_probs[player] = []
                        player_no_vig_over_probs[player].append(no_vig_over)

    # Calculate and save consensus no-vig probability averages for each player
    consensus_pass_td_probs = {}
    
    for player, over_probs in player_no_vig_over_probs.items():
        avg_no_vig_over = sum(over_probs) / len(over_probs)
        consensus_pass_td_probs[player] = avg_no_vig_over

    # Create a dictionary to save the data
    dictionary_pass_tds = {
        'average_pass_touchdowns': consensus_pass_td_probs
    }




# API URL with query parameters for event odds
sport = 'americanfootball_nfl'  # Specify the sport
 # Your specified event ID

# Parameters
api_key = '56b1c1af71544f4f9a63799520c4d826'
regions = 'us'
markets = 'player_pass_interceptions'  # Market type updated to player_pass_interceptions
date_format = 'iso'  # Specify the date format you want
odds_format = 'american'

url = f'https://api.the-odds-api.com/v4/sports/{sport}/events/{event_id}/odds'

# Parameters from the URL
params = {
    'apiKey': api_key,
    'regions': regions,
    'markets': markets,
    'dateFormat': date_format,
    'oddsFormat': odds_format,
}

# Function to convert American odds to implied probability
def american_to_implied_probability(odds):
    return 100 / (odds + 100) if odds > 0 else -odds / (-odds + 100)

# Function to calculate no-vig probabilities ensuring they sum to 100%
def calculate_no_vig(over_prob, under_prob):
    total = over_prob + under_prob
    return over_prob / total, under_prob / total

# Make the API request
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data
    data = response.json()
    
    # Dictionary to store no-vig over probabilities for each player
    player_no_vig_over_probs = {}

    # Loop through bookmakers and calculate no-vig probabilities
    for bookmaker in data['bookmakers']:
        for market in bookmaker['markets']:
            if market['key'] == 'player_pass_interceptions':  # Check for the new market type
                outcomes = market['outcomes']
                
                # Separate over and under for each player
                player_outcomes = {}
                for outcome in outcomes:
                    player_name = outcome['description']
                    outcome_type = outcome['name']  # "Over" or "Under"
                    
                    if player_name not in player_outcomes:
                        player_outcomes[player_name] = {}
                    player_outcomes[player_name][outcome_type] = american_to_implied_probability(outcome['price'])
                
                # Calculate no-vig probabilities for each player
                for player, probs in player_outcomes.items():
                    if 'Over' in probs and 'Under' in probs:
                        no_vig_over, _ = calculate_no_vig(probs['Over'], probs['Under'])
                        if player not in player_no_vig_over_probs:
                            player_no_vig_over_probs[player] = []
                        player_no_vig_over_probs[player].append(no_vig_over)

    # Calculate and save consensus no-vig probability averages for each player
    consensus_pass_interception_probs = {}
    
    for player, over_probs in player_no_vig_over_probs.items():
        avg_no_vig_over = sum(over_probs) / len(over_probs)
        consensus_pass_interception_probs[player] = avg_no_vig_over

    # Create a dictionary to save the data
    dictionary_pass_interceptions = {
        'average_pass_interceptions': consensus_pass_interception_probs
    }







# API URL with query parameters for event odds
sport = 'americanfootball_nfl'  # Specify the sport
 # Your specified event ID

# Parameters
api_key = '56b1c1af71544f4f9a63799520c4d826'
regions = 'us'
markets = 'player_anytime_td'  # Market type as per your example
date_format = 'iso'  # Specify the date format you want
odds_format = 'american'

url = f'https://api.the-odds-api.com/v4/sports/{sport}/events/{event_id}/odds'

# Parameters from the URL
params = {
    'apiKey': api_key,
    'regions': regions,
    'markets': markets,
    'dateFormat': date_format,
    'oddsFormat': odds_format,
}

# Headers
headers = {
    'accept': 'application/json'
}

# Function to convert American odds to implied probability
def american_to_implied_probability(odds):
    if odds > 0:
        return 100 / (odds + 100)
    else:
        return -odds / (-odds + 100)

# Make the API request
response = requests.get(url, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data
    data = response.json()
    
    # Dictionary to store probabilities for each player
    player_probabilities = {}

    # Loop through bookmakers and calculate probabilities
    for bookmaker in data['bookmakers']:
        for market in bookmaker['markets']:
            if market['key'] == 'player_anytime_td':
                outcomes = market['outcomes']
                
                # Process outcomes for each player
                for outcome in outcomes:
                    player_name = outcome['description']
                    odds = outcome['price']  # Get the odds for the player
                    implied_probability = american_to_implied_probability(odds) * 100  # Convert to percentage
                    
                    # Update player_probabilities with implied probabilities
                    if player_name not in player_probabilities:
                        player_probabilities[player_name] = []
                    player_probabilities[player_name].append(implied_probability)
                
    # Calculate and save average implied probabilities for each player
    consensus_anytime_td_probs = {}
    
    for player, probabilities in player_probabilities.items():
        average_probability = sum(probabilities) / len(probabilities)
        consensus_anytime_td_probs[player] = average_probability

    # Create a dictionary to save the data
    dictionary_anytime_td = {
        'average_anytime_td_probabilities': consensus_anytime_td_probs
    }





# API URL with query parameters for event odds
sport = 'americanfootball_nfl'  # Specify the sport
 # Your specified event ID

# Parameters
api_key = '56b1c1af71544f4f9a63799520c4d826'
regions = 'us'
markets = 'player_pass_tds'  # Market type as per your example 
date_format = 'iso'  # Specify the date format you want
odds_format = 'american'

url = f'https://api.the-odds-api.com/v4/sports/{sport}/events/{event_id}/odds'

# Parameters from the URL
params = {
    'apiKey': api_key,
    'regions': regions,
    'markets': markets,
    'dateFormat': date_format,
    'oddsFormat': odds_format,
}

# Headers
headers = {
    'accept': 'application/json'
}

# Make the API request
response = requests.get(url, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data
    data = response.json()
    
    # Initialize a dictionary to hold the total points and counts for each player
    player_points = {}

    # Iterate through each bookmaker
    for bookmaker in data['bookmakers']:
        for market in bookmaker['markets']:
            for outcome in market['outcomes']:
                description = outcome['description']
                point = outcome['point']

                # Add points to the corresponding player
                if description not in player_points:
                    player_points[description] = {'total_points': 0, 'count': 0}
                
                player_points[description]['total_points'] += point
                player_points[description]['count'] += 1

    # Calculate average points for each player
    average_points = {player: (info['total_points'] / info['count']) for player, info in player_points.items()}

    # Create a dictionary to save the data
    dictionary_pass_tds_over = {
        'average_pass_tds': average_points
    }





# API URL with query parameters for event odds
sport = 'americanfootball_nfl'  # Specify the sport
  # Your specified event ID

# Parameters
api_key = '56b1c1af71544f4f9a63799520c4d826'
regions = 'us'
markets = 'player_pass_interceptions'  # Market type as per your example
date_format = 'iso'  # Specify the date format you want
odds_format = 'american'

url = f'https://api.the-odds-api.com/v4/sports/{sport}/events/{event_id}/odds'

# Parameters from the URL
params = {
    'apiKey': api_key,
    'regions': regions,
    'markets': markets,
    'dateFormat': date_format,
    'oddsFormat': odds_format,
}

# Headers
headers = {
    'accept': 'application/json'
}

# Make the API request
response = requests.get(url, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data
    data = response.json()
    
    # Initialize a dictionary to hold the total points and counts for each player
    player_points = {}

    # Iterate through each bookmaker
    for bookmaker in data['bookmakers']:
        for market in bookmaker['markets']:
            for outcome in market['outcomes']:
                description = outcome['description']
                point = outcome['point']

                # Add points to the corresponding player
                if description not in player_points:
                    player_points[description] = {'total_points': 0, 'count': 0}
                
                player_points[description]['total_points'] += point
                player_points[description]['count'] += 1

    # Calculate average points for each player
    average_points = {player: (info['total_points'] / info['count']) for player, info in player_points.items()}

    # Create a dictionary to save the data
    dictionary_pass_interceptions = {
        'average_pass_interceptions': average_points
    }







# API URL with query parameters for event odds
sport = 'americanfootball_nfl'  # Specify the sport
  # Your specified event ID

# Parameters
api_key = '56b1c1af71544f4f9a63799520c4d826'
regions = 'us'
markets = 'player_receptions'  # Market type as per your example
date_format = 'iso'  # Specify the date format you want
odds_format = 'american'

url = f'https://api.the-odds-api.com/v4/sports/{sport}/events/{event_id}/odds'

# Parameters from the URL
params = {
    'apiKey': api_key,
    'regions': regions,
    'markets': markets,
    'dateFormat': date_format,
    'oddsFormat': odds_format,
}

# Headers
headers = {
    'accept': 'application/json'
}

# Make the API request
response = requests.get(url, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON data
    data = response.json()
    
    # Initialize a dictionary to hold the total receptions and counts for each player
    player_receptions = {}

    # Iterate through each bookmaker
    for bookmaker in data['bookmakers']:
        for market in bookmaker['markets']:
            for outcome in market['outcomes']:
                description = outcome['description']
                point = outcome['point']

                # Add receptions to the corresponding player
                if description not in player_receptions:
                    player_receptions[description] = {'total_receptions': 0, 'count': 0}
                
                player_receptions[description]['total_receptions'] += point
                player_receptions[description]['count'] += 1

    # Calculate average receptions for each player
    average_receptions = {player: (info['total_receptions'] / info['count']) for player, info in player_receptions.items()}

    # Create a dictionary to save the data
    dictionary_receptions_over = {
        'average_receptions': average_receptions
    }







combined_data = {**dictionary_pass_yards, **dictionary_rush_yards, **dictionary_reception_yards, **dictionary_receptions, **dictionary_pass_tds, **dictionary_pass_interceptions, **dictionary_anytime_td, **dictionary_pass_tds_over, **dictionary_pass_interceptions, **dictionary_receptions_over}

    # Save the dictionary2 to a JSON file
with open('player_prop_api/combinedRR.json', 'w') as json_file:
    json.dump(combined_data, json_file, indent=4)

