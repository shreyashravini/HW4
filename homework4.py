# Your name here
# Your CNET ID here (this is the part of your uchicago email id before the @)
# Your github user id here

"""
INSTRUCTIONS

Available: May 9th at 11:59PM

Due: May 16th at 11:59PM

Gentle reminder that, among other things, you

(a) Must answer your questions in the homework4.py file
(b) Must commit homework4.py and movies.csv to your clone of the 
GitHub homework repo
(c) Must link your GitHub repo to GradeScope
(d) Must NOT repeatedly use a hard-coded path for the working directory

Failure to do any of these will result in the loss of points
"""

"""
HOMEWORK 4

You and your roommate have decieded to delve into the history of US cinema,
choosing a random blockbuster every Friday to watch. The problem, of course, is
that (a) you don't have a list of US blockbusters and (b) your roommate is 
indecisive and choosing a "random" movie to watch is going to be a nightmare!

Wikipedia to the rescue! It has a set of pages detailing all American films 
released in a particular year. For example:
    
    https://en.wikipedia.org/wiki/List_of_American_films_of_1982
    
You can look at different pages by changing the year at the end of the URL
e.g. replacing 1982 with 1997

At the top of these pages is a table containing the top 10 highest-grossing films 
for that year. The structure of this page is pretty stable - every such page from
1970 onwards has this table.

YOUR TASK

In this exercise, you will create a python program that will scrape 
each such page from Wikipedia for the period 1970 to 2023. Using this 
information it will create a dataset of all the top-grossing movies, then open
the dataset and pick a movie at random.

MANDATORY

Do not use the wikipeia package or API

Ensure that you insert a pause of 3 seconds between requests for 
data to wikipedia. 

By "create a dataset", we mean you must save the data to a CSV file named
"movies.csv". Then, open the CSV file and pick a movie at random. Print 
the name of the chosen movie with the year in brackets e.g. John Wick (2004)

The CSV file must include the following columns: Year, Rank, Title, 
Distributor, Domestic gross

SUGGESTED WORKFLOW

This is a somewhat complex project, so I recommend executing it in the following 
steps. Obviously, you don't have to execute in these steps - there is no way for
us to check!
    
    1. Write code that takes the URL for a particular year, fetches the html,
    and converts the relevant table into a list object.
    
    2. Create a function that takes a year as an input, generates the appropriate
    url, and uses the code from step (1) to fetch html and convert the relevant
    table.
    
    3. Write a loop that goes from 1970 to 2023 and uses the function from (2)
    to add the data to a final_table list object. Use the sleep() method from
    the time package to ensure that you take a 3 second break between requests
    
    4. Convert final_table into a dataframe df; save it as a CSV
    
    5. Open the CSV and pick a random movies
    
HINTS

Hints for step 1:
    - Start with 1970, and make sure your code is working before you proceed
    - Be careful - there are many tables on this page, and the one
    you are looking for isn't the first one!
    - Don't forget to deal with the row that says "Rank", "Title" etc.
    - The table merges cells when the distributor is the same. For example, in
    1970, both MASH and Patton were distributed by 20th Century Fox, so the two
    cells are merged. For example, when converting the table to a list, the 
    entry for 'Patton' will not include the distributor, resulting in a row 
    shorter than expected.. Think of a way to deal with this!
    - Don't forget to add a Year "column"

Hints for step 2: 
    - You can copy paste the code from step 1 into this function
    and make a few changes to complete this step
    - Remember that the URL must be a string object even if the incoming year
    variable is an int
    
Hints for step 3:
    - Use the sleep() method from the time package to add a pause
    - For your peace of mind, print a note at the start of each iteration so that
    you know that it is working
    - Don't try to iterate over everything at once! Try 1970, then 1970 to 1971
    and so on till you are comfortable running it for 1970 to 2023
    
Hints for step 4:     
    You will know  your program works as intended if print(df.head()) generates
the following output:
    
      Rank           Title       Distributor Domestic gross  Year
    0    1      Love Story         Paramount   $106,397,186  1970
    1    2         Airport         Universal   $100,489,150  1970
    2    3         M*A*S*H  20th Century Fox    $81,600,000  1970
    3    4          Patton  20th Century Fox    $62,500,000  1970
    4    5  The Aristocats       Walt Disney    $41,162,795  1970

and print(df.tail()) generates the following output:
    
print(df.tail())
     Rank                              Title  ... Domestic gross  Year
525     6                 The Little Mermaid  ...   $298,172,056  2023
526     7                              Wonka  ...   $218,377,073  2023
527     8  Ant-Man and the Wasp: Quantumania  ...   $214,506,909  2023
528     9               John Wick: Chapter 4  ...   $187,131,806  2023
529    10                   Sound of Freedom  ...   $184,174,617  2023

Hints for step 5:
    - Use the random package
    - What kind of indexes does your data have?
"""


""" Step 1 
"""

import requests
from bs4 import BeautifulSoup

def get_top_grossing_movies(year):
    url = f"https://en.wikipedia.org/wiki/List_of_American_films_of_{year}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        tables = soup.find_all('table', class_='wikitable')
        if tables:
            for table in tables:
                header_row = table.find('tr')
                header_columns = header_row.find_all('th')
                if len(header_columns) > 1 and header_columns[1].text.strip() == "Title":
                    rows = table.find_all('tr')
                    movie_data = []
                    for row in rows[1:]:
                        columns = row.find_all(['td', 'th'])
                        if len(columns) >= 4:
                            movie_rank = columns[0].text.strip()
                            movie_title = columns[1].text.strip()
                            movie_distributor = columns[2].text.strip()
                            movie_domestic_gross = columns[3].text.strip()
                            movie_data.append([year, movie_rank, movie_title, movie_distributor, movie_domestic_gross])
                    return movie_data

# Test the function
movies_1970 = get_top_grossing_movies(1970)
for movie in movies_1970:
    print(movie)

""" Step 2
"""



def get_top_grossing_movies(year):
    url = f"https://en.wikipedia.org/wiki/List_of_American_films_of_{year}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        tables = soup.find_all('table', class_='wikitable')
        if tables:
            for table in tables:
                header_row = table.find('tr')
                header_columns = header_row.find_all('th')
                if len(header_columns) > 1 and header_columns[1].text.strip() == "Title":
                    rows = table.find_all('tr')
                    movie_data = []
                    for row in rows[1:]:
                        columns = row.find_all(['td', 'th'])
                        if len(columns) >= 4:
                            movie_rank = columns[0].text.strip()
                            movie_title = columns[1].text.strip()
                            movie_distributor = columns[2].text.strip()
                            movie_domestic_gross = columns[3].text.strip()
                            movie_data.append([year, movie_rank, movie_title, movie_distributor, movie_domestic_gross])
                    return movie_data

def fetch_top_grossing_movies_for_year(year):
    return get_top_grossing_movies(year)

# Test the function
movies_1970 = fetch_top_grossing_movies_for_year(1970)
for movie in movies_1970:
    print(movie)


""" Step 3
"""

from time import sleep

def get_top_grossing_movies(year):
    url = f"https://en.wikipedia.org/wiki/List_of_American_films_of_{year}"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Fetching data for {year}...")
        soup = BeautifulSoup(response.content, 'html.parser')
        tables = soup.find_all('table', class_='wikitable')
        if tables:
            for table in tables:
                header_row = table.find('tr')
                header_columns = header_row.find_all('th')
                if len(header_columns) > 1 and header_columns[1].text.strip() == "Title":
                    rows = table.find_all('tr')
                    movie_data = []
                    for row in rows[1:]:
                        columns = row.find_all(['td', 'th'])
                        if len(columns) >= 4:
                            movie_rank = columns[0].text.strip()
                            movie_title = columns[1].text.strip()
                            movie_distributor = columns[2].text.strip()
                            movie_domestic_gross = columns[3].text.strip()
                            movie_data.append([year, movie_rank, movie_title, movie_distributor, movie_domestic_gross])
                    return movie_data

def fetch_top_grossing_movies_for_period(start_year, end_year):
    all_movies = []
    for year in range(start_year, end_year + 1):
        year_data = get_top_grossing_movies(year)
        if year_data:
            all_movies.extend(year_data)
        sleep(3)  # Adding a 3-second pause between requests
    return all_movies

# Test the function
movies_1970_to_1971 = fetch_top_grossing_movies_for_period(1970, 1971)
for movie in movies_1970_to_1971:
    print(movie)


""" Step 4
"""

import pandas as pd


def get_top_grossing_movies(year):
    url = f"https://en.wikipedia.org/wiki/List_of_American_films_of_{year}"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Fetching data for {year}...")
        soup = BeautifulSoup(response.content, 'html.parser')
        tables = soup.find_all('table', class_='wikitable')
        if tables:
            for table in tables:
                header_row = table.find('tr')
                header_columns = header_row.find_all('th')
                if len(header_columns) > 1 and header_columns[1].text.strip() == "Title":
                    rows = table.find_all('tr')
                    movie_data = []
                    for row in rows[1:]:
                        columns = row.find_all(['td', 'th'])
                        if len(columns) >= 4:
                            movie_rank = columns[0].text.strip()
                            movie_title = columns[1].text.strip()
                            movie_distributor = columns[2].text.strip()
                            movie_domestic_gross = columns[3].text.strip()
                            movie_data.append([year, movie_rank, movie_title, movie_distributor, movie_domestic_gross])
                    return movie_data

def fetch_top_grossing_movies_for_period(start_year, end_year):
    all_movies = []
    for year in range(start_year, end_year + 1):
        year_data = get_top_grossing_movies(year)
        if year_data:
            all_movies.extend(year_data)
        sleep(3)  # Adding a 3-second pause between requests
    return all_movies

def save_movies_to_csv(movies, filename):
    df = pd.DataFrame(movies, columns=["Year", "Rank", "Title", "Distributor", "Domestic gross"])
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

# Fetch top-grossing movies data for the period 1970 to 2023
movies_data = fetch_top_grossing_movies_for_period(1970, 2023)

# Save the data to a CSV file
save_movies_to_csv(movies_data, "movies.csv")


""" Step 5
"""

import random

def get_random_movie(csv_file):
    df = pd.read_csv(csv_file)
    random_movie_index = random.randint(0, len(df) - 1)
    random_movie = df.iloc[random_movie_index]
    return random_movie

# Open the CSV file and pick a random movie
random_movie = get_random_movie("movies.csv")
print(random_movie["Title"], f"({random_movie['Year']})")








