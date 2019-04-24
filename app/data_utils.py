import csv
import os
from random import randint


def read_from_csv(path):
    with open(path) as csvfile:
        tsvreader =  csv.DictReader(csvfile)
        return list(tsvreader)

WHOLE_DB = read_from_csv(os.path.dirname(__file__) + "/resources/movies.tsv")

def select_n_rows(n_rows):
    items = []
    for item in range(n_rows):
        index = randint(0,len(WHOLE_DB)-1)
        items.append(WHOLE_DB[index])
    return _clean_is_adult(_clean_empty_values(items))

def _clean_is_adult(movies):
    for movie in movies:
        movie['isAdult'] = ((movie['isAdult'] or 0) == 1)
    return movies

def _clean_empty_values(movies):
    for movie in movies:
        for k,v in movie.items():
            if v == '\\N':
                movie[k]='N/A'
    return movies