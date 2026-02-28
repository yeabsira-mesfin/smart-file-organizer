import os

path = "D:\Python\MyOwnPractices\Smart File Organizer\smart-file-organizer\src\organizer.py"

folder, file_name = os.path.split(path)
base, ext = os.path.splitext(path)

print(f"""
      {folder}
      {file_name}
      """)
print(f"""
      {base}
      {ext}
      """)