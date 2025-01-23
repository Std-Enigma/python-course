# Session 27 - Working with JSON

import json

# 1. JSON encoding
data = {"name": "Devil", "age": 25, "is_student": True}

json_data = json.dumps(data)
print("JSON Data:", json_data)

# 2. JSON decoding
decoded_data = json.loads(json_data)
print("Decoded Data:", decoded_data)
