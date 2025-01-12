import os
import platform
import subprocess

def run():
    system_name = platform.system()

    ps_script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "ps/prelim.ps1"))
    bash_script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "bash/prelim.sh"))

    if system_name == "Windows":
        if not os.path.exists(ps_script_path):
            print(f"PowerShell script not found at: {ps_script_path}")
            return -1
        else:
            try:
                subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", ps_script_path], check=True)
                return 1
            except subprocess.CalledProcessError as e:
                print(f"Failed to execute prelim.ps1: {e}")
                return 0
    elif system_name in ["Darwin", "Linux"]:
        try:
            subprocess.run(["bash", bash_script_path], check=True)
            return 2
        except subprocess.CalledProcessError as e:
            print(f"Failed to execute prelim.sh: {e}")
            return 0
    else:
        print("Unsupported operating system.")
        return -1

if __name__ == "__main__":
    run()

