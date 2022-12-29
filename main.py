import json
import subprocess
import os
import sys

print("Starting ....")


def str2bool(v):
    return str(v).lower() in ("yes", "true", "t", "1")


with open('exeAsShourtcut.cfg', 'r') as f:
    array: dict = json.load(f)

current_directory_path = ""
extraArgs = " ".join(sys.argv[1:])
current_directory_enabled = array.get("currentDirectoryPathEnabled", False)
executable = array.get("executable",  False)

if executable is False:
    print("executable not found...")
    os._exit(1)

if str2bool(current_directory_enabled):
    current_directory_path = os.getcwd()

executable = current_directory_path + \
    executable if current_directory_enabled else executable

print("Trying to run:", executable)
print("Extra args:", extraArgs)

# DETACHED_PROCESS = 0x00000008

# pid = subprocess.run(
subprocess.run(
    [executable, extraArgs],
    # ["notepad.exe"],
    # ["cmd"],
    # creationflags=DETACHED_PROCESS
    # shell=True,
    # start_new_session=True
)
# ).pid

# print(pid)
print("Exit...")
