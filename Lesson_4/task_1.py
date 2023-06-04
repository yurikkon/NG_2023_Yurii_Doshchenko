import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--folder', dest="folder")
parser.add_argument('--file', dest="file")
args = parser.parse_args()
folder = args.folder
file = args.file

def search_files(folder,file):
    for file_s in os.listdir(folder):
        name = os.path.basename(file_s)
        path = os.path.join(folder , name)
        if file in name :
            print(path)


search_files(folder,file)

