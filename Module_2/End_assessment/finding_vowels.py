'''text=input()
count_vowel=0
vowels=[]
for char in text:
  if char in 'aeiouAEIOU':
    count_vowel=count_vowel+1
    vowels.append(char)
print(count_vowel,vowels)'''

def vowel_count(text):
  count_vowel=0
  vowels=[]
  for char in text:
    if char in 'aeiouAEIOU':
      count_vowel=count_vowel+1
      vowels.append(char)
  return count_vowel,vowels

text=input()
output=vowel_count(text)
print(output[0],output[1])