import time
import os
import shutil

def main():
     deleted_folders_count=0
     deleted_files_count=0

     pathvar='C:\Users\NETRA PRAKASH\Documents\Coding\TestFolder'

     days=30
     seconds=time.time()-(days*24*60*60)
     if os.path.exists(pathvar):
         for root_folder, folders, files in os.walk(pathvar):
             if seconds>=get_file_or_folder_age(root_folder):
                 remove_folder(root_folder)
                 deleted_folders_count+=1
                 break
             else:
                 for folder in folders:
                     folderpath=os.path.join(root_folder, folder)   
                     if seconds>=get_file_or_folder_age(folderpath):
                         remove_folder(folderpath)
                         deleted_folders_count+=1
                 for file in files:
                     filepath=os.path.join(root_folder, file)   
                     if seconds>=get_file_or_folder_age(filepath):
                         remove_file(filepath)
                         deleted_files_count+=1
                     else:
                          if seconds>=get_file_or_folder_age(pathvar):
                             remove_file(filepath)
                             deleted_files_count+=1

def remove_folder(pathvar):
    if not shutil.rmtree(pathvar):
        print('This file has been removed.')
    else:
        print('Unable to delete.')    
def remove_file(pathvar):
    if not os.remove(pathvar):
         print('This file has been removed.')
    else:
        print('Unable to delete.')
def get_file_or_folder_age(pathvar):
    ctime=os.stat(pathvar).st_ctime
    return ctime

main()



