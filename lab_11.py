from zipfile import ZipFile
import re


pattern_2 = '.+.{1}2[7-9]/Mar/2009:([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9].+GET.*robots.txt.*'

pattern_1 = '.+.{1}26/Mar/2009:(1[4-9]:(49:2[3-9]|5[0-9]:[0-5][0-9])|2[0-3]:[0-5][0-9]:[0-5][0-9]).+GET.*robots.txt.*'

pattern_3 = '.+.{1}30/Mar/2009:(0[0-8]:[0-5][0-9]:[0-5][0-9]|(0[0-9]|1[0-7]):([0-2][0-9]|3[0-6])).+GET.*robots.txt.*'

if __name__ == '__main__':
    file = "access.log.zip"
    with ZipFile(file, 'w') as zip_file:
        zip_file.write("access.log.txt")

    with ZipFile(file, 'r') as zip_file:
        unpacked_file = zip_file.extract("access.log.txt")

    f = open(unpacked_file, "r")
    lines = f.readlines()
    results = []
    for line in lines:
        if re.search(pattern_1, line) or re.search(pattern_2, line) or re.search(pattern_3, line) is not None:
            results.append(line)
    for i in results:
        print(i)
