from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


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
        frontier.add(node)    

        # Initialize the explored dictionary to be empty
        explored = {node.state : node.cost} 
        
        while True:
            if frontier.is_empty:
                return NoSolution(explored)

            new_node = frontier.remove()

            if new_node.state==grid.end:
                return Solution(new_node,explored)
            
            successors=grid.get_neighbours(new_node.state)

            for act in successors:
                estado_nuevo=successors[act]

                costo_nuevo = new_node.cost + estado_nuevo.cost

                if estado_nuevo not in explored or costo_nuevo < explored[estado_nuevo]:
                    new_node = Node("", estado_nuevo,
                                    node.cost + grid.get_cost(estado_nuevo),
                                    parent=node,action=act)
                    explored[estado_nuevo]=costo_nuevo
                    frontier.add(new_node)
                



        return NoSolution(explored)
