import os


def len_file(filename):
    with open(filename, 'r', encoding='utf8') as f:
        for i, _ in enumerate(f):
            pass
        return i + 1


script_dir = os.getcwd()
rel_path = 'Compound'
abs_files_path = os.path.join(script_dir, rel_path)
os.remove(os.path.join(abs_files_path, 'result.txt'))
str_num = {}
for file in os.listdir(abs_files_path):
    str_num[file] = len_file(os.path.join(abs_files_path, file))
sorted_couples = sorted(str_num.items(), key=lambda x: x[1])
sorted_str_num = dict(sorted_couples)

with open(os.path.join(abs_files_path, 'result.txt'), 'w', encoding='utf8') as res_file:
    for key, value in sorted_str_num.items():
        res_file.write(key + '\n' + str(value) + '\n')
        initial_file = open(os.path.join(abs_files_path, key), 'r', encoding='utf8')
        for line in initial_file:
            res_file.write(line)
        res_file.write('\n')
        initial_file.close()
