import subprocess

def system_update():
    print("Updating system...")
    subprocess.run("sudo apt update && sudo apt upgrade -y", shell=True)

if __name__ == "__main__":
    system_update()
