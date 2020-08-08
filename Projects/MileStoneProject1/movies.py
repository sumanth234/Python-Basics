# add a movie -> key a
#List all movies - > key l
#Find the movie by Title -> key f
#Enter q to quit -> key q

movies = []

add_movies = lambda title,director,year : {"MovieTitle":title,"Director":director,"YearOfRelease":year}

def list_movies() :
    print(movies)

def find_movies(movie_title) :
    if len(movies) > 0:
        for movie in movies:
            if movie_title == movie["MovieTitle"]:
                return movie
        else:
            return "No Movies Found with that title"
    else:
        print("Please add movies to search")
#or, but in the below line, else condition for for loop need to be handled
find_movies = lambda movie_title : [movie if movie_title == movie["MovieTitle"] else "Need to be handled as else condition for for loop and not if" for movie in movies ] if len(movies) > 0 else ["Please add movies to search"]

user_options = {
    "l" : list_movies

}
def start_application() :
    key = input("Please Enter key a to add movies,l to list all movies,f to find movies by movie title and q to quit the application")
    while key != "q" :
        if key in user_options:
            user_options[key]() # FirstClass Functions
            #list_movies()
        elif key == "a":
            movies.append(add_movies(input("Please Enter the title of movie"),input("Please Enter the name of Director"),input("Please Enter the year of release")))
        elif key == "f":
            # if len(movies) == 0:
            #     print("Please add movies to search")
            # else:
            print(find_movies(input("Please Enter the title of movie")))
        else:
            print("Please enter the valid key" )
        key = input("Please Enter key a to add movies,l to list all movies,f to find movies by movie title and q to quit the application")


start_application();