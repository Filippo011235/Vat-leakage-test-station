"""Module containing class that handles tests' results files, and their data.

Classes:
    TestDataHandler
"""

import matplotlib.pyplot as plt
from os import path, listdir, remove
import csv

from text_data import TEST_FILE_CODE, RESULTS_SAVE_DIR

class TestDataHandler():
    """Handle test data, saved as csv files, and extract information from them.

    Attributes:
        # tests_dir (str): Path to directory where .csv files are saved.
        # tests_list (list): Stores conductated tests, as dictionaries with 
                            information un-coded from the filenames.
    """

    def __init__(self, tests_results_dir=RESULTS_SAVE_DIR) -> None:
        """Init. with path to the directory with files, and list to hold data.

        Args:
            tests_results_dir (str) : Path to directory where .csv files are saved.
        """
        self.tests_dir = tests_results_dir
        self.tests_list = [] # Holds each test as a dict

    def parse_test_file(self, file_name):
        """Analyse filename to extract info. about test, based on keywords."""
        test_dict = {}

        # TODO czy filename jest legit? 1) istnieje, 2) name correct?

        test_data = file_name.split("_")
        # Iterate over every second field, stop at len-1, because of file ext.
        for idx in range(0, len(test_data)-1, 2):
            # idx holds data code name and idx+1 actual value.
            test_dict[test_data[idx]] = test_data[idx+1]

        if test_dict.keys() != TEST_FILE_CODE:
            raise ValueError("Something went wrong in file naming!")

        print(test_dict) # For init debug, TODO delete

        self.tests_list.append(test_dict)

    def update_data(self):
        """After new test was conducdated update tests_list with a new file."""
        pass

    def draw_graph(self):
        """Draw graph of air pressure versus time, from data in a csv file."""
        # plt.plot(t, X)
        # plt.savefig(RESULTS_SAVE_DIR)
        pass

    # def update_data(self):
    #     pass

    def clear_dir(self):
        """Remove all test results in directory."""
        # TODO check only for .csv files
        try:
            files_list = listdir(self.tests_dir)
            for file in files_list:
                file_path = path.join(self.tests_dir, file)
                if path.isfile(file_path):
                    remove(file_path)
        except OSError:
            print("\n Error occured while deleting files.\n")
            raise OSError
