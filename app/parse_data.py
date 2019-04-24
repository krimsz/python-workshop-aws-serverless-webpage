import pandas as pd

df = pd.DataFrame().from_csv("./title.basics.tsv",sep='\t')
only_movies = df[df.titleType=='movie']
only_movies.to_csv("./movies.tsv")
