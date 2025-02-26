import numpy as np
import datasets
import os
from .common import chatgenpath
from tqdm import tqdm
import json



def listSubjects():

    if not os.path.isdir(chatgenpath):
        os.makedirs(chatgenpath)

    subjectsFile = f"{chatgenpath}/subjects.json"

    if not os.path.isfile(subjectsFile):
        print("This bit takes ages, sorry...")
        data = datasets.load_dataset("wikimedia/wikipedia","20231101.en")

        subjects = [data["train"][i]["title"] for i in tqdm(range(0,len(data["train"])))]

        with open(subjectsFile,"w") as f:
            json.dump(subjects,f,indent=2)
    
    else:
        with open(subjectsFile,"r") as f:
            subjects = json.load(f)

    return subjects