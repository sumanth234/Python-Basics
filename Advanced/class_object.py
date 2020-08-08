#Normal class
class Movie:
    def __init__(self, new_name, new_director): # this is the initial method of class.It accepts 1st parameter as self always and rest depends on us
        self.name = new_name
        self.director = new_director

    def print_info(self): # u need to pass self or else it will be inaccesible
        print(f"<<{self.name}>> by {self.director}")

movie = Movie("I","Shankar")
movie.print_info()

print("\n--------------------------------------------\n")

#Class with magic functions as len and index

class Movie:
    def __init__(self):
        self.movies = []

    def __len__(self): # Magic functions -> we can do like this to find the length by accessing len(Movie() object)
        return len(self.movies)

    def  __getitem__(self, i): # to access by index
        return self.movies[i]

    def __repr__(self): # both str and repr behaves exacly the same way
        return f"Movie Object has {len(self)} movies"
    #or
    #def __str__(self):
        #return f"Movie has {len(self)} movies"

    def add_movie(self,movie):
        self.movies.append(movie)

movie = Movie()
movie.add_movie({"name":"I","year":2015})

print(len(movie))
#print(movie[0])

for mov in movie:
    print(mov)

print(movie)
