#Classe principal do programa
from box import Box
from longestPath import LongestPathDAG
from digraph import Digraph
from time import process_time

list_boxes = [] #Listas de caixas
longest_paths = {}
paths = []

def read_boxes(chosen):
    global list_boxes
    #Leitura dos dados
    with open(f"Casos\\{chosen}.txt", "r") as archive: #Leitura das linhas do arquivo txt para uma variável 
        for lines in archive:         #Itera sobre as linhas do txt
            measure = list(map(int, lines.strip().split()))  #Troca o valor das dimensoes para int
            measure.sort()                              #Ordena para comparação
            smallest, medium, greater = measure  #Adiciona os valores em ordem
            name = str(greater) + str(medium) + str(smallest) 
            box = Box(name, greater, medium, smallest)      #Cria a caixa com o nome e seus tamanhos
            list_boxes.append(box)      #Coloca a caixa na lista
        
def compare_boxes():
    global list_boxes

    for i in range(len(list_boxes)):        #Comparando as caixas da lista
        for j in range(len(list_boxes)):    # Fixa uma caixa e compara com as outras
            if i == j:          #Se a comparação for da caixa com ela mesma, pula a comparação
                continue
            elif (list_boxes[i].get_large_side() < list_boxes[j].get_large_side() and
                list_boxes[i].get_medium_side() < list_boxes[j].get_medium_side() and   #Comparando se as 3 dimensoes da caixa cabem na outra
                list_boxes[i].get_small_side() < list_boxes[j].get_small_side()):
                list_boxes[i].add_contida(list_boxes[j].get_name())      #Adiciona em uma lista dentro de cada caixa, que ela cabe dentro da outra caixa
                list_boxes[j].add_contem(list_boxes[i].get_name())      #Adiciona em um lista dentro de cada caixa, que esta caixa contem outra caixa

def write_txt():
    global list_boxes
    with open("Resultados\\grafo.txt", "w") as archive:     #Abrindo o arquivo de saida
        for box in list_boxes:          #Iterando sobre toda a lista
            for box_id in box.esta_contida:    #Pegando da caixa as caixas maiores que ela
                line = f"{box.get_name()} {box_id} \n"   #Criando a linha para escrevendo no txt
                archive.write(line)         #Escrevendo no txt

def dot(d):
    global list_boxes
    with open("Resultados\\grafo.dot", "w") as archive:
        archive.write(d.toDot())        #Escrevendo o .dot para geração de imagens

def longest_path(d):
    global list_boxes, longest_paths
    # Inicialize uma vez para todos os vértices
    
    for box in list_boxes:
        if box.contem_IsEmpty():
            lp = LongestPathDAG(d, box.get_name())
            lp.find_longest_path()
            longest_paths[box.get_name()] = lp

def calc_longest_path():
    global list_boxes, longest_paths, paths
    
    # Agora calcule os caminhos para todos os pares
    for source_box in list_boxes:
        for target_box in list_boxes:
            if source_box.get_name() in longest_paths:
                path = longest_paths[source_box.get_name()].path_to(target_box.get_name())
                if path is not None:  # Adiciona apenas se o caminho for válido (não vazio)
                    path_length = len(path)
                    paths.append((source_box.get_name(), target_box.get_name(), path, path_length))

def print_longest_path():
    global paths
    # Encontre o maior comprimento
    max_length = 0
    max_path_info = None
    for source, target, path, length in paths:
        if length > max_length:
            max_length = length
            max_path_info = (source, target, path)

    # Imprima o maior comprimento encontrado
    if max_path_info is not None:
        source, target, path = max_path_info
        print(f"O maior comprimento de todos os caminhos é: {max_length}")
        print(f"O caminho mais longo correspondente é de {source} para {target}: {path}")
    else:
        print("Não há caminhos válidos no grafo.")

def menu():
    option = input("""
    ===============================          
            Bem-vindo(a)
        ao menu de escolhas
    ===============================
    Digite o numero correspondente
      ao teste que deseja fazer       
    1 - 10 Vertices
    2 - 20 Vertices
    3 - 50 Vertices
    4 - 100 Vertices
    5 - 200 Vertices
    6 - 300 Vertices
    7 - 500 Vertices
    8 - 1000 Vertices
    9 - 2000 Vertices
    ===============================
    Opções de entradas maiores
    Não recomendado para todos
    10 - 5000 Vertices
    11 - 10000 Vertices
    ===============================  
    """)

    switch = {
        1: "teste10",
        2: "teste20",
        3: "teste50",
        4: "teste100",
        5: "teste200",
        6: "teste300",
        7: "teste500",
        8: "teste1000",
        9: "teste2000",
        10: "teste5000",
        11: "teste10000"
    }  
    if option.isdigit():
        return switch.get(int(option))
    else:
        menu()
            

def main():
    global list_boxes

    option = menu()
    start_time = process_time()
    read_boxes(option)
    compare_boxes()
    write_txt()
    d = Digraph("Resultados\\grafo.txt")
    dot(d)
    longest_path(d)
    calc_longest_path()
    print_longest_path()
    final_time = process_time()
    print(f"O tempo para rodar o {option} foi: {final_time - start_time}")






    # # Inicialize uma vez para todos os vértices
    # longest_paths = {}
    # for box in list_boxes:
    #     if box.contem_IsEmpty():
    #         source_name = box.get_name()
    #         lp = LongestPathDAG(d, source_name)
    #         lp.find_longest_path()
    #         longest_paths[source_name] = lp

    # paths = []

    # # Agora calcule os caminhos para todos os pares
    # for source_box in list_boxes:
    #     for target_box in list_boxes:
    #         source_name = source_box.get_name()
    #         target_name = target_box.get_name()
    #         if source_name in longest_paths:
    #             path = longest_paths[source_name].path_to(target_name)
    #             if path is not None:  # Adiciona apenas se o caminho for válido (não vazio)
    #                 path_length = len(path)
    #                 paths.append((source_name, target_name, path, path_length))

    # # paths agora contém todos os caminhos de todos os vértices para todos os outros vértices
    # # e os comprimentos dos caminhos

    # # Encontre o maior comprimento
    # max_length = 0
    # max_path_info = None
    # for source, target, path, length in paths:
    #     if length > max_length:
    #         max_length = length
    #         max_path_info = (source, target, path)

    # # Imprima o maior comprimento encontrado
    # if max_path_info is not None:
    #     source, target, path = max_path_info
    #     print(f"O maior comprimento de todos os caminhos é: {max_length}")
    #     print(f"O caminho mais longo correspondente é de {source} para {target}: {path}")
    # else:
    #     print("Não há caminhos válidos no grafo.")

if __name__ == "__main__":
    main() 