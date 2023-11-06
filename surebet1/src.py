import mod

sports = "soccer_epl"
investment = int(input("ENTER INVESTMENT: "))

print("Download in progress... please wait!")
mod.fetch_surebets(sports, investment)
mod.mybet()
mod.csv_to_xlsx()
print("Download is completed!")



"""
Reminder:

1. This program is designed to run on h2h market, but it is only using two odds, odds_a and odd_b. Therefore it is not yet accurate. I need to include a third odd or look for a market that uses two odds.

2. Most of the bookmarkers are not in Nigerian market. I need to find an api that will allow me to mine Nigerian specific data.

3. Add a third bookmarker and a third odd incase the game ends in a draw.
"""