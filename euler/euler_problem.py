from abc import ABC, abstractmethod

class EulerProblem(ABC):
    @abstractmethod
    def solve(self) -> int:
        raise Exception('Pls implement solve() method')
