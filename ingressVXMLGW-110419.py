from netmiko import ConnectHandler
from datetime import datetime
import time
import sys
import subprocess
import netmiko
# script by Michael A Wagner Cisco AS
# if you change the txt name here, you also have to do it at the end of this script
fd = open(r'C:\python\devnetlab1.txt', 'w')
old_stdout = sys.stdout
sys.stdout = fd

gw1 = {
    'device_type': 'cisco_ios',
    'ip': '198.18.133.226',
    'username': 'admin',
    'password': 'C1sco12345',
    'verbose': False,
}
# for 2nd gateway test
# gw2 = {
#    'device_type': 'cisco_ios',
#    'ip': '172.20.58.212',
#    'username': 'admin',
#    'password': 'B9vacolab810!',
#    'verbose': False,
# }

# gw3 = {
#    'device_type': 'cisco_ios',
#    'ip': '198.18.133.143',
#    'username': 'administrator',
#    'password': 'dCloud!23',
#    'verbose': False,
# }

gw4 = {
    'device_type': 'cisco_ios',
    'ip': '10.10.20.250',
    'username': 'administrator',
    'password': 'ciscopsdt',
    'verbose': False,
}

# add gw2 in this list when doing multiple gateways
gws = [gw1]
print()
print('This is the start of the proof of test for Cisco dCloud Labs.')
print()
print()
start_time = datetime.now()
print('The report started at: ' + (str(start_time)))
try:
    for a_device in gws:
        net_connect = ConnectHandler(**a_device)
        print("\n\n>>>>>>>>> Device {0} <<<<<<<<<".format(a_device['ip']))
        output = net_connect.send_command('enable')
        output = net_connect.check_enable_mode()
        print('Is the gateway in enable mode: ' + (str(output)))
        output = net_connect.find_prompt()
        print('The gateway prompt: ' + (str(output)))
        output = net_connect.send_command('terminal length 0')
        output = net_connect.send_command("sh flash: | i wav")
        if len(output) == 0:
            print('The WAV FILES are missing')
        #    print("\n\n>>>>>>>>> Device {0} <<<<<<<<<".format(a_device['ip']))
        print()
        print('This is a list of wav files located in flash:')
        print()
        print(output)
        #       print ((output).count) was trying to count the lines
        print()
        print('This is a list of tcl files located in flash:')
        print()
        output = net_connect.send_command('sh flash: | i tcl')
        if len(output) == 0:
            print('The TCL FILES are missing')
        time.sleep(1)
        print(output)
        print()
        print('This is a list of bin files located in flash:')
        print()
        output = net_connect.send_command('sh flash: | i bin')
        if len(output) == 0:
            print('The BIN FILES are missing')
        time.sleep(1)
        print(output)
        print()
        print('This is a list of vxml files located in flash:')
        print()
        output = net_connect.send_command('sh flash: | i vxml ')
        if len(output) == 0:
            print('The VXML FILES are missing')
        time.sleep(1)
        print(output)
        print()
        print('This is a list of the CCB files located in flash:')
        print()
        output = net_connect.send_command('sh flash: | i ccb')
        if len(output) == 0:
            print('The CCB FILES are missing')
        time.sleep(1)
        print(output)
        time.sleep(1)
        print()
        print('This is the version of the gateway:')
        print()
        output = net_connect.send_command("sh version | inc Version")
        print(output)
        print()
        print('This checks if all applications loaded correctly')
        print()
        output = net_connect.send_command("show call appl voice sum")
        print(output)
        print()
        print('This shows the version of the tcl file:')
        print()
        output = net_connect.send_command('more handoff.tcl | i Script ')
        time.sleep(.5)
        if len(output) == 0:
            print('The HandOff file is missing')
        print(output)
        output = net_connect.send_command('more bootstrap.tcl | i Script ')
        time.sleep(.5)
        if len(output) == 0:
            print('The bootstrap file is missing')
        print(output)
        output = net_connect.send_command('more cvp_ccb_dial.tcl | i Script ')
        time.sleep(.5)
        if len(output) == 0:
            print('The cvp-ccb-dial file is missing')
        print(output)
        output = net_connect.send_command('more cvp_ccb_poll.tcl | i Script ')
        time.sleep(.5)
        if len(output) == 0:
            print('The cvp-ccb-poll file is missing')
        print(output)
        output = net_connect.send_command('more cvp_ccb_vxml.tcl | i Script ')
        time.sleep(.5)
        if len(output) == 0:
            print('The svp-ccb-vxml file is missing.')
        print(output)
        output = net_connect.send_command('more cvperror.tcl | i Script ')
        time.sleep(.5)
        if len(output) == 0:
            print('The cvperror file is missing')
        print(output)
        output = net_connect.send_command('more CVPSelfService.tcl | i Script')
        time.sleep(.5)
        if len(output) == 0:
            print('The CVPSelfService file is missing')
        print(output)
        output = net_connect.send_command('more ringtone.tcl | i Script')
        #maw
        time.sleep(.5)
        if len(output) == 0:
            print('The ringtone file is missing')
        print(output)
        output = net_connect.send_command('more survivability.tcl | i Script')
        time.sleep(.5)
        if len(output) == 0:
            print('The Survivability file is missing')
        print(output)
        print()
        output = net_connect.send_command('show run | s dial-peer')
        print('Here is the list of dial peers on the gateway:')
        print()
        print(output)
        print()
        print('Here is a status of the dial-peers')
        output = net_connect.send_command('show dial-peer voice summ')
        print(output)
        print()
        print('Here is a status of the voice ports')
        output = net_connect.send_command('show voice port summ')
        if len(output) == 0:
            print('No VOICE PORTs are configured on this gateway')
        print(output)
        print()
        print('Here is a status of the http cache')
        output = net_connect.send_command('show http cl cache')
        print(output)
        print()
        print('Check http client stats for possible errors or timeouts')
        print('If so, could be device located in network between HTTP server and HTTP client')
        print()
        output = net_connect.send_command('show http cl stat')
        print(output)
        print()
        # reference https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/customer_voice_portal/cvp11_6/configuration/guide/ccvp_b_configuration-guide-for-cisco-unified/ccvp_b_configuration-guide-for-cisco-unified_chapter_01011.html
        print('Best practice for CVP has bind commands under voice service voip')
        output = net_connect.send_command('show run | inc bind')
        if len(output) == 0:
            print('The BIND command is missing')
        print(output)
        print()
        print('Best practice for CVP with a sip proxy')
        output = net_connect.send_command('show run | inc sip-server')
        print(output)
        print()
        print('Best practice for CVP - has mediaserver and mediaserverbackup')

        # if blank how to point this out - 11/6 found 1 solution
        output = net_connect.send_command('show run | inc mediaserver')
        if len(output) == 0:
            print('The IP HOST command is missing')
        print(output)
        print()
        print('Best practice for CVP with Enhanced UUI Feature turned on')
        output = net_connect.send_command('show run | inc signaling forward unconditional')
        if len(output) == 0:
            print('The UUI Feature is not Used')
        print(output)
        print()
        print('Best practice for Voice Service Voip - trusted IP')
        output = net_connect.send_command('show run | i trusted authenticate')
        if len(output) == 0:
            print('The Trusted Authenticate command is missing')
        print(output)
        print()
        print('Best practice for CVP with a gateway - no logging')
        output = net_connect.send_command('show run | inc no logging')
        if len(output) == 0:
            print('The no logging command is missing')
        print(output)
        print()
        time.sleep(.5)
        print('Best practice for CVP with a gateway - ip cef')
        output = net_connect.send_command('show run | inc ip cef')
        if len(output) == 0:
            print('The IP CEF command is missing')
        print(output)
        print()
        time.sleep(.5)
        print('Best practice for CVP with a gateway - voice rtp')
        output = net_connect.send_command('show run | inc voice rtp')
        if len(output) == 0:
            print('The VOICE RTP send-recv command is missing')
        print(output)
        print()
        time.sleep(.5)
        print('Best practice for CVP with a gateway - signaling forward')
        output = net_connect.send_command('show run | inc signaling forward')
        if len(output) == 0:
            print('The SIGNALING FORWARD command is missing')
        print(output)
        print()
        print('Best practice for CVP with a gateway - min-se')
        output = net_connect.send_command('show run | inc min-se')
        if len(output) == 0:
            print('The MIN SE command is missing')
        print(output)
        print()
        print('Best practice for CVP with a gateway - timer receive-rtcp')
        output = net_connect.send_command('show run | inc timer receive-rtcp')
        if len(output) == 0:
            print('The RECEIVE RTCP command is missing')
        print(output)
        print()
        print('Best practice for CVP with a gateway - ip rtcp')
        output = net_connect.send_command('show run | inc ip rtcp')
        if len(output) == 0:
            print('The IP RTCP command is missing')
        print(output)
        print()
        time.sleep(.5)
        print('Best practice for CVP with a gateway - reason-header')
        output = net_connect.send_command('show run | inc reason-header')
        if len(output) == 0:
            print('The REASON HEADER OVERRIDE command is missing')
        print(output)
        print()
        print('Best practice for CVP with a vxml gateway - 4 ivr commands')
        output = net_connect.send_command('show run | inc ivr')
        if len(output) == 0:
            print('The IVR commands are missing')
        print(output)
        print()
        print('Best practice for CVP with a vxml gateway - 3 mrcp commands')
        output = net_connect.send_command('show run | inc mrcp')
        if len(output) == 0:
            print('The MRCP commands are missing')
        print(output)
        print()
        time.sleep(.5)
        print('Best practice for CVP with a vxml gateway - 2 rtsp commands')
        output = net_connect.send_command('show run | inc rtsp')
        if len(output) == 0:
            print('The RTSP commands are missing')
        print(output)
        print()
        print('Best practice for CVP with a vxml gateway - 1 vxml tree')
        output = net_connect.send_command('show run | inc vxml tree')
        if len(output) == 0:
            print('The VXML TREE command is missing')
        print(output)
        print()
        time.sleep(.5)
        print('Best practice for CVP with a vxml gateway - 5 http client commands')
        output = net_connect.send_command('show run | inc http client')
        if len(output) == 0:
            print('The HTTP CLIENT commands are missing')
        print(output)
        print()
        print('Best practice for CVP from OAMP template gw - ip-source route')
        output = net_connect.send_command('show run | inc ip-source route')
        if len(output) == 0:
            print('The IP SOURCE ROUTE command is missing')
        print(output)
        print()
        time.sleep(.5)
        print('Best practice for CVP from OAMP template gw - header-passing')
        output = net_connect.send_command('show run | inc header-passing')
        if len(output) == 0:
            print('The HEADER PASSING command is missing')
        print(output)
        print()
        time.sleep(.5)
        print('Best practice for CVP from OAMP template gw - codec preference')
        output = net_connect.send_command('show run | inc codec preference')
        print(output)
        print()
        print('Best practice for CVP from OAMP template gw - sip-ua')
        output = net_connect.send_command('show run | inc sip-ua')
        print(output)
        print()
        print('Best practice for CVP from OAMP template gw - retry invite 2')
        output = net_connect.send_command('show run | inc retry invite 2')
        if len(output) == 0:
            print('The RETRY INVITE command is missing')
        print(output)
        print()
        print('Best practice for CVP from OAMP template gw - retry bye 2')
        output = net_connect.send_command('show run | inc retry bye 2')
        if len(output) == 0:
            print('The RETRY BYE command is missing')
        print(output)
        print()
        print('Best practice for CVP from OAMP template gw - timers expires ')
        output = net_connect.send_command('show run | inc timers expires')
        if len(output) == 0:
            print('The TIMERS EXPIRES command is missing')
        print(output)
        print()
        print('Best practice for CVP from OAMP template vxml gw - ip routing ')
        output = net_connect.send_command('show run | inc ip routing')
        if len(output) == 0:
            print('The IP ROUTING command is missing')
        print(output)
        print()
        print('Best practice for CVP from OAMP template vxml gw - asr-server ')
        output = net_connect.send_command('show run | inc asr-server')
        if len(output) == 0:
            print('The ASR SERVER command is missing')
        print(output)
        print()
        print('Best practice for CVP from OAMP template vxml gw - tts-server ')
        output = net_connect.send_command('show run | inc tts-server')
        if len(output) == 0:
            print('The TTS SERVER command is missing')
        print(output)
        #MAW
        print()
        print('Best practice for CVP from OAMP template vxml gw - vxml audioerror ')
        output = net_connect.send_command('show run | inc vxml audioerror')
        if len(output) == 0:
            print('The VXML AUDIOERROR command is missing')
        print(output)
        print()
        print('Best practice for CVP from OAMP template vxml gw - vxml version 2 ')
        output = net_connect.send_command('show run | inc vxml version')
        if len(output) == 0:
            print('The VXML VERSION command is missing')
        print(output)
        print()
        print('Best practice for CVP from OAMP template vxml gw -  ')
        output = net_connect.send_command('show run | inc  ')
        print(output)
        print()
        print('Check for network based recording on gateway to CUCM')
        output = net_connect.send_command('show run | inc uc wsapi')
        if len(output) == 0:
            print('The NETWORK BASED RECORDING command is missing')
        print(output)
        print()
        print()
        print('Check for NTP Servers')
        output = net_connect.send_command('show run | inc ntp server')
        if len(output) == 0:
            print('The seems to be no NTP Servers configured')
        print(output)
        print('Check SIP Status')
        output = net_connect.send_command('show sip status')
        print(output)
        print()
        print('Check CPU')
        output = net_connect.send_command('show process cpu history')
        print(output)
# Cisco IOS-XE doesn't do VVB, check to see if GW is IOS-XE. Need another then
# VVB doesn't support media streaming
# max cache size for VVB is 512 MB
# MAW
# VVB doesn't support video calls
# VVB doesn't work in IPv6
# VVB doesn't support RTSP Streaming
# VVB doesn't support RSM
# VVB doesn't support video in queue
# VVB check x-cisco-rai commands

        print()
        print(">>>>>>>>> End <<<<<<<<<")
except netmiko.ssh_exception.NetMikoTimeoutException as n:
    print(n)
    print('Is your VPN connected?')
except OSError as e:
    print(e)
print()
end_time = datetime.now()
print('This report ended at :' + (str(end_time)))
print()
total_time = end_time - start_time
print('Total time to run this report was ' + (str(total_time)))
print()

fd.close()
subprocess.Popen(['C:\\Windows\\System32\\notepad.exe', 'C:\\python\\devnetlab1.txt'])
