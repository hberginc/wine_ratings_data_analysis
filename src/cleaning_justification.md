
* The data contains information about 43 different countries and range between having 1 to 54,504 values available for that country. 

* After viewing the missing data for the 'country' column, there were a total of 63 missing countries.

* Looking deeper into the winery of each of these missing values, it looks like we alreay have sufficient data to work from and will drop these 63 rows. *For example, there were 7 missing values cited from a winery in Austria, but since we already have 3345 other rows containing Austrian information those extra seven rows are likely to be insignificant.* 

* The rows missing country name also correlate to the province missing values. Dropping those countries will also create non null values in the province column. 

* Focusing on the differences between title and designation column, it looks fairly repeditive. Each desgination has language repeated in the title column and would be unnecessary to utalize from here on out. The designation column will be dropped for the remainder of the data analysis. 

* All columns pertaining to taster information will also be dropped since I do not plan on finding inferences between the indiviual taster and their ratings at this time. 

* The description column which has no null values does not contain any informative information at this time, but might in the future if I determine there is a reason to look deaper into the phrases and words based on varieties.

* Province has some useful data that would allow looking into the intricacies of indiviual countries with more depth and will be kept. 

* Region_1 and Region_2 however has such a large number of null values and simply provides further detail to the Province column that It will also be dropped. 

* After all of the initial data investigation, I will be searching for statistical correlations using the following information. I have 129908 rows of information pertaining to the following non-null columns: Country, points, province, variety. I also will be utilizing the 120916 non-null price values.