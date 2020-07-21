# wine_ratings

![picture](images/vino.jpeg)

## OVERVIEW

History of wine ratings goes here: 
src to help: https://winefolly.com/tips/wine-ratings-explained/


## Questions
1. Is there actually statistical correlations between rating and description?

2. Which varieties are popuar in each individual region and does that popularity span to other regions?

## Cleaning the Data
* Viewing the data before dropping any values, this CSV has a total of 129,975 rows to investigate and 13 columns. The data provides the following columns: county, description, designation, points, price, province, regions_1, regions_2, taster_name, taster_twitter_handle, title, variety, and winery. 

* Columns that have no null values are [description, points, title, and winery]. After investigating the one missing variety value, it was determined that the variety could be included as 'Cabernet Sauvignon' which added that column to the no null values list. 

* The data contains information about 43 different countries and range between having 1 to 54,504 values available for that country. After viewing the missing data for the 'country' column, there were a total of 63 missing countries. Looking deeper into the winery of each of these missing values, it looks like we alreay have sufficient data to work from and will drop these 63 rows. For example, there were 7 missing values cited from a winery in Austria, but since we already have 3345 other rows containing Austrian information those extra seven rows are likely to be insignificant. Also, the rows missing country name also correlate to the province missing values. Dropping those countries will also create non null values in the province column. 

* Focusing on the differences between title and designation column, it looks fairly repeditive. Each desgination has language repeated in the title column and would be unnecessary to utalize from here on out. The designation column will be dropped for the remainder of the data analysis. 

* All columns pertaining to taster information will also be dropped since I do not plan on finding inferences between the indiviual taster and their ratings at this time. Similarly, the description column which has no null values does not contain any informative information at this time since I am not searching for correlations between ratings and specific wine descriptive terms.

* Province and region_1 have some useful data that would allow looking into the intricacies of indiviual countries with more depth and will be kept. Region_2 however has such a large number of null values and simply provides further detail to Region_1 column that It will also be dropped. 

* After all of the initial data investigation, I will be searching for statistical correlations using the following information. I have 129908 rows of information pertaining to the following non-null columns: Country, points, province, title, variety and winery. I also will be utilizing the 120916 non-null price values and possibly the 108724 non-null rows of region_1 for further research. 



## Hypothesis

First, I was interested in determining if there was a statistical correlations between wine rating and country. 

    Ho = Italian wines have the same average rating as other countries
    Ha = Italian wines have a statistically significant higher rating. 

    alpha = 0.05
    p_value = 8.839008131948766e-13

    I can reject my null hypothesis, Italian wines have a statistically significant higher rating than non Italian wines



    Ho = The variety Cabernet Sauvignon has the same rating distribution as others
    Ho = The variety Cabernet Sauvignon has a higher rating distribution than others


    Ho = The length of the description correlates by no more than .60 to the ratings.
    Ha = The length of the descriotion is statistically correlated to higher ratings








I believe that I will find that the more expensive wines are more likely to get a higher rating. I also believe that the higher the rating, the more likely that it is an Old World vinyard that produced the grapes. 

I will be searching through the data found on Kaggle's 'Wine Reviews' database for correlations between the rating the indiviual gave a specific wine compared to other wines with similar characteristics. 

There is a total of 14 columns in the csv file I plan on using with a total of 130,000 rows of data provided. This was data originally scraped from WineEnthusiast. The main columns I will be focusing on are the following, [country, designation, points, price, province, region1, region2]. Points and price provide numerical data while the other columns are categorical. Designation has about a quarter of the data missing and most likely will not play a pivital role in determining statistical inference but may be interesting to investigagte why they are Nan values. Region1 also contains Nan values 16% of the time which may highlight specific provinces and clarify why that is the case. Since region2 clarifies any more specific information avaiable about region1 and has fewer than 50% available data available. 
The only columns that do not have Nan values are the description and the rating columns. 

The minimum I plan on acomplishing with this available data is to state correlations between price and rating. The small percentage of Nan values in the price column would likely not have an effect on finding correlations through the data cleaning process and will likely be dropped. I will provide graphical visuals to express the dataset and explore the outliers. 

