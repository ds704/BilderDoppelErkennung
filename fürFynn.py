import os
import hashlib

def file_hash(filepath):
    with open(filepath, 'rb') as f:
        return md5(f.read()).hexdigest()

os.getcwd()
os.chdir(r'/home/ds704/Downloads')
os.getcwd()
file_list = os.listdir('.')
print(len(file_list))
duplicates = []
hash_keys = dict()
for index, filename in  enumerate(os.listdir('.')):  #listdir('.') = current directory
    if os.path.isfile(filename):
        with open(filename, 'rb') as f:
            print(filename)
            filehash = hashlib.md5(f.read()).hexdigest()
        if filehash not in hash_keys:
            hash_keys[filehash] = index
        else:
            duplicates.append((index,hash_keys[filehash]))

print(duplicates)


for index in duplicates:
    os.remove(file_list[index[0]])

