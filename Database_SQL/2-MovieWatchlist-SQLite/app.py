import datetime
import database

menu = """Please select one of the following options:
1) Add new movie
2) View upcoming movies
3) View all movies
4) Watch a movie
5) View watched movies
6) Add new user
7) Search a movie
8) Exit.

Your selection: """
welcome = "Welcome to the watchlist app!"


print(welcome)
database.create_tables()


def prompt_add_movie():
    title = input("Movie Title: ")
    releaseDate = input("Release Date (dd-mm-yyyy): ")
    parsedDate = datetime.datetime.strptime(releaseDate, "%d-%m-%Y")
    timestamp = parsedDate.timestamp()

    database.add_movies(title, timestamp)


def print_movie_list(heading, movies):
    print("------ {} Movies ------".format(heading))
    for _id, title, realise_Date in movies:
        movieDate = datetime.datetime.fromtimestamp(realise_Date)
        humanDate = movieDate.strftime("%b %d %Y")
        print("ID: {}, Movie: {}, Releas Date: {}".format(_id, title, humanDate))
    print("-----\n")


def promt_watched_movies():
    username = input("Insert the username: ")
    movie_id = input("Movie ID: ")
    database.watch_movie(username, movie_id)


def promt_add_user():
    username = input("Insert the username: ")
    database.add_user(username)


def promt_show_whatched_movies():
    username = input("Insert user name: ")
    movies = database.get_watched_movies(username)
    if movies:
        print_movie_list("Watched: ", movies)
    else:
        print("User haven't watched any movie yet!")


def prompt_search_movies():
    searchTerm = input("Movie to be searched: ")
    movies = database.search_movies(searchTerm)
    if movies:
        print_movie_list("Movies found: ", movies)
    else:
        print("No movies found!")


while (user_input := input(menu)) != "8":
    if user_input == "1":
        prompt_add_movie()
    elif user_input == "2":
        movies = database.get_movies(True)
        print_movie_list("Upcoming", movies)
    elif user_input == "3":
        movies = database.get_movies()
        print_movie_list("All", movies)
    elif user_input == "4":
        promt_watched_movies()
    elif user_input == "5":
        promt_show_whatched_movies()
    elif user_input == "6":
        promt_add_user()
    elif user_input == "7":
        prompt_search_movies()

    else:
        print("Invalid input, please try again!")
