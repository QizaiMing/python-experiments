import sys
import os

# Execute it doing
# python archivos_repetidos.py FOLDER_NAME

# Example:
# python archivos_repetidos.py testing
# will scan a folder in the current directory named 'testing'

if sys.argv[1]:
    folder = sys.argv[1]

    file_list = []
    content_list = []
    duplicate_files = []
    size_list = []

    print(f"Scanning: {sys.argv[1]}")

    # gets all the files inside the folder and their dirpaths
    print("*** Starting traversing folder *** \n")
    for dirpath, dirnames, files in os.walk(folder):
        print(f"Found directory: {dirpath}")
        for file_name in files:
            print(file_name)
            print(dirpath)
            file_list.append({"name": file_name, "dirpath": dirpath})

    print("\n*** Finished traversing folder *** \n")

    for file in file_list:
        name = file["name"]
        dirpath = file["dirpath"]
        relative_path = f"{dirpath}/{name}"
        f = open(relative_path, "r")
        content = f.read()
        size = os.path.getsize(relative_path)
        content_list.append(
            {"name": name, "dirpath": dirpath, "content": content, "size": size}
        )

    for content in content_list:
        temp_list = []
        file_content = content["content"]

        for content2 in content_list:
            if file_content == content2["content"]:
                temp_list.append(content)

        if len(temp_list) > 1:
            duplicate_files.append(content)

    print(f"Duplicated Files: {len(duplicate_files)}")
    for file in duplicate_files:
        dirpath = file["dirpath"]
        name = file["name"]
        size = file["size"]
        text = f"{dirpath}/{name} {size} Bytes"
        print(text)
        size_list.append(size)

    print(f"Total size: {sum(size_list)} Bytes")

else:
    print("ingresa el nombre de la carpeta a escanear")
