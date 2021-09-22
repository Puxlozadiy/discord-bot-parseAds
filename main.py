# coding=utf-8
from discord import client
from discord.flags import Intents
from discord.message import MessageReference
from openpyxl import load_workbook, Workbook
wb = load_workbook('Analusis.xlsx')
ws = wb.active
import discord
from discord.ext import commands, tasks
 
bot = commands.Bot(command_prefix='!', self_bot=True)
target_channel_id = 886915166120345670


@bot.event
async def on_message(message):
    if message.channel.id == target_channel_id:
        async for message in message.channel.history(limit=1):
            print("Новое объявление!")
            ifContainsAndStore(message)
        

def ifContainsAndStore(string):
    if string.content.find("родам") >= 0:
        if string.content.find("evo 6") >= 0 or string.content.find("Evo 6") >= 0 or string.content.find("евик 6") >= 0:
            storeData(string.content, 3, "Продаётся evo 6", "B")
        elif string.content.find("350z") >= 0 :
            storeData(string.content, 4, "Продаётся 350z", "C")
        elif string.content.find("s15") >= 0 :
            storeData(string.content, 5, "Продаётся silvia s15", "D")
        elif string.content.find("FX50") >= 0 or string.content.find("финик") >= 0:
            storeData(string.content, 6, "Продаётся Infinity", "F")
        elif string.content.find("Supra") >= 0 or string.content.find("супру") >= 0:
            storeData(string.content, 7, "Продаётся Toyota Supra", "F")
        elif string.content.find("WRX STI") >= 0 :
            storeData(string.content, 8, "Продаётся Subaru WRX STI", "G")
        elif string.content.find("Stinger") >= 0 or string.content.find("стингер") >= 0 or string.content.find("Киа") >= 0:
            storeData(string.content, 9, "Продаётся KIA Stinger", "H")
        elif string.content.find("R34") >= 0 or string.content.find("скайлик") >= 0 and string.content.find("34") >= 0:
            storeData(string.content, 10, "Продаётся Skyline R34", "I")
        elif string.content.find("X5 E70") >= 0 or string.content.find("x5 e70") >= 0 or string.content.find("X5 e70") >= 0:
            storeData(string.content, 11, "Продаётся BMW x5 e70", "J")
        elif string.content.find("Alfa") >= 0 or string.content.find("альфу") >= 0:
            storeData(string.content, 12, "Продаётся Alfa Romeo", "K")
        elif string.content.find("Raptor") >= 0 or string.content.find("раптор") >= 0 or string.content.find("Раптор") >= 0 or string.content.find("raptor") >= 0:
            storeData(string.content, 13, "Продаётся Ford Raptor", "L")
        elif string.content.find("GLS63") >= 0 or string.content.find("GLS") >= 0 or string.content.find("глс") >= 0:
            storeData(string.content, 14, "Продаётся Mercedes GLS63", "M")
        elif string.content.find("Mustang 2019") >= 0 :
            storeData(string.content, 15, "Продаётся Ford Mustang 2019", "N")
        elif string.content.find("M5F90") >= 0 :
            storeData(string.content, 16, "Продаётся BMW M5F90", "O")
        elif string.content.find("LX570") >= 0 or string.content.find("лексус") >= 0 or string.content.find("Лексус") >= 0:
            storeData(string.content, 17, "Продаётся Lexus LX570", "P")
        elif string.content.find("Model S") >= 0 :
            storeData(string.content, 18, "Продаётся Tesla Model S", "Q")
        elif string.content.find("G63") >= 0 or string.content.find("гелик") >= 0 or string.content.find("Гелик") >= 0:
            storeData(string.content, 19, "Продаётся Mercedes G63", "R")
        elif string.content.find("RS7") >= 0 :
            storeData(string.content, 20, "Продаётся Audi RS7", "S")
        elif string.content.find("X6 M") >= 0 or string.content.find("X6M") >= 0 or string.content.find("x6m") >= 0 or string.content.find("X6 m") >= 0 or string.content.find("х6м") >= 0:
            storeData(string.content, 21, "Продаётся BMW X6 M", "T")

def storeData(string, int, comment, letter):
    if convertToMoney(string) != "Цена договорная!" and convertToMoney(string) != "Скорее всего это обмен!":
        converted = convertToMoney(string)
        if converted != 0:
            x = ws[f'A{int}'].value
            ws[f'{letter}{x}'].value = converted
            ws[f'A{int}'].value = (x + 1)
            wb.save('Analusis.xlsx')
            print(comment, "за", converted)
        else:
            print("Ошибка в получении цены!")
    else:
        print("Цена договорная и она не записана в таблицу!")  

def convertToMoney(string):
    bool = 0
    millions = 0
    thousands = 0
    hundreds = 0
    block = 0
    count = 0
    count1 = 0
    for lines in string.splitlines():
        if string.find('догов') >= 0 or string.find('Догов') >= 0 or string.find('лс') >= 0:
            return "Цена договорная!"
        if string.find('бмен') >= 0 or string.find('Обмен') >= 0 or string.find('обмен') >= 0:
            count1 = count1 + 1
        if string.find('на') >= 0 and count1 == 1:
            return "Скорее всего это обмен!"
        if lines.find('гос') == -1 or lines.find('Гос') == -1:
            for str in string.split():
                if str.find("кк") >= 0 or str.find(",") >= 0 or str.find(".") >= 0 or str.find("к") >= 0 or startWithDigit(str) == 1 or str.find("kk") >= 0 or str.find("k") >= 0:
                    if startWithDigit(str) == 1:
                        if str.find('.') == 1 and str.find('.', 2) == 3 and str.find('.', 4) == 5:
                            return "Цена договорная!"
                        if str.find('.') == 1 or str.find(',') == 1 and str.find('кк') >= 0 or str.find('kk') >= 0: # проверка формата
                            for str1 in str:
                                if block <= 2:
                                    block = block + 1
                                    if str1.isdigit() == 1 and bool == 0:
                                        millions = int(str1)
                                    if str1 == "." or str1 == ",":
                                        bool = 1
                                    if str1.isdigit() == 1 and bool == 1:
                                        thousands = int(str1)
                        if str.find('.') == 3 and str.find('.') != 1 or str.find('к') == 3 and str.find('.') != 1 or str.find('k') == 3 and str.find('.') != 1: # проверка формата
                            count = 0
                            for str1 in str:
                                if count == 0:
                                    thousands = int(str1)
                                elif count == 2:
                                    hundreds = int(str1)
                                count = count + 1
                        elif str.find('.') == 1 and str.find('.', 2) == 5: # проверка формата
                                for str1 in str:
                                    if count <= 3:
                                        if str1.isdigit() and count == 0:
                                            millions = int(str1)
                                            count = count + 1
                                        elif str1.isdigit() and count == 1:
                                            thousands = int(str1)
                                            count = count + 1
                                        elif str1.isdigit() and count == 2:
                                            hundreds = int(str1)
                                            count = count + 1
                            
                                                
    millions = millions * 1000000
    thousands = thousands * 100000
    hundreds = hundreds * 10000
    millions = millions + thousands + hundreds
    return millions


def startWithDigit(str):
    if str.startswith('1') or str.startswith('2') or str.startswith('3') or str.startswith('4') or str.startswith('5') or str.startswith('6') or str.startswith('7') or str.startswith('8') or str.startswith('9'):
        return 1
    else:
        return 0

bot.run("mfa.68PoHXxzli3akZrhYYp-fa-CvS-P6PZvqC06WEq7w_FrEcAVbLPS-_UPLiimiDJr6NsqqgfGAI7LALDV0JjQ", bot=False)