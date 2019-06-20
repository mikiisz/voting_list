# voting_list
21.06.2019
Authors:
* Michał Szkarłat
* Mateusz Wieczorek


## Elections to the European Parliament 2019
Its a simple application that generate votes from packed data and plot various graphs. 
Raw data source is here:
```
https://wybory.gov.pl/pe2019/pl/dane_w_arkuszach
```

## Table of contents
* [Extracting data](#extracting-data)

## Extracting data
After dowloading raw packages we need to procces them in order to get valid data that represent ~ 14 milions Polish voters from election to the European Parliament. To achive that we need to use <b> split_votes.py </b> file. Result data looks like this and represent each signle voter:
