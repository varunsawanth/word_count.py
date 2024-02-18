def word_count(text):
  words = text.split()
  word_count = len(words)
  return word_count
user_text = input("Enter a text to count the words: ")
count = word_count(user_text)
print("The number of words in the text is:", count)
