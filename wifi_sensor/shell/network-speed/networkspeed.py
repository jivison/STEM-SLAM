import speedtest

servers = []

print("Running speedtest...")
s = speedtest.Speedtest()
s.get_servers(servers)
s.get_best_server()
s.download()
s.upload()
s.results.share()

results = s.results.dict()

host_ping = results['ping'] 
upload_spd = "{0:.1f}".format(results['upload'] / 1000000)
download_spd = "{0:.1f}".format(results['download'] / 1000000)

print("Pinged {} with a latency of {}ms".format(results['server']['sponsor'], host_ping))

#Appends all of the nmap data to the csv file
with open("../networkdetails.csv", "a+") as csv:
    csv.write(",{},{},{}".format(host_ping, upload_spd, download_spd))