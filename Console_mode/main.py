def draw_map(map):
    tic_tac_toe_art = r"""
  ______ _          ______                ______           
 /_  __/(_)_____   /_  __/____ _ _____   /_  __/____   ___ 
  / /  / // ___/    / /  / __ `// ___/    / /  / __ \ / _ \
 / /  / // /__     / /  / /_/ // /__     / /  / /_/ //  __/
/_/  /_/ \___/    /_/   \__,_/ \___/    /_/   \____/ \___/                                                                                                                                                                                                                                                                                                              
"""
    print(tic_tac_toe_art)
    print('-------------')
    for line in map:
        print('| ' + " | ".join(str(item) if item != 0 else ' ' for item in line) + ' |')
        print('-------------')

def create_map():
    return [[0 for i in range(3)] for j in range(3)]

def check_winner(map, symbole):
    for i in range(3):
        if all(map[i][j] == symbole for j in range(3)):
            return True
        if all(map[j][i] == symbole for j in range(3)):
            return True 
    if all(map[i][i] == symbole for i in range(3)):
        return True
    if all(map[i][2-i] == symbole for i in range(3)):
        return True       
    return False

def game():
    map = create_map()
    symboles = ['X', 'O']
    round = 0

    while True:
        player = round % 2
        symbole = symboles[player]
        
        draw_map(map)

        while True:
            try:
                row = int(input('Player {} ({}) \nEnter a number for the row (1 - 3): '.format(player + 1, symbole))) - 1
                column = int(input('Player {} ({}) \nEnter a number for the column (1 - 3): '.format(player + 1, symbole))) - 1
                if (map[row][column] == 0):
                    map[row][column] = symbole
                    break
                else:
                    draw_map(map)
                    print("Someone already play here, choose another place")

            except KeyboardInterrupt:
                print("\nProgram interrupted by user (Ctrl+C).")
                exit()
            except(ValueError, IndexError):
                print("Enter values between 1 and 3!")
        
        if (check_winner(map, symbole)):
            draw_map(map)
            print('Player {} ({}) WIN!!\n'.format(player + 1, symbole))
            break
        if all(map[i][j] != 0 for i in range(3) for j in range(3)):
            draw_map(map)
            print("Tie game !")
            break
        round += 1
        
game()