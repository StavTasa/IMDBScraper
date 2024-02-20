from scrapeMovies import movies

class FindMovies():
    # for every movie that was scraped check if it fits to the user preferences
    def findMovies(release_year, from_rating, to_rating):
        relevant_movies = []
        no_1_movie = []
        max_rating = 0
        for movie in movies:
            if movie.release_year == release_year or movie.release_year == "no year":
                if movie.rate == "no rate":
                    if from_rating == "" and to_rating == "":
                        relevant_movies.append(movie)
    
                else:
                    if from_rating == "" and to_rating == "":
                        relevant_movies.append(movie)

                    elif from_rating == "":
                        if float(movie.rate) <= float(to_rating):
                            relevant_movies.append(movie)

                    elif to_rating == "":
                        if float(movie.rate) > float(from_rating):
                            relevant_movies.append(movie)

                    elif float(movie.rate) > float(from_rating) and float(movie.rate) <= float(to_rating):
                        relevant_movies.append(movie)

                    if max_rating < float(movie.rate):
                        max_rating = float(movie.rate)
                        no_1_movie = []
                        no_1_movie.append(movie)

        return(relevant_movies, no_1_movie)


        
