#!/usr/bin/env python

# Read in two neighborhood avg-CSV files and compare them.

import argparse, csv, collections, json
parser = argparse.ArgumentParser()
parser.add_argument('--city1_file', default='pgh_nghd_autotags.json')
parser.add_argument('--city2_file', default='sf_nghd_autotags.json')
args = parser.parse_args()

city1 = json.load(open(args.city1_file))
city2 = json.load(open(args.city2_file))

for nghd1 in city1:
    for nghd2 in city2:
        if nghd1 == 'None' or nghd2 == 'None':
            continue
        tags1 = city1[nghd1]['autotags_90plus_minusbaseline']
        tags2 = city2[nghd2]['autotags_90plus_minusbaseline']
        total = 0
        for tag in tags1:
            if tag in tags2:
                total += tags1[tag] * tags2[tag]
        print "%s and %s, dot product: %s" % (nghd1, nghd2, total)
