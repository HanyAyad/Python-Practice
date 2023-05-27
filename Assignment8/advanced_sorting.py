def main():
    cities = [
        (1, 'Albany', 'NY', 162692),
        (3, 'Allegany', 'NY', 11986),
        (121, 'Wyoming', 'NY', 8722),
        (123, 'Yates', 'NY', 5094)
    ]
    sorted_cities = sorted(cities, key=lambda x: x[-1])
    print(sorted_cities)

    print('-'*40)

    users = ['10:User1', '80:User2', '100:User3', '00:User4', '75:User4', '45:User5']
    sorted_users = sorted(users, key=lambda x: int(x.split(':')[0]), reverse=True)
    print(sorted_users)

    print('-'*40)

    matrix = [[2, 6], [1, 3], [5, 4]]
    sorted_matrix = sorted(matrix, key=lambda x: x[1])
    print(sorted_matrix)

if __name__ == '__main__':
    main()
