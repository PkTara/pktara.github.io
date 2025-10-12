import argparse
from admin.add_spoons_carpet import add_spoons_carpet

def main():
    parser = argparse.ArgumentParser(description="Helper script for cv-website.")
    parser.add_argument(
        '--add-spoons-carpet',
        '--spoons',
        action='store_true',
        help='Add spoons to the carpet.'
    )

    args = parser.parse_args()

    if args.add_spoons_carpet:
        add_spoons_carpet()

        
if __name__ == "__main__":
    main()