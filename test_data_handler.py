"""Module containing class that handles tests' results files, and their data.

Classes:
    TestDataHandler
"""

import matplotlib.pyplot as plt
from os import path, listdir, remove, stat
import csv

from text_data import TEST_FILE_CODE, RESULTS_SAVE_DIR, RESULTS_BUFFER_FILE

class TestDataHandler():
    """Handle test data, saved as csv files, and extract information from them.

    Attributes:
        # tests_dir (str): Path to directory where .csv files are saved.
        # tests_list (list): Stores conducted tests, as dictionaries with 
                            information un-coded from the filenames.
    """

    def __init__(self, tests_results_dir=RESULTS_SAVE_DIR) -> None:
        """Init. with path to the directory with files, and list to hold data.

        Args:
            tests_results_dir (str) : Path to directory where .csv files are saved.
        """
        self.tests_dir = tests_results_dir
        self.tests_list = [] # Holds each test as a dict

    def parse_test_file(self, coded_test_data):
        """Analyse filename to extract info. about test, based on keywords."""
        test_dict = {}

        # TODO czy filename jest legit? 1) istnieje, 2) name correct?

        test_data = coded_test_data.split("_")
        # Iterate over every second field.
        for idx in range(0, len(test_data), 2):
            # idx holds data code name and idx+1 actual value.
            test_dict[test_data[idx]] = test_data[idx+1]

        if tuple(test_dict.keys()) != TEST_FILE_CODE:
            raise ValueError("Something went wrong in file naming!")

        print(test_dict) # For init debug, TODO delete

        self.tests_list.append(test_dict)

    def update_data(self):
        """After new test was conducted update tests_list with a new file."""
        press_vs_time_data = []

        buffer_file_path = path.join(RESULTS_SAVE_DIR, RESULTS_BUFFER_FILE)
        with open(buffer_file_path, "r") as f:
            # First line contains data about the test.
            buffer_test_header = f.readline().strip()
            # Rest of the file contains pressure versus time relation.
            for line in f:
                press_vs_time_data.append(line)

        # Uncode data about test and add it to the self.list of test.
        self.parse_test_file(buffer_test_header)
        # Prepare for creation of a csv file with graph data.
        new_test_file_name = buffer_test_header + ".csv"
        des_file = path.join(RESULTS_SAVE_DIR, new_test_file_name)
        with open(des_file, "w") as f:
            f_csv_writer = csv.writer(f)
            for measurement in press_vs_time_data:
                f_csv_writer.writerow(measurement)
        
        # files_list = listdir(self.tests_dir)
        # if len(files_list) > len(self.tests_list):
        #     # Some new file is out there! Look at .csv files:
        #     csv_list = [path.join(self.tests_dir, x) for x in files_list 
        #                 if x.endswith(".csv")]
        #     # Sort by creation time, in order to get the newest.
        #     csv_sorted = sorted(csv_list, key=lambda t: stat(t).st_ctime)
        #     newest_file = csv_sorted[-1]
        #     if newest_file not in self.tests_list:
        #         self.parse_test_file(newest_file)
        #     else:
        #         raise FileExistsError("Error while updating the files list.")

        # Count airtight/leaky vats



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
