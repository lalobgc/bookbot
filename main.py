file_path = "books/frankenstein.txt"

def main():
    txt_book = read_file(file_path)
    num_words = count_words(txt_book)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    chars_dict = count_chars(txt_book)
    print_report(chars_dict)

def read_file(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def count_words(txt_file):
    splitted_file = txt_file.split()
    return len(splitted_file)

def count_chars(txt_file):
    counts = {}
    lower_case_text = txt_file.lower()
    for char in lower_case_text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def convert_dict(dict):
    lst_dict = []
    for key, value in dict.items():
        if key.isalpha():
            lst_dict.append({"char": key, "num": value})
    def sort_on(dict):
        return dict["num"]
    lst_dict.sort(reverse=True, key=sort_on)
    return lst_dict

def print_report(dict):
    listed = convert_dict(dict)
    for i in range(len(listed)):
        print(f"The '{listed[i]["char"]}' character was found {listed[i]["num"]} times")

main()