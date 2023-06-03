from abc import ABC, abstractmethod


class Solver(ABC):
    def __init__(self, variables):
        self.vars = variables
        return

    @abstractmethod
    def update(self, grads):
        pass
