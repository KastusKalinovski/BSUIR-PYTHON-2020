import json


def to_json(obj):
    if type(obj) is bool:
        return "true" if obj is True else "false"
    elif isinstance(obj, (int, float)):
        return str(obj)
    elif isinstance(obj, str):
        return '"' + obj + '"'
    elif obj is None:
        return "null"
    elif isinstance(obj, (tuple, set, list)):
        result = ", ".join(to_json(element) for element in obj)
        return "[" + result + "]"
    elif isinstance(obj, dict):
        pairs = []
        for key, value in obj.items():
            if isinstance(key, (int, float, bool)) or key is None:
                pairs.append("\"" + to_json(key) + "\": " + to_json(value))
            else:
                pairs.append(to_json(key) + ": " + to_json(value))
        result = ", ".join(pair for pair in pairs)
        return "{" + result + "}"
    elif isinstance(obj, object):
        temp_dict = obj.__dict__
        return to_json(temp_dict)
    else:
        raise TypeError("Object of type " + str(type(obj)) + " is not JSON serializable")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == "__main__":
    data = {
        "firstName": "Jane",
        "lastName": "Doe",
        "hobbies": ["running", "sky diving", "singing"],
        "age": 35,
        "children": [
            {
                "firstName": "Alice",
                "age": 6
            },
            {
                "firstName": "Bob",
                "age": 8
            }
        ]
    }

    print(to_json(data))
    print(json.dumps(data))


