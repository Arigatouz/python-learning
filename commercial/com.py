import json
import re as regular
file_name = "messages.txt"
json_file = "commercial.json"

# commercial.json
# with open(file_name) as f:
#     lines = [l.strip() for l in f.readlines()]
#     for line in lines:
#         if line.startswith('Total Number of Direction(s)'):
#             counter += 1
#             data[counter] = ''
#             # data[counter] = line -- if you wanna
#         else:
#             data[counter] += line
# for k, v in data.items():
#     print(f'{k} --> {v}').


def read_file(file):
    counter = 0
    data = {}
    with open(file, 'r') as messages_file:
        lines = [line.strip() for line in messages_file.readlines()]
        for line in lines:
            if line.startswith('Total Number of Direction(s)'):
                counter += 1
                data[counter] = line
            else:
                data[counter] += line
        return data


def finding_non_commercial():
    collected_data = read_file(file_name)
    n = 0
    for key, value in collected_data.items():

        regex = regular.compile(
            r'\d\d\d\d\d\d\s\D\D\D\D\D\D\D\D\(')
        # regex2 = regular.compile(r'')

        out = [m.group() for m in regex.finditer(value)]
        if len(out) != 0:
            continue
        else:
            print(key)


finding_non_commercial()


# def write_data_as_json(file):
#     with open(file, 'w') as json_file:
#         json.dump(read_file(file_name), json_file)


# write_data_as_json(json_file)
