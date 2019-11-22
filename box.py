import argparse
import matplotlib.pyplot as plt
import sys
import matplotlib
matplotlib.use('Agg')

parser = argparse.ArgumentParser(
    description='Creates a box plot of tissues and genes')
parser.add_argument(
    '--tissues',
    nargs='+',
    type=str,
    help='The tissues to plot')
parser.add_argument(
    '--genes',
    nargs='+',
    type=str,
    help='The genes to plot')
parser.add_argument(
    '--out_file_name',
    type=str,
    help='The file to save the plot to')


def create_file(tissues, genes, out_file_name):
    """
    Create box plots of counts per Tissue/Gene pair

    Parameters
    ----------
    tissues : tissues to plot
    genes : genes to plot
    out_file_name : the file name (or path) to out file

    Returns
    ----------
    success : boolean

    """

    # Build out the counts for each Tissue/Gene pair
    final_counts = []
    for j in range(len(tissues)):
        counts = []
        for i in range(len(genes)):

            gene = genes[i]
            tissue = tissues[j]

            sample_to_count_map = {}

            f = open(gene + '_counts.txt')
            for l in f:
                A = l.rstrip().split()
                sample_to_count_map[A[0]] = int(A[1])

            f.close()

            count = []

            f = open(tissue + '_samples.txt')
            for l in f:
                sample = l.rstrip()
                if sample in sample_to_count_map:
                    count.append(sample_to_count_map[sample])
            f.close()

            counts.append(count)

        final_counts.append(counts)

    # Define plot size
    width = len(genes) * 3
    height = len(tissues) * 3
    plt.figure(figsize=(width, height), dpi=300)

    # Create subplots
    for j in range(len(tissues)):
        plt.subplot(len(tissues), 1, j+1)
        plt.boxplot(final_counts[j], labels=genes)
        plt.title(tissues[j])
        plt.ylabel('Count')

    # Save the image
    plt.savefig(out_file_name, bbox_inches='tight')

    return True


def main():
    """
    Runs all the needed functions.
    """

    # Parse args and read in data from the files
    args = parser.parse_args()
    success = create_file(args.tissues, args.genes, args.out_file_name)

    # Alert user to finished state
    if success:
        print("Finished successfully and wrote results to: %s" %
              args.out_file_name)
    else:
        print("Did not complete successfully.")
        sys.exit(1)


if __name__ == '__main__':
    main()
