import os
import random
import shutil
import argparse
import time

def copy_random_files(src_dir, dst_dir, num_files):
    # Get a list of all files in the source directory
    all_files = os.listdir(src_dir)

    # Randomly select num_files files from the list
    random_files = random.sample(all_files, num_files)

    # Copy the selected files to the destination directory
    for i,file_name in enumerate(random_files):
        src_path = os.path.join(src_dir, file_name)
        dst_path = os.path.join(dst_dir, file_name)
        print(f'{i+1}/{len(random_files)}')
        print(f'scr_path: {src_path}')
        print(f'dst_path: {dst_path}')
        print('-----------------------------------')
        shutil.copy(src_path, dst_path)
        time.sleep(60*2.5)
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('num_files', type=int, help='number of files to copy')
    # parser.add_argument('src_dir', type=str, help='source directory')
    # parser.add_argument('dst_dir', type=str, help='destination directory')
    args = parser.parse_args()

    src_dir = "your source path"
    dst_dir = "your desribution path"

    copy_random_files(src_dir, dst_dir, args.num_files)
