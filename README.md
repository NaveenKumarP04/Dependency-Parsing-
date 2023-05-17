
# Dependency Parsing with Stanford Parser

This repository contains code examples for performing dependency parsing using the Stanford Parser in Python. The Stanford Parser is a widely used natural language processing tool that provides high-quality dependency parsing for English sentences.
And the code in this repository gives the dependency relations and sequence of steps to produce the dependency relation by sing arc-standard algorithm

## Features

Here,for the input sentence given by the user will have output containing **DEPENDENCY TRIPLES**  , **PARSE TREE** and **SEQUENCE OF STEPS** to produce the dependency relations by **ARC-STANDARD ALGORITHM**.
+ **Parse Tree:** This will be in CONLL format containing 4 fields.In this, there  will be have four coloums containing **Word,POS(Parts of speech),Head Index,Dependency Relation** 
+ **Dependnecy Triples:** This will have 3 entities which **Head node , Dependency relation ,Dependent node.
+ **Sequence of steps:** In this,**Arc-Standard algorithm** followed and we will show the words in each step like what will contain in the stack and buffer.And the action performed in the each step(LEFT ARC/RIGHT ARC/SHIFT) and the relation added in the each step.


## Prerequisites

To run the code examples, you need to have the following installed:

- Natural language tool kit(NLTK)
- Stanford Parser library
- Python 3.X
- Tkinter(for GUI)

## Setup

1. Download the Stanford Parser library from the official website: [Stanford Parser](https://nlp.stanford.edu/software/lex-parser.shtml)

2. Extract the downloaded file to a directory on your machine.
3. You need to follow the commands given in the official website  to set up the Standford parser in your Computer. 
4. Start the Stanford CoreNLP server by running the following command in the terminal:


```
java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -port 9000 -timeout 15000
```
## Usage

1. Clone the repository:
```
git clone https://github.com/NaveenKumarP04/Dependency-Parsing.git
````
2. Navigate to the project directory:
```
cd Dependency-Parsing
```
3. Run the navgui.py file:
```
python navgui.py
```
4. Enter the sentence and Click "Parse" button to get the output.

## Licence


Please note that the above example assumes you have downloaded and set up the Stanford Parser correctly and have NLTK installed. Adjust the paths and dependencies according to your specific setup.








