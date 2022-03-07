import json
import os


def get_filepath(folder, file):
    return f"{folder}/{file}"

# create a main function that adds ipfs links to jsons (light formatting)


def main(folder, base_uri, extension):
    # clean the folder
    folder = os.path.abspath(folder)
    print(folder)

    # clean the extension
    extension = extension.split('.')[-1]

    # get all the items with the folder
    files = [f for f in os.listdir(
        folder) if os.path.isfile(get_filepath(folder, f))]
    print(f"Overwriting {len(files)} files")

    # iterate over all the json files
    for file in files:
        # get the filepath
        filepath = get_filepath(folder, file)

        # open each json file and read the data
        with open(filepath, 'r') as infile:
            data = json.loads(infile.read())

        # get the file id
        file_id = file.split('.')[0]

        # add the image link
        data['image'] = f"{base_uri}/{file_id}.{extension}"

        # save the json file
        with open(filepath, 'w') as outfile:
            outfile.write(json.dumps(data, indent=4))


if __name__ == '__main__':
    folder = input('Folder: ')
    base_uri = input('Base URI: ')
    extension = input('Extension: ')
    main(folder, base_uri, extension)
