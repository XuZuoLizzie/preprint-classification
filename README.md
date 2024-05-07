# Text classification for COVID-19 treatment preprints
## Background
Since the COVID-19 pandemic began, researchers have been investigating effective treatments for the coronavirus. Systematic reviews and meta-analyses of clinical studies are useful approaches to analyzing results from a number of relevant studies, thus increasing the statistical ability to detect the true value of treatments. However, manual search and extraction of biomedical literature can be both time-consuming and laborious. Therefore, this project aims to assist literature screening by developing an automated approach to identify the study type of studies related to COVID-19 treatments.
## Task
This is a multi-label classification task. The first step is data preprocessing, which includes data parsing and feature extraction. Basic features include word shapes, prefix-suffix, and bigrams. Additional features include TD-IDF and word embedding. For the label prediction, I plan to use three machine learning models (logistic regression, XGBoost, and support vector machines) as the baselines. The baseline models will be implemented using the scikit-learn library. Additionally, I plan to test two deep learning models (FastText and TextCNN) on this task. 

Choices of Language and Libraries:
- Python: For its robust ecosystem in data handling and machine learning.
- Scikit-learn and SpaCy: For implementing and deploying machine learning models.
- Pandas and NumPy: For data manipulation and numerical operations.

Data Quality and Variety:
- Inconsistent data formats and quality: Enable data cleaning and preprocessing steps.
- Imbalanced dataset: Balance the dataset using SMOTE to over-sample the minority classes.

## Dataset
The preprints used in this project were pre-labeled as “RCT”, “observational study”, and “other”. I downloaded preprint data, including titles, author names, affiliations, release dates, and abstracts, from preprint servers (MedRxiv and BioRxiv). The preprint datasets are saved as a TSV file. In case preprint datasets are inadequate for training and testing deep learning models, I also plan to retrieve and label additional PubMed articles related to COVID-19 treatments. The PubMed article datasets will be saved as XML files.
## Results and evaluation
The final deliverables will be the predictive labels of test data. The results will be reported numerically using evaluation metrics: precision, recall, and f-measure.
## Running the pipeline
Please follow the instructions to reproduce the analysis results.

**Clone repository**

```
git clone https://github.com/XuZuoLizzie/preprint-classification.git
```

**Set up the environment**

The pipeline requires Python 3.8. You can run the analysis pipeline with baseline models on local desktops. 
Create a virtual environment first for this project:

```
conda create -n preprint-classification python=3.8
```

**Use baseline model and sample data**

Install required packages:

```
pip install -r requirements.txt
```

Run the following script for training and prediction:

```
python classification_model.py
```

The evaluation results will be printed on your screen:

```
Training SVM model...
Evaluating SVM model...
Accuracy: 0.574468085106383
Classification Report:
               precision    recall  f1-score   support

           0       0.78      0.93      0.85        15
           1       0.43      0.86      0.57        14
           2       1.00      0.06      0.11        18

    accuracy                           0.57        47
   macro avg       0.74      0.62      0.51        47
weighted avg       0.76      0.57      0.48        47

Training XGBoost model...
Evaluating XGBoost model...
Accuracy: 0.9148936170212766
Classification Report:
               precision    recall  f1-score   support

           0       1.00      0.87      0.93        15
           1       0.81      0.93      0.87        14
           2       0.94      0.94      0.94        18

    accuracy                           0.91        47
   macro avg       0.92      0.91      0.91        47
weighted avg       0.92      0.91      0.92        47
```

**Use Docker container**

You can also run this pipeline using the baseline models and sample data with a docker container. Docker offers several significant advantages that can streamline development, enhance security, and increase portability across different computing environments. 

Download and open Docker Desktop from the Start menu. It should run the Docker daemon automatically.

Build the docker image:

```
docker build -t text-classification-app .
```

Run the docker container:

```
docker run text-classification-app
```

**Run the pipeline with customized datasets**

Note: The pipeline is only applicable to multi-class classification tasks.

If you would like to run this pipeline using your own datasets. Please convert your data into a TSV file. Please refer to the sample dataset `preprints.tsv` in `data/` directory.

The script `download_preprints.py` allows you to download preprints metadata and abstracts from MedRxiv API using a list of DOIs. A sample of downloaded data is provided in `data/preprints_by_dois.tsv`. 
