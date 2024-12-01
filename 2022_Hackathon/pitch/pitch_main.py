#console
import input_voice
import high_pitch

if __name__=='__main__':
    
    input_voice.record()            #녹음 파일 생성(wav)
    highest=high_pitch.h_pitch()    #최고음정 찾아 반환
    print(highest)                  
    
