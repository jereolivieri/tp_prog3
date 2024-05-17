from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node

#calculamos la distancia de manhattan
def manhattan(nodo_estado,final):
    xf , yf = final 
    x , y = nodo_estado
    distancia = abs(x-xf)+abs(yf-y)
    return distancia


class GreedyBestFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Greedy Best First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", grid.start, 0)

        #definimos la frontera como una cola y agregamos el nodo
        frontier = PriorityQueueFrontier()
        frontier.add(node,manhattan(node.state,grid.end))   

        # Initialize the explored dictionary to be empty
        explored = {node.state : node.cost} 

        #iniciamos el bucle       
        while True:

            #print('después de agregar \n',frontier)
            #si no hubiera mas nodos en la frontera, no hay solucion
            if frontier.is_empty():
                #print('a \n')
                return NoSolution(explored)
            
            #sacamos el siguiente nodo de la frontera
            new_node = frontier.pop()

            #si el nodo es solucion, devuelve el nodo y el camino explorado
            if new_node.state==grid.end:
                return Solution(new_node,explored)
            
            #agrega los nodos vecinos a la lista de sucesores
            successors=grid.get_neighbours(new_node.state)
            #para cada movimiento posible, definimos el estado nuevo como uno de los posibles movimientos
            #print('suc')
            for act in successors:
                #print(act)
                estado_nuevo=successors[act]
                #actualizamos el costo
                costo_nuevo = new_node.cost + grid.get_cost(estado_nuevo)
                #si el estado nuevo no fue explorado o el costo nuevo es menor, lo definimos como el nuevo nodo
                if estado_nuevo not in explored or costo_nuevo < explored[estado_nuevo]:
                    new_node_prima = Node("", estado_nuevo,
                                    costo_nuevo,
                                    parent=new_node,action=act)
                    #agregamos el costo nuevo 
                    explored[estado_nuevo]=costo_nuevo
                    #si no es solucion agrgamos el nodo a la frontera
                    frontier.add(new_node_prima,manhattan(new_node_prima.state,grid.end))

        #return NoSolution(explored)
