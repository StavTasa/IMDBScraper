import requests
from bs4 import BeautifulSoup
from movie import Movie
from lxml import etree as et

MOVIE_TITLE_CLASS = "ipc-title ipc-title--base ipc-title--title ipc-title-link-no-icon ipc-title--on-textPrimary sc-be6f1408-9 srahg cli-title"
MOVIE_RELEASE_YEAR_CLASS = "sc-be6f1408-8 fcCUPU cli-title-metadata-item"
MOVIE_RATE_CLASS = "ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating"
URL = "https://www.imdb.com/chart/moviemeter/"

movies = []
# scrape movies from IMDB by title, release year and rating
class ScrapeMovies():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"} 
    response = requests.get(URL, headers=headers)


    soup = BeautifulSoup(response.content, 'html.parser')
    movie_data = soup.find_all("li", class_ = 'ipc-metadata-list-summary-item')
    dom = et.HTML(str(soup))

    i = 0
    for movie in movie_data:
        title = movie.find("div", class_ = MOVIE_TITLE_CLASS).h3.text

        release_year = movie.find("span", class_ = MOVIE_RELEASE_YEAR_CLASS)
        if release_year is None:
            release_year = "no year"
        else:
            release_year = release_year.text

        rate = movie.find("span", class_ = MOVIE_RATE_CLASS)
        if rate is None:
            rate = "no rate"
        else:
            rate = rate.text[0:3]
        
        poster = movie.find("div", class_ = "ipc-media ipc-media--poster-27x40 ipc-image-media-ratio--poster-27x40 ipc-media--base ipc-media--poster-m ipc-poster__poster-image ipc-media__img").find('img').get('src')
        
        movies.append(Movie(title, release_year, rate))

        


