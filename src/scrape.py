"""Download and save Premier League data from FBref."""

import argparse


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seasons", default="2019-2025", help="Season range to scrape, e.g. 2019-2025")
    args = parser.parse_args()
    print(f"scrape.py: not implemented yet (seasons={args.seasons})")


if __name__ == "__main__":
    main()
