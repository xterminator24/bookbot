def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  word_count = get_word_count(text)
  chars_dict = get_character_dict(text)
  print(f"words: {word_count}")
  print(f"chars: {chars_dict}")

def get_book_text(path):
  with open(path) as f:
    return f.read()

def get_word_count(text):
  return len(text.split())

def get_character_dict(text):
  chars = {}
  for char in text:
    if char in chars:
      chars[char] += 1
    else:
      chars[char] = 1
  return chars

main()