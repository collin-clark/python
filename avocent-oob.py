import requests, json
import urllib3 #Can be removed when valid certificate is added
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) #Can be removed when valid certificate is added

#     Section: Authenticate to the API
#     Set the base URL for the API call
base = 'https://FQDN:48048/api/v1'

#     Define the final portion of the URL for authenticating and getting an auth token
sessionlogin = '/sessions/login'

#     Build the final URL to send
final_url = base + sessionlogin

#     Set the POST parameters
headers = {'Content-Type': 'application/json'}
credentials = {'username': 'root', 'password': 'linux'}

#     Send the POST and the parameters
response = requests.post (final_url, data=json.dumps(credentials), headers=headers, verify=False)
# verify=False can be removed when valid certificate is added

response.encoding = 'json'
#print(response.text) #TEXT/HTML
#print(response.status_code)

### Insert error checking
#if response.status_code != 200:
#    print('Call to API has failed. Response code is: ' + response.status_code)
#    quit()

#     Load the results as JSON
json_data = json.loads(response.text)
#     Pull out the token code
token = json_data['token']
#print(token)

#     Section: Create Header for JWT
header_token = {'Authorization': 'Bearer ' + token}
#print(header_token)

networksettings = '/network/settings'
final_url = base + networksettings
response = requests.get(final_url, headers=header_token, verify=False)
json_data = json.loads(response.text)
#print(json_data)
hostname = json_data['hostname']
# print(hostname)

#     Section: Get the System IP
intf = '/network/devices/eth0'
final_url = base + intf
response = requests.get(final_url, headers=header_token, verify=False)
#print(response.text)
json_data = json.loads(response.text)
ip_address = (json_data['ipv4Static']['ipv4Address'])

#     Section: Build the Help Section
resources = '/resources'
final_url = base + resources
response = requests.get(final_url, headers=header_token, verify=False)
# print(response.text)

#     Section: Build the serialPorts list
serialinfo = '/serialPorts'
final_url = base + serialinfo
response = requests.get(final_url, headers=header_token, verify=False)
#print(response.text)
json_data = json.loads(response.text)
for result in json_data['serialPorts']:
    serialport = result['port']
    ssh_port = result['cas']['sshAliasPort']
    serialstatus = result['status']
    pinout = result['physical']['pinout']
    speed = result['physical']['speed']
    deviceName = result['cas']['name']
    print(hostname,ip_address,serialport,ssh_port,deviceName,serialstatus,pinout,speed)
