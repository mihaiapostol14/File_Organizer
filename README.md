# File Organizer

A simple Python project for organizing and managing files in a directory. This tool automatically sorts files into folders by their type (based on file extension) and provides additional helper utilities for managing and cleaning up directories.

## Features

- **Organize Files by Type:** Automatically sorts files into folders named after their extensions (e.g., `pdf`, `jpg`, `txt`). Files without extensions go into a `no_extension` folder.
- **List and Sort Files:** List files in the directory, sorted by name, size, or date—ascending or descending.
- **Directory and File Utilities:** 
  - Create directories safely.
  - Create and write files from lists.
  - Remove duplicate entries from files.
  - Easily create temporary files and read their contents.
  - Random pause utility (useful for scripting or automation).
- **Extensible Helper Functions:** Modular helper class for file and directory manipulations.

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mihaiapostol14/File_Organizer.git
   cd File_Organizer
   ```
2. **Ensure Python 3.x is installed.**

3. **Install dependencies:**  
   There are no external dependencies; only the Python standard library is used.

4. **Run the organizer:**
   - Edit `main.py` and set your directory path in the example usage section.
   - Run using:
     ```bash
     python main.py
     ```

## Technologies Used

- **Language:** Python 3
- **Libraries:** 
  - `os`, `shutil`, `datetime` (standard library)
- **Structure:** 
  - Main logic in `main.py`
  - Helper utilities in `helper/helper.py`

## Extending

The code is modular and can be extended for more advanced organizing strategies or integrated into other projects.

## License

No license specified. Please contact the repository owner for usage terms.