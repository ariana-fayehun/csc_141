favorite_languages = {
    'jen': ['python', 'rust'],
    'sara': 'c',
    'ed': ['rust', 'go'],
    'phil': ['python', 'haskell'],
    }

# language = favorite_languages['sara'].title()
# print(f"Sara's favorite language is {language}.")

for name, languages in favorite_languages.items():
    print(f"{name.title()}'s favorite languages are:")
    for language in languages:
        print(language.title())

# for name in favorite_languages.keys():
#     print(name.title())

# friends = ['phil', 'ed']
# for name in favorite_languages.keys():
#     print(f"Hi {name.title()}!")

#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}!")

# if 'erin' not in favorite_languages.keys():
#     print("Erin, please take our poll!")

# print("The following languages hav been mentioned:")
# for language in set(favorite_languages.values()):
#     print(f"{language.title()}")

