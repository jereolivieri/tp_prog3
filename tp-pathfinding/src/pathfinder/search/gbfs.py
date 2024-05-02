from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node

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

        frontier = PriorityQueueFrontier()

        frontier.add(node,manhattan(node.state,grid.end))   

        # Initialize the explored dictionary to be empty
        explored = {node.state : node.cost} 
        
        while True:

            #print('después de agregar \n',frontier)

            if frontier.is_empty():
                #print('a \n')
                return NoSolution(explored)

            new_node = frontier.pop()

            if new_node.state==grid.end:
                return Solution(new_node,explored)

            successors=grid.get_neighbours(new_node.state)
            #print('suc')
            for act in successors:
                #print(act)
                estado_nuevo=successors[act]
                
                costo_nuevo = new_node.cost + grid.get_cost(estado_nuevo)

                if estado_nuevo not in explored or costo_nuevo < explored[estado_nuevo]:
                    new_node_prima = Node("", estado_nuevo,
                                    costo_nuevo,
                                    parent=new_node,action=act)
                    
                    explored[estado_nuevo]=costo_nuevo

                    frontier.add(new_node_prima,manhattan(new_node_prima.state,grid.end))

        return NoSolution(explored)
