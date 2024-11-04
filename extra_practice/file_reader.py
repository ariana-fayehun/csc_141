from pathlib import Path

path = Path('C:/Users/omolo/OneDrive/Desktop/CSC141/extra_practice/pi_digits.txt')
contents = path.read_text()


lines = contents.splitlines()
for line in lines:
    print(line)

