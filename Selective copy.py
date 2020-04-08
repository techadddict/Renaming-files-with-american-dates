"""
Write a program that walks through a folder tree and searches for files with
a certain file extension (such as .pdf or .jpg).
Copy these files from whatever location they are in to a new folder.

os.walk()
returns
1. A string of the current folder’s name
2. A list of strings of the folders in the current folder
3. A list of strings of the files in the current folder

"""
import os
import shutil
os.chdir(path_to_folder)

base_paths=[]
for folderName, subfolders, filenames in os.walk(path_to_folder):
         for path in folderName.split():

             for file in filenames:
                 extension=path+'/'+file

                 if ( file.endswith('.jpg') or file.endswith('.pdf')):

                    try:

                        shutil.copy(extension,'path_to_folder/Copied_files')

                    except Exception as e:

                            pass




