import unittest
import get_gene_counts
import random
import os


class TestBinaryTree(unittest.TestCase):
    def test_basic_counts(self):
        file_name = "./gene_counts.data"
        gene_name = "SDHB"
        out_file_name = "counts.out"

        # Check return status
        self.assertTrue(get_gene_counts.create_file(
            file_name, gene_name, out_file_name))
        # Check out file existence
        self.assertTrue(os.path.exists(out_file_name))
        # Check first line matches expected value
        with open(out_file_name) as f:
            self.assertEqual("GTEX-1117F-0226-SM-5GZZ7 1993\n", f.readline())

        # Remove file
        os.remove(out_file_name)

    def test_bad_data_file(self):
        file_name = "./NOT_A_FILE"
        gene_name = "SDHB"
        out_file_name = "counts.out"

        # Check return status
        self.assertFalse(get_gene_counts.create_file(
            file_name, gene_name, out_file_name))
        # Check out file existence
        self.assertFalse(os.path.exists(out_file_name))

    def test_bad_gene_name(self):
        file_name = "./gene_counts.data"
        gene_name = "NOT_A_GENE"
        out_file_name = "counts.out"

        # Check return status
        self.assertTrue(get_gene_counts.create_file(
            file_name, gene_name, out_file_name))
        # Check out file existence
        self.assertTrue(os.path.exists(out_file_name))
        # Check first line matches expected value
        with open(out_file_name) as f:
            self.assertEqual("", f.readline())


if __name__ == '__main__':
    unittest.main()
