text=input()
count_vowel=0
vowels=[]
for char in text:
  if char in 'aeiouAEIOU':
    count_vowel=count_vowel+1
    vowels.append(char)
print(count_vowel,vowels)