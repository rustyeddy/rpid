# Inventory of Raspberry Pis

class RPiList(object):

    def __init__(self, **kwargs):
        pass

    def add(self, rpi):
        """Add the given raspberry Pi to the inventory list"""
        name = rpi['name']
        self._list[name] = rpi
        return len(self._list)

class RPi(object):
    def __init__(self, **kwargs):
        self.name = None
        self.ipaddr = None
        self.macaddr= None

        
