
# Preprocessing


## Files


experiment_results/experiment_results.csvexperiment_results/experiment_results2.csv
experiment_results/experiment_results.csvtablet 10919880/experiment_results.csv
experiment_results/experiment_results.csvtablet 10919903/experiment_results.csv
(1500, 7)

## Dataset Validation



# Analysis of Efficiency


22 Burger Participants vs 28 Swipe Participants


## Burger over all tids


Repeated Measures
KruskalResult(statistic=64.780058038415632, pvalue=2.8628983270922086e-13)
FriedmanchisquareResult(statistic=126.34181818181833, pvalue=2.3580931508512059e-26)


Normality: NormaltestResult(statistic=695.92062379202275, pvalue=7.6340785142658078e-152) True


Description:
count      550.000000
mean      4638.118182
std       2276.283269
min       2379.000000
25%       3429.750000
50%       4086.500000
75%       5083.500000
max      35643.000000
Name: time_ms, dtype: float64


## Swipe


### [Swipe tid 1]


Mean Distance= 2]


Description:
count      140.000000
mean      2770.214286
std       1949.562245
min       1453.000000
25%       1933.000000
50%       2410.500000
75%       3031.500000
max      21906.000000
Name: time_ms, dtype: float64


Normality: NormaltestResult(statistic=233.02889653769526, pvalue=2.5027533700333242e-51) True


H0: 2770.21[S] == 4638.12[B]
Ttest_indResult(statistic=-9.7677785244985476, pvalue=3.048661963250753e-19)
Reject? True


### [Swipe tid 2]


Mean Distance= 5]


Description:
count      140.000000
mean      4204.864286
std       2912.472445
min       2521.000000
25%       3322.250000
50%       3758.500000
75%       4416.250000
max      36116.000000
Name: time_ms, dtype: float64


Normality: NormaltestResult(statistic=273.97444652098108, pvalue=3.2151767059582613e-60) True


H0: 4204.86[S] == 4638.12[B]
Ttest_indResult(statistic=-1.6374276606675802, pvalue=0.10324597758459234)
Reject? False


### [Swipe tid 3]


Mean Distance= 8]


Description:
count      140.000000
mean      5175.678571
std       1434.320852
min       3146.000000
25%       4098.750000
50%       4834.000000
75%       5789.250000
max      11129.000000
Name: time_ms, dtype: float64


Normality: NormaltestResult(statistic=54.208885869234592, pvalue=1.6931288052248813e-12) True


H0: 5175.68[S] == 4638.12[B]
Ttest_indResult(statistic=3.4616051586436036, pvalue=0.00060564874812197894)
Reject? True


### [Swipe tid 4]


Mean Distance=11]


Description:
count      140.000000
mean      6123.014286
std       1877.882456
min       3622.000000
25%       5070.000000
50%       5691.500000
75%       6742.000000
max      20070.000000
Name: time_ms, dtype: float64


Normality: NormaltestResult(statistic=137.8311534028133, pvalue=1.17583212497471e-30) True


H0: 6123.01[S] == 4638.12[B]
Ttest_indResult(statistic=7.981729679231651, pvalue=5.0201723649504874e-14)
Reject? True


### [Swipe tid 5]


Mean Distance=14]


Description:
count      140.000000
mean      7252.650000
std       2392.089355
min       4282.000000
25%       5917.750000
50%       6747.500000
75%       7843.500000
max      24822.000000
Name: time_ms, dtype: float64


Normality: NormaltestResult(statistic=142.01649538662491, pvalue=1.4504736953102628e-31) True


H0: 7252.65[S] == 4638.12[B]
Ttest_indResult(statistic=11.658440737398982, pvalue=1.7212956322485464e-24)
Reject? True


# Effectiveness


Burger Description count      550
unique       2
top       True
freq       538
Name: success, dtype: object


Swipe Description count      700
unique       2
top       True
freq       654
Name: success, dtype: object


H0: 0.9343[S] == 0.9782[B]
Ttest_indResult(statistic=-3.8996269795774503, pvalue=0.00010184696908914221)
Reject? True

