import json
from .common import chatgenpath
from typing import List
import os

def readCombinedChats() -> List[dict]:
    """
    Reads the combined chat file.

    Returns
    =======
    chats : list
        list of all conversations

    """

    chatFile = f"{chatgenpath}/chats.json"
    if not os.path.isfile(chatFile):
        print(f"File not found (have you combined chats?): {chatFile}")
        return []

    with open(chatFile,"r") as f:
        return json.load(f)
