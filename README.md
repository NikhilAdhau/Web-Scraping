# Web-Scraping
This is a Web-Scraping project using Scrapy and Sqlite3.

It scrapes the the list of popular movies and series based on the  variety of genres.

The project extracts Title, Year, Rating, Duration.
It also extracts the link a to trailer and a link to a more info page.

The extracted data is then stored in a sqlite database, where you can then sort movies or series based on rating or year.

# Requirements
You need to install scrapy first. 
Use this command - "sudo apt install scrapy".

Download above files and follow the steps:

# You can run a spider using the scrapy crawl command, such as:

$ scrapy crawl list

If you want to save the scraped data to a file, you can pass the -o option:

$ scrapy crawl list -o list.csv
