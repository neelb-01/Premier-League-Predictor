"""Simulate the rest of the season to project the final league table (Phase 3)."""

import argparse


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--runs", type=int, default=10000, help="Number of season simulations")
    args = parser.parse_args()
    print(f"simulate.py: not implemented yet (runs={args.runs})")


if __name__ == "__main__":
    main()
