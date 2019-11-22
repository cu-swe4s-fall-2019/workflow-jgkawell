import sys
import argparse

parser = argparse.ArgumentParser(
    description='Creates a file with the sample ids'
    + 'for a given tissue group.')
parser.add_argument(
    '--file_name',
    type=str,
    help='The file containing sample attributes')
parser.add_argument(
    '--tissue_name',
    type=str,
    help='The tissue to get samples for')
parser.add_argument(
    '--out_file_name',
    type=str,
    help='The file to save count data to')


def create_file(file_name, tissue_name, out_file_name):
    """
    Read gene data from file and prints counts to out file.

    Parameters
    ----------
    file_name : the file name (or path) to sample data file
    tissue_name : name of the sample group
    out_file_name : the file name (or path) to out file

    Returns
    ----------
    success : boolean

    """

    header = None
    sampid_col = -1
    smts_col = -1

    # Try to open the data file
    try:
        f = open(file_name)
    except FileNotFoundError:
        print("ERROR: The file could not be found."
              + " Check for a typo? {%s}" % file_name)
        return False

    # Create file to write counts to
    o = open(out_file_name, 'w')
    for l in f:
        A = l.rstrip().split('\t')
        if header is None:
            header = A
            sampid_col = A.index('SAMPID')
            smts_col = A.index('SMTS')
            continue

        if A[smts_col] == tissue_name:
            o.write(A[sampid_col] + '\n')

    # Close files
    f.close()
    o.close()

    return True


def main():
    """
    Runs all the needed functions.
    """

    # Parse args and read in data from the files
    args = parser.parse_args()
    success = create_file(args.file_name, args.tissue_name, args.out_file_name)

    # Alert user to finished state
    if success:
        print("Finished successfully and wrote results to: %s" %
              args.out_file_name)
    else:
        print("Did not complete successfully.")
        sys.exit(1)


if __name__ == '__main__':
    main()
