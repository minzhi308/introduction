layers = input("Enter the number of layers (2 to 5) = ")
side_length = input("Enter the side length of the top layer = ")
growth = input("Enter the growth of each layer = ")
trunk_width = input("Enter the trunk width (odd number, 3 to 9) = ")
trunk_height = input("Enter the trunk height (4 to 10) = ")

layers = int(layers)
side_length = int(side_length)
growth = int(growth)
trunk_width = int(trunk_width)
trunk_height = int(trunk_height)

# Use ‘#’ as the sides of each triangle, and use ‘@’ as the internal part of each triangle.
# Use ‘|’ to represent the trunk part of the Christmas Tree.

last_layer_side_length = side_length + (layers - 1) * growth
# print("The last layer side length is", last_layer_side_length)
last_layer_bottom = 2 * last_layer_side_length - 1
# print("The last layer bottom length is", last_layer_bottom)

# Draw the tree
for i in range(layers):
    for j in range(side_length):
        # space = (last_layer_bottom - ((j * 2 - 1) + 2)) // 2
        middle_length = j * 2 - 1
        space = (last_layer_bottom - (middle_length + 2)) // 2
        # space = 0
        if i == 0 and j == 0:
            print(" " * space + "#" + " " * space)
        elif j == 0:
            pass
        elif j == side_length - 1:
            print(" " * space + "#" + "#" * middle_length + "#" + " " * space)
        else:
            print(" " * space + "#" + "@" * middle_length + "#" + " " * space)

    side_length += growth

# Draw the trunk
space = (last_layer_bottom - trunk_width) // 2
for i in range(trunk_height):
    print(" " * space + "|" * trunk_width + " " * space)

#會計系 H14126173 賈閔之
