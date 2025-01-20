import re
name="prasanth@gopalakrishnan!"
name1="Prasanth123Gopala887"
name2="hello how are you Aswath!! well i am good"


def find_spl_char(data):
    reg_exp=re.findall(r'[^a-zA-Z0-9]',data)
    new_char=''.join(reg_exp)
    return new_char

def find_no(data):
    reg_exp=re.findall(r'[0-9]',data)
    new_int=''.join(reg_exp)
    return new_int

def find_char(data):
    reg_exp=re.findall(r'[a-zA-Z]',data)
    new_str=''.join(reg_exp)
    return new_str

def find_4_digit_char(data):
    reg_exp=re.findall(r'\b\w{4}\b',data)
    new_str=' '.join(reg_exp)
    return new_str

def find_vowels(data):
    reg_ex=re.findall(r'[aeiouAEIOU]',data)
    new_str=''.join(reg_ex)
    return new_str


print(find_spl_char(name))
print(find_no(name1))
print(find_char(name1))
print(find_4_digit_char(name2))
print("vowels----",find_vowels(name1))