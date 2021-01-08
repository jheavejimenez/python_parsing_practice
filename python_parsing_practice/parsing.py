import json


with open("practice.json", "r") as read_file:
    data = json.load(read_file)


'#1. How many Linux OS are there?'


def to_string(item):
    return ', ' .join(map(str, item))


def how_many(data):
    linux = []
    for os in data:
        if os['Name']:
            try:
                linux.append(os["Name"])
            except KeyError:
                print('None')
    return (
            f'There are {len(linux)} Linux OS in '
            f'the list and there names are {to_string(linux)}'
        )
print(how_many(data))


'#2. How many have Kernel versions >= 4.5?'


def Kernel_version(data):
    linux = []
    for os in data:
        if os["Kernel"] >= '4.5':
            try:
                linux.append(os["Name"])
            except KeyError:
                print("there are no 4.5 version in the list")
    return (
            f'There are {len(linux)} Linux OS '
            f'that is >= 4.5 and there names are {to_string(linux)}'
        )
print(Kernel_version(data))


'#3. How many are not in their Rolling Release version?'


def release_version(data):
    linux = []
    for os in data:
        if os["Version"] != 'Rolling Release':
            try:
                linux.append(os["Name"])
            except KeyError:
                print("None")
    return (
        f'There are {len(linux)} Linux OS That are not in '
        f'their Rolling Release version '
        f'and there names are {to_string(linux)}')
print((release_version(data)))
