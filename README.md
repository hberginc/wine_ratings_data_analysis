# wine_ratings

<p align="center">
    <img src="images/vino.jpeg" width='600'/>
</p>

## Motivation
As a self-proclaimed Oenophile, analyzing the data collected by wine experts employed by WineEnthusist, allowed me to dive into the controversial subject of wine ratings. Ratings help guide consumers to spend their money on wine that has verified, quantified quality. This key advertising strategy has launched a series of tasting events, social media rating apps along with wine competitions. Wine consumption has been skyrocketing, and as such, exploring our built in assumptions is a key aspect to moving forward in the wine industry. 

## About this Data
* Viewing this data before manipulating the points of interest, it seems like there is a total of thirteen categories. Of these thirteen, the following 5 columns provide the most interets. 
    1. country: This gives the full name of the Country where the wine was made.
    2. description: Here is the description given by the wine taster
    3. points: This refers to the rating given by the taster
    4. price: Price of wine at the moment it was tasted
    5. province: states, divisons or other special areas within a country where winery is located6

* With 43 different countries listed, the top included countries and the least included can be found in the image below. We see that US, Italy and France have the most available data per country. 
![picture](images/top_least_rated_bar.png)


* Price seems to drive much of the wine business. Viewing the inital disribution of prices, most wines tasted were between $4 and $80. However, these tasters have also ventured into the outlandish prices including the most exensive bottle at $330,000. 
![picture](images/price_box.png)
    * In the visual above we see the prices with the top five countrys all have substatial outliers, the most variation being in France. 
    * We also see an overall price drop when compared to the rating at or above, at and below the average point value of the data set. 

* The collection of ratings range from 80 to 100 which is a typical rating range for wines. In America, the ratings range from 80-100 and in Europe they range from 0 - 20. The ratings follow a bell curve shape centering around 88. 
![picture](images/Original_rate_dist.png)

Please check out my file, cleaning_justification.md for more information on how I determined which columns and rows to utilize for my questions. 

## Hypotheses
Personally, I prefer Italian wines to any other region I have tried. Lets see if the ratings show off my own preference? Let's also take a look at Caliornia to compare how it holds up to the popular wines of France. 

H1. Italian wines have higher ratings when compared to other countries. 

H2. Italian wines have higher ratings when compared to France.

H3. Italian wines have higher ratings when compared to California.

H3. French Wines have higher ratings when compared to California. 

![picture](images/side_hists.png)

    Conducting 10,000 samples from each region, we can see all averages fall between 86 points and 90 points with peaks varying for each region. While our non_Italian data looks to have higher in general, looking into statistical analysis will tell a more acurate store. 


Each of these hypotheses merit the use of the Mann Whitney U test all single tailed since I am looking for a clear 'best' characteristic of the regions ratings.

H1: Italy v. All Others
Setting a significance level of 0.05 and returning a p_value of 0.0008 determines that I am confident that the **Italian wines on average rate higher than the other countries wines** provided. 

H2. Italy v. France
Using the Bonferroni Correction, the new significance level is adusted to 0.025. Calculating a p_value of 

H3. Italian wines have higher ratings when compared to California.

H3. French Wines have higher ratings when compared to California. 






To determine superior ratings in my initial test, a single tailed test calculated a p-value of 0.001. 
When comparing the Italian and French wine ratings the p-value of 5.21e-23 shows a strong chance that the ratings  between these two regions have statistically significant difference. 
Similarly for the final two tests, Italian Wines compared to California wines calculated a p-value of 4.79e-09 and finally, French wines and California wines have a calculated p-value of 1.43e-07.

Each of these tests allow me to conclude that, yes, regions do have differences in ratings and that Italian wines have a statistically higher average rating than others.

Before you pick up a Tuscon Red for the weekend, the image below shows the cumulitive distribution functions for the regions in question. Although the p_values show a significant statistical difference, the practical difference between the ratings is minimal at best.

![picture](images/side_by_side_cdf.png)




