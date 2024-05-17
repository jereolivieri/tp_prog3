from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node

def manhattan(nodo_estado,final):
    xf , yf = final 
    x , y = nodo_estado
    distancia = abs(x-xf)+abs(yf-y)
    return distancia


class AStarSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using A* Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", grid.start, 0)

        # definimos la frontera como cola de prioridad y le agregamos el nodo inicial con su costo
        frontier = PriorityQueueFrontier()
        frontier.add(node, node.cost + manhattan(node.state,grid.end))   

        # iniciar el diccionario de explorados con el nodo y su costo
        explored = {node.state : node.cost} 

        #iniciamos el bucle
        while True:

            #si la frontera quedara vacia no encuentra solucion
            if frontier.is_empty():
                return NoSolution(explored)

            #tomamos el siguiente nodo de la frontera, si es igual a la solucion nos devuelve el camino explorado
            new_node = frontier.pop()
            if new_node.state==grid.end:
                return Solution(new_node,explored)

            #agregamos las casillas vecinas a la lista de sucesores
            successors=grid.get_neighbours(new_node.state)
            for act in successors:
                estado_nuevo=successors[act]
                
                #actualizamos el costo del camino
                costo_nuevo = new_node.cost + grid.get_cost(estado_nuevo)

                #si el estado nuevo no fue explorado o el costo nuevo es menor, lo definimos como el nuevo nodo
                if estado_nuevo not in explored or costo_nuevo < explored[estado_nuevo]:
                    new_node_prima = Node("", estado_nuevo,
                                    costo_nuevo,
                                    parent=new_node,action=act)
                    explored[estado_nuevo]=costo_nuevo
                    #si no es solucion agrgamos el nodo a la frontera
                    frontier.add(new_node_prima,new_node_prima + manhattan(new_node_prima.state,grid.end))

        #return NoSolution(explored)
