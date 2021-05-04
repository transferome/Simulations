"""Clear files except the package contents from the folder"""
import os
import glob
import shutil


def clean():
    files_keep = glob.glob('*.py')
    folders = [s for s in os.listdir() if os.path.isdir(s) and '.' not in s]
    for folder in folders:
        file_list = glob.glob('{}/*'.format(folder))
        init_true = 0
        for f in file_list:
            if 'fstsimulate.py' in f:
                init_true += 1
        if not init_true:
            shutil.rmtree(folder)
    files = [s for s in os.listdir() if os.path.isfile(s) and not s.startswith('.')]
    files_delete = [s for s in files if s not in files_keep]
    for g in files_delete:
        os.remove(g)


if __name__ == '__main__':
    clean()
