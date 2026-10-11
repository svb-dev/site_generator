import os
import shutil


def copy_static(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)

    os.mkdir(destination)
    copy_items(source, destination)


def copy_items(source, destination):
    for item in os.listdir(source):
        static_path = os.path.join(source, item)
        public_path = os.path.join(destination, item)

        if os.path.isfile(static_path):
            shutil.copy(static_path, public_path)

        else:
            os.mkdir(public_path)
            copy_items(static_path, public_path)
