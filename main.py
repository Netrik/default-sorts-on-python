from autotests import *
class allsorts:
    def bubblesort(numbers):
        i = 0
        j = 0
        swap = True
        while swap:
            swap = False
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                swap = True
            i += 1
        return numbers
    def choicesort(numbers):
        i = 0
        j = 0
        while i < len(numbers) - 1:
            minimal = i
            j = i + 1
            while j < len(numbers):
                if numbers[j] < numbers[minimal]:
                    minimal = j
                numbers[i], numbers[minimal] = numbers[minimal], numbers[i]
                j += 1
            i += 1
        return numbers
    def insertsort(numbers):
        i = 1
        j = 0
        while i < len(numbers):
            temp = numbers[i]
            j = i - 1
            while j >= 0 and temp < numbers[j]:
                numbers[j + 1] = numbers[j]
                j -= 1
            numbers[j + 1] = temp
            i += 1
        return numbers