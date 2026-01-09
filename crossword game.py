x = "LEARNING"
y = "SCIENCE"
z = "FUN"
# to set x,y and z as the default words in the game
words_input = input("Enter first word (or press Enter to use default words): ")
if words_input:
    word1 = words_input.upper()
    word2 = input("Enter second word: ").upper()
    word3 = input("Enter third word: ").upper()
    words = [word1, word2, word3]
else:
    words = [x, y, z] #use the default words if no input is given
import random
import string
# Set the grid size
rows = 10
cols = 10 # Set the grid size
def create_grid(rows, cols, words):
    grid = [[' ' for _ in range(cols)] for _ in range(rows)] # create an empty grid
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)] # horizontal, vertical, diagonal down-right, diagonal down-left
    for word1 in words: # place the first word in the grid
        placed = False
        while not placed:  # keep trying until the word is placed
            direction = random.choice(directions)
            if direction == (0, 1):  # horizontal
                row = random.randint(0, rows - 1)
                col = random.randint(0, cols - len(word1))   # ensure the word fits in the grid
            elif direction == (1, 0):  # vertical
                row = random.randint(0, rows - len(word1))
                col = random.randint(0, cols - 1)
            elif direction == (1, 1):  # diagonal down-right
                row = random.randint(0, rows - len(word1))
                col = random.randint(0, cols - len(word1))
            else:  # diagonal down-left
                row = random.randint(0, rows - len(word1))
                col = random.randint(len(word1) - 1, cols - 1)

            # Check if the word can be placed
            can_place = True
            for i in range(len(word1)):
                r = row + i * direction[0]
                c = col + i * direction[1]
                if grid[r][c] not in (' ', word1[i]):
                    can_place = False
                    break
            
            if can_place:
                for i in range(len(word1)):
                    r = row + i * direction[0]
                    c = col + i * direction[1]
                    grid[r][c] = word1[i]
                placed = True
    for word2 in words: # place the second word
        placed = False
        while not placed:  # keep trying until the word is placed
            direction = random.choice(directions)
            if direction == (0, 1):  # horizontal
                row = random.randint(0, rows - 1)
                col = random.randint(0, cols - len(word2))   # ensure the word fits in the grid
            elif direction == (1, 0):  # vertical
                row = random.randint(0, rows - len(word2))
                col = random.randint(0, cols - 1)
            elif direction == (1, 1):  # diagonal down-right
                row = random.randint(0, rows - len(word2))
                col = random.randint(0, cols - len(word2))
            else:  # diagonal down-left
                row = random.randint(0, rows - len(word2))
                col = random.randint(len(word2) - 1, cols - 1)

            # Check if the word can be placed
            can_place = True
            for i in range(len(word2)):
                r = row + i * direction[0]
                c = col + i * direction[1]
                if grid[r][c] not in (' ', word2[i]):
                    can_place = False
                    break
            
            if can_place:
                for i in range(len(word2)):
                    r = row + i * direction[0]
                    c = col + i * direction[1]
                    grid[r][c] = word2[i]
                placed = True
    for word3 in words: # place the third word
        placed = False
        while not placed:  # keep trying until the word is placed
            direction = random.choice(directions)
            if direction == (0, 1):  # horizontal
                row = random.randint(0, rows - 1)
                col = random.randint(0, cols - len(word3))   # ensure the word fits in the grid
            elif direction == (1, 0):  # vertical
                row = random.randint(0, rows - len(word3))
                col = random.randint(0, cols - 1)       
            elif direction == (1, 1):  # diagonal down-right
                row = random.randint(0, rows - len(word3))
                col = random.randint(0, cols - len(word3))
            else:  # diagonal down-left
                row = random.randint(0, rows - len(word3))
                col = random.randint(len(word3) - 1, cols - 1)
            # Check if the word can be placed
            can_place = True
            for i in range(len(word3)):
                r = row + i * direction[0]
                c = col + i * direction[1]
                if grid[r][c] not in (' ', word3[i]):
                    can_place = False
                    break

            if can_place:
                for i in range(len(word3)):
                    r = row + i * direction[0]
                    c = col + i * direction[1]
                    grid[r][c] = word3[i]
                placed = True
    # Fill empty spaces with random letters
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == ' ':
                grid[r][c] = random.choice(string.ascii_uppercase)

    return grid

grid = create_grid(rows, cols, words)

# Print the grid row by row
for row in grid:
    print(" ".join(row))
print("\nFind the words:", ", ".join(words))