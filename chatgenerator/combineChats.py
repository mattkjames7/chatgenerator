from .common import chatgenpath
from .collectChats import collectChats
from .filterChats import filterChats
import json

def combineChats(filter: bool = True, n: int = 2) -> None:
    """
    Combines and optionally filters all of the chats and saves them to a single file.

    Inputs
    ======
    filter :  bool
        If True, some of the chats will be filtered out
    n : int
        Number of messages to examine while filtering

    """

    chats = collectChats()
    if filter:
        chats = filterChats(chats,n)
    
    chatFile = f"{chatgenpath}/chats.json"
    with open(chatFile,"w") as f:
        json.dump(chats,f,indent=2)
    
    print(f"Combined chats saved in: {chatFile}")

