from pathlib import Path
import json

numbers = [2, 3, 4, 5, 7, 11, 13]

path = Path('C:/Users/omolo/OneDrive/Desktop/CSC141/10_files_and_exceptions/numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)