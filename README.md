# wine_ratings

 ![Viva la Vino](images/vino.jpg)

Is there actually statistical correlations between wine rating and price, region or province?
I believe that I will find that the more expensive wines are more likely to get a higher rating. I also believe that the higher the rating, the more likely that it is an Old World vinyard that produced the grapes. 

I will be searching through the data found on Kaggle's 'Wine Reviews' database for correlations between the rating the indiviual gave a specific wine compared to other wines with similar characteristics. 

There is a total of 14 columns in the csv file I plan on using with a total of 130,000 rows of data provided. This was data originally scraped from WineEnthusiast. The main columns I will be focusing on are the following, [country, designation, points, price, province, region1, region2]. Points and price provide numerical data while the other columns are categorical. Designation has about a quarter of the data missing and most likely will not play a pivital role in determining statistical inference but may be interesting to investigagte why they are Nan values. Region1 also contains Nan values 16% of the time which may highlight specific provinces and clarify why that is the case. Since region2 clarifies any more specific information avaiable about region1 and has fewer than 50% available data available. 
The only columns that do not have Nan values are the description and the rating columns. 

The minimum I plan on acomplishing with this available data is to state correlations between price and rating. The small percentage of Nan values in the price column would likely not have an effect on finding correlations through the data cleaning process and will likely be dropped. I will provide graphical visuals to express the dataset and explore the outliers. 

