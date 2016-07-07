#!/usr/bin/env python3
# -*- coding:utf8 -*-
"""
Description: Script for analyzing SwipingBurger results
"""
#  Imports {{{ #
from __future__ import print_function
import argparse
import pandas as pd
import sys
from scipy import stats
#  }}} Imports #

NORMALITY_TEST = stats.shapiro

#  Helpers {{{ #

def print_section(header, fillchar="=", textwidth=80, **kwargs):
    """ This is super fancy. """
    filled = header + (textwidth - len(header)) * fillchar
    print(filled, **kwargs)


def print_md_table(df, append=False):
    if not append:
        print()
    for key in df.keys():
        print("|", " | ".join([key, str(df[key])]), '|')


def print_md_header(level, *args):
    print()
    print("#" * level, *args)


def print_md_paragraph(*args, lineblock=False, append=False):
    if not append:
        print()
    if lineblock:
        for arg in args:
                print("|", arg)
    else:
        print(*args)


def print_md_list(*args,
                  bullet="*",
                  indentlevel=0,
                  shiftwidth=4,
                  append=False,
                  enum=False,
                  compact=True):
    indent = indentlevel * shiftwidth
    if not append:
        print()
    if enum:
        for idx, arg in enumerate(args):
            if not compact:
                print()
            print(indent * " " + "{}.".format(idx+1), arg)
    else:
        for arg in args:
            if not compact:
                print()
            print(indent * " " + bullet, arg)


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
    # return stats.normaltest(data) if len(data) >= 20 else stats.shapiro(data)
    return stats.shapiro(data)


def t_or_u(x, y, normtest=stats.shapiro, verbose=0):
    """ If both samples are normal distributed (tested via dagostino or
    shapiro), consult t-test, else consult u-test.

    :sample1: array-like of sample 1 to compare
    :sample2: array-like of sample 2 to compare
    :normtest: Defaults to stats.shapiro, normtest(sample)[1] should return
    pvalue
    :returns: result of either the t-test or the u-test

    """
    x_ntresult, y_ntresult = normtest(x), normtest(y)
    if verbose:
        print_md_paragraph(x_ntresult, y_ntresult, lineblock=True)
    # ha... 2nd statement was never evaluated until grouping by jobs
    # some misspelling of is_significant
    t_ok = not is_significant(x_ntresult[1]) and not is_significant(y_ntresult[1])

    testresult = stats.ttest_ind(x, y, equal_var=False) if t_ok else stats.mannwhitneyu(x, y)
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
#  }}} Helpers #
#  Task Questionnaire {{{1 #
def analyze_task_questionnaire(df, verbose=0):
    """Analyzes the task questionnaires and prints the results

    :df: The dataframe to operate on
    :returns: None

    """
    print_md_header(2, "Analysis of Task Questionnaires")
    for qid, question_df in df.groupby("qid"):
        print_md_header(3, "Question {}".format(qid))
        burger_df, swipe_df = split_groups(df, 'navigation', ['burger',
                                                              'swipe'])
        burger_tasks = split_groups(burger_df, 'tid', select='result')
        swipe_tasks = split_groups(swipe_df, 'tid', select='result')

        print_md_header(4, "Repeated Measures")
        print_md_paragraph("Burger:", stats.kruskal(*burger_tasks),
                           "Swipe:", stats.kruskal(*swipe_tasks),
                           lineblock=True)

        for (burger_tid, burger_task_df), (swipe_tid, swipe_task_df)\
                in zip(burger_df.groupby("tid"), swipe_df.groupby("tid")):
            burger_task, swipe_task = burger_task_df["result"],\
                swipe_task_df["result"]
            print_md_header(4, "Burger Task {} vs Swipe Task\
                            {}".format(burger_tid, swipe_tid))
            if verbose:
                print_md_paragraph("Burger Description:")
                print_md_table(burger_task.describe())
                print_md_paragraph("Swipe Description:")
                print_md_table(swipe_task.describe())

            result = t_or_u(swipe_task, burger_task)
            print_md_paragraph("H0: %.2f[S] == %.2f[B]"
                               % (swipe_task.mean(), burger_task.mean()),
                               result, "Reject? %s" %
                               is_significant(result[1]), lineblock=True)
#  Task Quesionnaire}}} #
#  Final Questionnaire {{{ #
def analyze_final_questionnaire(df, verbose=0):
    print_md_header(2, "Analysis of Final Questionnaire")
    for qid, question_df in df.groupby("qid"):
        print_md_header(3, "Question {}".format(qid))
        burger, swipe = split_groups(question_df,
                                     'navigation',
                                     ['burger', 'swipe'],
                                     'result')

        if verbose:
            print_md_header(4, "Burger Description")
            print_md_table(burger.describe())

        if verbose:
            print_md_header(4, "Swipe Description")
            print_md_table(swipe.describe())

        # burger_isnorm = is_significant(dagostino_or_shapiro(burger)[1])
        # swipe_isnorm = is_significant(dagostino_or_shapiro(swipe)[1])

        print_md_header(4, "Swipe vs Burger")
        # result = stats.mannwhitneyu(swipe, burger)
        result = t_or_u(swipe, burger)
        print_md_paragraph("H0: %.2f[S] == %.2f[B]" % (swipe.mean(),
                                                       burger.mean()), result,
                           "Reject? %s" % is_significant(result[1]),
                           lineblock=True)

#  }}} Final Questionnaire #
#  Descriptive Statistics {{{ #
def print_descriptions(*samples):
    """print_descriptions

    :param *samples:
    """
    for desc, sample in samples:
        print_md_header(3, *desc)
        print_md_table(sample.describe())

#  }}} Descriptive Statistics #
#  Efficiency {{{ #
def cross_compare(*samples):
    """cross_compare
    :param *samples:
    """
    for i, (x_desc, x) in enumerate(samples):
        for y_desc, y in samples[i+1:]:
            yield (x_desc,y_desc), t_or_u(x, y)


def one_vs_rest(one, *rest):
    """one_vs_rest

    :param one:
    :param *rest:
    """
    x_desc, x = one
    for y_desc, y in rest:
        yield ((x_desc, y_desc), t_or_u(x, y))


def analyze_efficiency(df, split_by='tid', verbose=0):
    burger_df, swipe_df = split_groups(df, 'navigation', ['burger', 'swipe'])

    print_md_header(2, "Burger over all {} values".format(split_by))

    burger_tasks = split_groups(burger_df, split_by, select='time_ms')
    # alternatives: repeated measures anova, friedmann test
    print_md_paragraph("Repeated Measures:", stats.kruskal(*burger_tasks),
                       lineblock=True)
    # no friedmann (sucks at distances) stats.friedmanchisquare(*burger_tasks))

    burger = burger_df["time_ms"]
    normality_test = dagostino_or_shapiro(burger)
    burger_isnorm = is_significant(normality_test[1])
    print_md_paragraph(normality_test, burger_isnorm, lineblock=True)
    burger_mean = burger.mean()

    if verbose:
        print_md_paragraph("Description:")
        print_md_table(burger.describe())

    print_md_header(2, 'Swipe')
    for tid, swipe_task_df in swipe_df.groupby(split_by):
        print_md_header(3, 'Swipe {0} {1}'.format(split_by, tid))
        if 'distance' in swipe_task_df:
            d = swipe_task_df['distance'].abs().mean()
            print_md_paragraph('Mean Distance : %2.f' % d)
        swipe_task = swipe_task_df['time_ms']
        if verbose:
            print_md_paragraph('Description:')
            print_md_table(swipe_task.describe())
            normality_test = dagostino_or_shapiro(swipe_task)
            swipe_task_isnorm = is_significant(normality_test[1])
            print_md_paragraph('Normality:', normality_test, swipe_task_isnorm,
                               lineblock=True)

        result = t_or_u(swipe_task, burger)
        print_md_paragraph("H0: %.2f[S] == %.2f[B]" % (swipe_task.mean(),
                                                       burger_mean), result,
                           "Reject? %s" % is_significant(result[1]),
                           lineblock=True)

#  }}} Efficiency #
#  Effectiveness {{{ #
def analyze_effectiveness(df, verbose=0):
    # TODO: also analyze single tasks
    print_md_header(2, "Effectiveness")
    df['success'] = df.apply(success, axis=1)
    burger, swipe = split_groups(df,
                                   'navigation',
                                   ['burger', 'swipe'],
                                   'success')
    if verbose:
        print_md_paragraph("Burger Description")
        print_md_table(burger.describe())
        print_md_paragraph("Swipe Description")
        print_md_table(swipe.describe())

    result = t_or_u(swipe,burger)
    print_md_paragraph("H0: %.4f[S] == %.4f[B]" % (swipe.mean(),
                                        burger.mean()), result,
        "Reject? %s" % is_significant(result[1]), lineblock=True)
#  }}} Effectiveness #

def print_full_description(groups, h=0):
    """TODO: Docstring for print_descriptions.

    :series: TODO
    :returns: TODO

    """
    for desc, sample in groups:
        print_md_header(h, desc)
        print_md_table(sample.describe())
        print_md_paragraph(NORMALITY_TEST.__name__,
                        NORMALITY_TEST(sample),
                        lineblock=True)
    pass

def print_full_analysis(df, field, h=1, by="tid", gd=True, sd=True, ffa=True, ovr=True, ovo=True):
    """Performs a full analysis of the data

    :df: THE data frame
    :field: field of interest such as 'time_ms' or 'success'
    :by: perform grouping on this attribute (the higher level split on
    "navigation" is always performed)
    :h: header level to start with
    :returns: nothing.

    """
    if by is None:
        sd = ffa = ovr = False
    nav_methods = df.groupby("navigation")
    if ffa or sd:
        groups = df.groupby(["navigation", by])[field]

    print_md_header(h, "Descriptions [{}]".format(field))

    # Global Descriptions
    if gd:
        print_md_header(h+1, "Global Descriptions [{}]".format(field))
        print_full_description(nav_methods[field],h=h+2)
    if sd:
        print_md_header(h+1, "Descriptions per {} [{}]".format(by, field))
        print_full_description(groups, h=h+2)

    # free for all
    if ffa:
        print_md_header(h, "Cross-compare Tests per {} [{}]".format(by, field))
        for desc, result in cross_compare(*groups):
            print_md_header(h+1, "{} vs {}".format(*desc))
            print_md_paragraph(result)

    # one vs rest
    if ovr:
        print_md_header(h, "Global Burger vs Swipe per {} Tests [{}]".format(by, field))
        burger = "burger", nav_methods.get_group("burger")[field]
        swipe_tasks = nav_methods.get_group("swipe").groupby(by)[field]
        for desc, result in one_vs_rest(burger, *swipe_tasks):
            print_md_header(h+1, "{} vs swipe {}".format(*desc))
            print_md_paragraph(result)

    # one vs one
    if ovo:
        print_md_header(h,
                        "Global Burger vs Global Swipe Test [{}]".format(field))
        for desc, result in cross_compare(*nav_methods[field]):
            print_md_header(h+1, "{} vs {}".format(*desc))
            print_md_paragraph(result)

#  Main {{{ #
def main():
    """main"""
    parser = argparse.ArgumentParser()
    parser.add_argument("file", nargs='+', type=argparse.FileType('r'))
    parser.add_argument("-d","--distance", action='store_true', dest='distance',
                        default=False,
                        help="Also analyze by distance instead of task id")
    parser.add_argument("-D", type=argparse.FileType('r'), dest='demographics',
                        default=None,
                        help="Also analyze demographics")
    parser.add_argument("-q", nargs='+', dest="task_q",
                        type=argparse.FileType('r'), help="Specify files for\
                        task questionnaire analysis.")
    parser.add_argument("-Q", nargs='+', dest="final_q",
                        type=argparse.FileType('r'), help="Specify files for\
                        final questionnaire analysis.")
    parser.add_argument("-v", "--verbose", action="count", default=0)
    args = parser.parse_args()

    print_md_header(1, "Analysis")
    print_md_header(2, "Preprocessing")
    print_md_paragraph(args)
    print_md_list(*[f.name for f in args.file])
    df = pd.concat(pd.read_csv(f) for f in args.file)
    if args.task_q:
        print_md_list(*[f.name for f in args.task_q], append=True)
        df_q = pd.concat(pd.read_csv(f) for f in args.task_q)
    if args.final_q:
        print_md_list(*[f.name for f in args.final_q], append=True)
        df_Q = pd.concat(pd.read_csv(f) for f in args.final_q)
    if args.demographics:
        print_md_list(*[f.name for f in args.demographics], append=True)
        df_D = pd.concat(pd.read_csv(f) for f in args.final_q)

    # move this somewhere else
    burger_df, swipe_df = split_groups(df,'navigation', ['burger','swipe'])
    N_burger = len(burger_df.groupby('pid'))
    N_swipe = len(swipe_df.groupby('pid'))
    print_md_paragraph("N = {}".format(N_burger+N_swipe),
                       "Nswipe = {}".format(N_swipe),
                       "Nburger = {}".format(N_burger),
                       lineblock=True)


    # TID 0 is training.
    print_md_paragraph("Dropping Task ID 0 (Training)")
    df = df[df["tid"] != 0]
    if args.task_q:
        df_q = df_q[df_q["tid"] != 0]

    print_md_paragraph("Asserting Absolute Distance Values!")
    df["distance"] = df["distance"].abs()

    # assert that we have the same number of samples for each pid, tid per
    # navigation method, ...
    chk = {str(field):
           len(pd.unique([len(group) for _, group in df.groupby(field)])) == 1
           for field in ["pid"]}

    print_md_paragraph("Dataset Validation:", chk, lineblock=True)

    print_md_paragraph("Adding success column based on",
                        "`opt_interactions == interactions`",
                       "in order to measure effectiveness.",
                        lineblock=True)
    df['success'] = df.apply(success, axis=1)

    if args.demographics:
        print_md_header(2, "Demographics")
        pass

    # REVISED BEGIN
    print_md_header(2, "Efficiency by Tasks")
    print_full_analysis(df, "time_ms", h=3)

    if args.distance:
        print_md_header(2, "Efficiency by Distances")
        print_full_analysis(df, "time_ms", h=3, by="distance", ovo=False)

    print_md_header(2, "Effectiveness by Tasks")
    print_full_analysis(df, "success", h=3)

    if args.task_q:
        print_md_header(2, "Task Questionnaires")
        for desc, q in df_q.groupby("qid"):
            print_md_header(3, "Task Question {}".format(desc))
            print_full_analysis(q, "result", h=4, by="tid")

    if args.final_q:
        print_md_header(2, "Final Questionnaires")
        for desc, q in df_Q.groupby("qid"):
            print_md_header(3, "Final Question {}".format(desc))
            print_full_analysis(q, "result", h=4, by=None, sd=False, ffa=False, ovr=False)

    # REVISED END
    exit(0)


if __name__ == '__main__':
    main()
#  }}} Main #
# vim: set fdm=marker:
