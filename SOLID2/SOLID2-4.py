from abc import ABC, abstractmethod


class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data: list) -> list:
        pass


class BubbleSort(SortStrategy):
    def sort(self, data: list) -> list:
        arr = data[:]
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr


class BuiltinSort(SortStrategy):
    def sort(self, data: list) -> list:
        return sorted(data)


class Sorter:
    def sort(self, data: list, strategy: SortStrategy) -> list:
        return strategy.sort(data)


class ReverseSort(SortStrategy):
    def sort(self, data: list) -> list:
        return sorted(data, reverse=True)


numbers = [5, 3, 8, 1, 9, 2]
sorter = Sorter()

print(sorter.sort(numbers, BubbleSort()))
print(sorter.sort(numbers, BuiltinSort()))
print(sorter.sort(numbers, ReverseSort()))
