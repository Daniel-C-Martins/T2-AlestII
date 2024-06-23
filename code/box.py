class Box:

    def __init__(self, name, bigger_side, medium_side, small_side):   #Construtor da caixa
        self._name = name
        self._bigger_side = bigger_side
        self._medium_side = medium_side
        self._small_side = small_side
        self.contain = []   #Lista de caixas que cabem dentro dessa caixa
        self.contained = [] #Lista de caixas que esta caixa cabe dentro 
      

    def __str__(self):
        contain_str = ', '.join(str(item) for item in self.contain)
        return f"Id da caixa: {self._name}, Maior lado: {self._bigger_side}, Lado médio: {self._medium_side}, menor lado: {self._small_side}, contém: {contain_str}"


    def get_name(self):
        return self._name
    
    def get_bigger_side(self):
        return self._bigger_side

    def get_medium_side(self):
        return self._medium_side
    
    def get_small_side(self):
        return self._small_side
    
    def get_contain(self):
        contain_str = ', '.join(str(item) for item in self.contain)
        return contain_str
    
    def get_contida(self):
        contain_str = ', '.join(str(item) for item in self.contained)
        return contain_str
    
    def add_contain(self, num):
        self.contain.append(num)

    def add_contained(self, num):
        self.contained.append(num)

    def contain_IsEmpty(self):
        return not self.contain


