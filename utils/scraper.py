# This file has tools for crawling websites
# It helps the Crawler Agent find pages

# Import tools we need
import scrapy  # For crawling
from urllib.parse import urljoin  # To fix relative URLs

class SimpleSpider(scrapy.Spider):
    name = 'simple_spider'  # Name of our crawler
    
    def __init__(self, start_url, pages, *args, **kwargs):
        # Set up the crawler with the website URL
        super().__init__(*args, **kwargs)
        self.start_urls = [start_url]  # Start at this URL
        self.pages = pages  # List to store pages
        self.allowed_domain = start_url.split('/')[2]  # e.g., python.com
        self.allowed_domains = [self.allowed_domain]  # For Scrapy settings

    def parse(self, response):
        # This function looks at a page and finds links
        current_url = response.url
        # Only save pages from the target website
        if self.allowed_domain in current_url:
            self.pages.append(current_url)  # Save the current page
        
        # Find all links on the page
        for href in response.css('a::attr(href)').getall():
            # Fix relative URLs (e.g., /about -> https://python.com/about)
            full_url = urljoin(response.url, href)
            # Only follow links on the same website
            if self.allowed_domain in full_url or href.startswith('/'):
                yield response.follow(full_url, self.parse)

# What's next?
# The Crawler Agent uses this to find pages
# We'll improve it later to handle bigger websites