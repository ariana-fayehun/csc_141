from pathlib import Path

path = Path('C:/Users/omolo/OneDrive/Desktop/CSC141/extra_practice/pi_digits.txt')
contents = path.read_text()


lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line

print(pi_string)
print(len(pi_string))
