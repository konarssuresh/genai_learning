import tiktoken


enc = tiktoken.encoding_for_model("gpt-4o")

text = 'hey there my name is suresh konarssss'

tokens = enc.encode(text)

print("Tokens ",tokens)


print("Decoded",enc.decode(tokens))