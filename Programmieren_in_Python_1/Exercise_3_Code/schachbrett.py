def draw_chessboard(n, s, upper_left = 'black'):
    
    black_white = int(n/2) * (s * '1' + s * '0')
    white_black = int(n/2) * (s * '0' + s * '1')
    
    if upper_left == 'black':
        first = black_white
        second = white_black
    else:
        first = white_black
        second = black_white
    
    for n_row in range(int(n/2)):
        for s_row in range(s):
            print(first)
        for s_row in range(s):
            print(second)

# draw example
draw_chessboard(6, 3, upper_left = 'white')