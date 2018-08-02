def main():
    test_bool = True

    if test_bool:
        print('True')

    if test_bool == True:
        print('== 사용하지 말자')

    if test_bool is True:
        print('is 사용하지 말자')


if __name__ == '__main__':
    main()
