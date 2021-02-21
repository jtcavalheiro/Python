
import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import mysql.connector
import ftplib

# Connect to mysql

dbConnection = mysql.connector.connect(
    host="your host",
    user="your user",
    password="your password",
    database="your db")


# Import data from mysql

frame = pd.read_sql("select * from news", dbConnection)
dbConnection.close()



text = " ".join(review for review in frame.title)
# Create stopword list:
stopwords = set(STOPWORDS)
stopwords.update(["de", "da", "na", "em", "que", "por"])
# Generate a word cloud image
wordcloud = WordCloud(stopwords=stopwords, background_color="white", width=800, height= 200, collocations=False).generate(text)
wordcloud.to_file('wordcloud.png')

filename = 'wordcloud.png'
session = ftplib.FTP('ftp host','ftp user','ftp pass')
session.cwd('htdocs/imgs')
with open(filename, "rb") as file:
    # use FTP's STOR command to upload the file
    session.storbinary('STOR wordcloud.png', file)
session.quit()