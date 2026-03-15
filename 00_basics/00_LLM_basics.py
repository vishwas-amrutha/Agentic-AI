"""
how llm works

what user gives as input is called as input tokens
what we get as output is output tokens

gpt -> generative pre-trained transformer

the transoformer architecture came from google translate tranformer
where it would take sequence input and generate output sequence

here gpt takes input tokens and as output it predicts the next token

ex --> we give hey there as input 
it generates one token at a time
generates I
again takes hey there I as input and generates am
again takes hey there I am as imput and generates good.
then responds with I am good.
then stops, this i show it predicts

ie y llm models require high GPU

tokens-> the characters that humans use are mapped to some numbers called tokens as computer only understands numbers
token system varies from model to model, ie tokens from gpt is diff from claude, diff from gemini and even
gpt 3.5 token system is diff from gpt 4

tokenization -> converting the user input to set of numbers understandable by llms

as gpt predicts the next tokens and serve them as input for predicting next tokens
at last after the end, the predicted tokens are then de tokenized to human language








"""