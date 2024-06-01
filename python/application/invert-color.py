# original_color = "ABC123"
original_color = input("Original color: ")

# Convert hex to RGB
r = int(original_color[1:3], 16)
g = int(original_color[3:5], 16)
b = int(original_color[5:7], 16)

# Invert RGB values
r_inv = 255 - r
g_inv = 255 - g
b_inv = 255 - b

# Convert RGB back to hex
inverted_color = f'{r_inv:02X}{g_inv:02X}{b_inv:02X}'

print(inverted_color)
