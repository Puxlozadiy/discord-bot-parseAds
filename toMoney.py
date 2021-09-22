def convertToMoney(string):
    if string.find('догов') >= 0 or string.find('Догов') >= 0 or string.find('лс') >= 0:
        return "Цена договорная!"
    bool = 0
    millions = 0
    thousands = 0
    hundreds = 0
    block = 0
    count = 0
    for str in string.split():
        if str.find("кк") >= 0 or str.find(",") >= 0 or str.find(".") >= 0 or str.find("к") >= 0 or startWithDigit(str) == 1 or str.find("kk") >= 0 or str.find("k") >= 0:
            if startWithDigit(str) == 1:
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

convertToMoney("5.1")