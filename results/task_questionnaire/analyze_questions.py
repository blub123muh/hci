#!/usr/bin/env python3
# -*- coding:utf8 -*-
from __future__ import print_function
import argparse
import pandas as pd
# from scipy import stats


def analyze_questionnaire(df):

    for nav_method, nav_method_df in df.groupby('navigation'):
        print(nav_method, "=" * 42)
        for qid, qdf in nav_method_df.groupby("qid"):
            print("Question%d" % qid, qdf["result"].describe(), sep="\n")


def main():
    """ Main Function """
    parser = argparse.ArgumentParser()
    parser.add_argument("file", nargs='+', type=argparse.FileType('r'))
    args = parser.parse_args()
    print("Loading files", *(f.name for f in args.file))
    df = pd.concat(pd.read_csv(f) for f in args.file)
    print(df.shape)
    df = df[df["tid"] != 0]  # drop training
    analyze_questionnaire(df)

    exit(0)

if __name__ == '__main__':
    main()
