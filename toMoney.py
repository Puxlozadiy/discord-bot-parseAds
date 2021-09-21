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