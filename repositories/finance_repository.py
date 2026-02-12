from abc import ABC, abstractmethod


class FinanceRepository(ABC):

    @abstractmethod
    def add(self, description, costs, total) -> None:
        pass

    @abstractmethod
    def update(self, record_id, description, costs, total) -> None:
        pass

    @abstractmethod    
    def delete(self, record_id) -> None:
        pass

    @abstractmethod
    def fetch_all(self) -> None:
        pass
