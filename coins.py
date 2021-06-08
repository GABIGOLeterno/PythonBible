# Classes são somente modelos,
# como na vida real, você tem modelos para padronizar objetos
# na vida real, objetos têm características e funcionalidades próprias
# em Python, são chamados de "states" e "methods"
# Classes são os modelos que fazem os objetos
# Depois os objetos tornam-se individuais e independentes
# Classes também têm methods

import random


class Coin:
    def __init__(self, rare = False, clean = True, heads = True, **kwargs):

        for key,value in kwargs.items():
            setattr(self,key,value) # set attribute, cria os states de acordo
            # com os parâmetros das palavras chaves do dic kwargs

        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads
                                                                                                                                                                                                                    
        if self.is_rare:
            self.value = self.original_value*1.25
        else:
            self.value = self.original_value

        if self.is_clean:
            self.colour = self.clean_colour
        else:
            self.colour = self.rusty_colour
            
    def rust(self):
        self.colour = self.rusty_colour

    def clean(self):
        self.colour = self.clean_colour

    def __del__(self):
        print("Moeda utilizada.")

    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice

    def __str__(self):
        if self.original_value < 1.00:
            return "R${} centavos".format(self.original_value)
        else:
            return "R${} real".format(int(self.original_value))
            


# a classe Pound herdou os methods da classe Coin geral
class Um_cent(Coin):
    def __init__(self):
        data = {
            "original_value":0.01,
            "clean_colour": "bronze",
            "rusty_colour": "marrom",
            "num_edges": 1,
            "diameter": 20.3,
            "thickness": 1.52,
            "mass": 3.56
            }
        super().__init__(**data)# Depacked as infos do dicionário aqui

class Cinco_cent(Coin):
    def __init__(self):
        data = {
            "original_value":0.05,
            "clean_colour": "bronze",
            "rusty_colour": "marrom",
            "num_edges": 1,
            "diameter": 18.0,
            "thickness": 1.77,
            "mass": 3.25
            }
        super().__init__(**data)


class Dez_cent(Coin):
    def __init__(self):
        data = {
            "original_value":0.10,
            "clean_colour": "dourado",
            "rusty_colour": None,
            "num_edges": 1,
            "diameter": 25.9,
            "thickness": 1.85,
            "mass": 7.12
            }
        super().__init__(**data)
        
        def rust(self):
            self.colour = self.clean_colour
            
        def clean(self):
            self.colour = self.clean_colour

class Cinquenta_cent(Coin):
    def __init__(self):
        data = {
            "original_value":0.50,
            "clean_colour": "prata",
            "rusty_colour": "esverdeado",
            "num_edges": 1,
            "diameter": 28.0,
            "thickness": 2.0,
            "mass": 8.30
            }
        super().__init__(**data)

class Um_real(Coin):
    def __init__(self):
        data = {
            "original_value":1.00,
            "clean_colour": "gold",
            "rusty_colour": "greenish",
            "num_edges": 1,
            "diameter": 31.5,
            "thickness": 1.85,
            "mass": 9.5
            }
        super().__init__(**data)

moedas = [Um_cent(), Cinco_cent(),Dez_cent(),Cinquenta_cent(),Um_real()]

for moeda in moedas:
    arguments = [moeda,moeda.colour,moeda.value,moeda.diameter,moeda.thickness,
                 moeda.num_edges,moeda.mass]
    string = "{} - Colour:{}, value :{},diameter(mm):{}, thickness(mm):{}, number of edges:{}, mass(g):{}".format(*arguments) # Unpacking de uma lista
    print(string)

