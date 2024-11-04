from pathlib import Path

contents = "I love programming."
contents += "\nI love creating new games."
contents += "\nI also love working with data."

path = Path('C:/Users/omolo/OneDrive/Desktop/CSC141/extra_practice/programming.txt')
path.write_text(contents)