#Classe principal do programa
import re
from box import Box
from digraph import Digraph
from depthfirstsearch import DepthFirstSearch
from topological import Topological

list_boxes = [] #Listas de caixas
paths = []

def read_boxes():
    global list_boxes
    #Leitura dos dados
    with open("Casos\\teste10.txt", "r") as archive: #Leitura das linhas do arquivo txt para uma variável 
        for lines in archive:         #Itera sobre as linhas do txt
            measure = lines.strip().split()     #Pega a linha e guarda em uma lista como strings
            name = re.sub('[^a-zA-Z0-9]', '', lines)    #Guarda o nome da caixa como as dimensoes
            map(int, measure)                           #Troca o valor das dimensoes para int
            measure.sort()                              #Ordena para comparação
            smallest, medium, greater = map(int, measure)   #Adiciona os valores em ordem
            
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

#NÂO MEXER PRA CIMA ===================================================================================================

# Função para calcular o caminho máximo para cada box na lista list_boxes
def caminho_maximo_para_boxes(d, list_boxes):
    global paths
    for box in list_boxes:
        #print(box)
        if (box.contem_IsEmpty()):
            dfs = DepthFirstSearch(d, box.get_name())
            #print(box.get_name())
            for v in list_boxes:
                caminho = 0   
                if dfs.hasPathTo(v.get_name()):
                    #print("Sim")
                    if caminho < (len(dfs.pathTo(v.get_name()))):
                        caminho = len(dfs.pathTo(v.get_name())) + 1
                        paths.append(caminho)
                    else:
                         caminho = len(dfs.pathTo(v.get_name())) + 1
                         paths.append(caminho)
                else:
                    paths.append(caminho)
                #print(caminho)
               
 

    # for v in d.getVerts():
    #     print(f"{v}: ", end="")
    #     if dfs.hasPathTo(v):
    #         for w in dfs.pathTo(v):
    #             print(f"{w} ", end="")
    #     print()
    # print()

def main():
    global list_boxes, paths

    read_boxes()
    compare_boxes()
    write_txt()
    d = Digraph("Resultados\\grafo.txt")
    dot(d)

    caminho_maximo_para_boxes(d, list_boxes)

    paths.sort(reverse=True)
    print(paths[0])

    # dfs = DepthFirstSearch(d, "680579148")
    # print(d.getAdj("680579148"))
    # print(dfs.pathTo("988955720"))
        
    
    

    #NÂO MEXER PRA CIMA ===================================================================================================    


    #Entendendo o problema
    #Pegar cada caixa e percorrer até o final usando a busca em profundidade, guardar o maior caminho
    #Pensando no seguinte, se tiver uma caixa1 que cabe dentro da caixa2, então o caminho maximo nunca vira da caixa2
    #E sim da caixa1, tendo uma lista em cada caixa, das caixas que cabem dentro dela
    #Podemos testar se algum caixa cabe dentro dela, se sim, não faz sentido testar se a partir dela existe um caminho maximo
    #Isso corta muitos vertices dag, então tentariamos a partir das caixas que não possuem uma ligação previa nelas 

if __name__ == "__main__":
    main() 