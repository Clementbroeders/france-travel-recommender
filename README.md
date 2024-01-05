# France-Travel-Recommander

<img src="https://th.bing.com/th/id/OIG.lH3gebRlw2.bpx0iqRae?pid=ImgGn" alt="Image" width="30%" height="30%">

## Introduction

After doing some user research, the marketing team of France Travel Recommander discovered that **70% of their users who are planning a trip would like to have more information about the destination they are going to**. 

In addition, user research shows that **people tend to be defiant about the information they are reading if they don't know the brand** which produced the content. 

Therefore, France Travel Recommander will help you to know where people should plan their next holidays. The application is based on real data about:

* Weather 
* Hotels in the area 

The notebook recommends the best destinations and hotels based on the above variables at any given time.


## How does it work ?

France Travel Recommander retrieves the datas from 3 sources :

1) API - Nominatim.org
Retrieve longitude and latitude coordinates for each city

2) API - openweathermap.org
Retrieve weather forecast for each city for the next 5 days

3) Scraping - booking.com
Retrieve hotel data for each city

All the data are compiled in this notebook, and the result is a map of the 20 best hotels within the 5 selected cities.