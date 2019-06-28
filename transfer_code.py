import subprocess
from os import listdir
from os.path import isfile, join


def transfer():
	#print("Enter destination IP address : ")
	ip = input("Enter destination IP address : ")
	user = input("Enter User name : ")
	ipMod = ip.replace('.',"-")
	#cmd = "scp -r -i /transfer "+user+"@ec2-"+ipMod+".compute-1.amazonaws.com: /"
	#args = ["scp", "-i", "crio.pem", "-r","transfer", user+"@ec2-"+ipMod+".compute-1.amazonaws.com:", "/"]
	#args = ["ls", "/transfer"]
	#send = subprocess.Popen(args)
	#output = send.communicate()
	#onlyfiles = [f for f in listdir("/transfer") if isfile(join("/transfer", f))]
	onlyfiles = [f for f in listdir("transfer")]
	#print(onlyfiles)
	for file in onlyfiles:
		args = ["sudo", "scp", "-i", "crio.pem","transfer/"+file, user+"@ec2-"+ipMod+".compute-1.amazonaws.com:~/"]
		print(" ".join(args))
		send = subprocess.Popen(args, stdout=subprocess.PIPE)
		output = send.communicate()
		print(output)
if __name__ == '__main__':
	transfer()
