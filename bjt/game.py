import time
import random
import configparser


def display_card(rank: str, suit: str) -> None:
    print('┌─────────┐')
    print(f'│{rank}        │') if rank != "10" else print(f'│{rank}       │')
    print('│         │')
    print('│         │')
    print(f'│    {suit}    │')
    print('│         │')
    print('│         │')
    print(f'│        {rank}│') if rank != "10" else print(f'│       {rank}│')
    print('└─────────┘')


def main():
    pass


if __name__ == '__main__':
    main()
