def main():
    # mode : w 上書き,  a 上書き,

    # f = open(file='users.txt', mode='w', encoding='utf8')
    # f.write('Bob,79')
    # f.close()

    with open(file='users.txt', mode='w', encoding='utf8') as f:
        f.write('Bob,79 \n')
        # f.write('Tom,59')
        print("withの中：", f.closed)
    print("withの外：", f.closed)


if __name__ == '__main__':
    main()
