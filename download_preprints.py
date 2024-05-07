"""
@Project : COVID-19 Preprint classification
@File    : Download preprints
@Time    : 2021/1/7 21:07
@Author  : Xu Zuo
@Class   : BMI 6319 Spring 2021
"""

# import libraries
import requests
import time


class Preprint:
    def __init__(self, title, abstract, authors, publication_date, doi):
        """
        Initializes a new instance of the Preprint class.

        :param title: str - Title of the preprint
        :param abstract: str - Abstract of the preprint
        :param authors: str - Comma-separated list of authors
        :param publication_date: str - Publication date of the preprint
        :param doi: str - DOI of the preprint
        """
        self.title = title
        self.abstract = abstract
        self.authors = authors
        self.publication_date = publication_date
        self.doi = doi


def fetch_preprint_by_doi(doi):
    """
    Fetches a single preprint from the MedRxiv API based on its DOI.

    :param doi: str - The DOI of the preprint
    :return: dict - A dictionary containing preprint data
    """
    url = f"https://api.biorxiv.org/pubs/medrxiv/{doi}"
    response = requests.get(url)
    data = response.json()
    return data['collection'][0] if data['collection'] else None


def create_preprint_object(preprint_data):
    """
    Creates a Preprint object from the fetched data.

    :param preprint_data: dict - Dictionary containing preprint data
    :return: Preprint - An instance of the Preprint class
    """
    title = preprint_data['preprint_title']
    abstract = preprint_data['preprint_abstract'].replace('\n', ' ').replace('\r', ' ')
    abstract = ' '.join(abstract.split())
    authors = preprint_data['preprint_authors']
    publication_date = preprint_data['preprint_date']
    doi = preprint_data['preprint_doi']
    return Preprint(title, abstract, authors, publication_date, doi)


def save_preprints_to_tsv(preprints, filename="preprints.tsv"):
    """
    Saves a list of Preprint objects to a TSV file.

    :param preprints: list - A list of Preprint instances
    :param filename: str - The name of the file to save the preprints
    """
    with open(filename, "w", encoding='utf-8') as file:
        # Write the header row
        file.write("Title\tAbstract\tAuthors\tPublication Date\tDOI\n")
        # Write data for each preprint
        for preprint in preprints:
            file.write(
                f"{preprint.title}\t{preprint.abstract}\t{preprint.authors}\t{preprint.publication_date}\t{preprint.doi}\n")


def read_dois_from_file(filename):
    """
    Reads a list of DOIs from a text file.

    :param filename: str - The name of the file containing the DOIs
    :return: list - A list of DOIs
    """
    with open(filename, 'r', encoding='utf-8') as file:
        dois = [line.strip() for line in file if line.strip()]
    return dois


def fetch_and_save_preprints_by_dois(dois_filename, result_filename="preprints_by_dois.tsv"):
    """
    Fetches and saves preprints based on a list of DOIs from a text file into a TSV file.

    :param dois_filename: str - The name of the file containing the DOIs
    :param result_filename: str - The name of the file to save the preprints
    """
    dois = read_dois_from_file(dois_filename)
    preprints = []
    for doi in dois:
        preprint_data = fetch_preprint_by_doi(doi)
        if preprint_data:
            preprint = create_preprint_object(preprint_data)
            preprints.append(preprint)
        time.sleep(0.1)
    save_preprints_to_tsv(preprints, result_filename)


if __name__ == "__main__":
    # Example usage: Fetch and save preprints for a list of DOIs from a file
    fetch_and_save_preprints_by_dois("data/doi_list.txt", result_filename="data/preprints_by_dois.tsv")
