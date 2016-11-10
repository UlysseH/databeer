# Databeer

### Introduction
The *databeer* projects aims at extracting intelligence from the hundreds of thousands beer recipes accessible online.
The first steps, which we are currently working on, are data crawling and data modelling.
Once the data is corrected and structured, we'll move on the machine learning part.

### 1. Crawling
We use *scrapy* for web crawling, a powerful and versatile web crawler framework for Python.
#### 1.1. brewtoad.com
The first source we crawled. Contains approximately 300 000 recipes.
Scrapy files can be found in **databeer/brewtoad**.
The data is then written in csv files, which you can found in **databeer/brewtoad/csv**.

#### 1.2. beersmith.com
TBD

### 2. Structuring data
This part is still at an early phase, and most notebooks are not fully commented or 
For the time being, there are mostly sandboxes to play with the data and find ideas for further applications.
#### 2.1. utils.py
In order to lighten the notebooks, some functions are defined in *utils.py* file.
This file is also a work in progress and will be refactored in the future.
#### 2.2. Sandbox notebook
Various aggregations and other tests on the data.
#### 2.3. Hops Studies notebook
An attempt to focus on Hops data.

### 3. Machine learning applications
Steps 1 and 2 gave us some ideas about what we'd like to obtain and how we might be able to do so.
Here are some examples:
+ From the hops (defined by time, alpha and relative quantity) sequence of each recipes, train a Recurrent Neural Network (RNN)
to suggest a additional hop given a list of hops.
This might also be done with Hidden Markov Model (HMM)
+ Same as hop but for fermentables
+ Same but for full recipe (hasn't been thought of in details for know, might not be ideal)
