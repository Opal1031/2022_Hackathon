#===========================================================================
# 8옥타브 12음계(C1~B8) 주파수표를 출력해 보기
# A4 = 440Hz, A5 = 880Hz  
# 파이썬코딩 : 김건 (https://blog.naver.com/PostView.nhn?isHttpsRedirect=true&blogId=gudhand&logNo=222024728187&categoryNo=0&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=postView)
#===========================================================================

# 2차원 리스트 초기화 
def octave_li():
    octave = [[0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]]

    # 1옥타브 12음계 주파수 비율 계산 440 * r**12 = 880 
    r = 2 ** (1/12)                       

    # 1옥타브 12음계 주파수 계산 list[열#][행#]
    col = 0
    row = 0
    freq = 0

    # row가 0~7까지 roop
    # col이 0~11까지 roop
    # freq는 55Hz에서 2배수로 증가
    for row in range(8):

        if row == 0:

            freq = 55

        else:

            freq = freq * 2         

        for col in range(12):

            octave[col][row] = round(freq/r**(9-col), 4)

    return octave
"""
print("C",list[0])
print("C#",list[1])
print("D",list[2])
print("D#",list[3])
print("E",list[4])
print("F",list[5])
print("F#",list[6])
print("G",list[7])
print("G#",list[8])
print("A",list[9])
print("A#",list[10])
print("B",list[11])
"""