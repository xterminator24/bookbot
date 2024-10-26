def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  word_count = get_word_count(text)
  chars_dict = get_character_dict(text)
  print_report(book_path, word_count, chars_dict)

def get_book_text(path):
  with open(path) as f:
    return f.read()

def get_word_count(text):
  return len(text.split())

def get_character_dict(text):
  chars = {}
  for char in text:
    if char.lower() in chars:
      chars[char.lower()] += 1
    else:
      chars[char.lower()] = 1
  return chars

def convert_dict_to_list(dict):
  my_list = []
  for item in dict:
    list_item = {
      "character": item,
      "count": dict[item]
    }
    if list_item["character"].isalpha():
      my_list.append(list_item)
  return my_list

def sort_on(dict):
  return dict["count"]

def print_report(path, word_count, chars_dict):
  dict_list = convert_dict_to_list(chars_dict)
  dict_list.sort(reverse=True, key=sort_on)
  print(f"--- Begin report of {path} ---")
  print(f"{word_count} words found in the document")
  print()
  for char in dict_list:
    print(f"The '{char["character"]}' was found {char["count"]} times")
  print('--- End report ---')
  print()

main()