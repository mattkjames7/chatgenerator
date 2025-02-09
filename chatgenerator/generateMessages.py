from .requestChat import requestChat,getPrompt
from tqdm import tqdm
from copy import deepcopy


def generateMessages(subject,count=50):

    
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

