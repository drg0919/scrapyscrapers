# scrapyscrapers
Scraping various resources with Scrapy

## Running scrapers
1. cd to the scraper
2. Run 'scrapy crawl <scrapername>'
3. To output data into json or csv, add '-o <filename>.<extension>' to command in point 2.

## IMDb
Available scrapers - 
* best_movies - Top 250 movies listed on IMDb
Data Returned - 
* title - Title of the movie
* year - Year of release
* rating - IMDb rating
* run_time - Running time
* rated - MPAA rating
* genre - Genre of the movie

## Stocks (moneycontrol.com)
Available scrapers - 
* positive_breakouts - Positive breakout stocks
* negative_breakouts - Negative breakout stocks
Data returned - 
* title - Name of stock
* current - Current price
* change - Change in price 
* sma_30/sma_50/sma_150/sma_200 - Simple moving average for 30,50,150 and 200 days respectively
* link - Link to the stock's page on moneycontrol.com
* pe_ratio - PE ratio
* ind_pe - Industry PE

## Goodreads
Additional setup - 
* Place 'chromedriver' in the root folder ie, inside 'goodreads' folder
Availabe scrapers - 
* quotes - Quotes on goodreads homepage
Data returned - 
* quote - Quote itself
* author - Author of quote

## Currence (x-rates.com)
Available scrapers - 
* exchange - Exchange rates for foreign currencies again INR
Data returned - 
* currency - Name of foreign currency
* rate - Exchange rate
