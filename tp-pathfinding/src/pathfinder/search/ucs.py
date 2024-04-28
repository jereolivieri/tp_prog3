from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node
from ..models.frontier import PriorityQueueFrontier

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
        node = Node("", grid.start, 0)

        # Initialize the explored dictionary to be empty
        explored = {} 
        
        # Add the node to the explored dictionary
        explored[node.state] = True
        
        if node.state == grid.end:
            return Solution(node,explored)

        frontier = PriorityQueueFrontier()
        frontier.add(node, node.cost)
        explored = {node.state: node.cost}


        while True:

            if frontier.is_empty():
                return NoSolution(explored)

            node = frontier.pop()

            successors=grid.get_neighbours(node.state)
            
            for act in successors:
                estado_nuevo=successors[act]
                
                costo_nuevo = node.cost + estado_nuevo.cost

                if estado_nuevo not in explored or costo_nuevo < explored[estado_nuevo].cost:
                    new_node = Node("", estado_nuevo,
                                    node.cost + grid.get_cost(estado_nuevo),
                                    parent=node,action=act)

                    if estado_nuevo == grid.end:
                        return Solution(new_node, explored)                    

                    explored[estado_nuevo]=True

                    frontier.add(new_node.cost, new_node)

        return NoSolution(explored)
