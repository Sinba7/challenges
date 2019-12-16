from datetime import datetime, timedelta
import time

def print_header():
    print('-----------------------------------------------')
    print("      WELCOME TO SINBA'S POMODPRO TIMER        ")
    print('-----------------------------------------------')


def pomodoro():
    timer = timedelta(minutes=25)
    print('25 min Pomodoro starts now.')
    while timer:
        time.sleep(1)
        timer -= timedelta(seconds=1)
        print(f'time remain:{timer}')
    print('Pomodoro ends. Take a break!')

def arbitary_timer(length):
    timer = timedelta(minutes=length)
    print(f'{length} minutes self-designed Pomodoro starts now.')
    while timer:
        time.sleep(1)
        timer -= timedelta(seconds=1)
        print(f'time remain:{timer}')
    print('Pomodoro ends. Take a break!')

def loop_timer(p_length=25, b_length=5, n_loops=7):
    pomo_timer = timedelta(seconds=p_length)
    break_timer = timedelta(seconds=b_length)
    print(f'Loop Pomodoro ({p_length} minutes) starts now for {n_loops} loops.')
    for i in range(n_loops):
        cur_pomo_timer = pomo_timer
        while cur_pomo_timer:
            time.sleep(1)
            cur_pomo_timer -= timedelta(seconds=1)
            print(f'Pomodoro time remaining:{cur_pomo_timer}')
        print(f'Pomodoro {i+1} ends. Take a break now!')
        cur_break_timer = break_timer
        while cur_break_timer:
            time.sleep(1)
            cur_break_timer -= timedelta(seconds=1)
            print(f'Break time remaining:{cur_pomo_timer}')
        if i+1 < n_loops:
            print('Break time ends. Time to study!')
        else:
            print('Good job! You finish all pomodoros. Time for party!')

def main():
    choice = input('Please select your timer:\n' 
                    ' A: Tomato Pomodoro(25min)\n'
                    ' B: Make Your Own Pomodoro\n'
                    ' C: Loop Pomodoro!\n'
                    ' D: Exit\n'
    )
    if choice in ['A', 'a']:
        pomodoro()
    elif choice in ['B', 'b']:
        user_length = int(input('Please input your timer length in minute:\n'))
        arbitary_timer(user_length)
    elif choice in ['C','c']:
        p_length = int(input('How long do you want to work ? (in minutes):\n'))
        b_length = int(input('How long do you want to break after work? (in minutes):\n'))
        n_loops = int(input('How many loops you want?\n'))
        loop_timer(p_length, b_length,n_loops)
    elif choice in ['D','d']:
        quit
    else:
        print('Sorry, invalid choice!')


if __name__ == "__main__":
    print_header()
    main()
