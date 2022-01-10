#!/usr/bin/env python
# coding: utf-8

# ## Data Pre-Processing

# - Pre-processing the metadata dataset to remove the columns with more number of missing values
# - Imputing the fields with categorical data with mode of the field 
# - Imputing the fields with the numerical data with the mean of the field

# ### Function to pre-process the metadata 

# In[1]:


import pandas as pd
import re
import numpy as np

# In[2]:


def pre_process_metadata(data):
    '''
    This function pre-processes the metadata dataset to remove the colums with more number of missing values and 
    imputing the fields with the categorical daata with the modeof the field and imputing the fields with numerical data 
    with the mean of the field
    param : data - Input metadata data to be pre-processes
    return : metadata_filtered - The metadata data which is pre-processed 
        
    '''
    # Dropping the below columns because of the NA values
    metadata_dropped_columns = data.drop([
                   'Unnamed: 26', 
                   'lineage_molecular_subtype',
                   'depmap_public_comments',
                   'depmap_public_comments',
                   'alias',
                   'COSMICID',
                   'WTSI_Master_Cell_ID',
                   'Sanger_Model_ID',
                   'lineage_sub_subtype',
                   'cell_line_name',
                   'RRID'
                   ], axis = 1)
    # Imputing mode of the column culture_type for the missing values and anomalies
    metadata_dropped_columns['sex'] = list(metadata_dropped_columns['sex'].map(lambda x : np.nan if bool(re.search(r'(908156)', str(x))) else x))
    metadata_dropped_columns['culture_type'] = list(metadata_dropped_columns['culture_type'].map(lambda x : np.nan if bool(re.search(r'\d', str(x))) else x))
    metadata_dropped_columns['Achilles_n_replicates'] = list(metadata_dropped_columns['Achilles_n_replicates'].map(lambda x : np.nan if bool(re.search(r'[a-zA-Z]', str(x))) else x))
    metadata_dropped_columns['source'] = list(metadata_dropped_columns['source'].map(lambda x : np.nan if bool(re.search(r'(Children&#39 | Male)', str(x))) else x))
    metadata_dropped_columns['sample_collection_site'] = list(metadata_dropped_columns['sample_collection_site'].map(lambda x : np.nan if bool(re.search(r'\d', str(x))) else x))
    # Imputing mode of the column primary_or_metastasis for the missing values and anomalies
    ColumnsToBeImputedByMode = ['primary_or_metastasis', 'culture_type', 'Achilles_n_replicates', 'source', 'sample_collection_site',
                          'primary_disease', 'Subtype', 'lineage', 'lineage_subtype', 'sex']
    for i in ColumnsToBeImputedByMode:
        metadata_dropped_columns[i].fillna(metadata_dropped_columns[i].mode()[0], inplace=True)
    # Imputing mean of the column age for the missing values and anomalies
    metadata_dropped_columns['age'] = list(metadata_dropped_columns['age'].map(lambda x : np.nan if bool(re.search(r'[a-zA-Z]', str(x))) else x))
    metadata_dropped_columns['age'] = metadata_dropped_columns['age'].map(float)
    metadata_dropped_columns['cas9_activity'] = list(metadata_dropped_columns['cas9_activity'].map(lambda x : np.nan if bool(re.search(r'[a-zA-Z]', str(x))) else x))
    metadata_dropped_columns['cas9_activity'] = metadata_dropped_columns['cas9_activity'].map(float)
    ColumnsToBeImputedByMean = ['age', 'cell_line_NNMD', 'cas9_activity']
    for i in ColumnsToBeImputedByMean:
        metadata_dropped_columns[i].fillna(metadata_dropped_columns[i].mean(), inplace=True)
    metadata_dropped_columns['culture_medium'].fillna("not found", inplace = True)
    metadata_filtered = metadata_dropped_columns
    return metadata_dropped_columns

