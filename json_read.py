import json

def input_json(input_filename):
    in_file = open(input_filename, 'r')
    new_var = json.load(in_file)
    in_file.close()
    return new_var

if __name__ == "__main__":
    x = input_json('patient.json')
    print(x['First Name'])
