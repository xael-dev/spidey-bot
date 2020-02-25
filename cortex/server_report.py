import scrapy
import logging
import operator

logging.getLogger('scrapy').setLevel(logging.WARNING)

class server_tracker(scrapy.Spider):
    name = 'DownDetector'
    start_urls = ['https://downdetector.com/status/escape-from-tarkov/']

    def parse (self, response):
        # entity_name is a list obj
        entity_name = response.css('div.h2.entry-title.color-danger::text').extract()
        trimmed_name = list(map(str.strip, entity_name))
        print (trimmed_name[0])

        # Grab Server Connection reports
        report_problem_percentages = response.css('div.text-center.font-weight-bold::text').extract()
        report_list_length = len(report_problem_percentages)
        trimmed_problem_percentages = list(map(str.strip, report_problem_percentages))
        probable_cause = index, value = max(enumerate(trimmed_problem_percentages), key=operator.itemgetter(1))
        (index, value) = probable_cause

        a = 0
        while a < report_list_length:
            if a == 0:
                print(" Current server outage reports are " +  trimmed_problem_percentages[a])
            elif a == 1:
                print(" Current login reports are " +  trimmed_problem_percentages[a])
            elif a == 2:
                print(" Current Website outage reports are " +  trimmed_problem_percentages[a])
            a = a + 1

        if index == 0:
            probable_assumption = "Server Outage"
        if index == 1:
            probable_assumption = "Login issues"
        if index == 2:
            probable_assumption = "Website Outage"

        print("The problem is presumed to be:", probable_assumption)