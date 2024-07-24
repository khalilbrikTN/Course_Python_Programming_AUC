
# Helper function to print the grid
def print_grid(grid):
    for row in grid:
        print(' '.join(map(str, row)))
    print()
    # Function to check if a position is within grid bounds
def is_within_bounds(x, y, m, n):
    return 0 <= x < m and 0 <= y < n

# Function to check if a position is on the border of the grid
def is_border_position(x, y, m, n):
    return x == 0 or x == m - 1 or y == 0 or y == n - 1

def GridEscape(n, m):
    from random import randint, choice

    # Get random starting position of the ant in the grid.
    col_position = randint(0, n - 1)
    row_position = randint(0, m - 1)

    # Create the initial grid with the ant's starting position marked as 'x'
    matrix = [[0 for _ in range(n)] for _ in range(m)]
    matrix[row_position][col_position] = 'x'

    # Store the grid status
    grid_status = []
    grid_status.append([row[:] for row in matrix])

    move_count = 1


    # Possible moves: (row change, column change)
    possible_moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    while True:
        # Filter out the move that would take the ant back to the previous position
        valid_moves = [(dr, dc) for dr, dc in possible_moves
                       if is_within_bounds(row_position + dr, col_position + dc, m, n)
                       and grid_status[-1][row_position + dr][col_position + dc] == 0]

        # If no valid moves are possible, break the loop (stuck condition)
        if not valid_moves:
            break

        # Choose a random valid move
        dr, dc = choice(valid_moves)

        # Update the ant's position
        row_position += dr
        col_position += dc

        # Mark the new position with the move count
        matrix[row_position][col_position] = move_count

        # Add the new state of the grid to the grid status
        grid_status.append([row[:] for row in matrix])

        move_count += 1

        # Check if the ant has reached the border
        if is_border_position(row_position, col_position, m, n):
            break

    # Print the initial grid
    print("Initial Grid:")
    print_grid(grid_status[0])

    # Print the final grid
    print("Final Grid:")
    print_grid(grid_status[-1])


GridEscape(5, 5)
GridEscape(4, 5)
GridEscape(3, 5)
