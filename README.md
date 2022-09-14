# Prompt-Engineering-LLMs
## Prompt Engineering: In-context learning with GPT-3 and other Large Language Models

A client has a system that collects news artifacts from web pages, tweets, facebook posts, etc. The client is interested in scoring a given new artifact against a topic. The client has hired experts to score a few of these news items in the range from 0 to 10; a score of 0 means the news item is totally NOT relevant while a score of 10 means the news item is very relevant. The range of results between 0 and 10 signifies the  degree of relevance of the news item to the topic. 
The client wants to explore how useful existing LLMs such as GPT-3 are for this task.I am are hired as a consultant to explore the efficiency of GPT3-like LLMs to this task. If my recommendation is positive, I must demonstrate that my strategies to design prompts are reproducible and produce a consistent result. 

The data we’re going to use for this project can be found at 
[Client-data](https://docs.google.com/spreadsheets/d/19N_K6SnIm0FylD2TBs-5y3WeSgdveb3J/edit?usp=sharing&ouid=108085860825615283789&rtpof=true&sd=true) , [Job-description-1](https://github.com/walidamamou/relation_extraction_transformer/blob/main/relations_dev.txt) and [Job-description-2](https://github.com/walidamamou/relation_extraction_transformer/blob/main/relations_test.txt)

## Prompt Engineering: In-context learning with GPT-3 and other Large Language Models

<!-- Table of contents -->
- [Prompt-Engineering-LLMs](#Prompt-Engineering-LLMs)
  - [About](#about)
  - [Objectives](#objectives)
  - [Data](#data)
  - [Requirements](#requirements)
  - [Contrbutors](#contrbutors)

## About
Large Language Models coupled with multiple AI capabilities are able to generate images and text, and also approach/achieve human level performance on a number of tasks.  The world is going through a revolution in art (DALL-E, MidJourney, Imagine, etc.), science (AlphaFold), medicine, and other key areas, and this approach is playing a role in this revolution.
 
In-context learning, popularized by the team behind the GPT-3 LLM, brought a new revolution for using LLMs in many tasks that the LLM was not originally not trained for. This stands in contrast to the usual fine-tuning that used to be required to equip AI models to improve performance in tasks they were not trained for.

## Objectives
The analysis objective of this project are divided into 4 sub-objectives that overall guides the workflow
-Setting up environment to use LLMs APIs 
-Comparing word-embedding based clustering with prompt based classification 
-Setting up repeatable ML framework for prompt engineering - Reporting and Dashboard

## Data
The following is the description of the components of the [Client-data]
-**Domain** - the base URL or a reference to the source these item comes from 
-**Title** - title of the item - the content of the item
-**Description** - the content of the item
-**Body** - the content of the item
-**Link** - URL to the item source (it may not functional anymore sometime)
-**Timestamp** - timestamp that this item was collected at
-**Analyst_Average_Score** -  target variable - the score to be estimated 
-**Analyst_Rank** - score as rank
-**Reference_Final_Score** - Not relevant for now - it is a transformed quantity

## Requirements
The project requires the following:
python3
Pip3

## Contrbutors
- Michael Getachew

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.