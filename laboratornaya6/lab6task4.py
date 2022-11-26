import json

INPUT_FILE = "input.csv"

def csv_to_list_dict(filename, delimeter=',',new_line='\n') -> list[dict]:
    with open(filename) as f:
        newf = []
        for index, line in enumerate(f):
            str_i = line.strip(new_line).split(delimeter)
            if index == 0:
                heads = str_i
                continue
            newf.append({})
            for i, _ in enumerate(heads):
                newf[-1][heads[i]] = str_i[i]
    return newf

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
