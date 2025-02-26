import os
from .common import chatgenpath
from .combineChats import combineChats
from typing import Optional
import huggingface_hub as hfhub

def uploadChats(repo: str, readme: Optional[str] = None, private: bool = False) -> None:
    """
    Uploads the combined conversations to huggingface

    Inputs
    ======
    repo : str
        This should be the full repo name, e.g. matt123/chats-v1.0.0
    readme : str|None
        If provided, the readme will also be uploaded alongside the chat file. 
    private : bool
        Repo visibility
    """

    #check the chat file exists
    chatFile = f"{chatgenpath}/chats.json"
    if not os.path.isfile(chatFile):
        print("Chat file combined, create it?")
        result = input("(y/n)")
        if result.lower() != "y":
            return
        combineChats()

    # get the huggingface token
    token = os.getenv("HF_TOKEN")
    if token == "" or token is None:
        print("Set $HF_TOKEN variable before continuing")
        return
    
    # check if the repo exists
    api = hfhub.HfApi()
    exists = api.repo_exists(
        repo_id=repo,
        token=token,
        repo_type="dataset"
    )

    # create it if needed
    if not exists:
        print(f"Creating {repo}")
        api.create_repo(
            repo_id=repo,
            token=token,
            repo_type="dataset",
            private=private
        )
    
    
    api.upload_file(
        path_or_fileobj=chatFile,
        path_in_repo="chats.json",
        repo_id=repo,
        token=token,
        repo_type="dataset"
    )
    print(f"Uploaded {chatFile}")

    if readme:
        if not os.path.isfile(readme):
            print(f"Could not find readme: {readme}")
            return
        api.upload_file(
            path_or_fileobj=readme,
            path_in_repo="README.md",
            repo_id=repo,
            token=token,
            repo_type="dataset"
        )
        print(f"Uploaded {readme}")    