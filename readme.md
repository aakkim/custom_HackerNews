# Custom Hacker News
This python script is created to scrape data from Hacker News, using Python3. Data collected are news with 100 votes or more. The title, link, and the number of votes are collected for each news. This helpful script allows you to browse the most up-voted news on Hacker News, instead of scrolling and searching for them. 

## Requirements
- beautifulsoup4 module: will need to be installed as it's not a built-in module
    > pip install beautifulsoup4
- requests module: will need to be installed as it's not a built-in module
    > pip install requests
- pprint module: a built-in module of python and does not require installation

## Instructions
Run the script in your terminal/cmd prompt by typing in python3 scrape.py

The output will show you the news with 100 votes or more with its' title, news link, and the number of votes. They are ordered from the highest number of votes to the lowest number of votes.