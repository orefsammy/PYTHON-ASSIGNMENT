def read_file_content(textFile):
  with open(textFile) as f:
    lines = f.read()
    return lines
    
def count_words():
  textFileInput = read_file_content('story.txt').replace('\n', ' ').split(' ')
  
  cache = {}
  for letter in textFileInput:
    if letter in cache and letter != ' ':
      cache[letter] = cache[letter]+1
    else:
      cache[letter] = 1
  print(cache)
  return cache

count_words()