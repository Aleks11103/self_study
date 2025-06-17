class TicTacToe:
    def __init__(self):
        self.board = [[None for _ in range(3)] for _ in range(3)]

    def draw_board(self):
        '''Отрисовка игрового поля'''
        for line in self.board:
            print(' --- --- --- ')
            lst = []
            for el in line:
                if el is None:
                    lst.append(' ')
                else:
                    lst.append(el)
            print(f'| {lst[0]} | {lst[1]} | {lst[2]} |')
        print(' --- --- --- ')

    def check_column(self, digit: int) -> bool:
        '''Проверка столбцов'''
        for i in range(3):
            col = []
            for j in range(3):
                col.append(self.board[j][i])
            if col.count(digit) == 3:
                return True
        return False

    def check_line(self, digit: int) -> bool:
        '''Проверка линий'''
        for line in self.board:
            if line.count(digit) == 3:
                return True
        return False

    def check_diagonal(self, digit: int) -> bool:
        '''Проверка диагоналей'''
        main_diag = []
        sec_diag = []
        for i in range(3):
            for j in range(3):
                if i == j:
                    main_diag.append(self.board[i][j])
                if 2 - j - i == 0:
                    sec_diag.append(self.board[i][j])
        if main_diag.count(digit) == 3 or sec_diag.count(digit) == 3:
            return True
        return False

    def move(self, player: int):
        '''Установка значка игрока на игровое поле'''
        while True:
            tpl = tuple(
                map(
                    int,
                    input(f'Игрок {player}, введите координаты ячейки в \
формате "x y": ').split()
                )
            )
            if self.board[tpl[0]][tpl[1]] is None:
                self.board[tpl[0]][tpl[1]] = player
                break
            else:
                print('Ячейка уже занята! Повторите ввод!')


board = TicTacToe()
for i in range(9):
    player = 1 if i % 2 == 0 else 2
    board.draw_board()
    board.move(player)
    if board.check_column(player) or board.check_diagonal(player) \
            or board.check_line(player):
        board.draw_board()
        print(f'{player} WON')
        break
else:
    board.draw_board()
    print('DRAW')
