import sys
import gzip
import argparse

parser = argparse.ArgumentParser(
    description='Creates a file with the sample ids'
    + 'and counts for a given gene.')
parser.add_argument(
    '--file_name',
    type=str,
    help='The file containing gene data')
parser.add_argument(
    '--gene_name',
    type=str,
    help='The gene to get counts for')
parser.add_argument(
    '--out_file_name',
    type=str,
    help='The file to save count data to')


def create_file(file_name, gene_name, out_file_name):
    """
    Read gene data from file and prints counts to out file.

    Parameters
    ----------
    file_name : the file name (or path) to gene data file
    gene_name : name of the gene to count
    out_file_name : the file name (or path) to out file

    Returns
    ----------
    success : boolean

    """

    version = None
    dim = None
    header = None

    # Try to open the data file
    try:
        f = gzip.open(file_name, 'rt')
    except FileNotFoundError:
        print("ERROR: The file could not be found."
              + " Check for a typo? {%s}" % file_name)
        return False

    # Create file to write counts to
    o = open(out_file_name, 'w')

    # Iterate through lines of gene counts and write to out file
    for l in f:
        A = l.rstrip().split('\t')
        if version is None:
            version = A
            continue
        if dim is None:
            dim = A
            continue
        if header is None:
            header = A
            continue
        if A[1] == gene_name:
            for i in range(2, len(header)):
                o.write(header[i] + ' ' + A[i] + '\n')

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
    success = create_file(args.file_name, args.gene_name, args.out_file_name)

    # Alert user to finished state
    if success:
        print("Finished successfully and wrote results to: %s" %
              args.out_file_name)
    else:
        print("Did not complete successfully.")
        sys.exit(1)


if __name__ == '__main__':
    main()
