# Gender Detector
## Introduction
I will be using a handmade CSV to analyze the genders of all the guests on The Daily Show with Trevor Noah (2015-2016). I want to better understand potential gender disparities between the guests that Trevor Noah books for his show. My sense is that he books more men than women, but this will provide me with more evidence to go by.

Findings: Trevor Noah has substantially more male guests than female guests in his short tenure.

## Methodology and Caveats
I created my own CSV for this project. I copied and pasted all the information of guests from [this Wikipedia page listing Trevor Noah's guest for part of 2015](https://en.wikipedia.org/wiki/List_of_The_Daily_Show_episodes_(2015)#2015_.28under_Noah.29) 
and [this Wikipedia page of his guests thus far in 2016](https://en.wikipedia.org/wiki/List_of_The_Daily_Show_episodes_(2016)). The final dataset can be found in [my Github](https://github.com/kapowers/compciv-2016/blob/master/projects/gender-detector/Stash/Trevor%20Noah%20Guests.csv)

I will analyze about ~60 records. I will try to separate the names of the record such as Joe Doe to just 'Joe' and then classify gender based upon the name. I will split the name using the below function to split and then only classify the first element in the list: <br />
&nbsp;	def extractable_usable_name(name): <br/>
&nbsp;&nbsp;		return name.split(' ')[0]

One of the problems I was unable to resolve was the presence of "''" in front of Rand Paul's name. It was literally the only name that had a weird error that could not be edited in the original data set. 

## Past Research and articles
- [When Women Run the Show, TV's Gender Gap Narrows](http://www.takepart.com/article/2015/09/15/women-television): This research discusses how when women run television networks, the gender gap on TV narrows. This precludes that women are generally not represented on TV programming, partiularly host shows, like the one I am analyzing, which is run by a man.
- [Closing the TV-Guest Gender Gap](http://www.theatlantic.com/entertainment/archive/2015/03/how-to-get-more-women-on-tv/386378/): This article speaks directly to the challenges hosts have in finding a balanced 50/50 guest list based on gender. I assume this will eventually make me more empathatic to the "plight" Trevor Noah faces in finding "quality TV" guests. (sarcasm deeply intended)
- [Gender and Ethnic Diversity in Prime-Time Cable News](http://mediamatters.org/research/diversity_report/): More depressing statistics and similar findings that show the overrepresentation in men in prime time television. 

## How to
- fetch_data.py - Running this script will download a CSV file of guests on The Daily Show with Trevor Noah, including the year they appeared and the description of their show.
- wrangle_data.py - Running this script will add appropriate headers of "year, name, description" to a new CSV from the one you downloaded
- fetch_gender_data.py - Running this script will download a list of all the names, genders, ratios, and totals within a zipfile of multiple years of Social Security Administration data.
- wrangle_gender_data.py - Running this script will add headers to a new JSON file that includes name, gender, ratio, females, males, and total for every year of data.
- gender.py - Creating gender.py creates a script that will eventually help you in identifying the gender of the name you want to analyze.
- classify.py - Running this script will separate out the first name of all the names you have and return a list of all the first names. It will then detect the gender of that first name.
- analyze.py - Running this script will tell you how many females vs male guests appeared on the TV shows, showing you ratios and a breakdown/comparison by year.

## Analysis
In my analysis, I did very simple calculations. I first determined how many men and women total have appeared on Trevor Noah's show. I found that, by ratio, men far outweighed women. I then did the same calculation for each year and found that women were again underrepresented. Finally, to hammer in my point, I compared the number of male guests in 2015 alone to the total number of female guests across both years to demonstrate how many more male guests are represented on the show.

