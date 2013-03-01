class DNSCfg(object):


    def __init__(self):
        pass

    def backup(self):
        pass

    def modify(self, dns):
        pass

    def restore(self):
        pass

    def printinfo(self):
        pass


def create_dnscfg():
    s = platform.system()
    if s == "Darwin":
        from dnscfg.darwin_dnscfg import DarwinDNSCfg
        return DarwinDNSCfg
    else if s == "Linux":
        from dnscfg.linux_dnscfg import LinuxDNSCfg
        return LinuxDNSCfg
    else if s == "Windows":
        from dnscfg.windows_dnscfg import WindowsDNSCfg
        return WindowsDNSCfg
    else:
        print "Unsuppoerted os"
        