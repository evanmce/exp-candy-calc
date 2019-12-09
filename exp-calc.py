import argparse
import math

def calc_erratic_lvls():
    lvls = []
    xp = 0
    for i in range(1, 101):
        if i <= 50:
            xp = math.floor(((i**3)*(100 - i)) / 50)
        elif i > 50 and i <= 68:
            xp = math.floor(((i**3)*(150-i)) / 100)
        elif i > 68 and i <= 98:
            xp = math.floor(((i**3)*(math.floor((1911-(10*i))/3)))/500)
        elif i > 98 and i <= 101:
            xp = math.floor(((i**3)*(160-i))/100)
        lvls.append(xp)
    lvls[0] = 0
    return lvls

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

def calc_med_slow_lvls():
    lvls = []
    xp = 0
    for i in range(1, 101):
        xp = math.floor((6*(i**3)/5) - 15*(i**2) + 100*i - 140)
        lvls.append(xp)
    lvls[0] = 0
    return lvls

def calc_slow_lvls():
    lvls = []
    xp = 0
    for i in range(1,101):
        xp = math.floor(5*(i**3)/4)
        lvls.append(xp)
    lvls[0] = 0
    return lvls

def calc_fluct_lvls():
    lvls = []
    xp = 0
    for i in range(1, 101):
        if i <= 15:
            xp = math.floor((i**3)*(((math.floor((i+1)/3)+24)/50)))
        elif i > 15 and i <= 36:
            xp = math.floor((i**3)*(((i+14)/50)))
        elif i > 36 and i <= 101:
            xp = math.floor((i**3)*(((math.floor(i/2)+32)/50)))
        lvls.append(xp)
    return lvls

def read_pkmn_file(filename):
    pkmn = []
    with open(filename) as fp:
        for line in fp:
            pkmn.append(line.rstrip())
    fp.close()
    return pkmn


def main():

    erratic = calc_erratic_lvls()
    fast = calc_fast_lvls()
    med_fast = calc_med_fast_lvls()
    med_slow = calc_med_slow_lvls()
    slow = calc_slow_lvls()
    fluct = calc_fluct_lvls()

    erratic_pkmn = read_pkmn_file("pkmn/erratic.txt")
    fast_pkmn = read_pkmn_file("pkmn/fast.txt")
    med_fast_pkmn = read_pkmn_file("pkmn/medium_fast.txt")
    med_slow_pkmn = read_pkmn_file("pkmn/medium_slow.txt") 
    slow_pkmn = read_pkmn_file("pkmn/slow.txt")
    fluct_pkmn = read_pkmn_file("pkmn/fluctuating.txt")

    pkmn_dict = {}

    for name in erratic_pkmn:
        pkmn_dict[name] = "erratic"
    for name in fast_pkmn:
        pkmn_dict[name] = "fast"
    for name in med_fast_pkmn:
        pkmn_dict[name] = "medium_fast"
    for name in med_slow_pkmn:
        pkmn_dict[name] = "medium_slow"
    for name in slow_pkmn:
        pkmn_dict[name] = "slow"
    for name in fluct_pkmn:
        pkmn_dict[name] = "fluctuating"

    xs = 100
    s = 800
    m = 3000
    l = 10000
    xl = 30000

    parser = argparse.ArgumentParser()

    parser.add_argument("pkmn_name", help="the name of the pokemon")
    parser.add_argument("lvl_from", help="the level from", type=int)
    parser.add_argument("lvl_to", help="the level to", type=int)

    parser.add_argument("-c", "--candy", choices=["xs", "s", "m", "l", "xl", "r"], help="which type of candy to use")

    args = parser.parse_args()

    level_group = pkmn_dict.get('{}'.format(args.pkmn_name))
    print(level_group)

if __name__ == "__main__":
    main()
