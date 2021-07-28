import scrapy 

class DrugSpider(scrapy.Spider): #class inherits from srcapy and inside scrapy inherits from a spider

	name = 'drugs' #name of spider
	#list of the urls to scrape
	start_urls =['http://www.centrallancashireformulary.nhs.uk/chaptersSubDetails.asp?FormularySectionID=4&SubSectionRef=04.02.02&SubSectionID=A100']

	def parse(self, response): #creating parse method that requires self reference and response which contains the source code of website to scrap

		#get all html elements containing the data (first 15 elements)
		data = response.css('td.normalDrug')[:15]

		#split the elements into groups of 3 forming every object container
		container = [ 
			#group by 3
			data[x:x+3] 
			#for all elements in data, increment by 3
			for x in range(0, len(data), 3) 
		]
		
		#loop through the list of objects container
		for element in container:

			#retrieve data according to the aprropriate td html element 
		     yield {
			    'drug_name': element.css('span.boldDrug::text').get().replace('\r\n\t  ',''), 
			    'status': element.css('strong::text').get(),
			    'colour': element.css('img:nth-child(2)::attr(alt)').get(),
			    'notes': element.css('p:nth-child(1)::text').get(),
			    'brand_name': element.css('br+p::text').get() 
			}