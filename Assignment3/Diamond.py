def print_diamond(height):
    if height % 2 == 0:
        raise ValueError("Height must be odd")
    for i in range(1, height+1, 2):
        print(" " * ((height-i)//2) + "*" * i)
    for i in range(height-2, 0, -2):
        print(" " * ((height-i)//2) + "*" * i)
        
# Example usage

def main():
    print_diamond(3)
    print_diamond(7)

if __name__ == "__main__":
    main()