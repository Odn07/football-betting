import requests




# Constants and API configuration
api_key = "YOUR_API_KEY"
region = "us"
mkt = "h2h"
sports = ["americanfootball_nfl", "americanfootball_ncaaf", "basketball_nba", "baseball_mlb", "mma_mixed_martial_arts", "americanfootball_nfl_super_bowl_winner"]



# Step 2
def compute_surebet(odds_a, odds_b):
    implied_prob_a = 1 / odds_a
    implied_prob_b = 1 / odds_b
    total_implied_prob = implied_prob_a + implied_prob_b

    if total_implied_prob < 1:
        profit_percentage = (1 - total_implied_prob) * 100
        investment = 1000

        bet_a = (investment * implied_prob_a) / odds_a
        bet_b = (investment * implied_prob_b) / odds_b

        return profit_percentage, bet_a, bet_b
    else:
        return None, None, None


# Step 3
def fetch_surebets(sport):
    # API request
    url = f"https://api.the-odds-api.com/v3/odds/?apiKey={api_key}&sport={sport}&region={region}&mkt={mkt}"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error: Request for {sport} returned status code {response.status_code}.")
        return

    data = response.json()

    if 'data' not in data:
        print(f"No data found for {sport}.")
        return

    # Calculate surebets
    surebets = []
    all_games = []
    # Step 4
    for event in data["data"]:
        team_a, team_b = event["teams"]
        odds_list = []

        for site in event["sites"]:
            odds = site["odds"]["h2h"]
            odds_list.append((site["site_nice"], odds))

        for i in range(len(odds_list)):
            for j in range(i + 1, len(odds_list)):
                site_a, odds_a = odds_list[i]
                site_b, odds_b = odds_list[j]

                profit, bet_a, bet_b = compute_surebet(odds_a[0], odds_b[0])  
                # Step 5 
                if profit:
                    surebets.append({
                        "Team A": team_a,
                        "Team B": team_b,
                        "Site A": site_a,
                        "Site B": site_b,
                        "Odds A": odds_a[0],
                        "Odds B": odds_b[0],
                        "Profit %": round(profit, 2),
                        "Bet A": round(bet_a, 2),
                        "Bet B": round(bet_b, 2),
                        "Timestamp": event.get("commence_time", None)
                    })

                all_games.append({
                    "Team A": team_a,
                    "Team B": team_b,
                    "Site": site_a,
                    "Odds A": odds_a[0],
                    "Odds B": odds_b[0],
                    "Timestamp": event.get("commence_time", None)
                    })
    
    #Display all games and surebet
    # ...
    # Display all games
   
