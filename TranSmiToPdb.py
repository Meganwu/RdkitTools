from pymol import *
import rdkit
from rdkit import Chem
from rdkit.Chem import AllChem
import rdkit.Chem
from rdkit.Chem import Draw 
import xlrd

import os
import numpy as np
from pandas import Series, DataFrame
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')
def readsmi(filename, smicolumn='SMILES'):
    try:
        smiles=pd.read_excel(filename, encoding = 'utf8')
#       smiles=pd.read_table(filename, encoding = 'utf8')
        smis=smiles['SMILES'].to_list()
        return smis
    except:
        print("Input or Read Error:file fails to read")
        
def TranSmiToPdb(smiles,firstname='new'):
    mols=[]
    num=1
    for smi in smiles:
      try:  
        name=firstname+str(num)+'.pdb'
        mol = Chem.MolFromSmiles(smi)
        molh=Chem.AddHs(mol)    # add H
        AllChem.EmbedMolecule(molh, randomSeed=3)
        AllChem.MMFFOptimizeMolecule(molh)
        Chem.MolToPDBFile(molh,name)
        mols.append(mol)
        num=num+1
      except:
        mols.append('error')
        num=num+1
        print("The %s th molecule fails to transform smiles to pdb, please check!" %  num)
        pass
      continue
     return mols
     
     
     
