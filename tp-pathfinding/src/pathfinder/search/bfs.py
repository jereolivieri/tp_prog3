from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class BreadthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Breadth First Search

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

        frontier = QueueFrontier()
        frontier.add(node)        

        while True:

            if frontier.is_empty():
                return NoSolution(explored)

            node = frontier.remove()

            successors=grid.get_neighbours(node.state)
            
            for act in successors:
                estado_nuevo=successors[act]

                if estado_nuevo not in explored:
                    new_node = Node("", estado_nuevo,
                                    node.cost + grid.get_cost(estado_nuevo),
                                    parent=node,action=act)

                    if estado_nuevo == grid.end:
                        return Solution(new_node, explored)                    

                    explored[estado_nuevo]=True

                    frontier.add(new_node)

        return NoSolution(explored)
