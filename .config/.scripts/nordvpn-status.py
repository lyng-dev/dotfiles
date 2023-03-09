import subprocess

result = subprocess.check_output(["nordvpn", "status"]).decode("utf-8")
result = result.strip("\n")
#status = dict(item.split(":") for item in result.split("\n"))
status = dict(map(lambda x: x.split(':'), result.split("\n"))) 
#print(status)

status = { k:v.strip() for k, v in status.items()}
#print(status)

title = "NordVPN: "
if status["Status"] == 'Connected':
  print(f"{title} <span foreground='green'>Connected</span>: {status['Country']} (IP: {status['Your new IP']})")
else:
  print(f"{title} <span foreground='red'>Disconnected</span>")
