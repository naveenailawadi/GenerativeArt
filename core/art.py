from PIL import Image


# set the folders for export
METADATA_FOLDER = 'metadata'
FILE_FOLDER = 'files'


# a class for one piece of art (good for storing data, as you can pass an entire trait into it)
class Art:
    def __init__(self, trait_dict):
        # keep all the trait dicts in a list (starting with the one passed)
        self.traits = [trait_dict]

        # open the full path
        self.image = Image.open(trait_dict['full_path'])
        print(f"Opened {trait_dict}")

    # paste a new trait dict onto the existing traits
    def paste(self, new_trait_dict):
        # append the trait dict to the list
        self.traits.append(new_trait_dict)

        # paste the new trait on the base
        new_image = Image.open(new_trait_dict['full_path'])
        self.image.paste(new_image, (0, 0), new_image)

    # export the data
    def export(self, art_name, folder, filename, art_extension, extra_traits=[], art_metadata=None):
        # make a filepath
        filepath = f"{folder}/{FILE_FOLDER}/{filename}.{art_extension}"

        # save the image
        self.image.save(filepath)

        # get the metadata and export it if necessary
        if not art_metadata:
            art_metadata = self.metadata

            # set the art name of the metadata
            art_metadata['name'] = art_name

            # extend the traits to include the extra traits
            art_metadata['attributes'] = extra_traits + \
                art_metadata['attributes']

            # export the metadata
            with open(f"{folder}/{METADATA_FOLDER}/{filename}", 'w') as outfile:
                outfile.write(json.dumps(art_metadata, indent=4))

    # function to create trait metadata
    def create_trait_metadata(self, trait):
        trait_metadata = {
            'trait_type': trait['trait_type'],
            'value': trait['trait_name']
        }

        return trait_metadata

    # function to create trait files
    def create_trait_filedata(self, trait):
        trait_filedata = {
            'trait_type': trait['trait_type'],
            'file': f"{trait['trait_type']}/{trait['file']}"
        }

        return trait_filedata

    # export all the trait's information (in opensea format)
    @property
    def metadata(self):
        metadata_dict = {
            "name": "",
            "image": "",
            # create from the trait data
            "attributes": [self.create_trait_metadata(trait) for trait in self.traits],
            # backwards link it for reproducability, also would be cool to link these to IPFS
            "trait_files": [self.create_trait_filedata(trait) for trait in self.traits]
        }

        return metadata_dict
