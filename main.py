import os

list_files=os.listdir('files')
save_in_one_file = {}

for i in list_files:
    dir = os.getcwd() + '''\\files'''
    open_i = os.path.join(dir,i)
    itog_files = 'itog.txt'
    dir_itog = os.getcwd() + '''\\itog'''
    open_write = os.path.join(dir_itog,itog_files)

    a=0
    with open(open_i, 'r', encoding='utf-8') as j:
        for line in j:
            if line.strip():
                a +=1
        save_in_one_file[a]=''
        save_in_one_file[a]=i
        list_keys = list(save_in_one_file.keys())
        list_keys.sort()
        with open(open_write, 'w', encoding='utf-8') as files_write:
            for i in list_keys:
                print(i, ':', save_in_one_file[i])
                name_files = str(save_in_one_file[i])
                files_write.write(name_files)
                files_write.write('\n')
                files_write.write(str(i))
                files_write.write('\n')
                with open(os.path.join(dir,name_files), 'r', encoding='utf-8') as f:
                    text = f.read()
                    files_write.write(text)
                    files_write.write('\n')
                f.close()
print(save_in_one_file)
print(list_keys)
