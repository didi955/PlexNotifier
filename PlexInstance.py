from plexapi.server import PlexServer


class PlexInstance:

    def __init__(self, name: str, ip: str, port: int, token: str):
        """
        Constructor that creates a PlexInstance from specified parameters.

        -- PlexInstance is the instance that target a specific Plex server.

        :param name: Name of the Plex instance
        :param ip: IP address of the Plex instance
        :param port: Port of the Plex instance
        :param token: Token of the Plex instance
        """
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

