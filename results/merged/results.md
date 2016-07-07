Analysis
========

Preprocessing
-------------

Namespace(demographics=None, distance=False, file=\[&lt;\_io.TextIOWrapper
name='experiment\_results.csv' mode='r' encoding='UTF-8'&gt;\],
final\_q=\[&lt;\_io.TextIOWrapper name='final\_questionnaire\_results.csv'
mode='r' encoding='UTF-8'&gt;\], task\_q=\[&lt;\_io.TextIOWrapper
name='task\_questionnaire\_results.csv' mode='r' encoding='UTF-8'&gt;\],
verbose=0)

-   experiment\_results.csv
-   task\_questionnaire\_results.csv
-   final\_questionnaire\_results.csv

N = 50\
Nswipe = 28\
Nburger = 22

Dropping Task ID 0 (Training)

Asserting Absolute Distance Values!

Dataset Validation:\
{'pid': True}

Adding success column based on\
`opt_interactions == interactions`\
in order to measure effectiveness.

Efficiency by Tasks
-------------------

### Descriptions \[time\_ms\]

#### Global Descriptions \[time\_ms\]

##### burger

count | 550.0 |\
mean | 4638.11818182 |\
std | 2276.28326918 |\
min | 2379.0 |\
25% | 3429.75 |\
50% | 4086.5 |\
75% | 5083.5 |\
max | 35643.0 |

shapiro\
(0.5968540906906128, 8.550004996808949e-34)

##### swipe

count | 700.0 |\
mean | 5105.28428571 |\
std | 2660.31481955 |\
min | 1453.0 |\
25% | 3496.25 |\
50% | 4796.0 |\
75% | 6205.0 |\
max | 36116.0 |

shapiro\
(0.7736766338348389, 5.710141920023298e-30)

#### Descriptions per tid \[time\_ms\]

##### ('burger', 1)

count | 110.0 |\
mean | 3882.02727273 |\
std | 1273.13599999 |\
min | 2379.0 |\
25% | 3038.0 |\
50% | 3454.5 |\
75% | 4136.5 |\
max | 9626.0 |

shapiro\
(0.8168985843658447, 2.2714176373117567e-10)

##### ('burger', 2)

count | 110.0 |\
mean | 4855.64545455 |\
std | 3550.99032468 |\
min | 2587.0 |\
25% | 3419.0 |\
50% | 4059.0 |\
75% | 5109.25 |\
max | 35643.0 |

shapiro\
(0.4090617895126343, 4.500466891123517e-19)

##### ('burger', 3)

count | 110.0 |\
mean | 4923.24545455 |\
std | 2443.8345722 |\
min | 2825.0 |\
25% | 3495.0 |\
50% | 4068.0 |\
75% | 5331.5 |\
max | 16458.0 |

shapiro\
(0.6884725093841553, 5.890605250758948e-14)

##### ('burger', 4)

count | 110.0 |\
mean | 4455.94545455 |\
std | 1740.15099965 |\
min | 2598.0 |\
25% | 3363.5 |\
50% | 3995.0 |\
75% | 4903.25 |\
max | 12386.0 |

shapiro\
(0.7651486396789551, 5.638249849643229e-12)

##### ('burger', 5)

count | 110.0 |\
mean | 5073.72727273 |\
std | 1391.01089839 |\
min | 3211.0 |\
25% | 4127.0 |\
50% | 4825.0 |\
75% | 5579.25 |\
max | 10924.0 |

shapiro\
(0.8667532205581665, 1.6438381322814166e-08)

##### ('swipe', 1)

count | 140.0 |\
mean | 2770.21428571 |\
std | 1949.56224485 |\
min | 1453.0 |\
25% | 1933.0 |\
50% | 2410.5 |\
75% | 3031.5 |\
max | 21906.0 |

shapiro\
(0.4316411018371582, 5.047697224178308e-21)

##### ('swipe', 2)

count | 140.0 |\
mean | 4204.86428571 |\
std | 2912.4724452 |\
min | 2521.0 |\
25% | 3322.25 |\
50% | 3758.5 |\
75% | 4416.25 |\
max | 36116.0 |

shapiro\
(0.28604620695114136, 3.420201117894323e-23)

##### ('swipe', 3)

count | 140.0 |\
mean | 5175.67857143 |\
std | 1434.32085184 |\
min | 3146.0 |\
25% | 4098.75 |\
50% | 4834.0 |\
75% | 5789.25 |\
max | 11129.0 |

shapiro\
(0.881258487701416, 3.353237021386235e-09)

##### ('swipe', 4)

count | 140.0 |\
mean | 6123.01428571 |\
std | 1877.88245579 |\
min | 3622.0 |\
25% | 5070.0 |\
50% | 5691.5 |\
75% | 6742.0 |\
max | 20070.0 |

shapiro\
(0.7405376434326172, 1.957654246771256e-14)

##### ('swipe', 5)

count | 140.0 |\
mean | 7252.65 |\
std | 2392.08935471 |\
min | 4282.0 |\
25% | 5917.75 |\
50% | 6747.5 |\
75% | 7843.5 |\
max | 24822.0 |

shapiro\
(0.713374674320221, 3.3856919106126353e-15)

### Cross-compare Tests per tid \[time\_ms\]

#### ('burger', 1) vs ('burger', 2)

MannwhitneyuResult(statistic=4084.0, pvalue=1.5658541604548195e-05)

#### ('burger', 1) vs ('burger', 3)

MannwhitneyuResult(statistic=3859.0, pvalue=1.7395206547774697e-06)

#### ('burger', 1) vs ('burger', 4)

MannwhitneyuResult(statistic=4510.0, pvalue=0.00055464375072409916)

#### ('burger', 1) vs ('burger', 5)

MannwhitneyuResult(statistic=2461.0, pvalue=1.4603875579048891e-14)

#### ('burger', 1) vs ('swipe', 1)

MannwhitneyuResult(statistic=2545.5, pvalue=5.3739527354119754e-20)

#### ('burger', 1) vs ('swipe', 2)

MannwhitneyuResult(statistic=6426.0, pvalue=0.012421146700796878)

#### ('burger', 1) vs ('swipe', 3)

MannwhitneyuResult(statistic=3044.5, pvalue=1.1832340237823803e-16)

#### ('burger', 1) vs ('swipe', 4)

MannwhitneyuResult(statistic=1688.0, pvalue=1.6234943894088597e-26)

#### ('burger', 1) vs ('swipe', 5)

MannwhitneyuResult(statistic=879.5, pvalue=1.4551418512540368e-33)

#### ('burger', 2) vs ('burger', 3)

MannwhitneyuResult(statistic=5763.5, pvalue=0.27230524102743087)

#### ('burger', 2) vs ('burger', 4)

MannwhitneyuResult(statistic=5675.5, pvalue=0.2141010726328908)

#### ('burger', 2) vs ('burger', 5)

MannwhitneyuResult(statistic=4089.5, pvalue=1.6477907306930181e-05)

#### ('burger', 2) vs ('swipe', 1)

MannwhitneyuResult(statistic=1517.0, pvalue=6.2046882486582092e-28)

#### ('burger', 2) vs ('swipe', 2)

MannwhitneyuResult(statistic=6141.5, pvalue=0.0030244034839489709)

#### ('burger', 2) vs ('swipe', 3)

MannwhitneyuResult(statistic=4963.5, pvalue=7.1526787854356572e-07)

#### ('burger', 2) vs ('swipe', 4)

MannwhitneyuResult(statistic=2883.5, pvalue=1.0733745632893838e-17)

#### ('burger', 2) vs ('swipe', 5)

MannwhitneyuResult(statistic=1655.5, pvalue=8.7897345573373952e-27)

#### ('burger', 3) vs ('burger', 4)

MannwhitneyuResult(statistic=5391.5, pvalue=0.081675269997733058)

#### ('burger', 3) vs ('burger', 5)

MannwhitneyuResult(statistic=4492.5, pvalue=0.00048634928385682863)

#### ('burger', 3) vs ('swipe', 1)

MannwhitneyuResult(statistic=1439.0, pvalue=1.3586702461712472e-28)

#### ('burger', 3) vs ('swipe', 2)

MannwhitneyuResult(statistic=5879.5, pvalue=0.00067121480094522003)

#### ('burger', 3) vs ('swipe', 3)

MannwhitneyuResult(statistic=5504.0, pvalue=5.4782820605463963e-05)

#### ('burger', 3) vs ('swipe', 4)

MannwhitneyuResult(statistic=3501.0, pvalue=6.9355700044163638e-14)

#### ('burger', 3) vs ('swipe', 5)

MannwhitneyuResult(statistic=2181.5, pvalue=1.209482241056887e-22)

#### ('burger', 4) vs ('burger', 5)

MannwhitneyuResult(statistic=3771.5, pvalue=6.9773905569607094e-07)

#### ('burger', 4) vs ('swipe', 1)

MannwhitneyuResult(statistic=1729.5, pvalue=3.5365303681484993e-26)

#### ('burger', 4) vs ('swipe', 2)

MannwhitneyuResult(statistic=6683.5, pvalue=0.036715528361448695)

#### ('burger', 4) vs ('swipe', 3)

MannwhitneyuResult(statistic=4638.0, pvalue=3.4412289343765112e-08)

#### ('burger', 4) vs ('swipe', 4)

MannwhitneyuResult(statistic=2628.5, pvalue=2.0386245118994627e-19)

#### ('burger', 4) vs ('swipe', 5)

MannwhitneyuResult(statistic=1526.0, pvalue=7.3859731612301278e-28)

#### ('burger', 5) vs ('swipe', 1)

MannwhitneyuResult(statistic=840.0, pvalue=6.2536829317850368e-34)

#### ('burger', 5) vs ('swipe', 2)

MannwhitneyuResult(statistic=3444.0, pvalue=3.2402389481877241e-14)

#### ('burger', 5) vs ('swipe', 3)

MannwhitneyuResult(statistic=7337.5, pvalue=0.26179339474167185)

#### ('burger', 5) vs ('swipe', 4)

MannwhitneyuResult(statistic=4246.0, pvalue=5.8282442410782173e-10)

#### ('burger', 5) vs ('swipe', 5)

MannwhitneyuResult(statistic=2222.5, pvalue=2.4529114846074024e-22)

#### ('swipe', 1) vs ('swipe', 2)

MannwhitneyuResult(statistic=2472.5, pvalue=1.4576933191791186e-27)

#### ('swipe', 1) vs ('swipe', 3)

MannwhitneyuResult(statistic=1021.0, pvalue=1.0616997031420499e-38)

#### ('swipe', 1) vs ('swipe', 4)

MannwhitneyuResult(statistic=570.0, pvalue=1.4519936452032371e-42)

#### ('swipe', 1) vs ('swipe', 5)

MannwhitneyuResult(statistic=418.0, pvalue=6.5546742737482944e-44)

#### ('swipe', 2) vs ('swipe', 3)

MannwhitneyuResult(statistic=4176.5, pvalue=5.2058578706528549e-17)

#### ('swipe', 2) vs ('swipe', 4)

MannwhitneyuResult(statistic=1732.5, pvalue=5.4063782042061323e-33)

#### ('swipe', 2) vs ('swipe', 5)

MannwhitneyuResult(statistic=832.0, pvalue=2.6916244230076441e-40)

#### ('swipe', 3) vs ('swipe', 4)

MannwhitneyuResult(statistic=6099.0, pvalue=2.3509168964023139e-08)

#### ('swipe', 3) vs ('swipe', 5)

MannwhitneyuResult(statistic=3160.5, pvalue=5.6464403753533496e-23)

#### ('swipe', 4) vs ('swipe', 5)

MannwhitneyuResult(statistic=5782.5, pvalue=1.5200785567733307e-09)

### Global Burger vs Swipe per tid Tests \[time\_ms\]

#### burger vs swipe 1

MannwhitneyuResult(statistic=8071.0, pvalue=1.2418694358581137e-47)

#### burger vs swipe 2

MannwhitneyuResult(statistic=31122.5, pvalue=0.00022970344985717234)

#### burger vs swipe 3

MannwhitneyuResult(statistic=25487.5, pvalue=3.2160499055159418e-10)

#### burger vs swipe 4

MannwhitneyuResult(statistic=14947.0, pvalue=2.4092928040063919e-29)

#### burger vs swipe 5

MannwhitneyuResult(statistic=8465.0, pvalue=1.846617100608964e-46)

### Global Burger vs Global Swipe Test \[time\_ms\]

#### burger vs swipe

MannwhitneyuResult(statistic=163706.0, pvalue=2.7478174405275066e-06)

Effectiveness by Tasks
----------------------

### Descriptions \[success\]

#### Global Descriptions \[success\]

##### burger

count | 550 |\
unique | 2 |\
top | True |\
freq | 538 |

shapiro\
(0.12739139795303345, 2.2420775429197073e-44)

##### swipe

count | 700 |\
unique | 2 |\
top | True |\
freq | 654 |

shapiro\
(0.26620155572891235, 0.0)

#### Descriptions per tid \[success\]

##### ('burger', 1)

count | 110 |\
unique | 2 |\
top | True |\
freq | 109 |

shapiro\
(0.06994897127151489, 3.1585817095650164e-23)

##### ('burger', 2)

count | 110 |\
unique | 2 |\
top | True |\
freq | 106 |

shapiro\
(0.18283003568649292, 5.362584042303219e-22)

##### ('burger', 3)

count | 110 |\
unique | 2 |\
top | True |\
freq | 106 |

shapiro\
(0.18283003568649292, 5.362584042303219e-22)

##### ('burger', 4)

count | 110 |\
unique | 2 |\
top | True |\
freq | 108 |

shapiro\
(0.11454051733016968, 9.348057262676717e-23)

##### ('burger', 5)

count | 110 |\
unique | 2 |\
top | True |\
freq | 109 |

shapiro\
(0.06994897127151489, 3.1585817095650164e-23)

##### ('swipe', 1)

count | 140 |\
unique | 2 |\
top | True |\
freq | 137 |

shapiro\
(0.1273578405380249, 3.3945333096716617e-25)

##### ('swipe', 2)

count | 140 |\
unique | 2 |\
top | True |\
freq | 131 |

shapiro\
(0.26299595832824707, 1.6702977931133302e-23)

##### ('swipe', 3)

count | 140 |\
unique | 2 |\
top | True |\
freq | 125 |

shapiro\
(0.3557870388031006, 3.3555234851260835e-22)

##### ('swipe', 4)

count | 140 |\
unique | 2 |\
top | True |\
freq | 132 |

shapiro\
(0.24434572458267212, 9.471951496601841e-24)

##### ('swipe', 5)

count | 140 |\
unique | 2 |\
top | True |\
freq | 129 |

shapiro\
(0.29717856645584106, 4.8660244383503074e-23)

### Cross-compare Tests per tid \[success\]

#### ('burger', 1) vs ('burger', 2)

MannwhitneyuResult(statistic=5885.0, pvalue=0.088514338258674385)

#### ('burger', 1) vs ('burger', 3)

MannwhitneyuResult(statistic=5885.0, pvalue=0.088514338258674385)

#### ('burger', 1) vs ('burger', 4)

MannwhitneyuResult(statistic=5995.0, pvalue=0.28273628216749636)

#### ('burger', 1) vs ('burger', 5)

MannwhitneyuResult(statistic=6050.0, pvalue=0.49742964452980454)

#### ('burger', 1) vs ('swipe', 1)

MannwhitneyuResult(statistic=7605.0, pvalue=0.22179890014407494)

#### ('burger', 1) vs ('swipe', 2)

MannwhitneyuResult(statistic=7275.0, pvalue=0.013774704590641996)

#### ('burger', 1) vs ('swipe', 3)

MannwhitneyuResult(statistic=6945.0, pvalue=0.0008566712200464943)

#### ('burger', 1) vs ('swipe', 4)

MannwhitneyuResult(statistic=7330.0, pvalue=0.021811891296381614)

#### ('burger', 1) vs ('swipe', 5)

MannwhitneyuResult(statistic=7165.0, pvalue=0.0054868348410904788)

#### ('burger', 2) vs ('burger', 3)

MannwhitneyuResult(statistic=6050.0, pvalue=0.49869675597742219)

#### ('burger', 2) vs ('burger', 4)

MannwhitneyuResult(statistic=5940.0, pvalue=0.20547426603584779)

#### ('burger', 2) vs ('burger', 5)

MannwhitneyuResult(statistic=5885.0, pvalue=0.088514338258674385)

#### ('burger', 2) vs ('swipe', 1)

MannwhitneyuResult(statistic=7585.0, pvalue=0.24008500168511188)

#### ('burger', 2) vs ('swipe', 2)

MannwhitneyuResult(statistic=7485.0, pvalue=0.162860956968579)

#### ('burger', 2) vs ('swipe', 3)

MannwhitneyuResult(statistic=7155.0, pvalue=0.018300662296952975)

#### ('burger', 2) vs ('swipe', 4)

MannwhitneyuResult(statistic=7540.0, pvalue=0.22392151178117164)

#### ('burger', 2) vs ('swipe', 5)

MannwhitneyuResult(statistic=7375.0, pvalue=0.082269468781977884)

#### ('burger', 3) vs ('burger', 4)

MannwhitneyuResult(statistic=5940.0, pvalue=0.20547426603584779)

#### ('burger', 3) vs ('burger', 5)

MannwhitneyuResult(statistic=5885.0, pvalue=0.088514338258674385)

#### ('burger', 3) vs ('swipe', 1)

MannwhitneyuResult(statistic=7585.0, pvalue=0.24008500168511188)

#### ('burger', 3) vs ('swipe', 2)

MannwhitneyuResult(statistic=7485.0, pvalue=0.162860956968579)

#### ('burger', 3) vs ('swipe', 3)

MannwhitneyuResult(statistic=7155.0, pvalue=0.018300662296952975)

#### ('burger', 3) vs ('swipe', 4)

MannwhitneyuResult(statistic=7540.0, pvalue=0.22392151178117164)

#### ('burger', 3) vs ('swipe', 5)

MannwhitneyuResult(statistic=7375.0, pvalue=0.082269468781977884)

#### ('burger', 4) vs ('burger', 5)

MannwhitneyuResult(statistic=5995.0, pvalue=0.28273628216749636)

#### ('burger', 4) vs ('swipe', 1)

MannwhitneyuResult(statistic=7675.0, pvalue=0.429353867493113)

#### ('burger', 4) vs ('swipe', 2)

MannwhitneyuResult(statistic=7345.0, pvalue=0.039349175524312156)

#### ('burger', 4) vs ('swipe', 3)

MannwhitneyuResult(statistic=7015.0, pvalue=0.0028380826908177329)

#### ('burger', 4) vs ('swipe', 4)

MannwhitneyuResult(statistic=7400.0, pvalue=0.060002832384090876)

#### ('burger', 4) vs ('swipe', 5)

MannwhitneyuResult(statistic=7235.0, pvalue=0.016660914589131787)

#### ('burger', 5) vs ('swipe', 1)

MannwhitneyuResult(statistic=7605.0, pvalue=0.22179890014407494)

#### ('burger', 5) vs ('swipe', 2)

MannwhitneyuResult(statistic=7275.0, pvalue=0.013774704590641996)

#### ('burger', 5) vs ('swipe', 3)

MannwhitneyuResult(statistic=6945.0, pvalue=0.0008566712200464943)

#### ('burger', 5) vs ('swipe', 4)

MannwhitneyuResult(statistic=7330.0, pvalue=0.021811891296381614)

#### ('burger', 5) vs ('swipe', 5)

MannwhitneyuResult(statistic=7165.0, pvalue=0.0054868348410904788)

#### ('swipe', 1) vs ('swipe', 2)

MannwhitneyuResult(statistic=9380.0, pvalue=0.038770512393067807)

#### ('swipe', 1) vs ('swipe', 3)

MannwhitneyuResult(statistic=8960.0, pvalue=0.0017670242686956415)

#### ('swipe', 1) vs ('swipe', 4)

MannwhitneyuResult(statistic=9450.0, pvalue=0.062622010514240933)

#### ('swipe', 1) vs ('swipe', 5)

MannwhitneyuResult(statistic=9240.0, pvalue=0.014343610809765796)

#### ('swipe', 2) vs ('swipe', 3)

MannwhitneyuResult(statistic=9380.0, pvalue=0.10079098881755333)

#### ('swipe', 2) vs ('swipe', 4)

MannwhitneyuResult(statistic=9730.0, pvalue=0.40205950418022463)

#### ('swipe', 2) vs ('swipe', 5)

MannwhitneyuResult(statistic=9660.0, pvalue=0.32217998161712597)

#### ('swipe', 3) vs ('swipe', 4)

MannwhitneyuResult(statistic=9310.0, pvalue=0.064351095787255674)

#### ('swipe', 3) vs ('swipe', 5)

MannwhitneyuResult(statistic=9520.0, pvalue=0.20590971152770549)

#### ('swipe', 4) vs ('swipe', 5)

MannwhitneyuResult(statistic=9590.0, pvalue=0.23888618804868444)

### Global Burger vs Swipe per tid Tests \[success\]

#### burger vs swipe 1

MannwhitneyuResult(statistic=38485.0, pvalue=0.48912520694291894)

#### burger vs swipe 2

MannwhitneyuResult(statistic=36865.0, pvalue=0.0045417664593209763)

#### burger vs swipe 3

MannwhitneyuResult(statistic=35215.0, pvalue=1.7057508017866935e-06)

#### burger vs swipe 4

MannwhitneyuResult(statistic=37140.0, pvalue=0.013145629148188419)

#### burger vs swipe 5

MannwhitneyuResult(statistic=36315.0, pvalue=0.00042387011906782973)

### Global Burger vs Global Swipe Test \[success\]

#### burger vs swipe

MannwhitneyuResult(statistic=184050.0, pvalue=0.00012578178491001905)

Task Questionnaires
-------------------

### Task Question 0

#### Descriptions \[result\]

##### Global Descriptions \[result\]

###### burger

count | 110.0 |\
mean | 6.90909090909 |\
std | 0.395976427467 |\
min | 4.0 |\
25% | 7.0 |\
50% | 7.0 |\
75% | 7.0 |\
max | 7.0 |

shapiro\
(0.24518823623657227, 2.9252628439826945e-21)

###### swipe

count | 140.0 |\
mean | 6.83571428571 |\
std | 0.458504203722 |\
min | 5.0 |\
25% | 7.0 |\
50% | 7.0 |\
75% | 7.0 |\
max | 7.0 |

shapiro\
(0.39919018745422363, 1.5329055243220379e-21)

##### Descriptions per tid \[result\]

###### ('burger', 1)

count | 22.0 |\
mean | 7.0 |\
std | 0.0 |\
min | 7.0 |\
25% | 7.0 |\
50% | 7.0 |\
75% | 7.0 |\
max | 7.0 |

shapiro\
(1.0, 1.0)

###### ('burger', 2)

count | 22.0 |\
mean | 6.90909090909 |\
std | 0.294244943168 |\
min | 6.0 |\
25% | 7.0 |\
50% | 7.0 |\
75% | 7.0 |\
max | 7.0 |

shapiro\
(0.3322211503982544, 4.875188253095075e-09)

###### ('burger', 3)

count | 22.0 |\
mean | 6.77272727273 |\
std | 0.751621623515 |\
min | 4.0 |\
25% | 7.0 |\
50% | 7.0 |\
75% | 7.0 |\
max | 7.0 |

shapiro\
(0.3419651389122009, 5.8100124711302215e-09)

###### ('burger', 4)

count | 22.0 |\
mean | 6.90909090909 |\
std | 0.294244943168 |\
min | 6.0 |\
25% | 7.0 |\
50% | 7.0 |\
75% | 7.0 |\
max | 7.0 |

shapiro\
(0.3322211503982544, 4.875188253095075e-09)

###### ('burger', 5)

count | 22.0 |\
mean | 6.95454545455 |\
std | 0.213200716356 |\
min | 6.0 |\
25% | 7.0 |\
50% | 7.0 |\
75% | 7.0 |\
max | 7.0 |

shapiro\
(0.22147256135940552, 7.41695094230721e-10)

###### ('swipe', 1)

count | 28.0 |\
mean | 6.85714285714 |\
std | 0.448395139423 |\
min | 5.0 |\
25% | 7.0 |\
50% | 7.0 |\
75% | 7.0 |\
max | 7.0 |

shapiro\
(0.365678608417511, 6.050620560138498e-10)

###### ('swipe', 2)

count | 28.0 |\
mean | 6.92857142857 |\
std | 0.262265264156 |\
min | 6.0 |\
25% | 7.0 |\
50% | 7.0 |\
75% | 7.0 |\
max | 7.0 |

shapiro\
(0.2873581051826477, 1.3197647141804936e-10)

###### ('swipe', 3)

count | 28.0 |\
mean | 6.82142857143 |\
std | 0.475594865606 |\
min | 5.0 |\
25% | 7.0 |\
50% | 7.0 |\
75% | 7.0 |\
max | 7.0 |

shapiro\
(0.43253177404403687, 2.463778070449507e-09)

###### ('swipe', 4)

count | 28.0 |\
mean | 6.82142857143 |\
std | 0.475594865606 |\
min | 5.0 |\
25% | 7.0 |\
50% | 7.0 |\
75% | 7.0 |\
max | 7.0 |

shapiro\
(0.43253177404403687, 2.463778070449507e-09)

###### ('swipe', 5)

count | 28.0 |\
mean | 6.75 |\
std | 0.585314097381 |\
min | 5.0 |\
25% | 7.0 |\
50% | 7.0 |\
75% | 7.0 |\
max | 7.0 |

shapiro\
(0.48425883054733276, 7.892020370547925e-09)

#### Cross-compare Tests per tid \[result\]

##### ('burger', 1) vs ('burger', 2)

MannwhitneyuResult(statistic=220.0, pvalue=0.080992169841587358)

##### ('burger', 1) vs ('burger', 3)

MannwhitneyuResult(statistic=220.0, pvalue=0.08104893779987532)

##### ('burger', 1) vs ('burger', 4)

MannwhitneyuResult(statistic=220.0, pvalue=0.080992169841587358)

##### ('burger', 1) vs ('burger', 5)

MannwhitneyuResult(statistic=231.0, pvalue=0.16990380614234185)

##### ('burger', 1) vs ('swipe', 1)

MannwhitneyuResult(statistic=275.0, pvalue=0.061389171314485569)

##### ('burger', 1) vs ('swipe', 2)

MannwhitneyuResult(statistic=286.0, pvalue=0.10790037602663682)

##### ('burger', 1) vs ('swipe', 3)

MannwhitneyuResult(statistic=264.0, pvalue=0.035323810007342034)

##### ('burger', 1) vs ('swipe', 4)

MannwhitneyuResult(statistic=264.0, pvalue=0.035323810007342034)

##### ('burger', 1) vs ('swipe', 5)

MannwhitneyuResult(statistic=253.0, pvalue=0.020341356769343476)

##### ('burger', 2) vs ('burger', 3)

MannwhitneyuResult(statistic=240.0, pvalue=0.47185717461959964)

##### ('burger', 2) vs ('burger', 4)

MannwhitneyuResult(statistic=242.0, pvalue=0.49060013900586225)

##### ('burger', 2) vs ('burger', 5)

MannwhitneyuResult(statistic=231.0, pvalue=0.28624482430604659)

##### ('burger', 2) vs ('swipe', 1)

MannwhitneyuResult(statistic=302.0, pvalue=0.41814383343092509)

##### ('burger', 2) vs ('swipe', 2)

MannwhitneyuResult(statistic=302.0, pvalue=0.40954587077471732)

##### ('burger', 2) vs ('swipe', 3)

MannwhitneyuResult(statistic=291.0, pvalue=0.28360268156813595)

##### ('burger', 2) vs ('swipe', 4)

MannwhitneyuResult(statistic=291.0, pvalue=0.28360268156813595)

##### ('burger', 2) vs ('swipe', 5)

MannwhitneyuResult(statistic=279.0, pvalue=0.1776214834950835)

##### ('burger', 3) vs ('burger', 4)

MannwhitneyuResult(statistic=240.0, pvalue=0.47185717461959964)

##### ('burger', 3) vs ('burger', 5)

MannwhitneyuResult(statistic=230.0, pvalue=0.26839195888913986)

##### ('burger', 3) vs ('swipe', 1)

MannwhitneyuResult(statistic=305.5, pvalue=0.47007151426311133)

##### ('burger', 3) vs ('swipe', 2)

MannwhitneyuResult(statistic=300.0, pvalue=0.37768095297605236)

##### ('burger', 3) vs ('swipe', 3)

MannwhitneyuResult(statistic=295.5, pvalue=0.3388315325050939)

##### ('burger', 3) vs ('swipe', 4)

MannwhitneyuResult(statistic=295.5, pvalue=0.3388315325050939)

##### ('burger', 3) vs ('swipe', 5)

MannwhitneyuResult(statistic=285.0, pvalue=0.23293475501797717)

##### ('burger', 4) vs ('burger', 5)

MannwhitneyuResult(statistic=231.0, pvalue=0.28624482430604659)

##### ('burger', 4) vs ('swipe', 1)

MannwhitneyuResult(statistic=302.0, pvalue=0.41814383343092509)

##### ('burger', 4) vs ('swipe', 2)

MannwhitneyuResult(statistic=302.0, pvalue=0.40954587077471732)

##### ('burger', 4) vs ('swipe', 3)

MannwhitneyuResult(statistic=291.0, pvalue=0.28360268156813595)

##### ('burger', 4) vs ('swipe', 4)

MannwhitneyuResult(statistic=291.0, pvalue=0.28360268156813595)

##### ('burger', 4) vs ('swipe', 5)

MannwhitneyuResult(statistic=279.0, pvalue=0.1776214834950835)

##### ('burger', 5) vs ('swipe', 1)

MannwhitneyuResult(statistic=288.5, pvalue=0.21488485789583234)

##### ('burger', 5) vs ('swipe', 2)

MannwhitneyuResult(statistic=300.0, pvalue=0.36081607462259746)

##### ('burger', 5) vs ('swipe', 3)

MannwhitneyuResult(statistic=277.5, pvalue=0.12983938884427548)

##### ('burger', 5) vs ('swipe', 4)

MannwhitneyuResult(statistic=277.5, pvalue=0.12983938884427548)

##### ('burger', 5) vs ('swipe', 5)

MannwhitneyuResult(statistic=266.0, pvalue=0.07519977300947886)

##### ('swipe', 1) vs ('swipe', 2)

MannwhitneyuResult(statistic=377.0, pvalue=0.31537541448498552)

##### ('swipe', 1) vs ('swipe', 3)

MannwhitneyuResult(statistic=378.5, pvalue=0.35525965271351878)

##### ('swipe', 1) vs ('swipe', 4)

MannwhitneyuResult(statistic=378.5, pvalue=0.35525965271351878)

##### ('swipe', 1) vs ('swipe', 5)

MannwhitneyuResult(statistic=363.5, pvalue=0.22518165687821007)

##### ('swipe', 2) vs ('swipe', 3)

MannwhitneyuResult(statistic=363.0, pvalue=0.19191432446450229)

##### ('swipe', 2) vs ('swipe', 4)

MannwhitneyuResult(statistic=363.0, pvalue=0.19191432446450229)

##### ('swipe', 2) vs ('swipe', 5)

MannwhitneyuResult(statistic=348.0, pvalue=0.10712672456029038)

##### ('swipe', 3) vs ('swipe', 4)

MannwhitneyuResult(statistic=392.0, pvalue=0.49461993710800994)

##### ('swipe', 3) vs ('swipe', 5)

MannwhitneyuResult(statistic=376.5, pvalue=0.3501076533991746)

##### ('swipe', 4) vs ('swipe', 5)

MannwhitneyuResult(statistic=376.5, pvalue=0.3501076533991746)

#### Global Burger vs Swipe per tid Tests \[result\]

##### burger vs swipe 1

MannwhitneyuResult(statistic=1473.0, pvalue=0.21665236926243431)

##### burger vs swipe 2

MannwhitneyuResult(statistic=1530.0, pvalue=0.45320928415997419)

##### burger vs swipe 3

MannwhitneyuResult(statistic=1419.0, pvalue=0.087083010808927386)

##### burger vs swipe 4

MannwhitneyuResult(statistic=1419.0, pvalue=0.087083010808927386)

##### burger vs swipe 5

MannwhitneyuResult(statistic=1362.0, pvalue=0.027199345369874211)

#### Global Burger vs Global Swipe Test \[result\]

##### burger vs swipe

MannwhitneyuResult(statistic=7203.0, pvalue=0.046318608676750285)

### Task Question 1

#### Descriptions \[result\]

##### Global Descriptions \[result\]

###### burger

count | 110.0 |\
mean | 1.89090909091 |\
std | 1.80897585981 |\
min | 1.0 |\
25% | 1.0 |\
50% | 1.0 |\
75% | 1.0 |\
max | 7.0 |

shapiro\
(0.5440710783004761, 6.783648646543276e-17)

###### swipe

count | 140.0 |\
mean | 2.86428571429 |\
std | 2.12964925773 |\
min | 1.0 |\
25% | 1.0 |\
50% | 2.0 |\
75% | 4.0 |\
max | 7.0 |

shapiro\
(0.799676775932312, 1.4816165872302833e-12)

##### Descriptions per tid \[result\]

###### ('burger', 1)

count | 22.0 |\
mean | 1.95454545455 |\
std | 2.01133153544 |\
min | 1.0 |\
25% | 1.0 |\
50% | 1.0 |\
75% | 1.0 |\
max | 7.0 |

shapiro\
(0.5299234390258789, 2.541320327509311e-07)

###### ('burger', 2)

count | 22.0 |\
mean | 1.77272727273 |\
std | 1.87545088374 |\
min | 1.0 |\
25% | 1.0 |\
50% | 1.0 |\
75% | 1.0 |\
max | 7.0 |

shapiro\
(0.4611632227897644, 5.790687396256544e-08)

###### ('burger', 3)

count | 22.0 |\
mean | 2.0 |\
std | 1.74574312189 |\
min | 1.0 |\
25% | 1.0 |\
50% | 1.0 |\
75% | 2.0 |\
max | 6.0 |

shapiro\
(0.6260440349578857, 2.5660463052190607e-06)

###### ('burger', 4)

count | 22.0 |\
mean | 1.77272727273 |\
std | 1.54092792643 |\
min | 1.0 |\
25% | 1.0 |\
50% | 1.0 |\
75% | 1.0 |\
max | 6.0 |

shapiro\
(0.5682213306427002, 6.146745477053628e-07)

###### ('burger', 5)

count | 22.0 |\
mean | 1.95454545455 |\
std | 1.98751514465 |\
min | 1.0 |\
25% | 1.0 |\
50% | 1.0 |\
75% | 1.0 |\
max | 7.0 |

shapiro\
(0.5327657461166382, 2.7092326604361006e-07)

###### ('swipe', 1)

count | 28.0 |\
mean | 2.75 |\
std | 2.36682315602 |\
min | 1.0 |\
25% | 1.0 |\
50% | 1.0 |\
75% | 4.25 |\
max | 7.0 |

shapiro\
(0.7217938303947449, 5.8795612858375534e-06)

###### ('swipe', 2)

count | 28.0 |\
mean | 2.67857142857 |\
std | 2.21198036674 |\
min | 1.0 |\
25% | 1.0 |\
50% | 1.0 |\
75% | 4.0 |\
max | 7.0 |

shapiro\
(0.7506808042526245, 1.617231646378059e-05)

###### ('swipe', 3)

count | 28.0 |\
mean | 2.82142857143 |\
std | 2.16116517662 |\
min | 1.0 |\
25% | 1.0 |\
50% | 2.0 |\
75% | 4.0 |\
max | 7.0 |

shapiro\
(0.7865198850631714, 6.232791929505765e-05)

###### ('swipe', 4)

count | 28.0 |\
mean | 2.85714285714 |\
std | 1.87999774851 |\
min | 1.0 |\
25% | 1.0 |\
50% | 3.0 |\
75% | 4.0 |\
max | 7.0 |

shapiro\
(0.8642818927764893, 0.0018409639596939087)

###### ('swipe', 5)

count | 28.0 |\
mean | 3.21428571429 |\
std | 2.11445015806 |\
min | 1.0 |\
25% | 1.0 |\
50% | 3.0 |\
75% | 4.0 |\
max | 7.0 |

shapiro\
(0.8491970896720886, 0.0009006079635582864)

#### Cross-compare Tests per tid \[result\]

##### ('burger', 1) vs ('burger', 2)

MannwhitneyuResult(statistic=231.5, pvalue=0.36950062145736295)

##### ('burger', 1) vs ('burger', 3)

MannwhitneyuResult(statistic=226.5, pvalue=0.32669163862815576)

##### ('burger', 1) vs ('burger', 4)

MannwhitneyuResult(statistic=237.5, pvalue=0.44908793706778233)

##### ('burger', 1) vs ('burger', 5)

MannwhitneyuResult(statistic=242.0, pvalue=0.4936172195955259)

##### ('burger', 1) vs ('swipe', 1)

MannwhitneyuResult(statistic=247.5, pvalue=0.082098002975044604)

##### ('burger', 1) vs ('swipe', 2)

MannwhitneyuResult(statistic=241.5, pvalue=0.066396878662638464)

##### ('burger', 1) vs ('swipe', 3)

MannwhitneyuResult(statistic=213.5, pvalue=0.020092875062028004)

##### ('burger', 1) vs ('swipe', 4)

MannwhitneyuResult(statistic=198.5, pvalue=0.010019521264436585)

##### ('burger', 1) vs ('swipe', 5)

MannwhitneyuResult(statistic=192.0, pvalue=0.0068101408106697112)

##### ('burger', 2) vs ('burger', 3)

MannwhitneyuResult(statistic=215.0, pvalue=0.20647583790178142)

##### ('burger', 2) vs ('burger', 4)

MannwhitneyuResult(statistic=235.0, pvalue=0.41428583227671284)

##### ('burger', 2) vs ('burger', 5)

MannwhitneyuResult(statistic=232.0, pvalue=0.37576224110670875)

##### ('burger', 2) vs ('swipe', 1)

MannwhitneyuResult(statistic=232.5, pvalue=0.038182542965196922)

##### ('burger', 2) vs ('swipe', 2)

MannwhitneyuResult(statistic=225.5, pvalue=0.028699028147674787)

##### ('burger', 2) vs ('swipe', 3)

MannwhitneyuResult(statistic=194.5, pvalue=0.0062373933525989578)

##### ('burger', 2) vs ('swipe', 4)

MannwhitneyuResult(statistic=179.5, pvalue=0.0028888514521789059)

##### ('burger', 2) vs ('swipe', 5)

MannwhitneyuResult(statistic=173.0, pvalue=0.001845925801493757)

##### ('burger', 3) vs ('burger', 4)

MannwhitneyuResult(statistic=221.0, pvalue=0.26964038824961989)

##### ('burger', 3) vs ('burger', 5)

MannwhitneyuResult(statistic=227.0, pvalue=0.33206339086194925)

##### ('burger', 3) vs ('swipe', 1)

MannwhitneyuResult(statistic=260.5, pvalue=0.14603135541294709)

##### ('burger', 3) vs ('swipe', 2)

MannwhitneyuResult(statistic=256.0, pvalue=0.12750985422970523)

##### ('burger', 3) vs ('swipe', 3)

MannwhitneyuResult(statistic=230.0, pvalue=0.049115891184390158)

##### ('burger', 3) vs ('swipe', 4)

MannwhitneyuResult(statistic=215.0, pvalue=0.026326679220802538)

##### ('burger', 3) vs ('swipe', 5)

MannwhitneyuResult(statistic=203.5, pvalue=0.014613622667340618)

##### ('burger', 4) vs ('burger', 5)

MannwhitneyuResult(statistic=237.0, pvalue=0.44276533380129457)

##### ('burger', 4) vs ('swipe', 1)

MannwhitneyuResult(statistic=238.5, pvalue=0.054909704407618581)

##### ('burger', 4) vs ('swipe', 2)

MannwhitneyuResult(statistic=233.0, pvalue=0.044870412680933683)

##### ('burger', 4) vs ('swipe', 3)

MannwhitneyuResult(statistic=209.0, pvalue=0.015775210433546256)

##### ('burger', 4) vs ('swipe', 4)

MannwhitneyuResult(statistic=192.5, pvalue=0.0070352388832014452)

##### ('burger', 4) vs ('swipe', 5)

MannwhitneyuResult(statistic=183.5, pvalue=0.0040067153811422793)

##### ('burger', 5) vs ('swipe', 1)

MannwhitneyuResult(statistic=246.0, pvalue=0.077014874525015403)

##### ('burger', 5) vs ('swipe', 2)

MannwhitneyuResult(statistic=240.5, pvalue=0.063535812872022673)

##### ('burger', 5) vs ('swipe', 3)

MannwhitneyuResult(statistic=211.5, pvalue=0.01809715117525822)

##### ('burger', 5) vs ('swipe', 4)

MannwhitneyuResult(statistic=198.5, pvalue=0.010033737896491264)

##### ('burger', 5) vs ('swipe', 5)

MannwhitneyuResult(statistic=190.5, pvalue=0.0062419441538161761)

##### ('swipe', 1) vs ('swipe', 2)

MannwhitneyuResult(statistic=389.5, pvalue=0.48562593257900771)

##### ('swipe', 1) vs ('swipe', 3)

MannwhitneyuResult(statistic=361.5, pvalue=0.29899029746393557)

##### ('swipe', 1) vs ('swipe', 4)

MannwhitneyuResult(statistic=348.5, pvalue=0.22808362379240826)

##### ('swipe', 1) vs ('swipe', 5)

MannwhitneyuResult(statistic=329.5, pvalue=0.14088538659882688)

##### ('swipe', 2) vs ('swipe', 3)

MannwhitneyuResult(statistic=364.5, pvalue=0.31879870403142863)

##### ('swipe', 2) vs ('swipe', 4)

MannwhitneyuResult(statistic=349.0, pvalue=0.23202420226563208)

##### ('swipe', 2) vs ('swipe', 5)

MannwhitneyuResult(statistic=328.0, pvalue=0.13662614652941502)

##### ('swipe', 3) vs ('swipe', 4)

MannwhitneyuResult(statistic=371.0, pvalue=0.36362070040972327)

##### ('swipe', 3) vs ('swipe', 5)

MannwhitneyuResult(statistic=343.5, pvalue=0.20657252218094635)

##### ('swipe', 4) vs ('swipe', 5)

MannwhitneyuResult(statistic=359.5, pvalue=0.29395572379615725)

#### Global Burger vs Swipe per tid Tests \[result\]

##### burger vs swipe 1

MannwhitneyuResult(statistic=1225.0, pvalue=0.017143625211004959)

##### burger vs swipe 2

MannwhitneyuResult(statistic=1196.5, pvalue=0.011075983661422355)

##### burger vs swipe 3

MannwhitneyuResult(statistic=1058.5, pvalue=0.00087828638876744818)

##### burger vs swipe 4

MannwhitneyuResult(statistic=984.0, pvalue=0.00018652482417813029)

##### burger vs swipe 5

MannwhitneyuResult(statistic=942.5, pvalue=6.5526352124271008e-05)

#### Global Burger vs Global Swipe Test \[result\]

##### burger vs swipe

MannwhitneyuResult(statistic=5406.5, pvalue=2.9062055593999374e-06)

Final Questionnaires
--------------------

### Final Question 0

#### Descriptions \[result\]

##### Global Descriptions \[result\]

###### burger

count | 22.0 |\
mean | 1.5 |\
std | 1.05785047102 |\
min | 1.0 |\
25% | 1.0 |\
50% | 1.0 |\
75% | 1.75 |\
max | 5.0 |

shapiro\
(0.5448707342147827, 3.567666624348931e-07)

###### swipe

count | 28.0 |\
mean | 1.53571428571 |\
std | 1.29048204766 |\
min | 1.0 |\
25% | 1.0 |\
50% | 1.0 |\
75% | 1.25 |\
max | 7.0 |

shapiro\
(0.4864434003829956, 8.3034956688266e-09)

#### Global Burger vs Global Swipe Test \[result\]

##### burger vs swipe

MannwhitneyuResult(statistic=302.5, pvalue=0.44941800310214225)

### Final Question 1

#### Descriptions \[result\]

##### Global Descriptions \[result\]

###### burger

count | 22.0 |\
mean | 2.22727272727 |\
std | 1.79766563398 |\
min | 1.0 |\
25% | 1.0 |\
50% | 1.0 |\
75% | 3.5 |\
max | 6.0 |

shapiro\
(0.6886584758758545, 1.4087103409110568e-05)

###### swipe

count | 28.0 |\
mean | 1.67857142857 |\
std | 1.18801332542 |\
min | 1.0 |\
25% | 1.0 |\
50% | 1.0 |\
75% | 2.0 |\
max | 6.0 |

shapiro\
(0.6186860203742981, 2.4386196173509234e-07)

#### Global Burger vs Global Swipe Test \[result\]

##### burger vs swipe

MannwhitneyuResult(statistic=281.0, pvalue=0.27788843237866634)

### Final Question 2

#### Descriptions \[result\]

##### Global Descriptions \[result\]

###### burger

count | 22.0 |\
mean | 1.22727272727 |\
std | 0.428932027229 |\
min | 1.0 |\
25% | 1.0 |\
50% | 1.0 |\
75% | 1.0 |\
max | 2.0 |

shapiro\
(0.5222699642181396, 2.1416671813767607e-07)

###### swipe

count | 28.0 |\
mean | 1.75 |\
std | 1.37773297418 |\
min | 1.0 |\
25% | 1.0 |\
50% | 1.0 |\
75% | 2.0 |\
max | 7.0 |

shapiro\
(0.6172786951065063, 2.343947329563889e-07)

#### Global Burger vs Global Swipe Test \[result\]

##### burger vs swipe

MannwhitneyuResult(statistic=255.5, pvalue=0.10358134878107761)

### Final Question 3

#### Descriptions \[result\]

##### Global Descriptions \[result\]

###### burger

count | 22.0 |\
mean | 5.13636363636 |\
std | 1.67034226733 |\
min | 2.0 |\
25% | 3.25 |\
50% | 5.5 |\
75% | 6.75 |\
max | 7.0 |

shapiro\
(0.8708899021148682, 0.008132589980959892)

###### swipe

count | 28.0 |\
mean | 4.5 |\
std | 1.45296631451 |\
min | 1.0 |\
25% | 4.0 |\
50% | 4.0 |\
75% | 5.25 |\
max | 7.0 |

shapiro\
(0.9325721859931946, 0.07159832864999771)

#### Global Burger vs Global Swipe Test \[result\]

##### burger vs swipe

MannwhitneyuResult(statistic=238.5, pvalue=0.084899251911718931)
