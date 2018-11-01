# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class H1BItem(scrapy.Item):

	job=scrapy.Field()
	no_of_h1b_filings=scrapy.Field()
	employer=scrapy.Field()
	job_title=scrapy.Field()
	base_salary= scrapy.Field()
	location1= scrapy.Field()
	submit_date= scrapy.Field()
	start_date=scrapy.Field()
	status= scrapy.Field()

