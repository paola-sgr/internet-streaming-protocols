#! /usr/bin/env python3

import argparse

import mysound


def main(duration, frequency, bar_period):
    sound = mysound.Sound(duration)
    sound.sin(frequency, 10000)
    print(sound.bars(bar_period))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('duration', type=float, help='Duration')
    parser.add_argument('frequency', type=float, help='Frequency',
                        nargs='?', default=440)
    parser.add_argument('bar_period', type=float, help='Bar period',
                        nargs='?', default=0.0001)
    args = parser.parse_args()
    main(args.duration, args.frequency, args.bar_period)
