#!/usr/bin/env python3
# -*- coding:utf8 -*-
""" Executable """
from __future__ import print_function
import argparse
import pandas as pd
from scipy import stats


def analyze_efficiency(df):
    nav_methods = df.groupby('navigation')
    burger_df, swipe_df = nav_methods.get_group('burger'), nav_methods.get_group('swipe')

    burger = burger_df["time_ms"]
    burger_normality = stats.shapiro(burger)[1] < 0.05
    print("Checking Burger for normal distribution:", burger_normality)
    print("Burger Navigation",burger.describe(), sep="\n")

    for tid, swipe_task_df in swipe_df.groupby("Tid"):
        swipe_task = swipe_task_df["time_ms"]
        swipe_task_normality = stats.shapiro(swipe_task)[1] < 0.05
        print ("Checking Task", tid, "for normal distribution:", swipe_task_normality)

        if burger_normality and swipe_task_normality:
            result = stats.ttest_ind(swipe_task, burger, equal_var=False)
        else:
            result = stats.mannwhitneyu(swipe_task, burger)

        # result = stats.ttest_ind(swipe_task, burger, equal_var=False) if (burger_normality and swipe_task_normality) else stats.mannwhitneyu(swipe_task, burger)
        print(tid, ":", result, result[1] < 0.05)


def main():
    """ Main Function """
    parser = argparse.ArgumentParser()
    parser.add_argument("file", nargs='?',type=argparse.FileType('r'), default="data-format.csv")
    args = parser.parse_args()
    df = pd.read_csv(args.file)

    check = {str(field) : len(pd.unique([len(group) for _, group in df.groupby(field)])) == 1 for field
             in ["Pid", ["navigation","Tid"]]}
    print("Dataset Validation:", check)
    analyze_efficiency(df)

    exit(0)


if __name__ == '__main__':
    main()
