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
        
        if node.state == grid.end:
            return Solution(node,explored)        

        frontier=StackFrontier()
        frontier.add(node)

        explored = {} 

        while True:

            if frontier.is_empty():
                return NoSolution(explored)

            node=frontier.remove()

            if node.state in explored:
                continue

            explored[node.state] = True

            successors=grid.get_neighbours(node.state)

            for act in successors:
                estado_nuevo=successors[act]

                if estado_nuevo==grid.end:
                    return Solution(new_node,explored)

                if estado_nuevo not in explored:
                    new_node=Node("", estado_nuevo,
                                    node.cost + grid.get_cost(estado_nuevo),
                                    parent=node,action=act)

                    frontier.add(new_node)

        return NoSolution(explored)
