import subprocess
from os import listdir


def transfer():
	"""
	Function to transfer file from local system to AWS EC2 instance.
	"""
	ip = input("Enter destination IP address : ")
	user = input("Enter User name : ")
	pemFileName = input("Enter pem file name : ")
	ipMod = ip.replace('.',"-")

	#List of files in the transfer folder
	onlyfiles = [f for f in listdir("transfer")]
	for file in onlyfiles:
		args = ["sudo", "scp", "-i", pemFileName,"transfer/"+file, user+"@ec2-"+ipMod+".compute-1.amazonaws.com:~/"]
		#scp command to transfer file to server
		print(" ".join(args))
		send = subprocess.Popen(args, stdout=subprocess.PIPE)
		output = send.communicate()
		print(output[0])

if __name__ == '__main__':
	transfer()
