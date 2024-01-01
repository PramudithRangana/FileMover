import os
import shutil


class FileMover:
    def __init__(self, source_directory, target_directory):
        self.source_directory = source_directory
        self.target_directory = target_directory

        self.num_files_moved = 0
        self.num_files_removed = 0
        self.num_dirs_moved = 0
        self.num_dirs_removed = 0

    def move_files_by_name(self, file_names, current_path=None):
        if current_path is None:
            current_path = self.source_directory

        for root, dirs, files in os.walk(current_path):
            for file in files:
                if file in file_names:
                    source_file_path = os.path.join(root, file)
                    target_file_path = os.path.join(self.target_directory, file)
                    shutil.move(source_file_path, target_file_path)

                    print(f"From {current_path} - File '{file}' moved successfully to '{self.target_directory}'.")
                    self.num_files_moved += 1

            for subdir in dirs:
                subdir_path = os.path.join(root, subdir)
                self.move_files_by_name(file_names, current_path=subdir_path)  # Recursive call to handle subdirectories

    def remove_files_by_name(self, file_names, current_path=None):
        if current_path is None:
            current_path = self.source_directory

        for root, dirs, files in os.walk(current_path):
            for file in files:
                if file in file_names:
                    file_path = os.path.join(root, file)
                    try:
                        os.remove(file_path)
                        print(f"File '{file}' removed successfully.")
                        self.num_files_removed += 1
                    except Exception as e:
                        print(f"Error removing file '{file}': {e}")

            for subdir in dirs:
                subdir_path = os.path.join(root, subdir)
                self.remove_files_by_name(file_names, current_path=subdir_path)

    def remove_files_by_extension(self, extensions, current_path=None):
        if current_path is None:
            current_path = self.source_directory

        for root, dirs, files in os.walk(current_path):

            # file removing
            for file in files:
                file_extension = os.path.splitext(file)[1]  # Get the file extension

                if file_extension in extensions:
                    file_path = os.path.join(root, file)

                    try:
                        os.remove(file_path)
                        print(f"File '{file}' with extension '{file_extension}' removed successfully.")
                        self.num_files_removed += 1
                    except Exception as e:
                        print(f"Error removing file '{file}': {e}")
                        pass

    def move_files_by_extension(self, extensions, current_path=None):
        if current_path is None:
            current_path = self.source_directory

        for root, dirs, files in os.walk(current_path):

            # file removing
            for file in files:
                file_extension = os.path.splitext(file)[1]  # Get the file extension

                if file_extension in extensions:
                    file_path = os.path.join(root, file)

                    try:
                        shutil.move(file_path, self.target_directory)
                        print(f"Directory '{file + file_extension}' moved successfully to {self.target_directory}.")
                        self.num_files_moved += 1
                    except Exception as e:
                        print(f"Error moving file '{file}': {e}")
                        pass

    def dir_move_to_dir(self, dir_to_move):
        for root, dirs, files in os.walk(self.source_directory, topdown=False):
            for dir_name in dirs:
                if dir_name in dir_to_move:
                    dir_path = os.path.join(root, dir_name)
                    target_file_path = os.path.join(self.target_directory, dir_name)
                    try:
                        shutil.move(dir_path, target_file_path)
                        print(f"Directory '{dir_name}' moved successfully to {target_file_path}.")
                        self.num_dirs_moved += 1
                    except OSError as e:
                        print(f"Error moving directory '{dir_name}': {e}")
                        pass  # Failed to remove directory, possibly not empty

    def move_empty_directories(self):
        for root, dirs, files in os.walk(self.source_directory, topdown=False):
            for dir_name in dirs:

                dir_path = os.path.join(root, dir_name)
                target_file_path = os.path.join(self.target_directory, dir_name)

                if not os.listdir(dir_path) or len(os.listdir(dir_path)) == 0:
                    try:
                        shutil.move(dir_path, target_file_path)
                        print(f"Directory '{dir_name}' removed successfully to {target_file_path}.")
                        self.num_dirs_moved += 1
                    except OSError as e:
                        print(f"Error moving directory '{dir_name}': {e}")
                        pass  # Failed to remove directory

    def remove_any_directories(self):
        for root, dirs, files in os.walk(self.source_directory, topdown=False):
            for dir_name in dirs:
                dir_path = os.path.join(root, dir_name)
                try:
                    shutil.rmtree(dir_path)
                    print(f"Directory '{dir_name}' removed successfully.")
                    self.num_dirs_removed += 1
                except OSError as e:
                    print(f"Error removing directory '{dir_name}': {e}")
                    pass  # Failed to remove directory, possibly not empty

    def remove_empty_directories(self):
        for root, dirs, files in os.walk(self.source_directory, topdown=False):
            for dir_name in dirs:

                dir_path = os.path.join(root, dir_name)

                if not os.listdir(dir_path) or len(os.listdir(dir_path)) == 0:
                    try:
                        shutil.rmtree(dir_path)
                        print(f"Directory '{dir_name}' removed successfully.")
                        self.num_dirs_removed += 1
                    except OSError as e:
                        print(f"Error removing directory '{dir_name}': {e}")
                        pass  # Failed to remove directory

    def get_num_files_moved(self):
        return self.num_files_moved

    def get_num_files_removed(self):
        return self.num_files_removed

    def get_num_dirs_moved(self):
        return self.num_dirs_moved

    def get_num_dirs_removed(self):
        return self.num_dirs_removed
