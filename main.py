import random
import string

def generate_random_string(length):
  chars = string.ascii_lowercase
  random_string = ''.join(random.choice(chars) for i in range(length))
  return random_string

def hyphen_split(string, chunkLenght):
  splitted = '-'.join([string[i:i+chunkLenght] for i in range(0, len(string), chunkLenght)])
  return splitted

result = generate_random_string(9)
print(result)

chunked = hyphen_split(result, 3)
print(chunked)
