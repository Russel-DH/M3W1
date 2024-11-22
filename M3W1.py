import random
count_num = 0
def count_calls():
    global count_num
    count_num += 1

def string_info(any_string):
    count_calls()
    any_string_i = []
    any_string_i.append(len(any_string))
    any_string_i.append(any_string.upper())
    any_string_i.append(any_string.lower())
    print(any_string_i)
    return

def is_contains(string, list_to_search):
    count_calls()
    for i in range(len(list_to_search)):
        if list_to_search[i] == string:
            is_true = True
            break
        else:
            is_true = False
    print(is_true)
    if is_true == 1:
        print(f'String "{string}" contains inside the [{list_to_search}]')
    else:
        print(f'String "{string}" doesnt contains inside the [{list_to_search}]')

for i in range(random.randrange(1,4)):
    string_info(input('Input some text: '))
print()
b = []
for i in range(random.randrange(1, 4)):
    is_contains(input('Input any string to search: '), input('Input any tuple: '))
print()
print(f'Count of defines: {count_num} times')