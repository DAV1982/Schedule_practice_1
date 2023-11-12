import schedule
import requests


def greeting():
    todos_dict = {
        '8:00': 'Drink coffee',
        '11:00': 'Work meeting',
        '23:59': 'Hack the Planet!'
    }

    print("Day's tasks")
    for k, v in todos_dict.items():
        print(f'{k} - {v}')

    response = requests.get(url='https://yobit.net/api/3/ticker/btc_usd')
    data = response.json()
    btc_price = f"BTC: {round(data.get('btc_usd').get('last'), 2)}$\n"

    print(btc_price)


def main():
    #greeting()

    schedule.every(4).seconds.do(greeting)

    while True:
        schedule.run_pending()


if __name__ == '__main__':
    main()
