import csv
import re


def get_coin_data():
    coin_data = {}
    with open("C:\\Users\sash9\Desktop\практика\currencies22.csv", 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            name = re.sub(r'\\s','', row[0].lower())
            price = re.sub(r'[^0-9\\.]','', row[1])
            cap =  re.sub(r'[^0-9]','', row[2])
            coin_data[name] = {"Price":float(price), "Market_cap":int(cap)}
            #print(name, float(price), int(cap))
    return coin_data


def main():
    coin_data = get_coin_data()
    while True:
        name = input("название валюты или пустая строка для остановки: ")
        if len(name)==0:
            break
        name = re.sub(r'\\s','',name.lower())
        if name in coin_data:
            for key, val in coin_data[name].items():
                print(key, val)
        else:
            print("coin not found")


if __name__ == "__main__":
    main()
