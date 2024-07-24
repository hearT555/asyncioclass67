import time

my_compute_time = 0.1  # Judit's thinking time in seconds
opponent_compute_time = 0.5  # Opponent's thinking time in seconds
opponents = 5  # Number of opponents
move_pairs = 30  # Number of move pairs

def game(x):
    # Loops 30 times to simulate both players making a move
    board_start_time = time.perf_counter()
    for i in range(move_pairs):
        time.sleep(my_compute_time)
        print(f"BOARD-{x} ({i+1}) Judit made a move.")
        
        time.sleep(opponent_compute_time)
        print(f"BOARD-{x} ({i+1}) Opponent made move.")
        
    print(f"BOARD-{x} >>>>>>>>>>>>>>> Finished move in {round(time.perf_counter() - board_start_time)} secs\n")
    return round(time.perf_counter() - board_start_time)

if __name__ == "__main__":
    start_time = time.perf_counter()
    board_time = 0
    # Loops 24 times because we are playing 24 opponents
    for board in range(opponents):
        board_time += game(board)
    
    print(f"Board exhibition finished in {board_time} secs.")
    print(f"Finished in {round(time.perf_counter() - start_time)} secs.")
