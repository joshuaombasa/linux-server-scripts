import subprocess

def manage_service(service_name, action):
    command = f"sudo systemctl {action} {service_name}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout if result.stdout else result.stderr)

if __name__ == "__main__":
    service = input("Enter service name: ")
    action = input("Enter action (start/stop/restart/status): ")
    manage_service(service, action)
