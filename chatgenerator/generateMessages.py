from .requestChat import requestChat,getPrompt
from tqdm import tqdm
from copy import deepcopy


def generateMessages(subject: str, count: int = 50) -> dict:
    """
    Generate messages about a specific subject. Messages are generated one by
    one, where the role is reversed each time.

    Inputs
    ======
    subject : str
        Topic of discussion
    count : int
        Number of messages to generate

    Returns
    =======
    chat : dict
        full conversation, starting with system prompt, followed by 
        generated user and assistant messages.
    
    """
    chats = [[getPrompt(subject)],[getPrompt(subject)]]

    for i in tqdm(range(0,count)):
        c = i % 2
        message = requestChat(chats[c])



        if i == 0:
            chats[0].append(deepcopy(message))
            chats[1].append(deepcopy(message))
            chats[0][1]["role"] = "assistant"
            chats[1][1]["role"] = "user"
        else:
            if c == 0:
                chats[0].append({
                    "role": "assistant",
                    "content": message["content"]
                })
                chats[1].append({
                    "role": "user",
                    "content": message["content"]
                })
            else:
                chats[0].append({
                    "role": "user",
                    "content": message["content"]
                })
                chats[1].append({
                    "role": "assistant",
                    "content": message["content"]
                })


    return chats[0]

