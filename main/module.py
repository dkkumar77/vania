import sys
import os
import subprocess

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'boot')))

import os_check



MAC = "os_mac.py"
WINDOWS = "os_win.py"
LINUX = "os_lin.py"

"""
    Error Code:
    -1 -> PS1 File not found
    0 -> Didn't execute prelim -1
    1 -> success with command installation with os windows
    2 -> success with command installatio nwith os darwin/linux
    

"""
EC1= os_check.run()

{
    0: lambda: (print("Exiting with a message...") or sys.exit(0)),
    1: lambda: subprocess.run(["python", WINDOWS]),
    2: lambda: subprocess.run(["python", MAC])
}.get(EC1, lambda: (print("Invalid value. Exiting...") or sys.exit(1)))()