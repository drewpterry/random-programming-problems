import unittest
from bisect import bisect

#0(n2)
def matching_movies(flight_length, movie_lengths):
    movies_exist = False
    for index, each in enumerate(movie_lengths):
        remaining_time = flight_length - each
        try:
            matching_movie_index = movie_lengths.index(remaining_time)
            print matching_movie_index

            if matching_movie_index != index:
                return True
        except:
            print 'nope'
    return movies_exist

#sort movie_lengths first to decrease runtime to 0(nlogn)
def matching_movies(flight_length, movie_lengths):
    #this makes a copy of list
    movie_lengths_sorted = sorted(movie_lengths) 
    movies_exist = False
    for index, each in enumerate(movie_lengths_sorted):
        remaining_time = flight_length - each
        #performs search on ordered list
        matching_movie_index = bisect(movie_lengths, remaining_time) 
        if matching_movie_index != index and matching_movie_index < len(movie_lengths):
            return True
    return False 

#search throgh set which is a hash so becomes 0(n)
def matching_movies(flight_length, movie_lengths):
    seen_movies = set()
    for each in movie_lengths:
        remaining_time = flight_length - each
        if remaining_time in seen_movies:
            return True
        else:
            seen_movies.add(each)
    return False 

class Test(unittest.TestCase):
    data = [
        3,
        2.3,
        2.5,
        3.1,
        1.3,
        1,
        2.5,
        1
    ]
    def test_cp(self):
        self.assertTrue(matching_movies(3.8,self.data))
        #don't watch same movie twice
        self.assertFalse(matching_movies(6,self.data))

if __name__ == "__main__":
    unittest.main()
