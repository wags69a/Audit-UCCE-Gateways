""""
This script will audit the CCE ingress and vxml gateway versions 9, 10 and 11.
The toolID for the AIDE agent is correct, you will need a PID. The metadata is the default, you will need to update.
This script was verified with a PC, a MAC has not been tested.
The IP address is the dCloud lab.
"""
from datetime import datetime
from netmiko import ConnectHandler

__version__ = '2.2'
__author__ = 'Michael A Wagner wagnerm@cisco.com'

import time
import sys
import subprocess
import netmiko
import paramiko
import aide

pid = int(input("Enter PID Number:"))
ip = input('Enter GW IP Address:')
username = input('Enter username:')
password = input('Enter password:')

gw1 = {
    'device_type': 'cisco_ios',
    'ip': ip,
    'username': username,
    'password': password,
    'verbose': False,
}

gws = [gw1]
print()
print('This is the start of the proof of test for Cisco dCloud Labs.')
print()
print()
start_time = datetime.now()
print('The report started at: ' + (str(start_time)))


def ccegate():

        with open('C:\\python39\\gatewayaudit012022v2.txt', 'w') as f:

            f.write('This is the start of the Gateway Audit \n')
            f.write(" \n")
            f.write('The report started at: ' + (str(start_time)))
            f.write(" \n")

            try:
                for a_device in gws:
                    net_connect = ConnectHandler(**a_device)
                    print("\n\n>>>>>>>>> Device {0} <<<<<<<<<".format(a_device['ip']))
                    f.write("\n\n>>>>>>>>> Device {0} <<<<<<<<<".format(a_device['ip']))
                    f.write("\n")
                    output = net_connect.send_command('enable')
                    output = net_connect.check_enable_mode()
                    print('Is the gateway in enable mode: ' + (str(output)))
                    f.write("Is the gateway in enable mode: " + (str(output)))
                    f.write(" \n")
                    output = net_connect.find_prompt()
                    print('The gateway prompt: ' + (str(output)))
                    f.write("The gateway prompt " + (str(output)))
                    f.write(" \n")
                    print()
                    output = net_connect.send_command('terminal length 0')
                    f.write(output)
                    f.write("\n \n")
                    f.write("This is a list of wav files found in flash:")
                    f.write("\n")
                    output = net_connect.send_command("sh flash: | i wav")
                    f.write(output)
                    f.write("\n")
                    if len(output) == 0:
                        print('The WAV FILES are missing')
                        f.write("The WAV files are missing")
                    f.write("\n")
                    f.write('This is a list of tcl files located in flash:')
                    f.write("\n")
                    output = net_connect.send_command('sh flash: | i tcl')
                    f.write(output)
                    if len(output) == 0:
                        f.write('The TCL FILES are missing')
                    f.write("\n")
                    print()
                    print('The script has started, please be patient.')
                    print()
                    f.write('This is a list of bin files located in flash:')
                    f.write("\n \n")
                    output = net_connect.send_command('sh flash: | i bin')
                    f.write(output)
                    if len(output) == 0:
                        f.write('The BIN FILES are missing')
                    time.sleep(1)
                    f.write("\n \n")
                    f.write('This is a list of vxml files located in flash:')
                    f.write("\n")
                    output = net_connect.send_command('sh flash: | i vxml ')
                    if len(output) == 0:
                        f.write('The VXML FILES are missing')
                    time.sleep(1)
                    f.write(output)
                    f.write("\n \n")
                    f.write('This is a list of the CCB files located in flash:')
                    f.write("\n")
                    output = net_connect.send_command('sh flash: | i ccb')
                    if len(output) == 0:
                        f.write('The CCB FILES are missing')
                    time.sleep(1)
                    f.write(output)
                    time.sleep(1)
                    f.write("\n \n")
                    f.write('This is the version of the gateway:')
                    f.write("\n")
                    output = net_connect.send_command("sh version | inc Version")
                    f.write(output)
                    f.write("\n \n")
                    f.write('This checks if all applications loaded correctly')
                    f.write("\n")
                    output = net_connect.send_command("show call appl voice sum")
                    f.write(output)
                    f.write("\n")
                    f.write('This shows the version of the tcl file:')
                    f.write("\n")
                    output = net_connect.send_command('more handoff.tcl | i Script ')
                    time.sleep(.5)
                    if len(output) == 0:
                        f.write('The HandOff file is missing')
                    f.write(output)
                    f.write("\n")
                    output = net_connect.send_command('more bootstrap.tcl | i Script ')
                    time.sleep(.5)
                    if len(output) == 0:
                        f.write('The bootstrap file is missing')
                    f.write(output)
                    f.write("\n")
                    output = net_connect.send_command('more cvp_ccb_dial.tcl | i Script ')
                    time.sleep(.5)
                    if len(output) == 0:
                        f.write('The cvp-ccb-dial file is missing')
                    f.write(output)
                    f.write("\n")
                    output = net_connect.send_command('more cvp_ccb_poll.tcl | i Script ')
                    time.sleep(.5)
                    if len(output) == 0:
                        f.write('The cvp-ccb-poll file is missing')
                    f.write(output)
                    f.write("\n")
                    print()
                    print("The Script is still running")
                    print()
                    output = net_connect.send_command('more cvp_ccb_vxml.tcl | i Script ')
                    time.sleep(.5)
                    if len(output) == 0:
                        f.write('The svp-ccb-vxml file is missing.')
                    f.write(output)
                    f.write("\n")
                    output = net_connect.send_command('more cvperror.tcl | i Script ')
                    time.sleep(.5)
                    if len(output) == 0:
                        f.write('The cvperror file is missing')
                    f.write(output)
                    f.write("\n")
                    output = net_connect.send_command('more CVPSelfService.tcl | i Script')
                    time.sleep(.5)
                    if len(output) == 0:
                        f.write('The CVPSelfService file is missing')
                    f.write(output)
                    f.write("\n")
                    output = net_connect.send_command('more ringtone.tcl | i Script')
                    #maw
                    time.sleep(.5)
                    if len(output) == 0:
                        f.write('The ringtone file is missing')
                    f.write(output)
                    f.write("\n")
                    output = net_connect.send_command('more survivability.tcl | i Script')
                    time.sleep(.5)
                    if len(output) == 0:
                        f.write('The Survivability file is missing')
                    f.write(output)
                    f.write("\n \n")
                    output = net_connect.send_command('show run | s dial-peer')
                    f.write('Here is the list of dial peers on the gateway:')
                    f.write("\n")
                    f.write(output)
                    f.write("\n \n")
                    f.write('Here is a status of the dial-peers')
                    f.write("\n")
                    output = net_connect.send_command('show dial-peer voice summ')
                    f.write(output)
                    f.write("\n \n")
                    f.write('Here is a status of the voice ports')
                    f.write("\n")
                    output = net_connect.send_command('show voice port summ')
                    if len(output) == 0:
                        f.write('No VOICE PORTs are configured on this gateway')
                    f.write(output)
                    f.write("\n \n")
                    f.write('Here is a status of the http cache')
                    f.write("\n")
                    output = net_connect.send_command('show http cl cache')
                    f.write(output)
                    f.write("\n \n")
                    f.write('Check http client stats for possible errors or timeouts')
                    f.write("\n")
                    f.write('If so, could be device located in network between HTTP server and HTTP client')
                    f.write("\n")
                    output = net_connect.send_command('show http cl stat')
                    f.write(output)
                    f.write("\n \n")
                    print("Script is still running")
                    f.write('Best practice for CVP has bind commands under voice service voip')
                    f.write("\n")
                    output = net_connect.send_command('show run | inc bind')
                    if len(output) == 0:
                        f.write('The BIND command is missing')
                    f.write(output)
                    f.write("\n \n")
                    f.write('Best practice for CVP with a sip proxy')
                    f.write("\n")
                    output = net_connect.send_command('show run | inc sip-server')
                    f.write(output)
                    f.write("\n \n")
                    f.write('Best practice for CVP - has mediaserver and mediaserverbackup')
                    f.write("\n")
                    # if blank how to point this out - 11/6 found 1 solution
                    output = net_connect.send_command('show run | inc mediaserver')
                    if len(output) == 0:
                        f.write('The IP HOST command is missing')
                    f.write(output)
                    f.write("\n \n")
                    f.write('Best practice for CVP with Enhanced UUI Feature turned on')
                    f.write("\n")
                    output = net_connect.send_command('show run | inc signaling forward unconditional')
                    if len(output) == 0:
                        f.write('The UUI Feature is not Used')
                    f.write(output)
                    f.write("\n \n")
                    f.write('Best practice for Voice Service Voip - trusted IP')
                    f.write("\n")
                    output = net_connect.send_command('show run | i trusted authenticate')
                    if len(output) == 0:
                        f.write('The Trusted Authenticate command is missing')
                    f.write(output)
                    f.write("\n \n")
                    f.write("\n")
                    f.write('Best practice for CVP with a gateway - no logging')
                    f.write("\n")
                    output = net_connect.send_command('show run | inc no logging')
                    if len(output) == 0:
                        f.write('The no logging command is missing')
                    f.write(output)
                    f.write("\n \n")
                    time.sleep(.5)
                    f.write('Best practice for CVP with a gateway - ip cef')
                    f.write("\n")
                    output = net_connect.send_command('show run | inc ip cef')
                    if len(output) == 0:
                        f.write('The IP CEF command is missing')
                    f.write(output)
                    f.write("\n \n")
                    time.sleep(.5)
                    f.write('Best practice for CVP with a gateway - voice rtp')
                    f.write("\n")
                    output = net_connect.send_command('show run | inc voice rtp')
                    if len(output) == 0:
                        f.write('The VOICE RTP send-recv command is missing')
                    f.write(output)
                    f.write("\n \n")
                    time.sleep(.5)
                    f.write('Best practice for CVP with a gateway - signaling forward')
                    f.write("\n")
                    output = net_connect.send_command('show run | inc signaling forward')
                    if len(output) == 0:
                        f.write('The SIGNALING FORWARD command is missing')
                    f.write(output)
                    f.write("\n \n")
                    f.write('Best practice for CVP with a gateway - min-se')
                    f.write("\n")
                    output = net_connect.send_command('show run | inc min-se')
                    if len(output) == 0:
                        f.write('The MIN SE command is missing')
                    f.write(output)
                    f.write("\n \n")
                    f.write('Best practice for CVP with a gateway - timer receive-rtcp')
                    f.write("\n")
                    output = net_connect.send_command('show run | inc timer receive-rtcp')
                    if len(output) == 0:
                        f.write('The RECEIVE RTCP command is missing')
                    f.write(output)
                    f.write("\n \n")
                    f.write('Best practice for CVP with a gateway - ip rtcp')
                    f.write("\n")
                    output = net_connect.send_command('show run | inc ip rtcp')
                    if len(output) == 0:
                        f.write('The IP RTCP command is missing')
                    f.write(output)
                    f.write("\n \n")
                    time.sleep(.5)
                    f.write('Best practice for CVP with a gateway - reason-header')
                    f.write("\n")
                    output = net_connect.send_command('show run | inc reason-header')
                    if len(output) == 0:
                        f.write('The REASON HEADER OVERRIDE command is missing')
                    f.write(output)
                    f.write("\n \n")
                    f.write('Best practice for CVP with a vxml gateway - 4 ivr commands')
                    f.write("\n")
                    output = net_connect.send_command('show run | inc ivr')
                    if len(output) == 0:
                        f.write('The IVR commands are missing')
                    f.write(output)
                    f.write("\n \n")
                    f.write('Best practice for CVP with a vxml gateway - 3 mrcp commands')
                    f.write("\n")
                    output = net_connect.send_command('show run | inc mrcp')
                    if len(output) == 0:
                        f.write('The MRCP commands are missing')
                    f.write(output)
                    f.write("\n \n")
                    time.sleep(.5)
                    print("The Script is still running")
                    f.write('Best practice for CVP with a vxml gateway - 2 rtsp commands')
                    f.write("\n")
                    output = net_connect.send_command('show run | inc rtsp')
                    if len(output) == 0:
                        f.write('The RTSP commands are missing')
                    f.write(output)
                    f.write("\n \n")
                    f.write('Best practice for CVP with a vxml gateway - 1 vxml tree')
                    f.write("\n")
                    output = net_connect.send_command('show run | inc vxml tree')
                    if len(output) == 0:
                        f.write('The VXML TREE command is missing')
                    f.write(output)
                    f.write("\n \n")
                    time.sleep(.5)
                    f.write('Best practice for CVP with a vxml gateway - 5 http client commands')
                    f.write("\n")
                    output = net_connect.send_command('show run | inc http client')
                    if len(output) == 0:
                        f.write('The HTTP CLIENT commands are missing')
                    f.write(output)
                    f.write(' \n \n')
                    f.write('Best practice for CVP from OAMP template gw - ip-source route')
                    f.write("\n")
                    output = net_connect.send_command('show run | inc ip-source route')
                    if len(output) == 0:
                        f.write('The IP SOURCE ROUTE command is missing')
                    f.write(output)
                    f.write(' \n \n')
                    time.sleep(.5)
                    f.write('Best practice for CVP from OAMP template gw - header-passing')
                    f.write("\n")
                    output = net_connect.send_command('show run | inc header-passing')
                    if len(output) == 0:
                        f.write('The HEADER PASSING command is missing')
                    f.write(output)
                    f.write(' \n \n')
                    time.sleep(.5)
                    f.write('Best practice for CVP from OAMP template gw - codec preference')
                    f.write("\n")
                    output = net_connect.send_command('show run | inc codec preference')
                    f.write(output)
                    f.write(' \n \n')
                    f.write('Best practice for CVP from OAMP template gw - sip-ua')
                    f.write("\n")
                    output = net_connect.send_command('show run | inc sip-ua')
                    f.write(output)
                    f.write(' \n \n')
                    f.write('Best practice for CVP from OAMP template gw - retry invite 2')
                    f.write("\n")
                    output = net_connect.send_command('show run | inc retry invite 2')
                    if len(output) == 0:
                        f.write('The RETRY INVITE command is missing')
                    f.write(output)
                    f.write(' \n \n')
                    f.write('Best practice for CVP from OAMP template gw - retry bye 2')
                    f.write("\n")
                    output = net_connect.send_command('show run | inc retry bye 2')
                    if len(output) == 0:
                        f.write('The RETRY BYE command is missing')
                    f.write(output)
                    f.write(' \n \n')
                    f.write('Best practice for CVP from OAMP template gw - timers expires ')
                    f.write("\n")
                    output = net_connect.send_command('show run | inc timers expires')
                    if len(output) == 0:
                        f.write('The TIMERS EXPIRES command is missing')
                    f.write(output)
                    f.write(' \n \n')
                    f.write('Best practice for CVP from OAMP template vxml gw - ip routing ')
                    f.write("\n")
                    output = net_connect.send_command('show run | inc ip routing')
                    if len(output) == 0:
                        f.write('The IP ROUTING command is missing')
                    f.write(output)
                    f.write(' \n \n')
                    f.write('Best practice for CVP from OAMP template vxml gw - asr-server ')
                    f.write("\n")
                    output = net_connect.send_command('show run | inc asr-server')
                    if len(output) == 0:
                        f.write('The ASR SERVER command is missing')
                    f.write(output)
                    f.write(' \n \n')
                    f.write('Best practice for CVP from OAMP template vxml gw - tts-server ')
                    f.write("\n")
                    print("The Report is almost Finished.")
                    output = net_connect.send_command('show run | inc tts-server')
                    if len(output) == 0:
                        f.write('The TTS SERVER command is missing')
                    f.write(output)
                    f.write("\n \n")
                    f.write("\n")
                    f.write('Best practice for CVP from OAMP template vxml gw - vxml audioerror ')
                    f.write("\n")
                    output = net_connect.send_command('show run | inc vxml audioerror')
                    if len(output) == 0:
                        f.write('The VXML AUDIOERROR command is missing')
                    f.write(output)
                    f.write("\n")
                    f.write('Best practice for CVP from OAMP template vxml gw - vxml version 2 ')
                    f.write("\n")
                    output = net_connect.send_command('show run | inc vxml version')
                    if len(output) == 0:
                        f.write('The VXML VERSION command is missing')
                    f.write(output)
                    f.write("\n")
                    f.write('New Commands can go here  ')
                    f.write("\n")
                    #un comment out the next line and replace the show run command with a new command.
                    #output = net_connect.send_command('show run | inc  ')
                    f.write(output)
                    f.write("\n")
                    f.write('Check for network based recording on gateway to CUCM')
                    f.write("\n")
                    output = net_connect.send_command('show run | inc uc wsapi')
                    if len(output) == 0:
                        f.write('The NETWORK BASED RECORDING command is missing')
                    f.write(output)
                    print()
                    f.write("\n")
                    f.write('Check for NTP Servers')
                    f.write("\n")
                    output = net_connect.send_command('show run | inc ntp server')
                    if len(output) == 0:
                        f.write('The seems to be no NTP Servers configured')
                    f.write(output)
                    f.write('Check SIP Status')
                    f.write("\n")
                    output = net_connect.send_command('show sip status')
                    f.write(output)
                    f.write("\n")
                    f.write('Check CPU')
                    f.write("\n")
                    output = net_connect.send_command('show process cpu history')
                    f.write(output)
                    f.write("\n")
                    #MAW
                    f.write("\n \n")
                    print()
                    print(">>>>>>>>> End <<<<<<<<<")
                    f.write(">>>>>>>>> End <<<<<<<<<")
            except netmiko.ssh_exception.NetMikoTimeoutException as n:
                print(n)
                print('Is your VPN connected?')
                f.write(' \n')
                f.write("Is the VPN connected, I see an error.")
                f.write(" \n")
            except netmiko.ssh_exception.NetmikoAuthenticationException as n:
                print(n)
                print('Invalid username or password.')
                f.write(' \n')
                f.write("Invalid Username or Password.")
                f.write(" \n")
            except OSError as e:
                print(e)


print()

if __name__ == "__main__":
    ccegate()


try:
    aide.submit_statistics(
        pid = pid,  # This should be a valid PID
        tool_id="106822",
        metadata={
            "potential_savings": 0.1666666, # Hours
            "report_savings": True,
        },
    )

except Exception:
    pass


end_time = datetime.now()
print('This report ended at :' + (str(end_time)))
print()
total_time = end_time - start_time
print('Total time to run this report was ' + (str(total_time)))
print()

with open('C:\\python39\\gatewayaudit012022v2.txt', 'a') as f:
    f.write(" \n")
    f.write('This report ended at : ' + (str(end_time)))
    f.write(" \n")
    f.write('Total time to run this report was ' + (str(total_time)))
    f.write(" \n")



