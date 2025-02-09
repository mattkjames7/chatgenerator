import numpy as np
import datasets
import os
from .common import dataPath
from tqdm import tqdm
import json



def listSubjects():

    if not os.path.isdir(dataPath):
        os.makedirs(dataPath)

    subjectsFile = f"{dataPath}/subjects.json"

    if not os.path.isfile(subjectsFile):

        data = datasets.load_dataset("wikimedia/wikipedia","20231101.en")

        subjects = [data["train"][i]["title"] for i in tqdm(range(0,len(data["train"])))]

        with open(subjectsFile,"w") as f:
            json.dump(subjects,f,indent=2)
    
    else:
        with open(subjectsFile,"r") as f:
            subjects = json.load(f)

    return subjects