# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ListSpider(CrawlSpider):
	name = 'list'
	allowed_domains = ['www.imdb.com']

	genres = {'1' : 'Action',  '2' : 'Adventure', '3' : 'Animation', '4' : 'Biography', '5' : 'Comedy', '6' : 'Crime',	
	'7' : 'Documentary', '8' : 'Drama', '9' : 'Family', '10' : 'Fantasy', '11' : 'Film Noir', '12' : 'History',	'13' : 'Horror',
	'14' : 'Music','15' : 'Musical','16' : 'Mystery','17' : 'Romance','18' : 'Sci-Fi','19' : 'Short Film','20' : 'Sport',
	'21' : 'Superhero', '22' : 'Thriller', '23' : 'War','24' : 'Western'}
	
	#Movies or Series
	print ("\nWhat are you looking for?")
	print("1.Movies\n2.Series\n")
	opt = input ("Enter your choice : ")
	print ("\n")
	#Selcting the genre for movies or series
	print ("Choose the genre!")
	for genre in genres:
		print (genre + ' : ' + genres[genre])
	genre = input ("\nEnter the genre from above : ")


	title_type = ''
	movies = 0
	series = 0

	if opt == '1':
		title_type = 'feature'
		movies = 1
		series = 0

	else:
		title_type = 'tv_series,mini_series'
		series = 1
		movies = 0

	
	start_urls = ['https://www.imdb.com/search/title/?genres=' + genres[genre] + '&title_type=' + title_type + '&explore=genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=facfbd0c-6f3d-4c05-9348-22eebd58852e&pf_rd_r=3YZAEBZDQPXZ15EFTDZY&pf_rd_s=center-6&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_mvpop_1']

	rules = (
	    Rule(LinkExtractor(restrict_xpaths = "//h3[@class = 'lister-item-header']/a"), callback='parse_item', follow=True),
	)

	def parse_item(self, response):
		if self.movies == 1 :
		    yield {
		    	'Movies' : self.movies,
			    'Title' : response.xpath ("//div[@class = 'title_wrapper']/h1/text()").get(),
			    'Year' : response.xpath("//span[@id = 'titleYear']/a/text()").get(),
			    'Duration' : response.xpath("//div[@class = 'subtext']/time/text()").get(),
			    'Rating' : response.xpath("//span[@itemprop = 'ratingValue']/text()").get(),
			    'Trailer' : response.urljoin(response.xpath("//div[@class = 'slate']/a/@href").get()),
			   	'Link' : response.url
		    }

		else :
			yield {
				'Movies' : self.movies,
				'Title' : response.xpath ("//div[@class = 'title_wrapper']/h1/text()").get(),
				'Year' : response.xpath("//a [@title = 'See more release dates']/text()").get(),
				'Total Episodes': response.xpath("//*[@id='title-overview-widget']/div[1]/div[3]/a/div/div/span/text()").get(),
			    'Rating' : response.xpath("//span[@itemprop = 'ratingValue']/text()").get(),
			    'Episode Duration' : response.xpath("//div[@class = 'subtext']/time/text()").get(),
			    'Trailer' : response.urljoin(response.xpath("//div[@class = 'slate']/a/@href").get()),
			   	'Link' : response.url

			}

