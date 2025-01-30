import subprocess

def manage_user(username, action):
    if action == "create":
        command = f"sudo useradd -m {username}"
    elif action == "delete":
        command = f"sudo userdel -r {username}"
    else:
        print("Invalid action. Use 'create' or 'delete'.")
        return
    
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout if result.stdout else result.stderr)

if __name__ == "__main__":
    user = input("Enter username: ")
    action = input("Enter action (create/delete): ")
    manage_user(user, action)
