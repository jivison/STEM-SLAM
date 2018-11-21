import speedtest

servers = []

def upload():

    s = speedtest.Speedtest()
    s.get_servers(servers)
    s.get_best_server()
    s.upload()
    s.results.share()

    results = s.results.dict()

    upload_spd = "{0:.1f}".format(results['upload'] / 1000000)

    return upload_spd

def download():

    s = speedtest.Speedtest()
    s.get_servers(servers)
    s.get_best_server()
    s.download()
    s.results.share()

    results = s.results.dict()

    download_spd = "{0:.1f}".format(results['download'] / 1000000)

    return download_spd