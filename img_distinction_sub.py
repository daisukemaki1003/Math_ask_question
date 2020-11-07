import glob
import pandas as pd
import os
import shutil
import pathlib

csv_path = '/Users/makidaisuke/Desktop/my_pands/数学/問題集/'
csv_file = glob.glob(csv_path + '*.csv')

img_path = '/Users/makidaisuke/Desktop/my_pands/数学/問題集/pdf_image/'
img_file = glob.glob(img_path + '*.png')

print(csv_file)
i = 0
while i < len(csv_file):
    s_t = pathlib.Path(csv_file[i]).stem
    print(s_t)
    df = pd.read_csv(csv_file[i])

    for t in df.Title:
        path = (img_path + t + '.png')
        print(path)
        if os.path.isfile(path):
            shutil.move(path, csv_path + s_t + '_img')
            print(path)

    i += 1


