import os
import requests
import json

chatgenpath = os.getenv("CHATGEN_PATH")
if not chatgenpath:
    home = os.getenv("HOME")
    chatgenpath = f"{home}/.chatgenerator"
    print(f"$CHATGEN_PATH not set, using {chatgenpath}")

if not os.path.isdir(chatgenpath):
    os.makedirs(chatgenpath)


def _getOllamaHost():

    while True:
        host = input("Enter Ollama host address (include port, usually 11434): ")

        response = requests.get(f"{host}/api/version")
        if response.status_code == 200:
            version = response.json()["version"]
            print(f"Found Ollama API version {version}")
            break
        else:
            print(f"API request failed with code: {response.status_code}, use anyway? (y/n)")
            choice = input()
            if choice.lower() == "y":
                break
    return host


def getConfig():

    configPath = f"{chatgenpath}/config.json"
    if not os.path.isfile(configPath):
        print(f"Config not found")
        host = _getOllamaHost()

        config = {"host": host}

        with open(configPath,"w") as f:
            json.dump(config,f,indent=2)

    else:
        with open(configPath, "r") as f:
            config = json.load(f)

    return config

config = getConfig()