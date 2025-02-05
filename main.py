def main():
    file = "/root/workspace/github.com/ctcastle/bookbot/books/frankenstein.txt"
    file_contents = read_file(file)

    print_report(file_contents, file)

def read_file(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents

def get_wc(file_contents):
    return len(file_contents.split())

def get_character_count(file_contents):
    file_contents = file_contents.lower()
    character_dict = {}
    for c in file_contents:
        if c in character_dict:
            character_dict[c] += 1
        else: 
            character_dict[c] = 1
    return character_dict

def print_report(file_contents, file):
    print(f"--- Begin report of {file} ---")
    print(f"{get_wc(file_contents)} words found in the document")
    print("")
    character_dict = get_character_count(file_contents)
    for key in character_dict:
        if key.isalpha():
            print(f"The '{key}' character was found {character_dict[key]} times")
    print("--- End report ---")

main()