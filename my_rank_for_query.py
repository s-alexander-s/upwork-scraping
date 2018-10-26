from urllib.parse import urlencode

import scrapy
from scrapy.exceptions import CloseSpider


class UpWorkQuerySpider(scrapy.Spider):
    name = 'freelancers'
    custom_settings = {
        # Have to use real User-Agent since UpWork returns 403 with scrapy default User-Agent
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/69.0.3497.100 Safari/537.36',
        'CONCURRENT_ITEMS': 1
    }

    URL = 'https://www.upwork.com/o/profiles/browse/?{params}'
    MAX_PAGE = 500  # UpWork gives access only to first 500 pages of freelancers (5000 freelancers) there maybe more
    FREELANCERS_ON_PAGE = 10

    def __init__(self, profile_id, query, page_limit=5, *args, **kwargs):
        super(UpWorkQuerySpider, self).__init__(*args, **kwargs)
        self.profile_id = profile_id
        self.query = query
        self.page_limit = min(int(page_limit), self.MAX_PAGE)  # There is no point in requesting more than 500 pages

    def start_requests(self):
        for page in range(1, self.page_limit + 1):
            yield scrapy.Request(
                self.URL.format(params=urlencode({'q': self.query, 'page': page})),
                meta={'page': page}  # We'll use it later to calculate freelancer's rank
            )

    def parse(self, response):
        page = response.meta['page']
        for i, freelancer in enumerate(response.css('h4 a.freelancer-tile-name')):
            name = freelancer.css('::text').extract_first().strip()
            profile_link = freelancer.css('::attr(href)').extract_first()
            rank = (page - 1) * self.FREELANCERS_ON_PAGE + i + 1
            yield {
                'name': name,
                'profile_link': profile_link,
                'page': page,
                'rank': rank,
                'page_link': response.url,
                'data': freelancer.css('::attr(data-ng-click)').extract_first()
            }
            if self.profile_id in profile_link:
                raise CloseSpider(f'Your profile rank is {rank}. You are at page {page}: {response.url}')
