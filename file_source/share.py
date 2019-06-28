from flask import Flask,render_template ,redirect, url_for , request,send_file
import subprocess
import os

app = Flask(__name__)

#api to get File system tree
@app.route('/get_fstree')
def get_tree():
	"""
	API to return the drectory tree of the public folder (folder to be shared)
	"""
	#output = subprocess.check_output(['tree','/home/pruthvi/Desktop/EC2-Fileshare/file_source/public'])
	subprocess.call('cd public',stdout=subprocess.PIPE,shell=True, preexec_fn=os.setsid)
	cmd = ['tree','-H','public/']
	output = subprocess.Popen( cmd, stdout=subprocess.PIPE ).communicate()[0]
	print(output)
	return output



if __name__ == '__main__':
    app.run(debug=True)