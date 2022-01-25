# Modules needed
import paramiko
from time import sleep
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Credentials for the session
hostname = '10.10.10.20'
username = 'admin'
password = 'Passw0rd01'
ssh.connect(hostname=hostname,username=username, password=password,look_for_keys=False, allow_agent=False)

connection = ssh.invoke_shell()

connection.send("top\r")
sleep(.5)
connection.send("scope chassis\r")
sleep(.5)
connection.send("power off\r")
sleep(.5)
connection.send("y\r")
sleep(.5)
connection.send("exit\r")
sleep(.5)
connection.send("exit\r")
sleep(.5)
output = connection.recv(65535)
print(output.decode("UTF-8"))
