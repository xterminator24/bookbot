def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  print(f"words: {count_words(text)}")
  print(f"chars: {count_characters(text)}")

def get_book_text(path):
  with open(path) as f:
    return f.read()

def count_words(text):
  return len(text.split())

def count_characters(text):
  chars = {}
  for char in text:
    if char in chars:
      chars[char] += 1
    else:
      chars[char] = 1
  return chars

main()