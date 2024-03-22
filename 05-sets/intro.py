subjects = [
    {"name":"Artificial Intelligence","duration":"4 months"},
    {"name":"Deep learning","duration":"4 months"},
    {"name":"Machine learning","duration":"3 months"},
    {"name":"Mathematics","duration":"6 months"},
    {"name":"Machine learning","duration":"3 months"},
    {"name":"Mathematics","duration":"6 months"},
    {"name":"Programming","duration":"4 months"}
    ]

new_subjects = list()
count = 0
for subject in subjects:
    if subject["name"] not in new_subjects:
        new_subjects.append(subject["name"])
        count = count + 1
         
print(count)
for subject in new_subjects:
    print(subject)
        