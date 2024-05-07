import pandas as pd


def merge_preprints_with_labels(preprints_filename, labels_filename, output_filename):
    """
    Merges preprint information with labels using pandas.

    :param preprints_filename: str - Filename of the TSV file containing preprint details.
    :param labels_filename: str - Filename of the TSV file containing labels for each preprint.
    :param output_filename: str - Filename for the merged output TSV file.
    """
    # Read the preprints and labels data from TSV files
    preprints_df = pd.read_csv(preprints_filename, sep='\t', dtype=str)
    labels_df = pd.read_csv(labels_filename, sep='\t', dtype=str, header=None, names=['DOI', 'Label'])

    # Merge the dataframes on the DOI column
    merged_df = pd.merge(preprints_df, labels_df, on='DOI', how='left')

    # Save the merged DataFrame to a new TSV file
    merged_df.to_csv(output_filename, sep='\t', index=False)

    print(f"Merged data saved to {output_filename}")


if __name__ == "__main__":
    merge_preprints_with_labels('data/preprints_by_dois.tsv', 'data/label_list.txt', 'data/preprints.tsv')
