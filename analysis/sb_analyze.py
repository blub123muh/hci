#!/usr/bin/env python3
# -*- coding:utf8 -*-
'''
File    : sb_analyze.py
Author  : Lukas Galke
Contact : vim@lpag.de
Date    : 2016 Jul 11

Description : Script for analyzing SwipingBurger results
'''
from __future__ import print_function
import argparse
import pandas as pd
import sys
from scipy import stats
import matplotlib.pyplot as plt


def print_md_table(df, append=False):
    """print_md_table

    :param df:
    :param append:
    """
    if not append:
        print()
        try:
            # DF
            cols = [" "] + df.columns
        except AttributeError:
            # Series
            cols = [" ", df.name]

        print("|", "|".join(cols), '|')
        dashes = ['-' * len(col) for col in cols]
        print("|", "|".join(dashes), '|')

    for key in df.keys():
        print("|", "|".join([key, str(df[key])]), '|')


def print_md_header(level, *args):
    """print_md_header

    :param level:
    :param *args:
    """
    print()
    print("#" * level, *args)


def print_md_paragraph(*args, **kwargs):
    """print_md_paragraph

    :param *args:
    :param lineblock:
    :param append:
    """
    lineblock = kwargs.pop('lineblock', False)
    append = kwargs.pop('append', False)
    if not append:
        print()
    if lineblock:
        for arg in args:
            print("|", arg)
    else:
        print(*args)


def print_md_list(*args, **kwargs):
    bullet = kwargs.pop('bullet', "*")
    indentlevel = kwargs.pop('indentlevel', 0)
    shiftwidth = kwargs.pop('shiftwidth', 4)
    append = kwargs.pop('append', False)
    enum = kwargs.pop('enum', False)
    compact = kwargs.pop('compact', True)
    """print_md_list

    :param *args:
    :param bullet:
    :param indentlevel:
    :param shiftwidth:
    :param append:
    :param enum:
    :param compact:
    """
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
    """opt_interactions
    Computes the optimal number of interactions
    :param row:
    """
    return 1 if row['navigation'] == 'burger' else abs(row['distance'])


def fail_interactions(row):
    """fail_interactions
    Computes the number of fail interactions
    :param row:
    """
    return opt_interactions(row) - row['n_interactions']


def effectiveness(row):
    """success

    :param row:
    """
    return 0 if fail_interactions(row) else 1


def efficiency(row):
    """efficiency

    :param row:
    """
    return 1000 * row['effectiveness'] / row['time_ms']


def is_significant(pvalue, alpha=0.05):
    """is_significant

    :param pvalue:
    :param alpha:
    """
    return pvalue < alpha


def pearson_or_shapiro(data):
    """pearson_or_shapiro

    Use D'agostino/Pearson if possible (n >= 20), else Shapiro
    :param data:
    """
    return stats.normaltest(data) if len(data) >= 20 else stats.shapiro(data)


def welch_satterthwaite(nobs1, std1, nobs2, std2):
    nominator = (std1**2/nobs1 + std2**2/nobs2)**2
    denominator = std1**4 / (nobs1 ** 2 * (nobs1 - 1))
    denominator += std2**4 / (nobs2 ** 2 * (nobs2 - 1))
    return nominator / denominator


def t_or_u(x, y, norm_test=stats.shapiro, verbose=0, dependent=False):
    """ If both samples are normal distributed (tested via dagostino or
    shapiro), consult t-test, else consult u-test.

    :sample1: array-like of sample 1 to compare
    :sample2: array-like of sample 2 to compare
    :normtest: Defaults to stats.shapiro, normtest(sample)[1] should return
    pvalue
    :returns: result of either the t-test or the u-test

    """
    if norm_test is not None:
        x_ntresult, y_ntresult = norm_test(x), norm_test(y)
        t_ok = not is_significant(
            x_ntresult[1], 0.05) and not is_significant(
            y_ntresult[1], 0.05)
    else:
        t_ok = True

    nobs1, nobs2 = len(x), len(y)
    nobs1, mean1, std1 = len(x), x.mean(), x.std()
    nobs2, mean2, std2 = len(y), y.mean(), y.std()
    nobs = nobs1 + nobs2

    result = {"N": nobs, "n1": nobs1, "n2": nobs2}
    if t_ok:
        # levene = stats.levene(x, y, center='mean')
        # eqvar = not is_significant(levene[1])
        if dependent:
            assert nobs1 == nobs2
            result['df'] = nobs1 - 1
            testresult = stats.ttest_rel(x, y)
        else:
            result['df'] = welch_satterthwaite(nobs1, std1, nobs2, std2)
            testresult = stats.ttest_ind(x, y, equal_var=False)

        effect_size = testresult[0] * (1/nobs1+1/nobs2)**0.5
        # result['levene'] = levene
        # result['equal_var'] = eqvar
    else:
        # no normal distributions
        if dependent:
            # dependent samples
            try:
                testresult = stats.wilcoxon(x, y)
                effect_size = 2 * testresult[0] / (nobs*nobs+1)
            except ValueError:
                testresult = "=== All pairs were equal ==="
                effect_size = "=== All pairs were equal ==="
        else:
            # independent samples
            testresult = stats.mannwhitneyu(x, y)
            effect_size = 1 - 2 * testresult[0] / (nobs1 * nobs2)

    result['test_result'] = testresult
    result['effect_size'] = effect_size
    return result


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


def cross_compare(*samples, **kwargs):
    """cross_compare
    :param *samples:
    """
    norm_test = kwargs.pop('norm_test', stats.shapiro)
    for i, (x_desc, x) in enumerate(samples):
        for y_desc, y in samples[i+1:]:
            dep = len(x_desc) >= 2 and len(y_desc) >= 2 and\
                x_desc[0] == y_desc[0]
            yield (x_desc, y_desc), t_or_u(x, y, norm_test=norm_test,
                                           dependent=dep)


def one_vs_rest(one, *rest, **kwargs):
    """one_vs_rest

    :param one:
    :param *rest:
    """
    norm_test = kwargs.pop('norm_test', stats.shapiro)
    x_desc, x = one
    for y_desc, y in rest:
        yield ((x_desc, y_desc), t_or_u(x, y, norm_test=norm_test))


def print_full_description(groups, norm_test=stats.shapiro, h=0):
    """TODO: Docstring for print_descriptions.

    :series: TODO
    :returns: TODO

    """
    for desc, sample in groups:
        print_md_header(h, desc)
        print_md_table(sample.describe())
        if norm_test:
            print_md_paragraph(norm_test.__name__,
                               norm_test(sample),
                               lineblock=True)


def print_full_analysis(df, field, h=1, by="tid", nt=stats.shapiro,
                        gd=True, sd=True, ffa=True, ovr=True, ovo=True):
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

    print_md_header(h, "Descriptions ({})".format(field))

    # Global Descriptions
    if gd:
        print_md_header(h+1, "Global Descriptions ({})".format(field))
        print_full_description(nav_methods[field], h=h+2, norm_test=nt)

    # Sample Descriptions
    if sd:
        print_md_header(h+1, "Repeated measures ({})".format(field))
        for desc, group in nav_methods:
            subgroups = [values for _, values in group.groupby(by)[field]]
            print_md_header(h+2, desc)
            print_md_paragraph(stats.kruskal(*subgroups),
                               stats.friedmanchisquare(*subgroups),
                               # stats.f_oneway(*subgroups),
                               lineblock=True)
        print_md_header(h+1, "Descriptions per {} ({})".format(by, field))
        print_full_description(groups, h=h+2, norm_test=nt)

    # free for all
    if ffa:
        print_md_header(h, "Cross-compare Tests per {} ({})".format(by, field))
        for desc, result in cross_compare(*groups, norm_test=nt):
            print_md_header(h+1, "{} vs {}".format(*desc))
            print_md_paragraph(result)

    # one vs rest
    if ovr:
        print_md_header(
            h, "Global Burger vs Swipe per {} Tests ({})".format(
                by, field))
        burger = "burger", nav_methods.get_group("burger")[field]
        swipe_tasks = nav_methods.get_group("swipe").groupby(by)[field]
        for desc, result in one_vs_rest(burger, *swipe_tasks,
                                        norm_test=nt):
            print_md_header(h+1, "{} vs swipe {}".format(*desc))
            print_md_paragraph(result)

    # one vs one
    if ovo:
        print_md_header(h,
                        "Global Burger vs Global Swipe Test ({})"
                        .format(field))
        for desc, result in cross_compare(*nav_methods[field],
                                          norm_test=nt):
            print_md_header(h+1, "{} vs {}".format(*desc))
            print_md_paragraph(result)


def main():
    """main"""
    norm_tests = {"shapiro": stats.shapiro,
                  "pearson": stats.normaltest,
                  "sop": pearson_or_shapiro,
                  "None": None}
    parser = argparse.ArgumentParser()
    parser.add_argument("file", nargs='+', type=argparse.FileType('r'),
                        help="Specify experiment results file")
    parser.add_argument(
        "-d",
        "--distance",
        action='store_true',
        dest='distance',
        default=False,
        help="Also analyze by distance instead of task id")
    parser.add_argument("-D", "--demographics", type=argparse.FileType('r'),
                        dest='demographics',
                        default=None, nargs='+',
                        help="Also analyze demographics")
    parser.add_argument("-q", "--task-questionnaires", nargs='+',
                        dest="task_q",
                        type=argparse.FileType('r'), help="Specify files for\
                        task questionnaire analysis.")
    parser.add_argument("-Q", "--final-questionnaires", nargs='+',
                        dest="final_q",
                        type=argparse.FileType('r'), help="Specify files for\
                        final questionnaire analysis.")
    parser.add_argument("-n", "--norm-test", type=str, dest="norm_test",
                        default="shapiro",
                        choices=norm_tests.keys(),
                        help="Specify normality test, 'None' forces t-test")
    parser.add_argument("-e", "--effectiveness", action='store_true',
                        default=False,
                        dest="effectiveness",
                        help="Also compare effectiveness")
    parser.add_argument("-p", "--plot", action='store_true', default=False,
                        dest="plot",
                        help="Also compare effectiveness")
    args = parser.parse_args()

    print_md_header(1, "Analysis")
    print_md_header(2, "Preprocessing")
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
        df_D = pd.concat(pd.read_csv(f) for f in args.demographics)

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

    print_md_paragraph("Dataset Validation:", chk.items(), lineblock=True)

    print_md_paragraph("Adding success column based on",
                       "`opt_interactions == interactions`",
                       "in order to measure effectiveness.",
                       lineblock=True)

    df["effectiveness"] = df.apply(effectiveness, axis=1)

    print_md_paragraph("Split by Navigation, Pid, Tid, apply `mean` combine!",
                       lineblock=True)
    df_by_tid = df.groupby(["navigation", "pid", "tid"]).mean().reset_index()
    print_md_paragraph("Drop jid and pid columns")
    df_by_tid = df_by_tid.drop("jid", axis=1)
    df_by_tid = df_by_tid.drop("pid", axis=1)

    print_md_paragraph("Computing efficiency task $1000 *\
                       mean_success/mean_time_ms$",
                       lineblock=True)

    df_by_tid['efficiency'] = df_by_tid.apply(efficiency, axis=1)

    norm_test = norm_tests[args.norm_test]
    if norm_test is not None:
        print_md_paragraph(
            "Using normality test: {}".format(
                norm_test.__name__))
    else:
        print_md_paragraph("No normality test, *Forcing t-test*!")

    if args.demographics:
        print_md_header(2, "Demographics")
        print_md_header(3, "age")
        print_md_table(df_D["age"].describe())
        for attribute in ["sex", "job", "smartphone", "comments"]:
            print_md_header(3, attribute)
            print_md_paragraph(*[(desc, len(subdf)) for desc, subdf in
                                 df_D.groupby(attribute)], lineblock=True)

    print_md_header(2, "Efficiency by Tasks")
    print_full_analysis(df_by_tid, "efficiency", h=3, by="tid", nt=norm_test)

    if args.effectiveness:
        print_md_header(2, "Effectiveness by Tasks")
        print_full_analysis(df_by_tid,
                            "effectiveness",
                            h=3,
                            by="tid",
                            nt=norm_test)

    if args.distance:
        print_md_header(2, "Efficiency by Distances")
        print_full_analysis(df, "efficiency", h=3, by="distance", ovo=False,
                            nt=norm_test)

    if args.task_q:
        print_md_header(2, "Task Questionnaires")
        for desc, q in df_q.groupby("qid"):
            print_md_header(3, "Task Question {}".format(desc))
            print_full_analysis(q, "result", h=4, by="tid", nt=norm_test)

    if args.final_q:
        print_md_header(2, "Final Questionnaires")
        for desc, fq in df_Q.groupby("qid"):
            print_md_header(3, "Final Question {}".format(desc))
            print_md_header(4, "Just counts grouped by Results")

            print_md_paragraph(*["Navigation {} answered {} stars:\
                                 {}".format(*desc, len(subdf)) for desc, subdf
                                 in fq.groupby(["navigation", "result"])],
                               lineblock=True)
            print_md_header(4, "{} Description".format(desc))
            print_md_table(fq['result'].describe())

            print_full_analysis(fq, "result", h=4, by=None, sd=False,
                                ffa=False,
                                ovr=False, nt=norm_test)

    if args.plot:
        df_plot = df_by_tid.groupby(['navigation',
                                     'tid'])['efficiency']
        values = {str(desc): value for desc, value in df_plot}

        df_plot = pd.DataFrame(values)

        # print(df_plot, file=sys.stderr)
        df_plot.plot.box()
        plt.show()

    exit(0)

if __name__ == '__main__':
    main()
