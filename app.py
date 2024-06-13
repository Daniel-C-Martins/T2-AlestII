#Classe principal do programa
from box import Box

list_boxes = [] #Listas de caixas


def read_boxes():
    global list_boxes
    #Leitura dos dados
    with open("Casos\\exemplo.txt", "r") as archive: #Leitura das linhas do arquivo txt para uma variável 
        id = 1
        for lines in archive:         #"For" responsável por ler cada linha
            measure = lines.strip().split()
            
            map(int, measure)
            measure.sort()
            smallest, medium, greater = map(int, measure)
            
            box = Box(id, greater, medium, smallest)
            list_boxes.append(box)
            id+=1
    

def compare_boxes():
    global list_boxes

    for i in range(len(list_boxes)):
        for j in range(len(list_boxes)):
            if i == j:
                continue
            elif (list_boxes[i].get_large_side() > list_boxes[j].get_large_side() and
                list_boxes[i].get_medium_side() > list_boxes[j].get_medium_side() and
                list_boxes[i].get_small_side() > list_boxes[j].get_small_side()):
                list_boxes[i].add_contem(list_boxes[j].get_name())


def write_txt():
    global list_boxes
    with open("Resultados\\grafo.txt", "w") as archive:
        for box in list_boxes:
            for contem_id in box.contem:
                line = f"{box.get_name()} {contem_id} \n"
                archive.write(line)

               


def main():
    global list_boxes

    read_boxes()
    compare_boxes()
    write_txt()
    
    for caixa in list_boxes:
        print(caixa)
    

if __name__ == "__main__":
    main() 