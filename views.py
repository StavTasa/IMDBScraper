import tkinter
from tkinter import ttk, Tk, messagebox, Text
import random
from findMovies import FindMovies
from movie import Movie

## create a main window for user preferences
window = Tk()
frame = ttk.Frame(window)
frame.pack()
window.title("Movie Finder")

user_preferences_frame  =tkinter.LabelFrame(frame, text="Your Preferences")
user_preferences_frame.grid(row= 0, column=0, padx=20, pady=10)

release_year_label = tkinter.Label(user_preferences_frame, text="Release Year")
release_year_label.grid(row=0, column=0)

release_year_entry = tkinter.Entry(user_preferences_frame)
release_year_entry.grid(row=1, column=0)

from_rating_label = tkinter.Label(user_preferences_frame, text="From Rating (not include)")
from_rating_spinbox = ttk.Spinbox(user_preferences_frame, from_=0, to=9)

from_rating_label.grid(row=0, column=2)
from_rating_spinbox.grid(row=1, column=2)

to_rating_label = tkinter.Label(user_preferences_frame, text="To Rating")
to_rating_spinbox = ttk.Spinbox(user_preferences_frame, from_=0, to=10)

to_rating_label.grid(row=0, column=4)
to_rating_spinbox.grid(row=1, column=4)

for widget in user_preferences_frame.winfo_children():
    widget.grid_configure(padx=10, pady= 5)

def choose_random_movies(movies, no_1_movie):
    res = []
    num_of_movies = min(3, len(movies))
    for i in range(1, num_of_movies):
        movie = random.choice(movies)
        if movie == no_1_movie:
            i-=1
        else:
            res.append(movie)
    return res

# show to chosen movies and #1 movie on a different screen
def show_movies(movies, no_1_movie):
    movies_window = tkinter.Toplevel()
    movies_window.title("Recommended Movies")

    no_1_movie_frame = tkinter.LabelFrame(movies_window, text="Your #1 Recommendation")
    no_1_movie_frame.grid(row= 0, column=0, padx=10, pady=20)

    no_1_movie_data = Text(no_1_movie_frame, height=12, width=40)
    no_1_movie_data.pack(expand=True)
    title = no_1_movie.title
    release_year = no_1_movie.release_year
    rate = no_1_movie.rate
    text = "Movie Name: " + title + '\n' +  "Release Year: " + release_year + '\n' + "Rate: " + rate + "\n"
    no_1_movie_data.insert('end', text)
    no_1_movie_data.config(state='disabled')


    recommended_movies_frame = tkinter.LabelFrame(movies_window, text="Recommended Movies")
    recommended_movies_frame.grid(row= 0, column=3, padx=10, pady=20)
    i = 0
    for movie in movies:
        movie_data = Text(recommended_movies_frame, height=12, width=40)
        movie_data.pack(expand=True)
        title = movie.title
        release_year = movie.release_year
        rate = movie.rate
        text = "Movie Name: " + title + '\n' +  "Release Year: " + release_year + '\n' + "Rate: " + rate + "\n"
        movie_data.insert('end', text)
        movie_data.config(state='disabled')

# get the data from the form and find relevan movies
def handle_user_data():
    release_year = release_year_entry.get()
    from_rating = from_rating_spinbox.get()
    to_rating = to_rating_spinbox.get()

    if release_year == "" and from_rating == "" and to_rating == "":
        messagebox.showerror("Error", "Please fill at least 1 of the fields")

    res = FindMovies.findMovies(release_year, from_rating, to_rating)
    movies_by_preference = res[0]
    no_1_movie = res[1]
    if movies_by_preference is not None:
        movies_to_show = choose_random_movies(movies_by_preference, no_1_movie)
        if no_1_movie == []:
            no_1_movie.append(Movie("no movie was found","0", "0"))
        show_movies(movies_to_show, no_1_movie[0])



button = tkinter.Button(frame, text="Find Me Movies!", command=handle_user_data)
button.grid(row=2, column=0, sticky='news', padx = 20, pady = 10)
window.mainloop()