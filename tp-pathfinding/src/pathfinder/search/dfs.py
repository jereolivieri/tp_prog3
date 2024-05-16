from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

        Args:
            grid (Grid): Grid of points
            
        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", grid.start, 0)
        
        #si el nodo es igual al estado final, retorna es solucion
        if node.state == grid.end:
            return Solution(node,explored)        

        #definimos la frontera como una pila y agregamos el nodo
        frontier=StackFrontier()
        frontier.add(node)

        # Initialize the explored dictionary to be empty
        explored = {} 

        #iniciamos el bucle
        while True:

            #si no hubiera mas nodos en la frontera, no hay solucion
            if frontier.is_empty():
                return NoSolution(explored)

            #sacamos el siguiente nodo de la frontera
            node=frontier.remove()

            if node.state in explored:
                continue

            explored[node.state] = True

            successors=grid.get_neighbours(node.state)
            #para cada movimiento posible en la lista de sucesores, definimos el estado nuevo como uno de los posibles movimientos    
            for act in successors:
                estado_nuevo=successors[act]

                #si el estado nuevo no fue explorado lo definimos como el nuevo nodo
                if estado_nuevo not in explored:
                    new_node=Node("", estado_nuevo,
                                    node.cost + grid.get_cost(estado_nuevo),
                                    parent=node,action=act)
                    
                    #si el estado nuevo es igual al objetivo devolvemos solucion                   
                    if estado_nuevo==grid.end:
                        return Solution(new_node,explored)
                    
                    #si no es solucion agrgamos el nodo a la frontera
                    frontier.add(new_node)

        return NoSolution(explored)
