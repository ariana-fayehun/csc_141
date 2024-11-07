from pathlib import Path
import json


path = Path('C:/Users/omolo/OneDrive/Desktop/CSC141/10_files_and_exceptions/numbers.json')
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)