from FileRemover import FileMover


# URL Reset
def convert_path(input_path):
    return input_path.replace('\\', '\\\\')


source_directory_path = convert_path(input("Source DIR : "))
target_directory_path = convert_path(input("Target DIR : "))

file_names_to_move = input("Enter file names to move (separated by space): ")

fm = FileMover(source_directory_path, target_directory_path)

fm.move_files_by_name(file_names_to_move)
# fm.remove_files_by_name(file_names_to_move)
# fm.remove_files_by_extension(file_names_to_move)
# fm.move_files_by_extension(file_names_to_move)

# fm.dir_move_to_dir(file_names_to_move)

# fm.move_empty_directories()
# fm.remove_any_directories()
# fm.remove_empty_directories()

num_moved_files = fm.get_num_files_moved()
num_removed_files = fm.get_num_files_removed()
num_moved_dirs = fm.get_num_dirs_moved()
num_removed_dirs = fm.get_num_dirs_removed()

print("+" * 100)
print(f"Number of files moved: {num_moved_files}")
print(f"Number of files removed: {num_removed_files}")
print(f"Number of directories moved: {num_moved_dirs}")
print(f"Number of directories removed: {num_removed_dirs}")

"""
Source DIR : C:\Users\Pramudith Rangana\Documents\Python_3 Project\Additional Src\Repo (Git)\File_Remover\toRemove
Target DIR : C:\Users\Pramudith Rangana\Documents\Python_3 Project\Additional Src\Repo (Git)\File_Remover\targetDir
Enter file names to move (separated by space): e.xlsx, r.rtf, w.docx, t.txt, p.pdf
"""
