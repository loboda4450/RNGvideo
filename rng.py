import multiprocessing
import sys
import os

import time
import Primes
import RNGutils
import cv2
import numpy as np
from math import log, e
import matplotlib.pyplot as plotter


def get_seed_from_pixel():
    video = cv2.VideoCapture('video_sample.mp4')
    w, h = int(video.get(3)), int(video.get(4))
    frames = []
    success, image = video.read()

    while success:
        success, image = video.read()
        try:
            frames.append(image)
        except Exception as e:
            pass

    frame_num, width, height = int(time.time() * 1000 % len(frames)), int(time.time() * 1000 % w), int(
        time.time() * 1000 % h)

    video.release()

    return int(sum(frames[frame_num][height][width]) / len(frames[frame_num][height][width]))


def entropy_handler(random_array, base=None):
    plotter.hist(random_array, 256)
    plotter.show()
    entropy = 0.
    n_labels = len(random_array)
    if n_labels <= 1:
        return 0

    value, counts = np.unique(random_array, return_counts=True)
    probs = counts / n_labels
    n_classes = np.count_nonzero(probs)
    if n_classes <= 1:
        return 0

    base = e if base is None else base
    for i in probs:
        entropy -= i * log(i, base)

    return entropy


def worker(length, rnd_range, threads):
    primes = Primes.Primes()
    rng = RNGutils.RNGutils()

    with open("output.txt", "a+") as file:
        seed = get_seed_from_pixel()
        [file.write(f'{number}\n') for number in
         rng.sequence(primes=primes, pixel_seed=seed, length=int(length / threads), rnd_range=rnd_range)]

    file.close()

    return


def main():
    try:
        os.remove('output.txt')
        print('removed output file!')
    except Exception as e:
        print(f'Error: {e}')

    if sys.argv[1] == "--sequence":
        start = time.time()
        processes = []

        for i in range(int(sys.argv[4])):
            p = multiprocessing.Process(target=worker, args=(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]),))
            processes.append(p)
            p.start()

        for process in processes:
            process.join()

        end = time.time()
        with open('output.txt') as f:
            print(f'{sys.argv[2]} random numbers sequence generated in {end - start}\nentropy: {entropy_handler([int(line.strip()) for line in f if line.strip()], base=2)}')

        f.close()

    elif sys.argv[1] == "--single":
        primes = Primes.Primes()
        rng = RNGutils.RNGutils()
        print("Single mode\n")
        video = cv2.VideoCapture('video_sample.mp4')
        seed = get_seed_from_pixel()
        video.release()
        with open("output.txt", "w+") as file:
            string = f'{rng.single(primes=primes, pixel_seed=seed, rnd_range=int(sys.argv[2]))}\n'
            if "-" not in string:
                file.write(string)
                print(string)

        file.close()


if __name__ == '__main__':
    main()
