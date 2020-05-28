import json


def create_person():
    bob = {"First Name": "Robert", "Last Name": "Smith"}
    return bob


def output_json(my_dict):
    filename = "patient.json"
    output_file = open(filename, 'w')
    json.dump(my_dict, output_file)
    output_file.close()


def alt_approach(my_dict):
    filename = "patient.json"
    with open(filename, 'w') as out_file:
        json.dump(my_dict, out_file)


if __name__ == "__main__":
    x = create_person()
    output_json(x)
