#!/usr/bin/env python3
# -*- coding:utf8 -*-
""" Executable """
from __future__ import print_function
import argparse
import pandas as pd
from scipy import stats


def analyze_efficiency(df, verbose=0):
    nav_methods = df.groupby('navigation')
    burger_df, swipe_df = nav_methods.get_group('burger'), nav_methods.get_group('swipe')

    burger = burger_df["time_ms"]
    burger_shapiro = stats.shapiro(burger)
    burger_normality = burger_shapiro[1] < 0.05
    print("Checking Burger for normal distribution:", burger_normality, burger_shapiro)


    burger_tasks = [group["time_ms"] for _, group in burger_df.groupby("Tid")]
    # alternatives: repeated measures anova, friedmann test
    print("[BURGER] Kruskal-Wallis H-Test: ", stats.kruskal(*burger_tasks))
    print("[BURGER] Friedmann Chi Square: ", stats.friedmanchisquare(*burger_tasks))
    # FIXME do these tests work as expected? (they report low p values but the data is all the same)


    if verbose:
        print("Burger Navigation",burger.describe(), sep="\n")

    for tid, swipe_task_df in swipe_df.groupby("Tid"):
        swipe_task = swipe_task_df["time_ms"]
        if verbose:
            print("Swipe Navigation, Task %d" %tid, swipe_task.describe(), sep="\n")
        swipe_task_shapiro = stats.shapiro(swipe_task)
        swipe_task_normality = swipe_task_shapiro[1] < 0.05
        print ("Checking Task", tid, "for normal distribution:", swipe_task_normality, swipe_task_shapiro)

        result = stats.ttest_ind(swipe_task, burger, equal_var=False)\
            if (burger_normality and swipe_task_normality) else\
            stats.mannwhitneyu(swipe_task, burger)
        print(tid, ":", result, result[1] < 0.05)


def main():
    """ Main Function """
    parser = argparse.ArgumentParser()
    parser.add_argument("file", nargs='?',type=argparse.FileType('r'), default="data-format.csv")
    parser.add_argument("-v", "--verbose", action="count", default=0)
    args = parser.parse_args()
    df = pd.read_csv(args.file)

    # assert that we have the same number of samples for each Pid, Tid per navigation method, ...
    check = {str(field) : len(pd.unique([len(group) for _, group in df.groupby(field)])) == 1
             for field in ["Pid", ["navigation","Tid"]]}
    print("Dataset Validation:", check)
    analyze_efficiency(df, verbose=args.verbose)

    exit(0)


if __name__ == '__main__':
    main()
