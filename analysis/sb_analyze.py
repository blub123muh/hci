#!/usr/bin/env python3
# -*- coding:utf8 -*-
""" Executable """
from __future__ import print_function
import argparse
import pandas as pd
from scipy import stats

# {{{1 Helper Functions
def print_section(header, fillchar="=", textwidth=80, **kwargs):
    """ This is super fancy. """
    filled = header + (textwidth - len(header)) * fillchar
    print(filled, **kwargs)


def opt_interactions(row):
    """ Computes the optimal number of interactions """
    return 1 if row['navigation'] == 'burger' else abs(row['distance'])


def fail_interactions(row):
    """ Computes the number of fail interactions """
    return opt_interactions(row) - row['n_interactions']

def success(row):
    return not fail_interactions(row)


def is_significant(pvalue, alpha=0.05):
    """ Return: Boolean significance value """
    return pvalue < alpha

def dagostino_or_shapiro(data):
    """ Use D'agostino/Pearson if possible (n >= 20), else Shapiro"""
    return stats.normaltest(data) if len(data) >= 20 else stats.shapiro(data)

def t_or_u(sample1,sample2):
    """ If both samples are normal distributed (tested via dagostino or
    shapiro), consult t-test, else consult u-test.

    :sample1: array-like of sample 1 to comprae
    :sample2: array-like of sample 2 to compare
    :returns: TODO

    UNUSED
    """
    both_norm = is_significant(dagostino_or_shapiro(sample1)[1]) and\
        is_significant(dagostino_or_shapiro(sample2)[1])

    testresult = stats.ttest_ind(sample1, sample2, equal_var=False)\
            if both_norm else\
            stats.mannwhitneyu(sample1, sample2)
    return testresult

def split_groups(df, key, values=None, select=None):
    """Splits df on key and returns i < len(values) dataframes with
    df[key]=values[i]

    :df: DataFrame
    :key: Column Identifier
    :values: Column values to split on
    :select: Returns a i series by selecting select
    :returns: List of i dataframes with df[key]=values[i]
    """
    groups = df.groupby(key)

    groups = [groups.get_group(value) for value in values] if values\
        else [group for _, group in groups]

    if select:
        groups = [group[select] for group in groups]

    return groups
#  1}}} #
#  Task Questionnaire {{{1 #
def analyze_task_questionnaire(df, verbose=0):
    """Analyzes the task questionnaires and prints the results

    :df: The dataframe to operate on
    :returns: None

    """
    for qid, question_df in df.groupby("qid"):
        print_section("Question {}".format(qid))
        burger_df, swipe_df = split_groups(df, 'navigation', ['burger',
                                                                'swipe'])
        # Repeated measures
        # burger_tasks = [group["result"] for _, group in burger_df.groupby('tid')]
        # swipe_tasks = [group["result"] for _, group in swipe_df.groupby('tid')]
        burger_tasks = split_groups(burger_df, 'tid', select='result')
        swipe_tasks = split_groups(swipe_df, 'tid', select='result')

        print("Repeated Measures burger:", stats.kruskal(*burger_tasks))
        print("Repeated Measures swipe:", stats.kruskal(*swipe_tasks))

        for (burger_tid, burger_task_df), (swipe_tid, swipe_task_df) in zip(burger_df.groupby("tid"),\
                swipe_df.groupby("tid")):
            burger_task, swipe_task = burger_task_df["result"],\
                swipe_task_df["result"]
            print_section("BURGER Task {} vs SWIPE Task {}".format(burger_tid,
                                                                swipe_tid),
                          fillchar="-")
            if verbose:
                print("Burger Description:", burger_task.describe(), sep="\n")
                print("Swipe Description:", swipe_task.describe(), sep="\n")

            result = t_or_u(swipe_task, burger_task)
            print("H0: %.2f[S] == %.2f[B]" % (swipe_task.median(),
                                              burger_task.median()), result,
                "Reject? %s" % is_significant(result[1]), sep="\n")
#  Task Quesionnaire}}} #
#  Final Questionnaire {{{ #
def analyze_final_questionnaire(df, verbose=0):
    for qid, question_df in df.groupby("qid"):
        print_section("Question {}".format(qid))
        burger, swipe = split_groups(question_df,
                                       'navigation',
                                       ['burger', 'swipe'],
                                       'result')

        if verbose:
            print_section("[Burger Description]", fillchar="-")
            print(burger.describe())

        if verbose:
            print_section("[Swipe Description]",fillchar="-")
            print(swipe.describe())

        # burger_isnorm = is_significant(dagostino_or_shapiro(burger)[1])
        # swipe_isnorm = is_significant(dagostino_or_shapiro(swipe)[1])

        print_section("[Swipe vs Burger]", fillchar="-")
        # result = stats.mannwhitneyu(swipe, burger)
        result = t_or_u(swipe,burger)
        print("H0: %.2f[S] == %.2f[B]" % (swipe.mean(),
                                            burger.mean()), result,
            "Reject? %s" % is_significant(result[1]), sep="\n")

#  }}} Final Questionnaire #
#  Efficiency {{{ #
def analyze_efficiency(df, verbose=0):
    burger_df, swipe_df = split_groups(df, 'navigation', ['burger', 'swipe'])

    print("%d BURGERS vs %d SWIPERS" % (len(burger_df.groupby('pid')),
                                        len(swipe_df.groupby('pid'))))
    print_section("[BURGER over all Tasks]")

    burger_tasks = split_groups(burger_df, 'tid', select='time_ms')
    # alternatives: repeated measures anova, friedmann test
    print("Repeated Measures:")
    print(stats.kruskal(*burger_tasks))
    print(stats.friedmanchisquare(*burger_tasks))

    burger = burger_df["time_ms"]
    normality_test = dagostino_or_shapiro(burger)
    burger_isnorm = is_significant(normality_test[1])
    print("Normality:", normality_test, burger_isnorm)
    burger_mean = burger.mean()

    if verbose:
        print("Description:", burger.describe(), sep="\n")

    for tid, swipe_task_df in swipe_df.groupby("tid"):
        print_section("[Swipe Task {}]".format(tid), fillchar="=")
        if 'distance' in swipe_task_df:
            d = swipe_task_df["distance"].abs().mean()
            print("mean distance=%1.f]" % d)
        swipe_task = swipe_task_df["time_ms"]
        if verbose:
            print("Description:", swipe_task.describe(), sep="\n")
            normality_test = dagostino_or_shapiro(swipe_task)
            swipe_task_isnorm = is_significant(normality_test[1])
            print("Normality:", normality_test, swipe_task_isnorm)

        result = t_or_u(swipe_task, burger)
        print("H0: %.2f[S] == %.2f[B]" % (swipe_task.mean(), burger_mean), result,
              "Reject? %s" % is_significant(result[1]), sep="\n")
#  }}} Efficiency #
#  Effectiveness {{{ #
def analyze_effectiveness(df, verbose=0):
    df['success'] = df.apply(success, axis=1)
    burger, swipe = split_groups(df,
                                   'navigation',
                                   ['burger', 'swipe'],
                                   'success')
    if verbose:
        print("Burger Description", burger.describe(), end="\n")
        print("Swipe Description", swipe.describe(), end="\n")

    result = t_or_u(swipe,burger)
    print_section("Effectiveness")
    print("H0: %.4f[S] == %.4f[B]" % (swipe.mean(),
                                        burger.mean()), result,
        "Reject? %s" % is_significant(result[1]), sep="\n")
#  }}} Effectiveness #
#  By Distance {{{ # 
def analyze_by_distance(df, verbose=0):
    # TODO
    pass
#  }}} By Distance # 
# {{{1 main
def main():
    """ Main Function """
    parser = argparse.ArgumentParser()
    parser.add_argument("file",
                        nargs='+',
                        type=argparse.FileType('r'))
    parser.add_argument("-v", "--verbose", action="count", default=0)
    args = parser.parse_args()
    print("Loading files", *(f.name for f in args.file))
    df = pd.concat(pd.read_csv(f) for f in args.file)
    print(df.shape)

    # TID 0 is training.
    if "tid" in df:
        df = df[df["tid"] != 0]

    # assert that we have the same number of samples for each pid, tid per
    # navigation method, ...
    chk = {str(field):
           len(pd.unique([len(group) for _, group in df.groupby(field)])) == 1
           for field in ["pid"]}

    print("Dataset Validation:", chk)

    if "time_ms" in df:
        analyze_efficiency(df, verbose=args.verbose)
        analyze_effectiveness(df, verbose=args.verbose)
    if "result" in df:
        if"tid" in df:
            analyze_task_questionnaire(df, verbose=args.verbose)
        else:
            analyze_final_questionnaire(df, verbose=args.verbose)

    exit(0)


if __name__ == '__main__':
    main()
# }}}1

# vim: set fdm=marker:
