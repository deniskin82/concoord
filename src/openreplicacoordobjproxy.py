#automatically generated by the proxygenerator
from clientproxyonerun import *

class OpenReplicaCoordProxy():
    def __init__(self, bootstrap):
        self.proxy = ClientProxy(bootstrap)

    def __str__(self):
        self.proxy.invoke_command("__str__")

    def addnodetosubdomain(self, subdomain, node):
        self.proxy.invoke_command("addnodetosubdomain", subdomain, node)

    def delnodefromsubdomain(self, subdomain, node):
        self.proxy.invoke_command("delnodefromsubdomain", subdomain, node)

    def delsubdomain(self, subdomain):
        self.proxy.invoke_command("delsubdomain", subdomain)

    def getnodes(self, subdomain):
        self.proxy.invoke_command("getnodes", subdomain)

    def getsubdomains(self):
        self.proxy.invoke_command("getsubdomains")

