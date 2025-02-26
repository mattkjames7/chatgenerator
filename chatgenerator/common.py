import os

chatgenpath = os.getenv("CHATGEN_PATH")
if not chatgenpath:
    home = os.getenv("HOME")
    chatgenpath = f"{home}/.chatgenerator"
    print(f"$CHATGEN_PATH not set, using {chatgenpath}")

if not os.path.isdir(chatgenpath):
    os.makedirs(chatgenpath)

