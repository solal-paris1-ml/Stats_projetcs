import seaborn as sns
import matplotlib.pyplot as plt
import os
import glob
import numpy as np
from pathlib import Path

dir = r"C:/Users/ville/PycharmProjects/stat_projetcs/Appr_Stat"

if os.path.exists(dir):
    print("Connexion established")
else:
    print("Path connexion problem")

