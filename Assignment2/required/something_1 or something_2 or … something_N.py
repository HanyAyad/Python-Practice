import sys
def main():
    inp = input("Do you really want to quit [y/Y/yes]? ")
    if inp.lower() in ['y', 'yes']: 
        print('bye')
        sys.exit(0)
    print('The show goes on...')

if __name__ == "__main__":
    main()