#!/usr/bin/env python3
# -*- coding:utf8 -*-
""" Executable """
from __future__ import print_function
import argparse
import pandas as pd
from scipy import stats

def is_significant(pvalue, alpha=0.05):
    return pvalue < alpha

def dagostino_or_shapiro(data):
    n = len(data)
    test = stats.normaltest if n >= 20 else stats.shapiro
    result = test(data)
    return result


def analyze_efficiency(df, verbose=0):
    nav_methods = df.groupby('navigation')
    burger_df, swipe_df = nav_methods.get_group('burger'), nav_methods.get_group('swipe')
    print("%d BURGERS vs %d SWIPERS" % (len(burger_df.groupby('pid')), len(swipe_df.groupby("pid"))))
    # print("=" * 78)
    print("[BURGER]" + "=" * 70)
    burger = burger_df["time_ms"]
    normality_test = dagostino_or_shapiro(burger)
    burger_isnorm = is_significant(normality_test[1])
    print("Normality>", normality_test, burger_isnorm)

    burger_tasks = [group["time_ms"] for _, group in burger_df.groupby("tid")]
    # alternatives: repeated measures anova, friedmann test
    print(stats.kruskal(*burger_tasks))
    print(stats.friedmanchisquare(*burger_tasks))
    # FIXME do these tests work as expected? (they report low p values but the data is all the same)


    if verbose:
        print("[BURGER] Description",burger.describe(), sep="\n")

    for tid, swipe_task_df in swipe_df.groupby("tid"):
        print("=" * 78)
        swipe_task = swipe_task_df["time_ms"]
        d = swipe_task_df["distance"].abs().mean()
        if verbose:
            print("[SWIPE: Task %d(d=%.1f)] Description" % (tid, d), swipe_task.describe(), sep="\n")
        # Dagostino Pearson if possible, else shapiro
        normality_test = dagostino_or_shapiro(swipe_task)
        swipe_task_isnorm = is_significant(normality_test[1])
        print("[SWIPE: Task %d(d=%.1f)] Normality" % (tid, d), normality_test, swipe_task_isnorm, sep="\n")

        result = stats.ttest_ind(swipe_task, burger, equal_var=False)\
            if (burger_isnorm and swipe_task_isnorm) else\
            stats.mannwhitneyu(swipe_task, burger)
        print("[SWIPE: Task %d(d=%.1f)]" % (tid, d), result, is_significant(result[1]))


def main():
    """ Main Function """
    parser = argparse.ArgumentParser()
    parser.add_argument("file", nargs='?',type=argparse.FileType('r'), default="prepilot.csv")
    parser.add_argument("-v", "--verbose", action="count", default=1)
    args = parser.parse_args()
    df = pd.read_csv(args.file)

    # assert that we have the same number of samples for each pid, tid per navigation method, ...
    check = {str(field) : len(pd.unique([len(group) for _, group in df.groupby(field)])) == 1
             for field in ["pid", ["navigation","tid"]]}
    print("Dataset Validation:", check)
    analyze_efficiency(df, verbose=args.verbose)

    exit(0)


if __name__ == '__main__':
    main()
