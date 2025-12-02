
BLUE = "\033[94m"    # Blue for Player X
RED = "\033[91m"     # Red for Player O
GREEN = "\033[92m"   # Green for win/draw messages
YELLOW = "\033[93m"  # Yellow for board lines
RESET = "\033[0m"    # Resets color to default


board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '] ,
    [' ', ' ', ' ']
]


def display_board():
    
    print(f"\n  {YELLOW}0 1 2{RESET}")
    print(f"{YELLOW}-------{RESET}")
    for i in range(3):
        row_str = f"{i}{YELLOW}|{RESET}"
        for j in range(3):
            cell = board[i][j]

            if cell == 'X':
                row_str += f" {BLUE}X{RESET} " 
            elif cell == 'O':
                row_str += f" {RED}O{RESET} "
            else:
                row_str += "   " 
            if j < 2: 
                row_str += f"{YELLOW}|{RESET}"
        print(row_str)
     
        if i < 2:
            print(f"{YELLOW}---+---+---{RESET}")
    print("\n")


def check_win(player):
    
    
   
    for row in board:
        if all([cell == player for cell in row]):
            return True
    
   
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
            
    
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    
    
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
        
    return False


def check_draw():
    """Checks if the board is full and no player has won."""
    
    for row in board:
        
        if ' ' in row:
            return False 
    return True 


def tic_tac_toe():
    current_player = 'X'
    turns = 0
    
    print(f"{GREEN}Welcome to Command-Line Tic-Tac-Toe!{RESET}")
    
    while turns < 9: 
        display_board()
        
        player_color = BLUE if current_player == 'X' else RED
        print(f"Player {player_color}{current_player}{RESET}'s turn.")
        
        try:
           
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            
           
            if not (0 <= row <= 2 and 0 <= col <= 2):
                print(f"{RED}Error: Row/Column must be 0, 1, or 2. Try again.{RESET}")
                continue
                
            if board[row][col] != ' ':
                print(f"{RED}Error: That spot is already taken! Try again.{RESET}")
                continue
                
          
            board[row][col] = current_player
            turns += 1
            
            if check_win(current_player):
                display_board()
                print(f"{GREEN}🎉🎉 Player {player_color}{current_player}{GREEN} wins! Congratulations! 🎉🎉{RESET}")
                break
                
           
            if check_draw(): 
                display_board()
                print(f"{GREEN}It's a draw!{RESET}")
                break
            
            current_player = 'O' if current_player == 'X' else 'X'
            
        except ValueError:
            print(f"{RED}Error: Invalid input. Please enter a number (0, 1, or 2).{RESET}")
            continue


if __name__ == "__main__":
    tic_tac_toe()