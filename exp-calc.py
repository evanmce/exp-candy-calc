import argparse
import math

def calc_fast_lvls():
    lvls = []
    xp = 0
    for i in range(1, 101):
        xp = math.floor(4*(i**3)/5)
        lvls.append(xp)
    return lvls

def calc_med_fast_lvls():
    lvls = []
    xp = 0
    for i in range(1, 101):
        xp = i**3
        lvls.append(xp)
    lvls[0] = 0
    return lvls


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("pkmn_name", help="the name of the pokemon")
    parser.add_argument("lvl_from", help="the level from", type=int)
    parser.add_argument("lvl_to", help="the level to", type=int)

    parser.add_argument("-c", "--candy", choices=["xs", "s", "m", "l", "xl"], help="which type of candy to use")

    args = parser.parse_args()

    if args.candy:
        print("calculating using XS candies")

    fast = calc_fast_lvls()
    med_fast = calc_med_fast_lvls()

    for x in range(len(med_fast)):
        print(med_fast[x])

if __name__ == "__main__":
    main()
