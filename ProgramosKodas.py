import matplotlib.pyplot as plt

# Duotas skaičių sąrašas
h1 = [2, 2, 3, 5, 5, 6, 3, 1, 2, 5, 8, 10, 14, 9, 7, 4, 3, 2]

def find_highest_support(heights):
    # Grąžina aukščiausios atramos numerį (indeksą)
    return heights.index(max(heights))

def find_lowest_supports(heights):
    # Grąžina žemiausių atramų numerius (indeksus)
    lowest_support = min(heights)
    return  [index for index, height in enumerate(heights) if height == lowest_support]

def find_longest_rise(heights):
    # Suranda ilgiausią pakilimą ir grąžina jo pradžios atramos numerį bei atramų skaičių
    longest = 0
    current_length = 0
    start_index = 0
    for i in range(1, len(heights)):
        if heights[i] > heights[i-1]:
            if current_length == 0:
                current_start = i-1
            current_length += 1
        else:
            if current_length > longest:
                longest = current_length
                start_index = current_start
            current_length = 0
    return start_index, longest + 1 if longest > 0 else 0

def find_peaks(heights):
    # Suranda visus pikus
    peaks = []
    for i in range(1, len(heights) - 1):
        if heights[i] > heights[i-1] and heights[i] > heights[i+1]:
            peaks.append(i)
    return peaks

def find_steepestAscent_and_descent(heights):
    # Suranda staciausia pakilima ir nusileidima
    start_of_ascend=0
    ascend_height=0
    start_of_descend=0
    descend_height=0
    for i in range(1, len(heights)):
        if heights[i] > heights[i-1] and heights[i] - heights[i-1] > ascend_height:
            ascend_height = heights[i] - heights[i-1]
            start_of_ascend = i-1
        if heights[i] < heights[i-1] and heights[i-1] - heights[i] > descend_height:
            descend_height = heights[i-1] - heights[i]
            start_of_descend = i-1
    return start_of_ascend, ascend_height, start_of_descend, descend_height

# Funkcijų išbandymas
highest_support = find_highest_support(h1)
lowest_supports = find_lowest_supports(h1)
longest_rise_start, longest_rise_length = find_longest_rise(h1)
peaks = find_peaks(h1)

start_of_ascend, ascend_height, start_of_descend, descend_height = find_steepestAscent_and_descent(h1)

# Rezultatų spausdinimas
print(f"Highest support number: {highest_support}")
print(f"Lowest supports numbers: {lowest_supports}")
print(f"Longest rise starts at support number {longest_rise_start} and includes {longest_rise_length} supports")
print(f"Peaks at supports numbers: {peaks}")

# Grafiko braižymas
plt.figure(figsize=(10, 6))
plt.plot(h1, label="Height", marker='o')
plt.plot([start_of_ascend, start_of_ascend + 1], [h1[start_of_ascend], h1[start_of_ascend + 1]], label=f"Steepest Ascend = {ascend_height}",marker='o', linestyle='-', linewidth=2, color='magenta')
plt.plot([start_of_descend, start_of_descend + 1], [h1[start_of_descend], h1[start_of_descend + 1]], label=f"Steepes Descent = {descend_height}",marker='o', linestyle='-', linewidth=2, color='cyan')

plt.scatter(peaks, [h1[i] for i in peaks], color='red', label="Peaks", marker='+', zorder=4)

plt.scatter(longest_rise_start, h1[longest_rise_start], color='black', marker='x', label="Start of the longest rise", zorder=3)

plt.scatter(range(longest_rise_start, longest_rise_start + longest_rise_length), 
            [h1[i] for i in range(longest_rise_start, longest_rise_start + longest_rise_length)], 
            color='yellow', s=50, label="Longest Rise", zorder=2)

plt.title("American Roller Coaster Supports")
plt.xlabel("Support Number")
plt.ylabel("Height")
plt.legend()
plt.show()