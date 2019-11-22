import unittest
import get_tissue_samples
import random
import os


class TestGetTissueSamples(unittest.TestCase):
    def test_basic_counts(self):
        file_name = "./sample_attributes.data"
        tissue_name = "Blood"
        out_file_name = "ids.out"

        # Check return status
        self.assertTrue(get_tissue_samples.create_file(
            file_name, tissue_name, out_file_name))
        # Check out file existence
        self.assertTrue(os.path.exists(out_file_name))
        # Check first line matches expected value
        with open(out_file_name) as f:
            self.assertEqual("GTEX-1117F-0003-SM-58Q7G\n", f.readline())

        # Remove file
        os.remove(out_file_name)

    def test_bad_data_file(self):
        file_name = "./NOT_A_FILE"
        tissue_name = "Blood"
        out_file_name = "ids.out"

        # Check return status
        self.assertFalse(get_tissue_samples.create_file(
            file_name, tissue_name, out_file_name))
        # Check out file existence
        self.assertFalse(os.path.exists(out_file_name))

    def test_bad_tissue_name(self):
        file_name = "./sample_attributes.data"
        tissue_name = "NOT_A_GENE"
        out_file_name = "ids.out"

        # Check return status
        self.assertTrue(get_tissue_samples.create_file(
            file_name, tissue_name, out_file_name))
        # Check out file existence
        self.assertTrue(os.path.exists(out_file_name))
        # Check first line matches expected value
        with open(out_file_name) as f:
            self.assertEqual("", f.readline())


if __name__ == '__main__':
    unittest.main()
