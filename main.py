import os
import shutil
from datetime import datetime
from helper import Helper



class FileOrganizer(Helper):
    """
    A class for sorting and organizing files in a directory.
    """

    def __init__(self, path_dir: str = ''):
        self.path_dir = path_dir or os.getcwd()

    def list_files(self, sort_by: str = "name", reverse: bool = False):
        """
        List and sort files in the directory.

        :param sort_by: 'name', 'size', or 'date'
        :param reverse: If True, sort in descending order
        :return: List of (filename, size, modified_date)
        """
        try:
            files = [
                (f, os.path.getsize(os.path.join(self.path_dir, f)),
                 datetime.fromtimestamp(os.path.getmtime(os.path.join(self.path_dir, f))))
                for f in os.listdir(self.path_dir)
                if os.path.isfile(os.path.join(self.path_dir, f))
            ]

            if sort_by == "size":
                files.sort(key=lambda x: x[1], reverse=reverse)
            elif sort_by == "date":
                files.sort(key=lambda x: x[2], reverse=reverse)
            else:
                files.sort(key=lambda x: x[0].lower(), reverse=reverse)

            return files

        except FileNotFoundError:
            print(f"Directory '{self.path_dir}' not found.")
            return []

    def organize_by_type(self):
        """
        Organize files into folders by file type (extension).
        """
        for filename in os.listdir(self.path_dir):
            file_path = os.path.join(self.path_dir, filename)

            if os.path.isfile(file_path):
                ext = os.path.splitext(filename)[1][1:].lower() or "no_extension"
                folder_path = os.path.join(self.path_dir, ext)

                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                shutil.move(file_path, os.path.join(folder_path, filename))
                print(f"Moved: {filename} ➜ {ext}/")


# Example usage
if __name__ == "__main__":
    fs = FileOrganizer("your_directory_path_here")  # Replace with your path

    print("\nBefore organizing:")
    for name, size, date in fs.list_files(sort_by="name"):
        print(f"{name} - {size} bytes - {date}")

    print("\nOrganizing files by type...\n")
    fs.organize_by_type()

    print("\nAfter organizing:")
    for folder in os.listdir(fs.path_dir):
        folder_path = os.path.join(fs.path_dir, folder)
        if os.path.isdir(folder_path):
            print(f"\nFolder: {folder}")
            for file in os.listdir(folder_path):
                print(f" - {file}")
