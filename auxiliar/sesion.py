class sesion:
    __instance = None
    vin = ''
    ip_port = ''
    coordenadas = []

    def __init__(self, vin='', ip_port=''):
        if sesion.__instance is not None:
            raise Exception("Esta clase es un singleton!")
        else:
            self.vin = vin
            self.ip_port = ip_port
            sesion.__instance = self

    @staticmethod
    def get_instance():
        if sesion.__instance is None:
            sesion()
        return sesion.__instance

    def set_vin(self, vin):
        self.vin = vin

    def get_vin(self):
        return self.vin

    def set_ip_port(self, ip_port):
        self.ip_port = ip_port

    def get_ip_port(self):
        return self.ip_port

    def clear(self):
        self.vin = ''
        self.ip_port = ''

    def set_coordenadas(self, coordenadas):
        self.coordenadas = coordenadas

    def get_coordenadas(self):
        return self.coordenadas
