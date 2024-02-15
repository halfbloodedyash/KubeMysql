import subprocess
import time

def backup_data():
    # Perform MySQL backup using mysqldump
    f = open("backup.sql", "w")
    dump = subprocess.run(["mysqldump", "-h", "127.0.0.1", "-u", "root", "-psakila", "anish"], capture_output=True, text=True)
    f.write(dump.stdout)
    print('back up done :)')

def update_configuration():
    # Update configuration here (replace with actual commands)
    pass

def rolling_update():
    # Trigger a rolling update for the StatefulSet
    subprocess.run(["kubectl", "rollout", "restart", "statefulset/mysql"])

def configuration_management():
    # Assuming you want to check MySQL configuration within Pods
    # pod_list = subprocess.run(["kubectl", "get", "pods"], capture_output=True, text=True).stdout
    print('Mysql is running!' if subprocess.run(["mysql", "status", "-h", "127.0.0.1", "-u", "root", "-psakila", "anish"], capture_output=True, text=True).returncode else 'MySQL is not running')



def testing():
    retcode = 0
    # Example: Test MySQL selection
    retcode = max(subprocess.run(["mysql", "-h", "127.0.0.1", "-u", "root", "-psakila", "-e", "USE anish; SELECT * from test1"], text=True).returncode, retcode)
    
    # Example: Perform CRUD operations
    retcode = max(subprocess.run(["mysql", "-h", "127.0.0.1", "-u", "root", "-psakila", "-e", "USE anish; INSERT INTO test1(id) VALUE (6);"], text=True).returncode, retcode)

    # Example: Verify replication (if applicable)
    retcode = max(subprocess.run(["mysql", "-h", "127.0.0.1", "-u", "root", "-psakila", "-e", "SHOW SLAVE STATUS\G"], text=True).returncode, retcode)

    print("Testing Successful (:" if not retcode else "Testing unsuccessful :(")
    
def monitoring():
    # Get the list of MySQL Pods
    pod_list = subprocess.run(['kubectl', 'get', 'pods', '--output=custom-columns=NAME:.metadata.name', '--no-headers'], capture_output=True, text=True).stdout

    # Loop through each MySQL Pod and check its status
    for pod in pod_list.split():
        if pod.strip():  # Check if pod name is not empty
            print(f"MySQL Pod: {pod}")
            # Check Pod status
            subprocess.run(["kubectl", "get", "pod", pod])
            # Check MySQL process status
            # subprocess.run(["kubectl", "exec", pod, "--", "ps", "aux", "|", "grep", "mysql"])
            # Check MySQL logs for errors
            # subprocess.run(["kubectl", "logs", pod, "|", "grep", "-i", "error"])           
if __name__ == "__main__":
    # while True:
        # Execute the tasks
        backup_data()
        # update_configuration()
        # rolling_update()
        configuration_management()
        # testing()
        monitoring()
        
        # Sleep for 1 hour before running again
        # time.sleep(3600)  # Sleep for 1 hour (3600 seconds)import subprocess
