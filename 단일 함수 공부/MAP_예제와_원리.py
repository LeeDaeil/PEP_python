'''

map의 기능 - 첫번째 매개변수의 함수와 두번째 변수인 리스트를 매핑해서 반환해주는 역할
map(function, list) list의 요수값을 반복하여 사용한다.
map(function, dict) dict의 key값을 반복하여 사용한다.

'''

ORGIN_DATA = [1, 1, 1, 0, 0, 3]
ORGIN_DATA_2ARRAY = [[1, 1, 1, 0, 0, 3], [1, 1, 1, 0, 0, 3]]


def change_value(data):
    # data의 리스트 중 1을 'on' 0을 'off'로 변환하는 함수
    if data is 1:
        return 'on'
    elif data is 0:
        return 'off'
    else:
        return data


def main():
    out_data = map(change_value, ORGIN_DATA)
    print(list(out_data))

    out_data_2array = map(change_value, ORGIN_DATA_2ARRAY)
    print(list(out_data_2array))
    # list 요소를 사용하다보니 이경우 계산이 안되는 부족한 점이 발생한다.


if __name__ == '__main__':
    main()
