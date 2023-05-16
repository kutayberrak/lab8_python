from abc import ABC, abstractmethod


class TextAnalyzer(ABC):
    def __init__(self, address):
        self.address = address

    @abstractmethod
    def calculateFreqs(self):
        pass


class ListCount(TextAnalyzer):
    def calculateFreqs(self):
        frequency_list = [0] * 26

        with open(self.address, 'r') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        index = ord(char.lower()) - ord('a')
                        frequency_list[index] += 1

        for i, frequency in enumerate(frequency_list):
            char = chr(ord('a') + i)
            print(f"List -> {char} Resulting List -> {char} = {frequency}")


class DictCount(TextAnalyzer):
    def calculateFreqs(self):
        frequency_dict = {}

        with open(self.address, 'r') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        char = char.lower()
                        frequency_dict[char] = frequency_dict.get(char, 0) + 1

        sorted_dict = dict(sorted(frequency_dict.items()))

        for char, frequency in sorted_dict.items():
            print(f'Dict -> "{char}" 0 Updated Dict -> "{char}" {frequency}')


file_address = "weirdWords.txt"

list_counter = ListCount(file_address)
print("ListCount:")
list_counter.calculateFreqs()

print("\n")

dict_counter = DictCount(file_address)
print("DictCount:")
dict_counter.calculateFreqs()
