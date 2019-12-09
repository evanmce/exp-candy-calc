import argparse

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("pkmn_name", help="the name of the pokemon")
    parser.add_argument("lvl_from", help="the level from", type=int)
    parser.add_argument("lvl_to", help="the level to", type=int)

    parser.add_argument("-c", "--candy", choices=["xs", "s", "m", "l", "xl"], help="which type of candy to use")

    args = parser.parse_args()

    if args.candy:
        print("calculating using XS candies")

if __name__ == "__main__":
    main()
