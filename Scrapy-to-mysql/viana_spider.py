
# This is only the spider file for Scrapy, you need a scrapy project to run it

import time
import scrapy
import mysql.connector


#Connect to mysql

db = mysql.connector.connect(
    host="your host",
    user="your user",
    password="your password",
    database="your database")

myquery = db.cursor(buffered=True)

# This project is scraping news from my hometown news websites

class VianaSpider(scrapy.Spider):

    name = "viana"

    # Pages to scrap

    def start_requests(self):
        url_geice = "https://radiogeice.com/categoria/informacao-regional/"
        yield scrapy.Request(url=url_geice, callback=self.parse_geice)


    

    def parse_geice(self, response):

        # Information you want to scrap

        titles = response.xpath('//*[@class="title-box-noticia-minimal"]//a/@title').extract()
        links = response.xpath('//*[@class="title-box-noticia-minimal"]//a/@href').extract()

        # Fetch last database entry

        myquery.execute("select *from news ORDER BY FIELD(source, 'radiogeice') DESC, id DESC ")
        result = myquery.fetchone()
        if not result:
            last_news= "empty"
        else:
            last_news = result[3]

        z = 0
        lenght = len(titles)

        # Compare last database entry with your scrapped data

        while z < lenght and titles[z] != last_news:
            z += 1

        # Remove duplicates

        del titles[z:]
        del links[z:]

        sc = "radiogeice"
        ts = time.strftime('%Y-%m-%d %H:%M:%S')

        # Save new data to mysql and to file

        with open('news.txt', 'w') as f:
            for u, l in zip(reversed(titles), reversed(links)):
                f.write(u + "\n" + l + "\n")

                mycursor = db.cursor()
                sql = "INSERT INTO news (date, source, title, href) VALUES (%s, %s, %s, %s)"
                val = (ts, sc ,u , l)
                mycursor.execute(sql, val)
                db.commit()


