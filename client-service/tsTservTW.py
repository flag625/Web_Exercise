#!/usr/bin/env python

from twisted.internet import protocol, reactor
from time import ctime

PROT = 21567

class TSServProtocol(protocol.Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print('...connected from: ', clnt)
    def dataReceived(self, data):
        self.transport.write(b'[%s] %s' %(ctime().encode(), data))

factory = protocol.Factory()
factory.protocol = TSServProtocol
print('waiting for connection...')
reactor.listenTCP(PROT, factory)
reactor.run()