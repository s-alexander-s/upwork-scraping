# upwork-scraping
Project aimed to provide set of utilities to scrape some useful information from UpWork. I develop it according to my personal need but if you have an idea feel free to create an issue.

## my_rank_for_query.py
It's a simle scraper that helps you to determine your place (rank) in UpWork freelancers search in terms of particular query. Here is an example of how to check rank of my agency on UpWork ([blue underlined link](https://www.upwork.com/companies/~0140676ee0e4006401)):

```
scrapy runspider -a profile_id="~0140676ee0e4006401" -a query="telegram bot" -a page_limit=10 -o freelancer.json my_rank_for_query.py

```

You should use your agency `profile_id` if your are agency freelancer otherwise you should use your personal `profile_id`. You can get profile id from these links:

