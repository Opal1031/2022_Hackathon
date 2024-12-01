import set_octave
def high(value):    
    if value==0:
        return '도'
    elif value==1:
        return '도#'
    elif value==2:
        return '레'
    elif value==3:
        return '레#'
    elif value==4:
        return '미'
    elif value==5:
        return '파'
    elif value==6:
        return '파#'
    elif value==7:
        return '솔'
    elif value==8:
        return '솔#'
    elif value==9:
        return '라'
    elif value==10:
        return '라#'
    elif value==11:
        return '도#'
#2옥 도 ~ 4옥 시    2옥도[0][1] 2옥시[11][1]    4옥도[0][3] 4옥시[11][3]
#  set_octave.octave_li()[0][1]    set_octave.octave_li()[0]
def com_voice(a):
    last=''
    octave=set_octave.octave_li()
    for i in range(1,5):
        for j in range(12):
            if (a <= (octave[j][i]+2.0) and a >= (octave[j][i]-2.0)):
                last=str(str(i+1)+"옥"+high(j))
    return last
