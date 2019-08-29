favourite_languages = {
    'jen':    'python',
    'sarah':  'c',
    'edward': 'ruby',
    'phil':   'python',
}

for name, language in favourite_languages.items():
    print (name.title() + "'s favourite language is " +
    language.title() + ".")

print ("\nThe people who took the poll are:")

for name in favourite_languages:#.keys():
    print (name.title())

for name in sorted (favourite_languages):
    print (name.title() + ", thank you for taking hte poll.")

print ("\nAll the languages (with repeats) in poll are:")

for language in favourite_languages.values():
    print (language.title())

print ("\nAll the languages in poll are:")

for language in set (favourite_languages.values()):
    print (language.title())
