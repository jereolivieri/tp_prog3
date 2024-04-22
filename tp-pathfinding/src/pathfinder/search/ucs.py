from ..models.grid import Grid
from ..models.frontier import StackFrontier
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
        node = Node("", grid.start, 0)


        # Initialize the explored dictionary with the position's node
        explored = {node.state: node}


        # Creo la frontera
        frontier = PriorityQueueFrontier()
        frontier.add(node, node.cost)



        while True:


            #  Fail if the frontier is empty
            if frontier.is_empty():
                return NoSolution(explored)

            # Explorar el nodo
            node = frontier.pop()


            # Test Objetivo
            if node.state == grid.end:
                return Solution(node, explored)

            # Explorar estados
            successors = grid.get_neighbours(node.state)


            for action, postion in successors.items():
                c_cost = node.cost + grid.get_cost(postion)

                # Chequeo que si ya estaba alcanzado por un costo menor o no alcanzado
                if postion not in explored or c_cost < explored[postion].cost:
                    c_node = Node(
                        value="",
                        state=postion,
                        cost=c_cost,
                        parent=node,
                        action=action)

                    frontier.add(c_node, c_node.cost)
                    # actualizo su costo
                    explored[c_node.state] = c_node

