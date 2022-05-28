# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True



def find_anagrams(word, value):
  cache = {}
  value = value.replace(' ', '')
  for letter in word:
    if letter in cache and letter != ' ':
      cache[letter] = cache[letter]+1
    else:
      cache[letter] = 1

  for letter in value:
    if letter in cache:
      if cache[letter] != 0:
        cache[letter] = cache[letter] - 1
      else:
        return False
    else:
      return False
  return True

print(find_anagrams('anagram', 'nag a ram'));

