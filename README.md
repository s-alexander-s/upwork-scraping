# upwork-scraping
Project aimed to provide set of utilities to scrape some useful information from UpWork. I develop it according to my personal need but if you have an idea feel free to create an issue.

## my_rank_for_query.py
It's a simle scraper that helps you to determine your place (rank) in [UpWork freelancers search](https://www.upwork.com/o/profiles/browse/) in terms of particular query. Here is an example of how to check the rank of my agency on UpWork ([blue underlined link](https://www.upwork.com/companies/~0140676ee0e4006401)):

```
> scrapy runspider -a profile_id="~0140676ee0e4006401" -a query="telegram bot" -a page_limit=10 -o telegram_bot.json my_rank_for_query.py
2018-10-23 19:45:55 [scrapy.utils.log] INFO: Scrapy 1.5.1 started (bot: scrapybot)
...
2018-10-23 19:45:58 [scrapy.core.engine] INFO: Spider closed (Your profile rank is 26. You are at page 3: https://www.upwork.com/o/profiles/browse/?q=telegram+bot&page=3)
```

Let's go to the link and check the results (I recomend you to be logged out and use incognito mode of your browser): https://www.upwork.com/o/profiles/browse/?q=telegram+bot&page=3


### profile_id
You should use your agency `profile_id` if your are agency freelancer otherwise you should use your personal `profile_id`. You can get profile id from these links:

#### Personal link
Here is my personal profile: https://www.upwork.com/freelancers/~01b101e9259c8483ee  
![Personal link](/images/personal_link.png)

#### Agency link
Here is my agency profile: https://www.upwork.com/companies/~0140676ee0e4006401  
Since I am agency freelancer I am using as a parameter for the scraper.  
![Agency link](/images/agency_link.png)

### query
`query` is a search query what you want to check, `telegram bot` e.g.

### page_limit
UpWork limit the page number at 500 although there maybe more freelancers. But if you don't want to scrape so many pages you can use `page_limit` parameter.

## Ouput
In addition to determining your place in the search results scraper also saves some data about all scraped freelancers in the output file. Here it is `telegram_bot.json`.
