# wine_ratings

![picture](images/vino.jpeg)

## Motivation
As a self-proclaimed Oenophile, analyzing the data collected by wine experts employed by WineEnthusist, allowed me to dive into the controversial subject of wine ratings. Ratings help guide consumers to spend their money on wine that has verified, quantified quality. This key advertising strategy has launched a series of tasting events, social media rating apps along with wine competitions. Wine consumption has been skyrocketing, and as such, exploring our built in assumptions is a key aspect to moving forward in the wine industry. 

## Questions
1. Do our tasters have a more lengthy description of the wines they have rated higher? 
2. Do specific regions or countries have statistically higher ratings?

## About this Data
* Viewing this data before manipulating the points of interest, it seems like there is a total of thirteen categories. 
    1. Country: This gives the full name of the Country where the wine was made.
    2. description: Here is the description given by the wine taster
    3. designation: Typically this indicates unusual qualities of the wine like color but can also count as a labeled reserve or special selection
    4. points: This refers to the rating given by the taster
    5. price: Price of wine at the moment it was tasted
    6. province: states, divisons or other special areas within a country where winery is located
    7. region_1: more specific area of winery than province
    8. region_2: the most specific geographical area provided 
    9. taster_name: Name of the taster, info about the individual can be found on WineEnthusiast.com
    10. taster_twitter_handle: taster's available social media
    11. title: the name of the wine
    12. variety: what variety or type classifies the wine
    13. winery: specific name of wine's original location

* With 43 different countries listed, I was interested in the amount of wines from each country were rated in this data set. Here is a visual of the top included countries and the least included. 
![picture](images/top_least_rated_bar.png)

* Price seems to drive much of the wine business. Viewing the inital disribution of prices, most wines tasted were between $10 and $70. However, these tasters have also ventured into the outlandish prices including the most exensive bottle: $300,000. 
![picture](images/price_box.png)
    * In the visual above we see the prices with the top five countrys all have substatial outliers, the most sigificant being France. 
    * We also see an overall price drop when compared to the rating above, at and below the average point value of the data set. 

* The collection of ratings does follow the expectation which was centering around the center option of 90 points. 
![picture](images/Original_rate_dist.png)





* The data contains information about 43 different countries and range between having 1 to 54,504 values available for that country. After viewing the missing data for the 'country' column, there were a total of 63 missing countries. Looking deeper into the winery of each of these missing values, it looks like we alreay have sufficient data to work from and will drop these 63 rows. For example, there were 7 missing values cited from a winery in Austria, but since we already have 3345 other rows containing Austrian information those extra seven rows are likely to be insignificant. Also, the rows missing country name also correlate to the province missing values. Dropping those countries will also create non null values in the province column. 

* Focusing on the differences between title and designation column, it looks fairly repeditive. Each desgination has language repeated in the title column and would be unnecessary to utalize from here on out. The designation column will be dropped for the remainder of the data analysis. 

* All columns pertaining to taster information will also be dropped since I do not plan on finding inferences between the indiviual taster and their ratings at this time. Similarly, the description column which has no null values does not contain any informative information at this time since I am not searching for correlations between ratings and specific wine descriptive terms.

* Province and region_1 have some useful data that would allow looking into the intricacies of indiviual countries with more depth and will be kept. Region_2 however has such a large number of null values and simply provides further detail to Region_1 column that It will also be dropped. 

* After all of the initial data investigation, I will be searching for statistical correlations using the following information. I have 129908 rows of information pertaining to the following non-null columns: Country, points, province, title, variety and winery. I also will be utilizing the 120916 non-null price values and possibly the 108724 non-null rows of region_1 for further research. 



## Hypothesis

1. I was interested in determining if there was a statistical correlations between wine rating and country. 

    Null Hypothesis: Italian wines have the same average rating as other countries
    Alternative Hypothesis: Italian wines have a statistically significant higher rating. 

    After calculating a p_value of 8.839008131948766e-13 I can safely reject my null Hypothesis and determine that Italian wines have a statistically higher rating than other wines

![picture](images/overlapping_cdf.png)
    Here we seet the cumulative distribution functions for the ratings of the Italian Wines versus the others.


2. I was also interested in looking closer at the relationship between the description and the rating value.

    Null Hypothesis: Wines that are less than the median rating have a the same length descriptions as wines with points above the median.
    Alternative Hypothesis: Wines that are higher than the median rating have longer descriptions than the wines with lower ratings.

    Once finding a p_value of exactly 0 I can certainly conclude that the rating value is connected to having longer descriptions.

![picture](images/desc_per_rate_violin.png)

3. Similar to my second hypothesis, I wondered if the reverse concept was true. 
    Null Hypothesis: Wines that have fewer than the median number of words in the description no difference in ratings ratings than those with longer descriptions. 
    Alternative Hypothesis: Wines that have greater than the median number of words in the description have higher ratings.

    Using this similar hypothesis, I also found a p_value of exactly 0. The length of the description is correlated with having higher reviews.

![picture](images/points_scatter_per_desc.png)





#36247 CA Reviews
#22093 FR Reviews
#19540 IT Reviews

'''
Ho = Wines that are less than the median rating have a the same length descriptions as wines with points above the median.
Ha = Wines that are higher than the median rating have longer descriptions than the wines with lower ratings.
alpha = 0.05
p_value of 0 
Reject the Null Hypothesis
'''

'''
Ho = Wines that have fewer than the median number of words have fewer points.
Ha = Wines that have greater than the median number of words have higher ratings.
alpha = 0.05
alpha = 0
Reject the Null Hypothesis
'''