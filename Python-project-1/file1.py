# Vulnerable code
user_input = input("Enter some Python code: ")
result = eval(user_input)
print(f"The result is: {result}")

# Vulnerable code
user_code = input("Enter Python code to execute: ")
exec(user_code)

import pickle

# Vulnerable code
data = input("Enter serialized data: ")
obj = pickle.loads(data)
print(obj)

import yaml

# Vulnerable code
yaml_content = input("Enter YAML content: ")
data = yaml.load(yaml_content)
print(data)