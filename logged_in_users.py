import subprocess

def list_logged_in_users():
    result = subprocess.run("who", shell=True, capture_output=True, text=True)
    print(result.stdout)

if __name__ == "__main__":
    list_logged_in_users()
