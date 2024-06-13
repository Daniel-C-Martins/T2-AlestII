class Box:

    def __init__(self, name, large_side, medium_side, small_side):   #Construtor da caixa
        self._name = name
        self._large_side = large_side
        self._medium_side = medium_side
        self._small_side = small_side
        self.contem = []   #Lista de caixas que cabem dentro dessa caixa
      

    def __str__(self):
        contem_str = ', '.join(str(item) for item in self.contem)
        return f"Id da caixa: {self._name}, Maior lado: {self._large_side}, Lado médio: {self._medium_side}, menor lado: {self._small_side}, contém: {contem_str}"


    def get_name(self):
        return self._name
    
    def get_large_side(self):
        return self._large_side

    def get_medium_side(self):
        return self._medium_side
    
    def get_small_side(self):
        return self._small_side
    
    def get_contem(self):
        contem_str = ', '.join(str(item) for item in self.contem)
        return contem_str
    
    def add_contem(self, num):
        self.contem.append(num)


