import argparse
import os
import shutil

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("origin_dir", help="origin_dir")
    parser.add_argument("--target_dir", help="Mac cache will be moved to this dir.")
    args = parser.parse_args()
    return args


class RemoveMacCache:

    @staticmethod
    def is_mac_cache(file_name, file_names) -> bool:
        if file_name == ".DS_Store":
            return True

        if file_name.startswith("._") and file_name[2:] in file_names:
            return True
        return False

    @staticmethod
    def remove_by_dir_path(origin_dir, target_dir):
        files_in_dir = os.listdir(origin_dir)

        for file_name in files_in_dir:
            file_path = os.path.join(origin_dir, file_name)
            if os.path.isdir(file_path):
                file_target_dir = os.path.join(target_dir, file_name)
                RemoveMacCache.remove_by_dir_path(file_path, file_target_dir)
            else:
                if RemoveMacCache.is_mac_cache(file_name, files_in_dir):
                    os.makedirs(target_dir, exist_ok=True)
                    target_path = os.path.join(target_dir, file_name)
                    shutil.move(file_path, target_path)
                    print(f"move {file_path} to {target_path}.")

if __name__ == '__main__':
    args = parse_args()
    origin_dir = args.origin_dir
    target_dir = args.target_dir
    if target_dir is None:
        target_dir = os.path.join(os.path.dirname(origin_dir), os.path.basename(origin_dir)+"_mac_cache")

    remove_mac = RemoveMacCache()
    remove_mac.remove_by_dir_path(origin_dir, target_dir)






