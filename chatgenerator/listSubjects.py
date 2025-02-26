import numpy as np
import datasets
import os
from .common import chatgenpath
from tqdm import tqdm
import json
from typing import List


def listSubjects() -> List[str]:
    """
    Returns a list of subjects which the agents can chat about.
    The list originates from wikipedia, and is simply a list of 
    all of the english wikipedias page titles.

    Beware - the initial download and reading of the wikipedia data
    takes ages and uses a bit of space.

    Returns
    =======
    subjects : list
        list of subject strings
    
    """
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