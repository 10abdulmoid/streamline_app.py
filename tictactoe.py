import streamlit as st

# Define game state
board = [" " for _ in range(9)]
current_player = "X"
game_over = False

# Winning conditions
winning_conditions = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
    (0, 4, 8), (2, 4, 6)            # Diagonals
]


# Function to check for a winner
def check_winner():
    global game_over
    for condition in winning_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != " ":
            game_over = True
            return board[condition[0]]
    # Check for a draw
    if all(x != " " for x in board) and not game_over:
        game_over = True
        return "Draw"
    return None


# Function to handle player clicks
def handle_click(index):
    global board, current_player
    if board[index] == " " and not game_over:
        board[index] = current_player
        winner = check_winner()
        if winner:
            st.write(f"{winner} Wins!")
        else:
            current_player = "X" if current_player == "O" else "O"


# Streamlit app layout
st.title("Tic Tac Toe")
st.write("Current Player:", current_player)

for i in range(3):
    col1, col2, col3 = st.columns(3)
    col1.button(board[i * 3], key=f"{i * 3}", on_click=lambda x=i * 3: handle_click(x), disabled=game_over)
    col2.button(board[i * 3 + 1], key=f"{i * 3 + 1}", on_click=lambda x=i * 3 + 1: handle_click(x), disabled=game_over)
    col3.button(board[i * 3 + 2], key=f"{i * 3 + 2}", on_click=lambda x=i * 3 + 2: handle_click(x), disabled=game_over)

if game_over:
    st.button("Reset Game", on_click=lambda: [global board, current_player, game_over; board = [" " for _ in range(9)], current_player = "X", game_over = False])

