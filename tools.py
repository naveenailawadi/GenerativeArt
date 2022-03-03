import json
import pandas as pd
import random


# class for handling a bunch of traits
class TraitGroupHandler:
    def __init__(self, folder, trait_csv):
        # save the folder name
        self.folder = folder

        # open the trait csv
        self.df = pd.read_csv(trait_csv)

    # get the traits --> export as a dict
    @property
    def traits(self):
        traits = self.df.to_dict(orient='records')

        return traits

    # get the length
    def __len__(self):
        return len(self.df)


# class to handle merging jpegs
class FileMerger:
    def __init__(self, directory, config_file='config.json'):
        # load the config
        with open(config_file, 'r') as infile:
            self.data = infile.read()

        # make trait groups
        self.trait_groups = [TraitGroupHandler(
            trait_group['folder'], trait_group['csv']) for trait_group in self.data['trait_groups']]

    # make a property to calculate the number of combinationations
    @property
    def combinations(self):
        combination_count = 1

        # iterate over the group and multiply the new combinations
        for group in self.trait_groups:
            combination_count *= len(group)

        return combination_count
