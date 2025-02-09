from .generateMessages import generateMessages
from .listSubjects import listSubjects
import hashlib
from .common import dataPath
from random import choice,randint
import os
import json

def generateChats(n=1000,count=50):

    chatDir = f"{dataPath}/chats"
    if not os.path.isdir(chatDir):
        os.makedirs(chatDir)

    subjects = listSubjects()

    for i in range(0,n):
        subject = choice(subjects)
        print(f"{i:5d} of {n:5d} : {subject}")
        hash = hashlib.sha256(str(randint(0,2**32)).encode("utf-8")).hexdigest()[:12]

        chatFile = f"{chatDir}/{hash}.json"
        chat = generateMessages(subject,count)

        with open(chatFile,"w") as f:
            json.dump(chat,f,indent=2)
        print(f"Saved: {chatFile}")



