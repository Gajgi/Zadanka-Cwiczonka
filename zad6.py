#Napisz funkcję, która przyjmuje dwa parametry: listę liczb oraz wartość progową.
# Funkcja powinna zwrócić nową listę zawierającą tylko te liczby, które są większe od wartości progowej.

def filter_above_threshold(numbers, threshold):
    return [numbers for numbers in numbers if numbers > threshold]


numbers = [3, 7, 1, 4, 9, 12, 6]
threshold = 5
filtered_numbers = filter_above_threshold(numbers, threshold)
print(filtered_numbers)  