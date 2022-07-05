# Colonoscopy
#The primary code is in solutions, which calls for the other scripts. 
The database is claims.db located here:
https://drive.google.com/file/d/1-HRWmdRpQQGE_CrmRo75GklAWVHFPKWx/view?usp=sharing

Original instructions for the code are below:

Your task is to create a scalable/extensible system in Python that translates a medical rule into a performant task (query, pipeline, etc) that traverses a database and returns insights about doctor performance. Your tool(s) should output the historical performance (violation rate) of each doctor, showing how many opportunities a doctor had to follow the rule (the denominator), and how many times they violated the rule (numerator). Whatever you build should also be able to handle similar problems such that a change to the rule (e.g. a new set of diagnosis codes) could be easily implemented. Your solution should be a zipped directory containing the .py file(s) where your function(s) and/or constructor(s) reside, as well as a .py script or .ipynb notebook titled "solution" where you demonstrate how to use your tools.

A good solution meets the following criteria: 
Has a notebook/script that calls your function(s) or constructor(s) to produce results
Has a notebook that analyzes the results 
Has a .py source file (or files) that contains only your function(s) or constructor(s) that are used in the notebook/script.
Runs without errors or user input. 
Has the ability to handle a slightly different rule set.
Is easily understandable and follows modern best practices.
Is easily extensible.
Clearly abstracts the salient features of the problem.
Predicts a doctor’s future performance based on the historical data.
