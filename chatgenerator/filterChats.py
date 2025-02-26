from typing import List
from tqdm import tqdm

def filterChats(chats: List[dict],n: int = 2) -> List[dict]:
    """
    Attempt to filter out chats which have been formatted incorrectly by the LLM,
    e.g. where a single message contains more than one message. This function 
    will need more work.

    Inputs
    ======
    chats : list
        list of chats
    n : int
        number of messages to check in each chat

    Returns
    =======
    out : list
        filtered list of chats
    
    """

    out = []
    for chat in tqdm(chats,desc="Filtering chats"):
        keep = True
        if len(chat["messages"]) < n + 1:
            continue
        for i in range(n):
            message = chat["messages"][i+1]["content"]
            # replace this with something better
            if "Me:" in message and "Friend:" in message:
                keep = False
                break
        if keep:
            out.append(chat)

    return out
