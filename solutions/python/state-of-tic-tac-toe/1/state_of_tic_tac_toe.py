def gamestate(board):
    board = [list(row) for row in board]
    cells = [cell for row in board for cell in row]
    
    x_count = cells.count('X')
    o_count = cells.count('O')
    
    # Turn order validation
    if o_count > x_count:
        raise ValueError("Wrong turn order: O started")
    
    if x_count - o_count > 1:
        raise ValueError("Wrong turn order: X went twice")
    
    # Winning lines
    lines = []
    for i in range(3):
        lines.append(board[i])
        lines.append([board[0][i], board[1][i], board[2][i]])
    
    lines.append([board[0][0], board[1][1], board[2][2]])
    lines.append([board[0][2], board[1][1], board[2][0]])
    
    x_wins = any(line == ['X', 'X', 'X'] for line in lines)
    o_wins = any(line == ['O', 'O', 'O'] for line in lines)
    
    # Both players winning → invalid
    if x_wins and o_wins:
        raise ValueError("Impossible board: game should have ended after the game was won")
    
    # Validate win states
    if x_wins:
        if x_count != o_count + 1:
            raise ValueError("Impossible board: game should have ended earlier")
        return "win"
    
    if o_wins:
        if x_count != o_count:
            raise ValueError("Impossible board: game should have ended earlier")
        return "win"
    
    # Draw or ongoing
    if all(cell in ['X', 'O'] for cell in cells):
        return "draw"
    
    return "ongoing"