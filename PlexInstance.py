from plexapi.server import PlexServer


class PlexInstance:

    """
    Constructor that creates a PlexInstance from specified parameters.
    """
    def __init__(self, name: str, ip: str, port: int, token: str):
        self.name = name
        self.ip = ip
        self.port = port
        self.token = token
        self.baseurl = "http://" + self.ip + ":" + str(self.port)
        self.plex = PlexServer(self.baseurl, self.token)

    def getPlex(self):
        return self.plex

    def getUrl(self):
        return self.baseurl

    def getIp(self):
        return self.ip

    def getPort(self):
        return self.port

    def getName(self):
        return self.name

    def getToken(self):
        return self.token

