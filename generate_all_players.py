# Imports Selenium, BeautifulSoup and Pandas
# Selenium used for Controlling Web Browsers
# BeatuifulSoup used for scraping websites for data
# Pandas used for data analysis and data manipulation (making tables)
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import string

def generate_all_players():
    """
    Scrapes basketball-reference.com for all recorded NBA & ABA players
    """
    players = [] #List to store names of the players
    starts = [] #List to store starting date for the players
    ends = [] #List to store retirement date
    poss = [] #List to store basic positions (G for guard, F for forward, C for Center)

    alphabet = list(string.ascii_lowercase)

    # Iterate through all letters of alphabet
    for letter in alphabet:
        
        if letter == "x":   # Skips X because no players with X as last name.
            continue
            
        # Scrape website for list of players at every letter
        driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
        driver.get(f'https://www.basketball-reference.com/players/{letter}/')

        content = driver.page_source
        soup = BeautifulSoup(content)

        # Iterate and find any data in a table
        for a in soup.findAll('tr'):
            
            # Scrape data, and add to list
            players.append(a.find(attrs={'data-stat':'player'}).get_text())         # Scrapes player name
            starts.append(a.find(attrs={'data-stat':'year_min'}).get_text())        # Scrapes date of first NBA game
            ends.append(a.find(attrs={'data-stat':'year_max'}).get_text())          # Scrapes data of last NBA game
            poss.append(a.find(attrs={'data-stat':'pos'}).get_text())               # Scrapes player position

    # Add newfound data to CSV
    df = pd.DataFrame({'Player Name':players,'Start year':starts,'End year':ends, 'Position':poss}) 
    df.to_csv('players.csv', index=False, encoding='utf-8')

if __name__ == "__main__":
    generate_all_players()
