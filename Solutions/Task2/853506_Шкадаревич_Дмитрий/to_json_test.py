import unittest
import json
from to_json import to_json, Person


class JsonTestCase(unittest.TestCase):
    def test_json(self):
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
        person = Person("Dima", 25)
        self.assertEqual(to_json(person),json.dumps(person.__dict__))
        self.assertEqual(to_json(data), json.dumps(data))


unittest.main()
