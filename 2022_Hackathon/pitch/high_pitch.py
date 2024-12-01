import compare
import csv
import os,sys
import pandas as pd
#2옥 도 ~ 4옥 시    2옥도[0][1] 2옥시[11][1]    4옥도[0][3] 4옥시[11][3]
#  set_octave.octave_li()[0][1]    set_octave.octave_li()[0]
def h_pitch():
    crepe = "python -m crepe output.wav"    #crepe로 wav의 pitch 찾음. [초, Hz, 정확도]
    os.system(crepe)                                     #터미널 창에서 쓰는 것과 같음

    #with open('output.f0.csv', newline='') as csvfile:#
    data=pd.read_csv('output.f0.csv')   #crepe로 찾은 pitch를 csv파일로 저장
    selectdata=pd.DataFrame(data, columns=['frequency','confidence'])
    idx_drop=selectdata[selectdata['confidence']<0.9].index     #정확도 0.9 미만은 삭제
    selectdata=selectdata.drop(idx_drop)
    round_value=round(selectdata['frequency'])
    round_value=round_value.tolist()
    highest=0
    for i in round_value:
        if highest>=i:
           highest=i
    # if os.path.exists('output.f0.csv'): #생성한 csv 파일 제거
    #     os.remove('output.f0.csv')
    return compare.com_voice(highest)


