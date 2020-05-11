# the list "girls" is already defined
girls_for_bryce = []
for girl in girls:
    if girl['education'] == 'MIT' and girl['about']:
        girls_for_bryce.append(girl['name'])

print(*girls_for_bryce, sep=', ')
