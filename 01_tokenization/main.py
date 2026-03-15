import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o") # defining model used for encoding

text = "Hey there! My name is Vishwas" # text sent as input tokens
tokens = enc.encode(text) # defifing which to endcode
print(tokens) # [25216, 1354, 0, 3673, 1308, 382, 119951, 9844]

tokens_decoded = enc.decode(tokens)
print(tokens_decoded) # Hey there! My name is Vishwas