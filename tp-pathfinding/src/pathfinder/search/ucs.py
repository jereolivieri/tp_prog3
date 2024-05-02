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

        frontier = PriorityQueueFrontier()
        frontier.add(node, node.cost)

        while not frontier.is_empty():
            node = frontier.pop()

            if node.state == grid.end:
                return Solution(node, explored)

            succesors = grid.get_neighbours(node.state)

            for action, estado_nuevo in succesors.items():
                new_cost = node.cost + grid.get_cost(estado_nuevo)

                if estado_nuevo not in explored or new_cost < explored[estado_nuevo].cost:
                    new_node = Node(
                        value="",
                        state=estado_nuevo,
                        cost=new_cost,
                        parent=node,
                        action=action)
                    frontier.add(new_node, new_node.cost)
                    explored[new_node.state] = new_node

        return NoSolution(explored)
