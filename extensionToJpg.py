import os

def change_extension(folder_path, new_extension='.jpg'):
    #Iterate through each file in folder
    for filename in os.listdir(folder_path):
        # Check if the item is a file (not a folder)
        if os.path.isfile(os.path.join(folder_path, filename)):
            # Split the filename into root and extension parts
            root, _ = os.path.splitext(filename)
            new_filename = root + new_extension
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_filename)
            os.rename(old_path, new_path)
            print(f'Renamed: {filename} -> {new_filename}')

def count_items(folder_path):
    items = os.listdir(folder_path)
    count = len(items)
    print(f'Total extensions changed in the folder: {count}')

#FOLDER PATH HERE   
folder_path = ''
change_extension(folder_path)
count_items(folder_path)
