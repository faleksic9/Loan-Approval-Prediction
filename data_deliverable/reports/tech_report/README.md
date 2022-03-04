# Tech Report
This is where you can type out your tech report.

### Where is the data from?
There are 224,325 entries in our data set currently for the State of Rhode Island in 2013-2017, so there is ample data to perform analysis on. Depending on our question and how we phrase it, the split of the data could be different. This is because our question may be based on the type loan approvals and the specific classification of loans which we choose. In general, most mortgages are approved so there will most be more approvals than rejections in our dataset. This is already enough data to do enough analysis on just the state of Rhode Island. If we want to make observations that are more generalizable, we may need to look at data from other states as well. 

### How did you collect your data?
Thousands of financial institutions have been reporting data about mortgages under the Home Mortgage Disclosure Act (HMDA). The data is publicly available through their online archive from 2007-2017 and has approximately 183 Million entries. 

### Is the source reputable?
The source is reputable since it is a government owned and regulated database.

### How did you generate the sample? Is it comparably small or large? Is it representative or is it likely to exhibit some kind of sampling bias?
We generated our sample by joining the tables which had loans data for Rhode Island for years 2013, 2014, 2015, 2016, and 2017. The size is comparably large since we have data from 4 years, resulting in hundreds of thousands of entries. Since we are only looking at data from one state, there is a sampling bias in terms of the implications that come with the location of Rhode Island (type of loans, political beliefs, etc). 


### Are there any other considerations you took into account when collecting your data? This is open-ended based on your data; feel free to leave this blank. (Example: If it's user data, is it public/are they consenting to have their data used? Is the data potentially skewed in any direction?)
No.

### How clean is the data? Does this data contain what you need in order to complete the project you proposed to do? (Each team will have to go about answering this question differently, but use the following questions as a guide. Graphs and tables are highly encouraged if they allow you to answer these questions more succinctly.)
### How many data points are there total? How many are there in each group you care about (e.g. if you are dividing your data into positive/negative examples, are they split evenly)? Do you think this is enough data to perform your analysis later on?
### Are there missing values? Do these occur in fields that are important for your project's goals?
### Are there duplicates? Do these occur in fields that are important for your project's goals?
### How is the data distributed? Is it uniform or skewed? Are there outliers? What are the min/max values? (focus on the fields that are most relevant to your project goals)
### Are there any data type issues (e.g. words in fields that were supposed to be numeric)? Where are these coming from? (E.g. a bug in your scraper? User input?) How will you fix them?
### Do you need to throw any data away? What data? Why? Any reason this might affect the analyses you are able to run or the conclusions you are able to draw?
Our dataset contains 224,325 records and 78 attributes. Since the data was government owned and regulated, it was extremely clean and combed through very finely for any errors like missing values, repetitions or data type issues. We found one attribute (application_date_indicator) had around 20% missing entries, but we figured since we had the year in a different attribute, we didn’t need to consider it. For the rest of the entries, 99.2% or more of the data is filled. Because of this, we did not need to do any cleaning of the data at all. However, we might consider dropping or looking into application_date_indicator since there are too many missing values even though  for now we used all attributes and did not throw any data away, because we found each point could be relevant to our analysis. The data was distributed in a uniform manner, with some outliers, especially since our data has many qualitative entries. We were able to see a preview of the data before we downloaded it and concluded that it passed our threshold for cleanliness since we were able to very clearly understand the purpose and use for all columns. We noticed outliers the following variables: number_of_1_to_4_family_units, minority_population, tract_to_msamd_income. However, we are just acknowledging that there are outliers and we will deal with them accordingly later since they might impact the performance of our model but could also be very insightful. 
[Screen-Shot-2022-03-03-at-8-24-02-PM.png](https://postimg.cc/ThL583hK)
[Screen-Shot-2022-03-03-at-8-25-04-PM.png](https://postimg.cc/HcfxWbjV)
[Screen-Shot-2022-03-03-at-8-25-56-PM.png](https://postimg.cc/8s6cKXnW)
When it comes to the distribution, we didn’t notice much skewness:
[Screen-Shot-2022-03-03-at-8-27-20-PM.png](https://postimg.cc/xNDfVYFm)


### Summarize any challenges or observations you have made since collecting your data. Then, discuss your next steps and how your data collection has impacted the type of analysis you will perform. (approximately 3-5 sentences)
We initially wanted to gather data from 2017-2020 to see how covid affected loans data in California and Florida. However, we had trouble downloading the data due to the sheer volume, so we shifted our focus to Rhode Island data. In our next steps, I anticipate we will have some challenges coming up with holistic statistics, especially in regards to qualitative attributes. Additionally, it may be difficult to accurately address how bias has affected our data collection and analysis, since we don’t have another state or previous loan reports to compare Rhode Island loan statistics to. 

