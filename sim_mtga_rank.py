import random

init_level = 10
winning_goal = 20
test_times = 100000

print('enter the win-rate')
win_rate = input()

try:
    win_rate = float(win_rate)
except ValueError:
    print('not number')
    exit()

if win_rate < 0 or win_rate > 1:
    print('too big or too small')
    exit()

def test_loop_bo1():
    current_level = init_level
    game_cnt = 0
    while current_level < winning_goal or game_cnt > 99999:
        game_cnt += 1
        if(random.random() < win_rate): # this is a win
            current_level += 1
        else:
            current_level = max(0, current_level - 1)
    return game_cnt, game_cnt

def test_one_game_bo3():
    round_cnt_ingame = 0
    win_cnt_ingame = 0
    while round_cnt_ingame < 3:
        round_cnt_ingame += 1 
        if(random.random() < win_rate): # this is a win
            win_cnt_ingame += 1
            if win_cnt_ingame >= 2:
                break
    return win_cnt_ingame >= 2, round_cnt_ingame

def test_loop_bo3():
    current_level = init_level
    game_cnt = 0
    round_cnt = 0
    while current_level < winning_goal or game_cnt>99999:
        game_cnt += 1
        is_win, round_cnt_ingame = test_one_game_bo3()
        round_cnt += round_cnt_ingame
        if is_win:
            current_level += 1
        else:
            current_level = max(0, current_level - 1)
    return game_cnt, round_cnt

game_sum = 0
round_sum = 0
for i in range(test_times):
    game_cnt, round_cnt = test_loop_bo1()
    game_sum += game_cnt
    round_sum += round_cnt
print('bo1 res:', game_sum/float(test_times), '\t',
        round_sum/float(test_times))

game_sum = 0
round_sum = 0
for i in range(test_times):
    game_cnt, round_cnt = test_loop_bo3()
    game_sum += game_cnt
    round_sum += round_cnt
print('bo1 res:', game_sum/float(test_times), '\t',
        round_sum/float(test_times))
