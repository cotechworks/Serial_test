import serial
from time import sleep

def main():
    with serial.Serial('COM8',9600,timeout=1) as ser:
        while True:
            ser.write(bytes('Test\n\r','utf-8'))
            sleep(0.5)
            ser.write(bytes('Test\n\r','utf-8'))
            flag = bytes(input(),'utf-8')

            #シリアル通信で文字を送信する際は, byte文字列に変換する
            #input()する際の文字列はutf-8

            ser.write(flag)
            ser.write(bytes('\n\r','utf-8'))

            #シリアル通信:送信

            if(flag == bytes('a','utf-8')):
                break;
        ser.close()

if __name__ == "__main__":
    main()
