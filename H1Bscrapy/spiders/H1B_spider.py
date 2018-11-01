from scrapy import Spider, Request
from scrapy.selector import HtmlXPathSelector
from H1Bscrapy.items import H1BItem




class H1Bspider(Spider):
	name= "H1B_spider"
	allowed_urls= ["https://h1bdata.info/"]
	start_urls=["https://h1bdata.info/topjobs.php"]

	
	def parse(self, response):
		rows_main=response.xpath('/html/body/div[2]/center/div/table//tr')

		for row in rows_main:
			job= row.xpath('.//td[2]/a/text()').extract_first()  
			print(job)
			try:
				no_of_h1b_filings=  row.xpath('.//td[3]/text()').extract_first()
				no_of_h1b_filings= 	int(no_of_h1b_filings.replace(',',''))
				print(no_of_h1b_filings)
			except:
				continue

			url= row.xpath('.//td[2]/a/@href').extract_first()  
			##https://h1bdata.info/index.php?year=2018&job=PROGRAMMER+ANALYST
			##https://h1bdata.info/index.php?em=&job=PROGRAMMER+ANALYST&city=&year=All+Years
			##https://h1bdata.info/index.php?em=&job=SOFTWARE+ENGINEER&city=&year=All+Years

			ans= "".join([x.replace(' ','+') for x in job])
			result_url2= 'https://h1bdata.info/index.php?em=&job={}&city=&year=All+Years'.format(ans) #for all years


			yield Request(url= result_url2, meta={ 'job' :job, 'no_of_h1b_filings' :no_of_h1b_filings },
			 callback=self.parse_result_page)


	def parse_result_page(self,response):

		

		job=response.meta['job']
		no_of_h1b_filings=response.meta['no_of_h1b_filings']

		

		row_jobs= response.xpath('//*[@id="myTable"]//tr')  #ignored tbody
		
		print(len(row_jobs))
		print('-'* 50 )

		for row_job in row_jobs:
			employer=row_job.xpath('./td[1]/a/text()').extract_first()
			print(employer)
			job_title=row_job.xpath('./td[2]/a/text()').extract_first()
			print(job_title)
			base_salary=row_job.xpath('./td[3]/text()').extract_first() 
			print(base_salary)
			location1=row_job.xpath('./td[4]/a/text()').extract_first()
			print(location1)	
			submit_date=row_job.xpath('./td[5]/text()').extract_first() 
			print(submit_date)
			start_date=row_job.xpath('./td[6]/text()').extract_first() 
			print(start_date)
			status=row_job.xpath('./td[7]/text()').extract_first()
			print(status)


			item= H1BItem()
			item['job']= job
			item['no_of_h1b_filings']= no_of_h1b_filings
			item['employer']=employer
			item['job_title']=job_title
			item['base_salary']=base_salary
			item['location1']=location1
			item['start_date']=start_date
			item['submit_date']=submit_date
			item['status']=status

			yield item

			
						



			

