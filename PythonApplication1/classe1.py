class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5
    def mudaCanalParaBaixo(self):
        self.canal -= 1
    def mudaCanalParaCima(self):
        self.canal += 1 