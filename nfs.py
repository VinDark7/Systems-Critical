import time
import serial
import keyboard
import pyautogui

ser = serial.Serial("COM3", 9600)


def loop1():
    while True:
        cc = str(ser.readline())
        # print(cc[2:][:-5])

        # print(eval(cc))
        conver = eval(cc)
        match eval(cc):
            case b'11111111001\r\n':
                outcome = str("b")
                # keyboard.press_and_release('e')
                #time.sleep(.5)
                a = eval(cc)
                return a
                break
            case b'00000000001\r\n':
                outcome = str("e")
                keyboard.press_and_release('windows+d')
                a = eval(cc)
                return a
                break
            case b'01010101001\r\n':
                outcome = str("forward")
                while True:
                    if eval(cc) == b'01010101001\r\n':
                        keyboard.press('w')
                    if eval(cc) != b'01010101001\r\n':
                        keyboard.release('w')
                        break

                a = eval(cc)
                return a
            case b'10101111001\r\n':
                outcome = str("stop")
                while True:
                    if eval(cc) == b'10101111001\r\n':
                        keyboard.press('s')
                        
                    if eval(cc) != b'10101111001\r\n':
                        keyboard.release('s')
                        break
            
            case b'01010101010\r\n':
                outcome = str("right+forward")
                while True:
                    if eval(cc) == b'01010101010\r\n':
                        keyboard.press('d')
                        keyboard.press('w')
                    if eval(cc) != b'01010101010\r\n':
                        keyboard.release('d')
                        keyboard.release('w')
                        break    
             case b'11111111010\r\n':
                outcome = str("right")
                while True:
                    if eval(cc) == b'11111111010\r\n':
                        keyboard.press('d')
                       
                    if eval(cc) != b'11111111010\r\n':
                        keyboard.release('d')
                        
                        break   
            case b'10101111010\r\n':
                outcome = str("right+stop")
                while True:
                    if eval(cc) == b'10101111010\r\n':
                        keyboard.press('d')
                        keyboard.press('s')
                    if eval(cc) != b'10101111010\r\n':
                        keyboard.release('d')
                        keyboard.release('s')
                        break  
            
            case b'01010101000\r\n':
                outcome = str("left+forward")
                while True:
                    if eval(cc) == b'01010101000\r\n':
                        keyboard.press('a')
                        keyboard.press('w')
                    if eval(cc) != b'01010101000\r\n':
                        keyboard.release('a')
                        keyboard.release('w')
                        break  
            
            case b'11111111000\r\n':
                outcome = str("left")
                while True:
                    if eval(cc) == b'11111111000\r\n':
                        keyboard.press('a')
                    if eval(cc) != b'11111111000\r\n':
                        keyboard.release('a')
                        break                      

            case b'10101111000\r\n':
                outcome = str("left+stop")
                while True:
                    if eval(cc) == b'10101111000\r\n':
                        keyboard.press('a')
                        keyboard.press('s')
                    if eval(cc) != b'10101111000\r\n':
                        keyboard.release('a')
                        keyboard.release('s')
                        break  
            
            

            case b'01111111001\r\n':

                outcome = str("three")
                keyboard.press('windows')
                keyboard.press('m')
                time.sleep(0.002)
                keyboard.release('m')
                keyboard.release('windows')
                a = eval(cc)
                return a
                break



            case b'11110111001\r\n':
                outcome = str("opera")
                keyboard.press_and_release('windows')
                time.sleep(1.5)
                keyboard.write('opera')
                time.sleep(0.5)
                keyboard.press_and_release('enter')

                a = eval(cc)
                return a
                break

            case b'11111101001\r\n':
                outcome = str("desktop")
                keyboard.press_and_release('windows+up')

                time.sleep(.5)
                a = eval(cc)
                return a
                break

            case b'01011111001\r\n':
                outcome = str("tm")
                keyboard.press_and_release('ctrl+shift+esc')
                time.sleep(1.5)
                a = eval(cc)
                return a
                break

            case b'01110111001\r\n':
                outcome = str("reset gpu")
                keyboard.press_and_release('windows+ctrl+shift+b')
                time.sleep(1.5)
                a = eval(cc)
                return a
                break

            case b'01111101001\r\n':
                outcome = str("wsleft")
                keyboard.press_and_release('ctrl+windows+left')
                a = eval(cc)
                return a
                break

            case b'11010111001\r\n':
                outcome = str("baba")
                keyboard.press_and_release('ctrl+windows+right')

                a = eval(cc)
                return a
                break

            case b'11011101001\r\n':

                outcome = str("opera")
                keyboard.press_and_release('windows')
                time.sleep(1.5)
                keyboard.write('discord')
                time.sleep(1.5)
                keyboard.press_and_release('enter')
                a = eval(cc)
                return a
                break
            case b'11110101001\r\n':
                outcome = str("gun")
                outcome = str("opera")
                keyboard.press_and_release('windows')
                time.sleep(1.5)
                keyboard.write('vs')
                time.sleep(1.5)
                keyboard.press_and_release('enter')
                a = eval(cc)
                return a
                break

            case _:
                # outcome=str("defeat")
                # outcome=str("opera")
                # keyboard.press_and_release('windows')
                # time.sleep(1.5)
                # keyboard.write('steam')
                # time.sleep(1.5)
                # keyboard.press_and_release('enter')
                # a=eval(cc)
                # return a
                break
        print(outcome)


while True:
    a = loop1()
    while True:
        cc = str(ser.readline())
        # print(cc[2:][:-5])

        # print(eval(cc))
        conver = eval(cc)
        time.sleep(0.01)
        if eval(cc) != a:
            break
