import os
import argparse

# argparse
parser = argparse.ArgumentParser()
parser.add_argument('directory')
args = parser.parse_args()
print(args.directory)

#Variables
i = 1

for file in os.listdir(args.directory):
    if file.endswith('.jpg'):
        os.rename(args.directory + '/' + file, args.directory + '/' + str(i) + '.jpg')
    elif file.endswith('.png'):
        os.rename(args.directory + '/' + file, args.directory + '/' + str(i) + '.png')
    i += 1