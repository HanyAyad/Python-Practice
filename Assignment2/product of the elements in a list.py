def product_of_list(lst):
    product = 1
    for num in lst:
        product *= num
    return product
def main():
    lst = [1, 2, 3, 4, 5]
    product = product_of_list(lst)
    print(product) 
if __name__=="__main__":
    main()
