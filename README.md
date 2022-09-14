# Prompt-Engineering-LLMs
## Prompt Engineering: In-context learning with GPT-3 and other Large Language Models

A client has a system that collects news artifacts from web pages, tweets, facebook posts, etc. The client is interested in scoring a given new artifact against a topic. The client has hired experts to score a few of these news items in the range from 0 to 10; a score of 0 means the news item is totally NOT relevant while a score of 10 means the news item is very relevant. The range of results between 0 and 10 signifies the  degree of relevance of the news item to the topic. 
The client wants to explore how useful existing LLMs such as GPT-3 are for this task.I am are hired as a consultant to explore the efficiency of GPT3-like LLMs to this task. If my recommendation is positive, I must demonstrate that my strategies to design prompts are reproducible and produce a consistent result. 

The data we’re going to use for this project can be found at 
[Client-data](https://docs.google.com/spreadsheets/d/19N_K6SnIm0FylD2TBs-5y3WeSgdveb3J/edit?usp=sharing&ouid=108085860825615283789&rtpof=true&sd=true) , [Job-description-1](https://github.com/walidamamou/relation_extraction_transformer/blob/main/relations_dev.txt) and [Job-description-2](https://github.com/walidamamou/relation_extraction_transformer/blob/main/relations_test.txt)