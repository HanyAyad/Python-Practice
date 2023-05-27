def reverse_sublist(a, i, j):
    sublist = a[i:j+1]
    sublist.reverse()
    a[i:j+1] = sublist
    
    return a

def main():
    a = [1, 2, 9, 6, 5]
    print("Original list:", a)
    
    i = 2
    j = 4

    print("Reversed sublist:", reverse_sublist(a, i, j))

if __name__ == '__main__':
    main()
