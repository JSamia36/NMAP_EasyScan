import argparse
import subprocess
import os

IP_file = input("IP File: ")
while True:
	nmap_choice = input('Choices: \n(1) Basic Scan \n(2) Vulnerability Scan ')
	if nmap_choice == '1':
		nmap_options = (f'-sC -sV -vv -oN {IP_file}.nmap')
		break
	elif nmap_choice == '2':
		nmap_options = '--script vuln'
		break
	else:
		print('Please Select a Valid Option')

print(f'Using file: {IP_file}')
print('Current working directory:', os.getcwd())

try:
	with open(IP_file, 'r') as file:
		for line in file:
			ip = line.strip()

			nmap_command = (f'nmap {nmap_options} {ip}')

			print(nmap_command)
			try:
				subprocess.run(nmap_command, check=True, shell=True)
			except subprocess.CalledProcessError as e:
				print(f'Error for {ip}: {e}')

except FileNotFoundError:
	print(f'File {IP_file} was not found.')
