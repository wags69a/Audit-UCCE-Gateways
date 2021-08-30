# #Use Case Description
This code is for cisco UCCE solutions 10.x, 11.x and 12.x
This python code should be run on Ingress and VXML gateways for Contact center.
The output file is sent to C:/python, you can change the location to where ever it is allowed.
The script can test multiple gateways, it is set to only 1 at the moment. Change gws to list all the gateways you want tested and uncomment them.

#Installation
This python code is written in 3.7. Put it on a server that has access to the gateways to be audited.

#Usage
This code has been tested in Cisco dCloud and other customer environments.

#DevNet Sandbox
At the time of this writting, there was no Devnet sandbox for UCCE, however as said above, you can run this on a lab.

#Known issues
The script is long and it could fail in different places, but error handling has been included for the errors I saw when runing the lab. The first error is having no access to the gateways. You need the dCloud VPN and if you didn't I told the error message to check the VPN. You can modify this message to your situation. This script also output a file and you might need permissions to do this on the customer network.

#Getting help 
Contact the owner if he is not too busy.

#Credits and references
UCCE 10 and 11 configuration and staging guide.
OAMP gateway templates are also used.

#Best Practice
The above guides gave the guidance for the best practice audit commands.
Try is script in your lab or dCloud first so you can get used to it. Do not try it first in front of the customer as all errors for different environments are not thought of here.

#Step by step
1) Down load Audit-UCCE-Gateways code from GitHub.
2) PIP import requirements.txt
3) Verify connection to the gateways that you want to audit. (VPN)
4) Put the UCCE Gateway IP address, username and password in the script.
5) Run the script
6) Troubleshoot any access errors.
7) Look at the results via notepad.
8) Fix anything that the audit finds, as long as it fits your version.

[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/wags69a/Audit-UCCE-Gateways)
