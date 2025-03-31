# This is problem to convert all the negative coordinates to a positive coordinates;
# The agenda is to get all the coordinates in 0 or positive values keeping the relative distance same;
# We can add or delete any number from the coordinates ; however graph should not be changed;

# Input: [(1,-2), (-2, 4), (-1,-1),(-8, -3), (0, 4), (10,-3)]
# Output : [(9,6), (6, 12), (7,7),(0, 5), (8, 12), (18,5)]

def convert_coordinates(coordinates):
    # Find the minimum val in coordinates
    minimum = min([min(coord) for coord in coordinates])
    offset = -minimum if minimum < 0 else 0
    converted_coordinates = [(x + offset, y + offset) for x, y in coordinates]

    return converted_coordinates

input_coordinates = [(1, -2), (-2, 4), (-1, -1), (-8, -3), (0, 4), (10, -3)]
output_coordinates = convert_coordinates(input_coordinates)
print(output_coordinates)