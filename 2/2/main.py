from alphabet import *
import warnings
warnings.filterwarnings("ignore")

latEntropy = 0
kirEntropy = 0
binEntropy = 0
# а) рассчитать энтропию алфавитовна латинице и кириллице входной параметр провизвольный электронный документ
print("Рассчитать энтропию алфавитов: один – на латинице, другой – на кириллице \n")
latEntropy = entropy(text_reader("D://универ//Крипта//лабы//2//2//latin.txt"))
print("Энтропия латиницы: ", latEntropy)
kirEntropy = entropy(text_reader("D://универ//Крипта//лабы//2//2//kirilitsa.txt"))
print("Энтропия кириллицы: ", kirEntropy)
# частоты появления символов алфавитов оформить в виде гистограмм
serialize("D://универ//Крипта//лабы//2//2//probs_lat.xml", probs(text_reader("D://универ//Крипта//лабы//2//2//latin.txt")))
serialize("D://универ//Крипта//лабы//2//2//probs_kir.xml", probs(text_reader("D://универ//Крипта//лабы//2//2//kirilitsa.txt")))

# б) определить энтропию бинарного алфавита
print("\nДля входных документов, представленных в бинарных кодах, определить энтропию бинарного алфавита \n")
binEntropy = entropy(convert_to_ascii(text_reader("D://универ//Крипта//лабы//2//2//latin.txt")))
print("Энтропия бинарного для документа на латинице: ", binEntropy)
print("Энтропия бинарного для документа на кириллице: ", entropy(convert_to_ascii("D://универ//Крипта//лабы//2//2//kirilitsa.txt")))

# в) подсчитать кол - во информации в ФИО на исх.алфавите и кодах ASCII
print("\nПодсчитать количество информации в сообщении, состоящем из собственных фамилии, имени и отчества\n")
print("Количество информации на латинице: ", quantity_of_information(latEntropy,"Siatkoŭskaja Kaciaryna Dźmitryjeŭna"))
print("Количество информации на кириллице: ", quantity_of_information(kirEntropy,"Сяткоўская Кацярына Дзмітрыеўна"))
print("Количество информации в ASCII: ", quantity_of_information(binEntropy,convert_to_ascii("Siatkoŭskaja Kaciaryna Dźmitryjeŭna")))

# г) вероятность 0,1
print("\nПри условии, что вероятность ошибочной передачи единичного бита сообщения составляет\n")
print("Количество информации на латинице с вероятностью 0,1: ", mistake_quantity(0.1,"Siatkoŭskaja Kaciaryna Dźmitryjeŭna",latEntropy))
print("Количество информации на кириллице с вероятностью 0,1: ", mistake_quantity(0.1,"Сяткоўская Кацярына Дзмітрыеўна",kirEntropy))
print("Количество информации в ASCII с вероятностью 0,1: " , mistake_quantity(0.1,convert_to_ascii("Siatkoŭskaja Kaciaryna Dźmitryjeŭna"),binEntropy))
# вероятность 0,5
print("\nКоличество информации на латинице с вероятностью 0,5: ",mistake_quantity(0.5,"Siatkoŭskaja Kaciaryna Dźmitryjeŭna", 1))
print("Количество информации на кириллице с вероятностью 0,5: ",mistake_quantity(0.5,"Сяткоўская Кацярына Дзмітрыеўна",1))
print("Количество информации в ASCII с вероятностью 0,5: ",mistake_quantity(0.5,convert_to_ascii("Siatkoŭskaja Kaciaryna Dźmitryjeŭna"),1))
# вероятность 1,0
print("\nКоличество информации на латинице с вероятностью 1,0: ",mistake_quantity(0.999,"Siatkoŭskaja Kaciaryna Dźmitryjeŭna",latEntropy))
print("Количество информации на кириллице с вероятностью 1,0: ",mistake_quantity(0.999,"Сяткоўская Кацярына Дзмітрыеўна",kirEntropy))
print("Количество информации в ASCII с вероятностью 1,0: " ,mistake_quantity(0.999,convert_to_ascii("Siatkoŭskaja Kaciaryna Dźmitryjeŭna"),binEntropy))
