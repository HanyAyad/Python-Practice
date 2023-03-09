def main():
    student_info =  [('Shabayk', 2002, 162), ('Hany', 2002, 183),
              ('Fathy', 2001, 188), ('Abood', 2002, 193), 
              ('Omar', 2003, 185), 
              ('Abohesha', 2002, 175), ('Kareem', 2002, 179)]
    
    print ("{0:^12} {1:^16} {2:^16}".format("Name", "Year of Birth", "Height"))
    print ("-"*46)
    for element in student_info:
        print ("{0:^12} {1:^16} {2:^16}".format(element[0], element[1], 
                                         element[2]))

if __name__ == "__main__":
    main()