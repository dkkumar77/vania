import sys
import os
import subprocess
import shutil

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'boot')))

import os_check

MAC = "os_mac.py"
WINDOWS = "os_win.py"
LINUX = "os_lin.py"

def get_python_executable():
    if shutil.which("python3"):
        return "python3"
    elif shutil.which("python"):
        return "python"
    else:
        raise FileNotFoundError("No suitable Python executable found")

python_exec = get_python_executable()

EC1 = os_check.run()

{
    0: lambda: (print("Exiting with a message...") or sys.exit(0)),
    1: lambda: subprocess.run([python_exec, WINDOWS]),
    2: lambda: subprocess.run([python_exec, MAC])
}.get(EC1, lambda: (print("Invalid value. Exiting...") or sys.exit(1)))()

