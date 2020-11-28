import os
import numpy as np
import pandas as pd
from pymol import *
import rdkit
from rdkit import Chem
from rdkit.Chem import AllChem
import rdkit.Chem
from rdkit.Chem import Draw 
from rdkit.Chem import rdFMCS



import math
import time

import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')


from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report

import DealTimeOut
import ShowFigure
import TranSmiToPdb

import time
import eventlet

import sys

if __name__ == '__main__':
#    filename=sys.argv[1]
     filename='1116he.xlsx'   ###
     smiles=readsmi(filename, smicolumn='SMILES')
     mols=TranSmiToPdb(smiles,firstname='new')
#    template1=Chem.MolFromSmiles('CS(=O)(NC1=CC=CC=C1)=O')   
     drawMols(mols,saved_dir='./newmols')
     
