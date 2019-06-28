# EC2-Fileshare

Python code to transfer files from local system to AWS EC2 instance

###How to Use ?

1) Clone the repository
2) Place the pem file used to ssh into the server, in the directory.
3) Place all the files required to transfer in the "transfer" folder
4) Run the python code

###Python Code

Inputs needed - 

1) Public IP address of the instance.
2) User name 
- Ex: ssh -i "abc.pem" ubuntu@ec2-54-162-41-176.compute-1.amazonaws.com (User name is 'ubuntu')
3) Name of the pem file with the .pem extension.
- ExL abc.pem

> Note : Works only for files.
