from lxml import etree

# Define a simple 5x7 bitmap font for "Bramha" (1 = green dot, 0 = unchanged)
# Each letter is a 5x7 grid, 6 letters total
font = {
    'B': [
        [1, 1, 1, 0, 0],
        [1, 0, 0, 1, 0],
        [1, 0, 0, 1, 0],
        [1, 1, 1, 0, 0],
        [1, 0, 0, 1, 0],
        [1, 0, 0, 1, 0],
        [1, 1, 1, 0, 0]
    ],
    'r': [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0],
        [1, 0, 0, 1, 0],
        [1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0]
    ],
    'a': [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [1, 0, 0, 1, 0],
        [1, 0, 0, 1, 0],
        [1, 1, 1, 1, 0],
        [1, 0, 0, 1, 0]
    ],
    'm': [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 0, 0, 1, 0],
        [1, 1, 1, 1, 0],
        [1, 0, 0, 1, 0],
        [1, 0, 0, 1, 0],
        [1, 0, 0, 1, 0]
    ],
    'h': [
        [1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0],
        [1, 0, 0, 1, 0],
        [1, 0, 0, 1, 0],
        [1, 0, 0, 1, 0]
    ],
    'a2': [  # Second 'a'
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [1, 0, 0, 1, 0],
        [1, 0, 0, 1, 0],
        [1, 1, 1, 1, 0],
        [1, 0, 0, 1, 0]
    ]
}

# Load the SVG file
svg_file = "dist/github-snake.svg"
tree = etree.parse(svg_file)
root = tree.getroot()

# Find all <rect> elements (dots in the contribution grid)
rects = root.findall(".//{http://www.w3.org/2000/svg}rect")

# Assume the grid is approximately 53 weeks (x) by 7 days (y)
# Select a region for "Bramha" (e.g., starting at week 10, covering 6 letters)
start_week = 10
letter_width = 7  # Each letter uses 7 columns (5 for letter + 2 for spacing)
total_width = letter_width * 6  # 6 letters

# Map the font to the grid
for letter_idx, letter in enumerate(['B', 'r', 'a', 'm', 'h', 'a2']):
    letter_grid = font[letter]
    for row in range(7):  # 7 rows per letter
        for col in range(5):  # 5 columns per letter
            if letter_grid[row][col] == 1:
                # Calculate the target dot position
                week = start_week + letter_idx * letter_width + col
                day = row
                # Find the corresponding <rect> by its position
                for rect in rects:
                    x = float(rect.get('x', 0))
                    y = float(rect.get('y', 0))
                    # Approximate matching (x, y) to grid position
                    # SVG coordinates depend on the generated SVG; adjust if needed
                    if abs(x - week * 13) < 10 and abs(y - day * 13) < 10:  # 13 is typical dot spacing
                        rect.set('fill', '#00FF00')  # Green color
                        break

# Save the modified SVG
tree.write(svg_file)