# WebScraper
## Project implementation steps
### Steps 1-3
1. Provide url of the products opinions page
2. Send the request to provided url
3. Fetch the product name
4. Fetch all opinions from the webpage
5. Parse opinions to extract required data
6. Check if there is next page with opinions
7. Repeat steps from 4 to 6 for all pages with opinions about product
8. Save aquired opinions
## Project inputs 
### Product codes
- 173179719
- 174130671
- 186933309
- 180826505
- 90558892
- 39562616
### Opinion structure
|component|name|selector|
|---------|----|--------|
|opinion ID|opinion_id|[data-entry-id]|
|opinion’s author|author|span.user-post__author-name|
|author’s recommendation|reccomendation|span.user-post__author-recomendation > em|
|score expressed in number of stars|score|span.user-post__score-count|
|opinion’s content|content|div.user-post__text|
|list of product advantages|pros|div.review-feature__item--positive|
|list of product disadvantages|cons|div.review-feature__item--negative|
|how many users think that opinion was helpful|helpful|button.vote-yes[data-total-vote]|
|how many users think that opinion was unhelpful|unhelpful|button.vote-no[data-total-vote]|
|publishing date|publish_date|span.user-post__published > time:nth-child(1)[datetime]|
|purchase date|purchase_date|span.user-post__published > time:nth-child(2)[datetime]|


