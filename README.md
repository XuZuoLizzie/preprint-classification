# Text classification for COVID-19 treatment preprints
## Background
Since the COVID-19 pandemic began, researchers have been investigating effective treatments for the coronavirus. Systematic reviews and meta-analyses of clinical studies are useful approaches to analyzing results from a number of relevant studies, thus increasing the statistical ability to detect the true value of treatments. However, manual search and extraction of biomedical literature can be both time-consuming and laborious. Therefore, this project aims to assist literature screening by developing an automated approach to identify the study type of studies related to COVID-19 treatments.
## Task
This is a multi-label classification task. The first step is data preprocessing, which includes data parsing and feature extraction. Basic features include word shapes, prefix-suffix, and bigrams. Additional features include TD-IDF and word embedding. For the label prediction, I plan to use three machine learning models (logistic regression, XGBoost, and support vector machines) as the baselines. The baseline models will be implemented using the scikit-learn library. Additionally, I plan to test two deep learning models (FastText and TextCNN) on this task. 
Choices of Language and Libraries
- Python: For its robust ecosystem in data handling and machine learning.
- Scikit-learn and SpaCy: For implementing and deploying machine learning models.
- Pandas and NumPy: For data manipulation and numerical operations.
## Dataset
The preprints used in this project were pre-labeled as “RCT”, “observational study”, and “other”. I downloaded preprint data, including titles, author names, affiliations, release dates, and abstracts, from preprint servers (MedRxiv and BioRxiv). The preprint datasets are saved as a TSV file. In case preprint datasets are inadequate for training and testing deep learning models, I also plan to retrieve and label additional PubMed articles related to COVID-19 treatments. The PubMed article datasets will be saved as XML files.
## Results and evaluation
The final deliverables will be the predictive labels of test data. The results will be reported numerically using evaluation metrics: precision, recall, and f-measure.
## Running the pipeline
Please follow the instructions to reproduce the analysis results.

**Clone repository**

`git clone https://github.com/XuZuoLizzie/preprint-classification.git`

**Set up the environment**

The pipeline requires Python 3.8. You can run the analysis pipeline with baseline models on local desktops. 
Create a virtual environment first for this project:
`conda create -n preprint-classification python=3.8`

**Prediction with baseline model and sample data**

Install required packages:

`pip install -r requirements.txt`

Run the following script for training and prediction:

`python3 classification_model.py`

The evaluation results will be printed on your screen.

**Run the pipeline with customized datasets**

Note: The pipeline is only applicable to multi-class classification tasks.

If you would like to run this pipeline using your own datasets. 
Please convert your data into a TSV file.
Please refer to the sample dataset `preprints.tsv` in `data/` directory.
