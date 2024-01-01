
# FileMover Module

The FileMover module provides functionality for moving and removing files and directories based on specified criteria.

## Class: FileMover

### Initialization

```python
import os
import shutil

class FileMover:
    def __init__(self, source_directory, target_directory):
        """
        Initializes a FileMover object.

        Parameters:
        - source_directory (str): The source directory path.
        - target_directory (str): The target directory path.

        Attributes:
        - num_files_moved (int): Number of files moved successfully.
        - num_files_removed (int): Number of files removed successfully.
        - num_dirs_moved (int): Number of directories moved successfully.
        - num_dirs_removed (int): Number of directories removed successfully.
        """
```

### Methods

> move_files_by_name(file_names, current_path=None)

Move files with specified names from the source to the target directory.

```python
def move_files_by_name(self, file_names, current_path=None):
    """
    Moves files with specified names from the source to the target directory.

    Parameters:
    - file_names (list): List of file names to be moved.
    - current_path (str): Current directory path (default is None).

    Returns:
    None
    """
```

> remove_files_by_name(file_names, current_path=None)

Remove files with specified names from the source directory.

```python
def remove_files_by_name(self, file_names, current_path=None):
    """
    Removes files with specified names from the source directory.

    Parameters:
    - file_names (list): List of file names to be removed.
    - current_path (str): Current directory path (default is None).

    Returns:
    None
    """
```

> remove_files_by_extension(extensions, current_path=None)

Remove files with specified extensions from the source directory.

```python
def remove_files_by_extension(self, extensions, current_path=None):
    """
    Removes files with specified extensions from the source directory.

    Parameters:
    - extensions (list): List of file extensions to be removed.
    - current_path (str): Current directory path (default is None).

    Returns:
    None
    """
```

> move_files_by_extension(extensions, current_path=None)

Move files with specified extensions from the source to the target directory.

```python
def move_files_by_extension(self, extensions, current_path=None):
    """
    Moves files with specified extensions from the source to the target directory.

    Parameters:
    - extensions (list): List of file extensions to be moved.
    - current_path (str): Current directory path (default is None).

    Returns:
    None
    """
```

> dir_move_to_dir(dir_to_move)

Moves directories with specified names from the source to the target directory.

```python
def dir_move_to_dir(self, dir_to_move):
    """
    Moves directories with specified names from the source to the target directory.

    Parameters:
    - dir_to_move (list): List of directory names to be moved.

    Returns:
    None
    """
```

> move_empty_directories()

Moves empty directories from the source to the target directory.

```python
def move_empty_directories(self):
    """
    Moves empty directories from the source to the target directory.

    Returns:
    None
    """
```

> remove_any_directories()

Removes any directories from the source directory.

```python
def remove_any_directories(self):
    """
    Removes any directories from the source directory.

    Returns:
    None
    """
```

> remove_empty_directories()

Removes empty directories from the source directory.

```python
def remove_empty_directories(self):
    """
    Removes empty directories from the source directory.

    Returns:
    None
    """
```

> get_num_files_moved()

Returns the number of files moved.

```python
def get_num_files_moved(self):
    """
    Returns the number of files moved.

    Returns:
    int: Number of files moved.
    """
```

> get_num_files_removed()

Returns the number of files removed.

```python
def get_num_files_removed(self):
    """
    Returns the number of files removed.

    Returns:
    int: Number of files removed.
    """
```

> get_num_dirs_moved()

Returns the number of directories moved.

```python
def get_num_dirs_moved(self):
    """
    Returns the number of directories moved.

    Returns:
    int: Number of directories moved.
    """
```

> get_num_dirs_removed()

Returns the number of directories removed.

```python
def get_num_dirs_removed(self):
    """
    Returns the number of directories removed.

    Returns:
    int: Number of directories removed.
    """
```

### Usage Example

```python
from FileRemover import FileMover

# URL Reset
def convert_path(input_path):
    return input_path.replace('\\', '\\\\')


source_directory_path = convert_path(input("Source DIR : "))
target_directory_path = convert_path(input("Target DIR : "))

file_names_to_move = input("Enter file names to move (separated by space): ")

fm = FileMover(source_directory_path, target_directory_path)

fm.move_files_by_name(file_names_to_move)
```
    Source DIR : C:\path\to\directory\toRemove
    Target DIR : C:\path\to\directory\targetDir

    Enter file names to move (separated by space): e.xlsx, r.rtf, w.docx, t.txt, p.pdf
---
