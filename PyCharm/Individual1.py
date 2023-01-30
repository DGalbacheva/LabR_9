#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from datetime import time

if __name__ == '__main__':
    trains = []
    while True:
        command = input('>>> ').lower()

        if command == 'exit':
            break

        elif command == 'add':
            destination = input("Название пункта назначения: ")
            number = int(input("Номер поезда: "))
            time = input("Время отправления: ")

            train = {
                'destination': destination,
                'number': number,
                'time': time,
            }

            trains.append(train)
            if len(trains) > 1:
                trains.sort(key=lambda item: item.get('number', ''))

        elif command == 'list':
            for idx, train in enumerate(trains, 1):
                print(
                    '| {:>4} | {:<10} | {:<10} | {:>8} |'.format(
                        idx,
                        train.get('number', 0),
                        train.get('destination', ''),
                        train.get('time', '')
                    )
                )

        elif command.startswith('select'):
            parts = command.split(' ', maxsplit=1)
            num = int(parts[1])

            for train in trains:
                if num == train.get('number', ''):
                    print(
                        "Поезде с номером {:>1} отправляется в город {:>1} в {:>1}".format(
                            num,
                            train.get('destination', ''),
                            train.get('time', '')
                        )
                    )
                    break

            else:
                print("Поезд с заданным номером не найдены.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
