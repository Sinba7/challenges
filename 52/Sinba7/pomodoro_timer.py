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

def main():
    choice = input('Please select your timer:\n' 
                    ' A: Standard Pomodoro(25min)\n'
                    ' B: Make Your Own Pomodoro\n'
                    ' C: Exit\n'
    )
    if choice in ['A', 'a']:
        pomodoro()
    elif choice in ['B', 'b']:
        user_length = int(input('Please input your timer length in minute:\n'))
        arbitary_timer(user_length)
    elif choice in ['C','c']:
        quit
    else:
        print('Sorry, invalid choice!')


if __name__ == "__main__":
    print_header()
    main()
