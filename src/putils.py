import random
import shutil
import string
from pathlib import Path


def random_string(len=8):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(len))


def mkdir(directory, parents=True, exists_ok=True):
    return Path(directory).mkdir(parents=parents, exist_ok=exists_ok)


def delete_folder(path):
    try:
        shutil.rmtree(path)
    except Exception as e:
        pass


def save_file(path, data):
    with open(path, "w") as f:
        f.write(data)


def prepare_dir(project_name):
    project_name = 'projects/' + project_name
    dir = '/home/alien/Desktop/git/spark-python/' + project_name

    dataset = dir + '/dataset'
    mkdir(dataset)

    dataset_img = dir + '/dataset/img'
    mkdir(dataset_img)

    dataset_txt = dir + '/dataset/txt'
    mkdir(dataset_txt)

    output = dir + '/output'
    mkdir(output)

    logs = dir + '/logs/txt'
    mkdir(logs)

    return dataset_img, dataset_txt, output, logs


def pretty_print(stream):
    pass