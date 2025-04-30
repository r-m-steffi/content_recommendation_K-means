class Proj_Param:
    data_folder = './data'
    data_collection_dict = {
            'movie_lens_1m'  : 'https://files.grouplens.org/datasets/movielens/ml-1m.zip'
    }
    data_files_dict = {
            'ratings'        : {'path':'/ml-1m/ratings.dat',
                                'cols': ['userId','movieId','rating','timestamp'],
                               },
            'movies'         : {'path':'/ml-1m/movies.dat',
                                'cols': ['movieId','title','genres'],
                               },
            'users'           : {'path':'/ml-1m/users.dat',
                                'cols': ['userId','gender','age','occupation','zip-code'],
                               },
            
    }

    def __init__(self):
        pass
