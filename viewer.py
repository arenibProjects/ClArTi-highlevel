# -*- coding: utf-8 -*-

import socket
import json

class Viewer:
    def __init__(self, map):
        self.__map = map
        self.__clientSockets = []
        self.__debugSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__debugSocket.bind(('', 15555))
        self.__debugSocket.listen(5)

    def __del__(self):
        self.__debugSocket.close()
        
    def checkConnections(self):
        readable, writable, errored = select.select(self.__clientSockets + [self.__debugSocket], [], [])
        for s in readable:
            if s is self.__debugSocket:
                clientSocket, address = server_socket.accept()
                self.__clientSockets.append(clientSocket)
                print "[Viewer] Received connection from ", address
                
            else:
                data = s.recv(1024)
                if data:
                    # .... processing data .... WIP
                else:
                    s.close()
                    self.__clientSockets.remove(s)

    # Send functions
    def sendToAll(self, data):
        for clientSocket in self.__clientSockets:
            self.send(data, clientSocket)

    def send(self, data, destinationSocket = self.__debugSocket):
        destinationSocket.send(json.dumps(data).encode("utf-8"))
        #print(json.dumps(object.serialize()).encode())
    
    # Communication implementation
    def addEntity(self, entity):
        data = {"type":"addEntity", entity.getId(), }