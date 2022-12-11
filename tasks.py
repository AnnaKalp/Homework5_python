# 1-Напишите программу, удаляющую из текста все слова, содержащие 
# заданную строку.
# Пример:
# Пугать ты галок пугай => заданная строка "галок" => Пугать ты пугай
# Пугать ты галок пугай => заданная строка "пуг" => Пугать ты галок


# some_text = 'Пугать ты галок пугай'
# my_text = list(filter(lambda i: 'галок' not in i, some_text.split()))
# print(f' {" ".join(my_text)}')



# 2-Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021(или сколько вы скажете) конфет.
# Играют два игрока делая ход друг после друга. Первый ход определяется
# жеребьёвкой. За один ход можно забрать не более чем 28(или сколько 
# вы зададите в начале) конфет. Все конфеты оппонента достаются
# сделавшему последний ход. Сделайте эту игру.

# import random

# first_player_name = input("Как зовут первого игрока? ")
# second_player_name = input("Как зовут второго игрока? ")
# player = random.randrange(1,3)
# candies = int(input('Сколько конфет всего? '))
# if player == 1:
#     print('Первый ход делает', first_player_name)
# else:
#      print('Первый ход делает', second_player_name) 
# while candies > 0:
#    if candies > 28:
#       player1 = int(input('Можешь взять до 28 конфет.Сколько конфет взял(а)? '))
#       candies = candies - player1
#       if candies > 28:
#          player2 = int(input('Можешь взять до 28 конфет.Сколько конфет взял(а)? '))
#          candies = candies - player2
#          if candies <= 28:
#             if player == 1:
#                print('Осталось',candies, 'конфет, это последний ход, все конфеты берёт', first_player_name)
#             else:    
#                print('Осталось',candies, 'конфет, это последний ход, все конфеты берёт', second_player_name)
#       else:
#          if player == 1:
#             print('Осталось',candies, 'конфет, это последний ход, все конфеты берёт', second_player_name)
      
#          else:
#             print('Осталось',candies, 'конфет, это последний ход, все конфеты берёт', first_player_name)   
            


# 3-Создайте программу для игры в ""Крестики-нолики"".
import random

def print_game(new_list: list):
    for i in new_list: print(i)

def return_poz(number: int, newList: list, count: str) -> list:
    if number == 1: new_list[0][0] = count
    elif number == 2: new_list[0][1] = count
    elif number == 3: new_list[0][2] = count
    elif number == 4: new_list[1][0] = count
    elif number == 5: new_list[1][1] = count
    elif number == 6: new_list[1][2] = count
    elif number == 7: new_list[2][0] = count
    elif number == 8: new_list[2][1] = count
    elif number == 9: new_list[2][2] = count
    return new_list

def true_false(new_list: list, count: str):
    check_input = False
    for i in range(len(new_list)):
        for j in range(len(new_list)):
            if new_list[i][j] == count:
                check_input = True
                break
    return check_input

def win_game(new_list: list):
    if new_list[0][0] == new_list[1][1] == new_list[2][2] != ' ':
         return True 
    elif new_list[0][2] == new_list[1][1] == new_list[2][0] != ' ':
         return True
    elif new_list[0][0] == new_list[0][1] == new_list[0][2] != ' ': 
        return True
    elif new_list[1][0] == new_list[1][1] == new_list[1][2] != ' ':
         return True
    elif new_list[2][0] == new_list[2][1] == new_list[2][2] != ' ':
         return True
    elif new_list[0][0] == new_list[1][0] == new_list[2][0] != ' ':
         return True
    elif new_list[0][1] == new_list[1][1] == new_list[2][1] != ' ': 
        return True
    elif new_list[0][2] == new_list[1][2] == new_list[2][2] != ' ': 
        return True
    else: 
        return False

new_list = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
new_list2 = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
print('Номера ячеек:')
print_game(new_list2)
print()
gamers = random.randint(1, 2)

if gamers == 1: print('Первый ход достаётся первому игроку!')
else: print('Первый ход достаётся второму игроку!')
print()
for i in range(len(new_list)*2):
    if true_false(new_list, ' '):
        if gamers == 1:
            print_game(new_list)
            number = int(input('Ходит первый игрок. Введите номер свободной ячейки: '))
            print()
            new_list = return_poz(number, new_list, 'X')
            if win_game(new_list) == True:
                print_game(new_list)
                print(f'Победил игрок номер {gamers}!')
                break
            elif true_false(new_list, ' '): 
                gamers = 2
        if gamers == 2:
            print_game(new_list)
            number = int(input('Ходит второй игрок. Введите номер свободной ячейки: '))
            print()
            new_list = return_poz(number, new_list, '0')
            if win_game(new_list) == True:
                print_game(new_list)
                print(f'Победил игрок номер {gamers}!')
                break
            elif true_false(new_list, ' '): 
                gamers = 1
    else: 
        print_game(new_list)
        print('Ничья!')