def find_duplicates(string):
    duplicates = []
    for char in string:
        if string.count(char) > 1 and char not in duplicates:
           duplicates.append(char)
    return duplicates

def count_duplicates(string):
    duplicates = {}
    for char in string:
        if string.count(char) > 1 and char not in duplicates:
            duplicates[char] = string.count(char)
    return duplicates

print(find_duplicates("prasanth gopalakrishnan"))
print(count_duplicates("prasanth gopalakrishnan"))