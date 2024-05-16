from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Uniform Cost Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", state=grid.start, cost=0)

        # Initialize the explored dictionary
        explored = {node.state: node}

        #definimos la frontera como una cola y agregamos el nodo con su costo
        frontier = PriorityQueueFrontier()
        frontier.add(node, node.cost)

        #iniciamos el bucle, mientras la frontera no este vacia, tomamos el prox nodo segun la prioridad
        while not frontier.is_empty():
            node = frontier.pop()

            #si el estado del nodo es igual al objetivo, retornamos solucion
            if node.state == grid.end:
                return Solution(node, explored)

            #agrega los nodos vecinos a la lista de sucesores
            succesors = grid.get_neighbours(node.state)

            #para cada movimiento posible, definimos el estado nuevo como uno de los posibles movimientos
            for action, estado_nuevo in succesors.items():
                #definimos nuevo costo, sumando al costo del nodo al costo del estado
                new_cost = node.cost + grid.get_cost(estado_nuevo)

                #si el estado nuevo no fue explorado o el costo nuevo es menor, lo definimos como el nuevo nodo
                if estado_nuevo not in explored or new_cost < explored[estado_nuevo].cost:
                    new_node = Node(
                        value="",
                        state=estado_nuevo,
                        cost=new_cost,
                        parent=node,
                        action=action)
                    
                    #si no es solucion agrgamos el nodo a la frontera
                    frontier.add(new_node, new_node.cost)
                    explored[new_node.state] = new_node

        return NoSolution(explored)
