f = open(r'./data/txt/office/labeled_source_images_dslr.txt', 'r')
names = []
for line in f.readlines():
    name = line.split('/')[2]
    name = name.replace('_', ' ')
    if name not in names:
        names.append(name)

print(len(names))
print(names)