import os
from .common import chatgenpath
from typing import List
from tqdm import tqdm
import json

def collectChats() -> List[dict]:
    """
    Read all of the individual chats into a single list of dictionaries
    
    Returns
    =======
    chats : list
        list of chat dicts
    """

    chatPath = f"{chatgenpath}/chats"
    files = os.listdir(chatPath)
    files = [file for file in files if file.endswith(".json")]
    filePaths = [f"{chatPath}/{file}" for file in files]

    print(f"Found {len(files)} files")

    chats = []
    for file,filePath in tqdm(zip(files,filePaths), desc="Reading chats"):
        key = file.split(".")[0]
        with open(filePath,"r") as f:
            messages = json.load(f)
        #remove empty messages
        messages = [message for message in messages if message["content"] != ""]
        chat = {
            "name": key,
            "messages": messages
        }
        chats.append(chat)

    return chats