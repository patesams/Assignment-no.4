#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup

# URL of the Wikipedia page
url = "https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the table containing the most viewed videos
table = soup.find("table", {"class": "wikitable"})

# Initialize lists to store data
rank_list = []
name_list = []
artist_list = []
upload_date_list = []
views_list = []

# Loop through each row in the table (excluding the header row)
for row in table.find_all("tr")[1:]:
    # Extract data from each column in the row
    columns = row.find_all("td")
    
    # Extracting data from columns
    rank = columns[0].text.strip()
    name = columns[1].text.strip()
    artist = columns[2].text.strip()
    upload_date = columns[3].text.strip()
    views = columns[4].text.strip()
    
    # Append data to respective lists
    rank_list.append(rank)
    name_list.append(name)
    artist_list.append(artist)
    upload_date_list.append(upload_date)
    views_list.append(views)

# Print the scraped data
for rank, name, artist, upload_date, views in zip(rank_list, name_list, artist_list, upload_date_list, views_list):
    print("Rank:", rank)
    print("Name:", name)
    print("Artist:", artist)
    print("Upload Date:", upload_date)
    print("Views:", views)
    print()


# In[2]:


import requests
from bs4 import BeautifulSoup

# URL of the BCCI website
url = "https://www.bcci.tv/"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the section containing the international fixtures
fixtures_section = soup.find("section", {"class": "js-list"})

# Initialize lists to store data
series_list = []
place_list = []
date_list = []
time_list = []

# Loop through each fixture in the section
for fixture in fixtures_section.find_all("a", {"class": "js-match"}):
    # Extract data from each fixture
    series = fixture.find("h3", {"class": "fixture__format"}).text.strip()
    place = fixture.find("p", {"class": "fixture__additional-info"}).text.strip()
    date = fixture.find("span", {"class": "fixture__date"}).text.strip()
    time = fixture.find("span", {"class": "fixture__time"}).text.strip()
    
    # Append data to respective lists
    series_list.append(series)
    place_list.append(place)
    date_list.append(date)
    time_list.append(time)

# Print the scraped data
for series, place, date, time in zip(series_list, place_list, date_list, time_list):
    print("Series:", series)
    print("Place:", place)
    print("Date:", date)
    print("Time:", time)
    print()


# In[3]:


import requests
from bs4 import BeautifulSoup

# URL of the website
url = "http://statisticstimes.com/"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the link to the page containing State-wise GDP
link = soup.find("a", text="GDP of Indian states")

# Extract the URL of the page containing State-wise GDP
state_gdp_url = link['href']

# Send a GET request to the State-wise GDP page
state_gdp_response = requests.get(state_gdp_url)

# Parse the HTML content of the State-wise GDP page
state_gdp_soup = BeautifulSoup(state_gdp_response.content, "html.parser")

# Find the table containing State-wise GDP data
table = state_gdp_soup.find("table", {"id": "table_id"})

# Initialize lists to store data
rank_list = []
state_list = []
gsdp_18_19_list = []
gsdp_19_20_list = []
share_18_19_list = []
gdp_billion_list = []

# Loop through each row in the table (excluding the header row)
for row in table.find_all("tr")[1:]:
    # Extract data from each column in the row
    columns = row.find_all("td")
    
    # Extracting data from columns
    rank = columns[0].text.strip()
    state = columns[1].text.strip()
    gsdp_18_19 = columns[2].text.strip()
    gsdp_19_20 = columns[3].text.strip()
    share_18_19 = columns[4].text.strip()
    gdp_billion = columns[5].text.strip()
    
    # Append data to respective lists
    rank_list.append(rank)
    state_list.append(state)
    gsdp_18_19_list.append(gsdp_18_19)
    gsdp_19_20_list.append(gsdp_19_20)
    share_18_19_list.append(share_18_19)
    gdp_billion_list.append(gdp_billion)

# Print the scraped data
for rank, state, gsdp_18_19, gsdp_19_20, share_18_19, gdp_billion in zip(rank_list, state_list, gsdp_18_19_list, gsdp_19_20_list, share_18_19_list, gdp_billion_list):
    print("Rank:", rank)
    print("State:", state)
    print("GSDP(18-19) - at current prices:", gsdp_18_19)
    print("GSDP(19-20) - at current prices:", gsdp_19_20)
    print("Share(18-19):", share_18_19)
    print("GDP($ billion):", gdp_billion)
    print()


# In[4]:


import requests
from bs4 import BeautifulSoup

# URL of the GitHub trending page
url = "https://github.com/trending"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the list of trending repositories
repositories = soup.find_all("article", {"class": "Box-row"})

# Initialize lists to store data
repository_titles = []
repository_descriptions = []
contributors_counts = []
languages_used = []

# Loop through each repository
for repo in repositories:
    # Extract data from each repository
    title = repo.find("h1", {"class": "h3 lh-condensed"}).text.strip()
    description = repo.find("p", {"class": "col-9 color-text-secondary my-1 pr-4"}).text.strip()
    contributors_count = repo.find("a", {"class": "Link--muted d-inline-block mr-3"}).text.strip().split()[0]
    language_used = repo.find("span", {"itemprop": "programmingLanguage"})
    if language_used:
        language_used = language_used.text.strip()
    else:
        language_used = "Not specified"
    
    # Append data to respective lists
    repository_titles.append(title)
    repository_descriptions.append(description)
    contributors_counts.append(contributors_count)
    languages_used.append(language_used)

# Print the scraped data
for title, description, contributors_count, language_used in zip(repository_titles, repository_descriptions, contributors_counts, languages_used):
    print("Repository Title:", title)
    print("Repository Description:", description)
    print("Contributors Count:", contributors_count)
    print("Language Used:", language_used)
    print()


# In[5]:


import requests
from bs4 import BeautifulSoup

# URL of the Billboard top 100 songs page
url = "https://www.billboard.com/charts/hot-100/"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the list of songs
songs = soup.find_all("li", {"class": "chart-list__element display--flex"})

# Initialize lists to store data
song_names = []
artist_names = []
last_week_ranks = []
peak_ranks = []
weeks_on_board = []

# Loop through each song
for song in songs:
    # Extract data from each song
    song_name = song.find("span", {"class": "chart-element__information__song text--truncate color--primary"}).text.strip()
    artist_name = song.find("span", {"class": "chart-element__information__artist text--truncate color--secondary"}).text.strip()
    last_week_rank = song.find("span", {"class": "chart-element__meta text--center color--secondary text--last"}).text.strip()
    peak_rank = song.find("span", {"class": "chart-element__meta text--center color--secondary text--peak"}).text.strip()
    weeks_on_board = song.find("span", {"class": "chart-element__meta text--center color--secondary text--week"}).text.strip()
    
    # Append data to respective lists
    song_names.append(song_name)
    artist_names.append(artist_name)
    last_week_ranks.append(last_week_rank)
    peak_ranks.append(peak_rank)
    weeks_on_board.append(weeks_on_board)

# Print the scraped data for the top 10 songs
for i in range(10):
    print("Song Name:", song_names[i])
    print("Artist Name:", artist_names[i])
    print("Last Week Rank:", last_week_ranks[i])
    print("Peak Rank:", peak_ranks[i])
    print("Weeks on Board:", weeks_on_board[i])
    print()


# In[6]:


import requests
from bs4 import BeautifulSoup

# URL of the page containing highest selling novels
url = "https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-grey-compare"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the table containing highest selling novels data
table = soup.find("table", {"class": "in-article sortable"})

# Initialize lists to store data
book_names = []
author_names = []
volumes_sold = []
publishers = []
genres = []

# Loop through each row in the table (excluding the header row)
for row in table.find_all("tr")[1:]:
    # Extract data from each column in the row
    columns = row.find_all("td")
    
    # Extracting data from columns
    book_name = columns[1].text.strip()
    author_name = columns[2].text.strip()
    volumes_sold = columns[3].text.strip()
    publisher = columns[4].text.strip()
    genre = columns[5].text.strip()
    
    # Append data to respective lists
    book_names.append(book_name)
    author_names.append(author_name)
    volumes_sold.append(volumes_sold)
    publishers.append(publisher)
    genres.append(genre)

# Print the scraped data
for book_name, author_name, volume_sold, publisher, genre in zip(book_names, author_names, volumes_sold, publishers, genres):
    print("Book Name:", book_name)
    print("Author Name:", author_name)
    print("Volumes Sold:", volumes_sold)
    print("Publisher:", publisher)
    print("Genre:", genre)
    print()


# In[7]:


import requests
from bs4 import BeautifulSoup

# URL of the IMDb page containing the most watched TV series
url = "https://www.imdb.com/list/ls095964455/"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the list of TV series
series_list = soup.find_all("div", {"class": "lister-item-content"})

# Initialize lists to store data
names = []
year_spans = []
genres = []
runtimes = []
ratings = []
votes = []

# Loop through each TV series
for series in series_list:
    # Extract data from each TV series
    name = series.find("h3", {"class": "lister-item-header"}).a.text.strip()
    year_span = series.find("span", {"class": "lister-item-year"}).text.strip()
    genre = series.find("span", {"class": "genre"}).text.strip()
    runtime = series.find("span", {"class": "runtime"}).text.strip()
    rating = series.find("div", {"class": "ipl-rating-star"}).span.text.strip()
    vote = series.find("span", {"name": "nv"}).text.strip().replace(",", "")
    
    # Append data to respective lists
    names.append(name)
    year_spans.append(year_span)
    genres.append(genre)
    runtimes.append(runtime)
    ratings.append(rating)
    votes.append(vote)

# Print the scraped data
for name, year_span, genre, runtime, rating, vote in zip(names, year_spans, genres, runtimes, ratings, votes):
    print("Name:", name)
    print("Year Span:", year_span)
    print("Genre:", genre)
    print("Run Time:", runtime)
    print("Rating:", rating)
    print("Votes:", vote)
    print()


# In[8]:


import requests
from bs4 import BeautifulSoup

# URL of the UCI Machine Learning Repository
url = "https://archive.ics.uci.edu/"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the link to the datasets page
datasets_link = soup.find("a", text="View ALL Data Sets")

# Extract the URL of the datasets page
datasets_url = datasets_link['href']

# Send a GET request to the datasets page
datasets_response = requests.get(datasets_url)

# Parse the HTML content of the datasets page
datasets_soup = BeautifulSoup(datasets_response.content, "html.parser")

# Find the table containing dataset details
table = datasets_soup.find("table", {"border": "1"})

# Initialize lists to store data
dataset_names = []
data_types = []
tasks = []
attribute_types = []
no_of_instances = []
no_of_attributes = []
years = []

# Loop through each row in the table (excluding the header row)
for row in table.find_all("tr")[1:]:
    # Extract data from each column in the row
    columns = row.find_all("td")
    
    # Extracting data from columns
    dataset_name = columns[0].text.strip()
    data_type = columns[1].text.strip()
    task = columns[2].text.strip()
    attribute_type = columns[3].text.strip()
    no_of_instances = columns[4].text.strip()
    no_of_attributes = columns[5].text.strip()
    year = columns[6].text.strip()
    
    # Append data to respective lists
    dataset_names.append(dataset_name)
    data_types.append(data_type)
    tasks.append(task)
    attribute_types.append(attribute_type)
    no_of_instances.append(no_of_instances)
    no_of_attributes.append(no_of_attributes)
    years.append(year)

# Print the scraped data
for dataset_name, data_type, task, attribute_type, no_instances, no_attributes, year in zip(dataset_names, data_types, tasks, attribute_types, no_of_instances, no_of_attributes, years):
    print("Dataset Name:", dataset_name)
    print("Data Type:", data_type)
    print("Task:", task)
    print("Attribute Type:", attribute_type)
    print("No of Instances:", no_instances)
    print("No of Attributes:", no_attributes)
    print("Year:", year)
    print()


# In[ ]:




