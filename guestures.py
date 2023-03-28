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
            case b'11111111\r\n':
                outcome = str("b")
                # keyboard.press_and_release('e')
                time.sleep(.5)
                a = eval(cc)
                return a
                break
            case b'00000000\r\n':
                outcome = str("e")
                keyboard.press_and_release('windows+d')
                a = eval(cc)
                return a
                break
            case b'01010101\r\n':
                outcome = str("dota")
                keyboard.press_and_release('windows')
                time.sleep(.5)
                keyboard.write('dota')
                time.sleep(.5)
                keyboard.press('down')
                keyboard.press('down')
                time.sleep(.5)
                keyboard.press_and_release('enter')
                a = eval(cc)
                return a
                break
            case b'01111111\r\n':

                outcome = str("three")
                keyboard.press('windows')
                keyboard.press('m')
                time.sleep(0.002)
                keyboard.release('m')
                keyboard.release('windows')
                a = eval(cc)
                return a
                break

            case b'11011111\r\n':
                outcome = str("pea")
                keyboard.press_and_release('ctrl+shift+n')
                time.sleep(.5)
                a = eval(cc)
                return a
                break

            case b'11110111\r\n':
                outcome = str("opera")
                keyboard.press_and_release('windows')
                time.sleep(1.5)
                keyboard.write('opera')
                time.sleep(0.5)
                keyboard.press_and_release('enter')

                a = eval(cc)
                return a
                break

            case b'11111101\r\n':
                outcome = str("desktop")
                keyboard.press_and_release('windows+up')

                time.sleep(.5)
                a = eval(cc)
                return a
                break

            case b'01011111\r\n':
                outcome = str("tm")
                keyboard.press_and_release('ctrl+shift+esc')
                time.sleep(1.5)
                a = eval(cc)
                return a
                break

            case b'01110111\r\n':
                outcome = str("reset gpu")
                keyboard.press_and_release('windows+ctrl+shift+b')
                time.sleep(1.5)
                a = eval(cc)
                return a
                break

            case b'01111101\r\n':
                outcome = str("wsleft")
                keyboard.press_and_release('ctrl+windows+left')
                a = eval(cc)
                return a
                break

            case b'11010111\r\n':
                outcome = str("baba")
                keyboard.press_and_release('ctrl+windows+right')

                a = eval(cc)
                return a
                break

            case b'11011101\r\n':

                outcome = str("opera")
                keyboard.press_and_release('windows')
                time.sleep(1.5)
                keyboard.write('discord')
                time.sleep(1.5)
                keyboard.press_and_release('enter')
                a = eval(cc)
                return a
                break
            case b'11110101\r\n':
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