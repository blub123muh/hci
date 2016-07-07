Analysis
========

Preprocessing
-------------

Namespace(demographics=\[&lt;\_io.TextIOWrapper
name='demographic\_data\_fixed.csv' mode='r' encoding='UTF-8'&gt;\],
distance=False, file=\[&lt;\_io.TextIOWrapper name='experiment\_results.csv'
mode='r' encoding='UTF-8'&gt;\], final\_q=\[&lt;\_io.TextIOWrapper
name='final\_questionnaire\_results.csv' mode='r' encoding='UTF-8'&gt;\],
norm\_test='None', task\_q=\[&lt;\_io.TextIOWrapper
name='task\_questionnaire\_results.csv' mode='r' encoding='UTF-8'&gt;\])

-   experiment\_results.csv
-   task\_questionnaire\_results.csv
-   final\_questionnaire\_results.csv
-   demographic\_data\_fixed.csv

Dropping Task ID 0 (Training)

Asserting Absolute Distance Values!

Dataset Validation:\
{'pid': True}

Adding success column based on\
`opt_interactions == interactions`\
in order to measure effectiveness.

No normality test, *Forcing t-test*!

Demographics
------------

### age

count | 50.0 |\
mean | 24.1 |\
std | 2.90144228737 |\
min | 20.0 |\
25% | 22.0 |\
50% | 24.0 |\
75% | 25.0 |\
max | 35.0 |

### sex

('f', 29)\
('m', 21)

### job

('Agrarwissenschaften', 5)\
('Agribusiness', 1)\
('Betriebswirtschaftslehre', 1)\
('Biochemie', 1)\
('Biologie', 1)\
('Ernährungs- und Verbraucherökonomie', 2)\
('Finanzmathematik', 2)\
('Informatik / Nachhilfelehrer', 1)\
('Mathemathik / Chemie', 1)\
('Mathemathik / Deutsch / Psychologie', 1)\
('Mathemathik / Geologie', 1)\
('Mathemathik / Geschichte', 1)\
('Mathemathik / Philosophie', 1)\
('Mathemathik / Physik', 1)\
('Mathemathik / Sport', 1)\
('Mathematik', 4)\
('Mathematik / Informatik', 1)\
('Mathematik / Spanisch', 1)\
('Medizin', 1)\
('Musikwissenschaft / Philosophie', 1)\
('Physik', 1)\
('Politikwissenschaft / Ur- und Frühgeschichte', 1)\
('Psychologie', 4)\
('Rechtswissenschaften', 1)\
('Soziologie / Pädagogik', 1)\
('Volkswirtschaftslehre', 3)\
('Wirtschaftsinformatik', 6)\
('Wirtschaftsingenieur', 2)\
('Wirtschaftswissenschaften Profil: Handelslehrer', 1)

### smartphone

('None', 1)\
('android', 37)\
('nodroid', 12)

### comments

('Ich zweifle die Aussagekraft der Studie an, da die Navigation nur aus
„Wischen nach links“ und „Wischen nach rechts“ besteht.', 1)\
('Menü-Steuerung: nur 5/7 Steine da: Menü zum Ausklappen. besser: dauerhaft
ausgeklappt - &gt;1 Klick statt 2', 1)\
('Samsung', 1)\
('man könnte die Bedienung noch vereinfachen, indem man durch wischen von Tür
zu Tür kann', 1)\
('schön kurz :)', 1)

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

##### swipe

count | 700.0 |\
mean | 5105.28428571 |\
std | 2660.31481955 |\
min | 1453.0 |\
25% | 3496.25 |\
50% | 4796.0 |\
75% | 6205.0 |\
max | 36116.0 |

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

##### ('burger', 2)

count | 110.0 |\
mean | 4855.64545455 |\
std | 3550.99032468 |\
min | 2587.0 |\
25% | 3419.0 |\
50% | 4059.0 |\
75% | 5109.25 |\
max | 35643.0 |

##### ('burger', 3)

count | 110.0 |\
mean | 4923.24545455 |\
std | 2443.8345722 |\
min | 2825.0 |\
25% | 3495.0 |\
50% | 4068.0 |\
75% | 5331.5 |\
max | 16458.0 |

##### ('burger', 4)

count | 110.0 |\
mean | 4455.94545455 |\
std | 1740.15099965 |\
min | 2598.0 |\
25% | 3363.5 |\
50% | 3995.0 |\
75% | 4903.25 |\
max | 12386.0 |

##### ('burger', 5)

count | 110.0 |\
mean | 5073.72727273 |\
std | 1391.01089839 |\
min | 3211.0 |\
25% | 4127.0 |\
50% | 4825.0 |\
75% | 5579.25 |\
max | 10924.0 |

##### ('swipe', 1)

count | 140.0 |\
mean | 2770.21428571 |\
std | 1949.56224485 |\
min | 1453.0 |\
25% | 1933.0 |\
50% | 2410.5 |\
75% | 3031.5 |\
max | 21906.0 |

##### ('swipe', 2)

count | 140.0 |\
mean | 4204.86428571 |\
std | 2912.4724452 |\
min | 2521.0 |\
25% | 3322.25 |\
50% | 3758.5 |\
75% | 4416.25 |\
max | 36116.0 |

##### ('swipe', 3)

count | 140.0 |\
mean | 5175.67857143 |\
std | 1434.32085184 |\
min | 3146.0 |\
25% | 4098.75 |\
50% | 4834.0 |\
75% | 5789.25 |\
max | 11129.0 |

##### ('swipe', 4)

count | 140.0 |\
mean | 6123.01428571 |\
std | 1877.88245579 |\
min | 3622.0 |\
25% | 5070.0 |\
50% | 5691.5 |\
75% | 6742.0 |\
max | 20070.0 |

##### ('swipe', 5)

count | 140.0 |\
mean | 7252.65 |\
std | 2392.08935471 |\
min | 4282.0 |\
25% | 5917.75 |\
50% | 6747.5 |\
75% | 7843.5 |\
max | 24822.0 |

### Cross-compare Tests per tid \[time\_ms\]

#### ('burger', 1) vs ('burger', 2)

Ttest\_indResult(statistic=-2.7069257840177166, pvalue=0.0076584106293651174)

#### ('burger', 1) vs ('burger', 3)

Ttest\_indResult(statistic=-3.9630138423637753, pvalue=0.00011019834573310358)

#### ('burger', 1) vs ('burger', 4)

Ttest\_indResult(statistic=-2.7916856663246765, pvalue=0.0057525652209190247)

#### ('burger', 1) vs ('burger', 5)

Ttest\_indResult(statistic=-6.6281974576990477, pvalue=2.6654505205089786e-10)

#### ('burger', 1) vs ('swipe', 1)

Ttest\_indResult(statistic=5.4326153841753113, pvalue=1.3586526333931942e-07)

#### ('burger', 1) vs ('swipe', 2)

Ttest\_indResult(statistic=-1.1762922471638779, pvalue=0.24087795976855594)

#### ('burger', 1) vs ('swipe', 3)

Ttest\_indResult(statistic=-7.5408734262828094, pvalue=9.1456060724920978e-13)

#### ('burger', 1) vs ('swipe', 4)

Ttest\_indResult(statistic=-11.215580212273252, pvalue=8.4091646308958142e-24)

#### ('burger', 1) vs ('swipe', 5)

Ttest\_indResult(statistic=-14.29368458997773, pvalue=3.0267427720130829e-33)

#### ('burger', 2) vs ('burger', 3)

Ttest\_indResult(statistic=-0.16447445278862544, pvalue=0.86952948719325696)

#### ('burger', 2) vs ('burger', 4)

Ttest\_indResult(statistic=1.0600946394028834, pvalue=0.29071432820462006)

#### ('burger', 2) vs ('burger', 5)

Ttest\_indResult(statistic=-0.59974584216808413, pvalue=0.54963357840520244)

#### ('burger', 2) vs ('swipe', 1)

Ttest\_indResult(statistic=5.538439361373503, pvalue=1.2306063779073432e-07)

#### ('burger', 2) vs ('swipe', 2)

Ttest\_indResult(statistic=1.5546815529967002, pvalue=0.12153553523730215)

#### ('burger', 2) vs ('swipe', 3)

Ttest\_indResult(statistic=-0.88991887096624867, pvalue=0.37506981652796878)

#### ('burger', 2) vs ('swipe', 4)

Ttest\_indResult(statistic=-3.3893532956398862, pvalue=0.00088695190095300206)

#### ('burger', 2) vs ('swipe', 5)

Ttest\_indResult(statistic=-6.0785193664476225, pvalue=6.928771693524431e-09)

#### ('burger', 3) vs ('burger', 4)

Ttest\_indResult(statistic=1.633653476860327, pvalue=0.10392934344192963)

#### ('burger', 3) vs ('burger', 5)

Ttest\_indResult(statistic=-0.56126498193436625, pvalue=0.57534354989927383)

#### ('burger', 3) vs ('swipe', 1)

Ttest\_indResult(statistic=7.5444054072566527, pvalue=1.4527959234468714e-12)

#### ('burger', 3) vs ('swipe', 2)

Ttest\_indResult(statistic=2.1194676350640345, pvalue=0.035049242537354371)

#### ('burger', 3) vs ('swipe', 3)

Ttest\_indResult(statistic=-0.96107503820804641, pvalue=0.33790867474880881)

#### ('burger', 3) vs ('swipe', 4)

Ttest\_indResult(statistic=-4.2556029720583979, pvalue=3.2035131582151195e-05)

#### ('burger', 3) vs ('swipe', 5)

Ttest\_indResult(statistic=-7.550993296996201, pvalue=9.8652818305802416e-13)

#### ('burger', 4) vs ('burger', 5)

Ttest\_indResult(statistic=-2.908423978077963, pvalue=0.0040271469815081331)

#### ('burger', 4) vs ('swipe', 1)

Ttest\_indResult(statistic=7.209186111149064, pvalue=7.0263378717603719e-12)

#### ('burger', 4) vs ('swipe', 2)

Ttest\_indResult(statistic=0.84582913729034226, pvalue=0.3985168455092658)

#### ('burger', 4) vs ('swipe', 3)

Ttest\_indResult(statistic=-3.5026414730410522, pvalue=0.00056297399386590681)

#### ('burger', 4) vs ('swipe', 4)

Ttest\_indResult(statistic=-7.2606750152898689, pvalue=5.2712588147746732e-12)

#### ('burger', 4) vs ('swipe', 5)

Ttest\_indResult(statistic=-10.693428350595326, pvalue=3.5536454454504528e-22)

#### ('burger', 5) vs ('swipe', 1)

Ttest\_indResult(statistic=10.890538484235995, pvalue=8.5016546211500906e-23)

#### ('burger', 5) vs ('swipe', 2)

Ttest\_indResult(statistic=3.1074578497467975, pvalue=0.0021494163532751534)

#### ('burger', 5) vs ('swipe', 3)

Ttest\_indResult(statistic=-0.56740454887630598, pvalue=0.57097571413562109)

#### ('burger', 5) vs ('swipe', 4)

Ttest\_indResult(statistic=-5.0731662549008609, pvalue=7.6882650857723662e-07)

#### ('burger', 5) vs ('swipe', 5)

Ttest\_indResult(statistic=-9.0116498280847814, pvalue=8.0218560476693546e-17)

#### ('swipe', 1) vs ('swipe', 2)

Ttest\_indResult(statistic=-4.8434258013998477, pvalue=2.274961213270276e-06)

#### ('swipe', 1) vs ('swipe', 3)

Ttest\_indResult(statistic=-11.759414000225329, pvalue=8.3981981627819097e-26)

#### ('swipe', 1) vs ('swipe', 4)

Ttest\_indResult(statistic=-14.655532120635145, pvalue=2.0532387279374739e-36)

#### ('swipe', 1) vs ('swipe', 5)

Ttest\_indResult(statistic=-17.186752811829475, pvalue=4.2694464640700814e-45)

#### ('swipe', 2) vs ('swipe', 3)

Ttest\_indResult(statistic=-3.5382178337888495, pvalue=0.00049943120019875324)

#### ('swipe', 2) vs ('swipe', 4)

Ttest\_indResult(statistic=-6.5492908547573476, pvalue=3.5428937762053603e-10)

#### ('swipe', 2) vs ('swipe', 5)

Ttest\_indResult(statistic=-9.5682857766159515, pvalue=7.5669739907302645e-19)

#### ('swipe', 3) vs ('swipe', 4)

Ttest\_indResult(statistic=-4.7435792201219673, pvalue=3.4662492531819365e-06)

#### ('swipe', 3) vs ('swipe', 5)

Ttest\_indResult(statistic=-8.8109429254330092, pvalue=3.2416911874714276e-16)

#### ('swipe', 4) vs ('swipe', 5)

Ttest\_indResult(statistic=-4.3950718940401625, pvalue=1.6076088389444222e-05)

### Global Burger vs Swipe per tid Tests \[time\_ms\]

#### burger vs swipe 1

Ttest\_indResult(statistic=9.7677785244985476, pvalue=3.048661963250753e-19)

#### burger vs swipe 2

Ttest\_indResult(statistic=1.6374276606675802, pvalue=0.10324597758459234)

#### burger vs swipe 3

Ttest\_indResult(statistic=-3.4616051586436036, pvalue=0.00060564874812197894)

#### burger vs swipe 4

Ttest\_indResult(statistic=-7.981729679231651, pvalue=5.0201723649504874e-14)

#### burger vs swipe 5

Ttest\_indResult(statistic=-11.658440737398982, pvalue=1.7212956322485464e-24)

### Global Burger vs Global Swipe Test \[time\_ms\]

#### burger vs swipe

Ttest\_indResult(statistic=-3.3427694548324953, pvalue=0.00085423271669792108)

Effectiveness by Tasks
----------------------

### Descriptions \[success\]

#### Global Descriptions \[success\]

##### burger

count | 550 |\
unique | 2 |\
top | True |\
freq | 538 |

##### swipe

count | 700 |\
unique | 2 |\
top | True |\
freq | 654 |

#### Descriptions per tid \[success\]

##### ('burger', 1)

count | 110 |\
unique | 2 |\
top | True |\
freq | 109 |

##### ('burger', 2)

count | 110 |\
unique | 2 |\
top | True |\
freq | 106 |

##### ('burger', 3)

count | 110 |\
unique | 2 |\
top | True |\
freq | 106 |

##### ('burger', 4)

count | 110 |\
unique | 2 |\
top | True |\
freq | 108 |

##### ('burger', 5)

count | 110 |\
unique | 2 |\
top | True |\
freq | 109 |

##### ('swipe', 1)

count | 140 |\
unique | 2 |\
top | True |\
freq | 137 |

##### ('swipe', 2)

count | 140 |\
unique | 2 |\
top | True |\
freq | 131 |

##### ('swipe', 3)

count | 140 |\
unique | 2 |\
top | True |\
freq | 125 |

##### ('swipe', 4)

count | 140 |\
unique | 2 |\
top | True |\
freq | 132 |

##### ('swipe', 5)

count | 140 |\
unique | 2 |\
top | True |\
freq | 129 |

### Cross-compare Tests per tid \[success\]

#### ('burger', 1) vs ('burger', 2)

Ttest\_indResult(statistic=1.3566596213974287, pvalue=0.17678194158108454)

#### ('burger', 1) vs ('burger', 3)

Ttest\_indResult(statistic=1.3566596213974287, pvalue=0.17678194158108454)

#### ('burger', 1) vs ('burger', 4)

Ttest\_indResult(statistic=0.57912400691442567, pvalue=0.56316817234044769)

#### ('burger', 1) vs ('burger', 5)

Ttest\_indResult(statistic=0.0, pvalue=1.0)

#### ('burger', 1) vs ('swipe', 1)

Ttest\_indResult(statistic=0.80739517975463093, pvalue=0.42023551788635605)

#### ('burger', 1) vs ('swipe', 2)

Ttest\_indResult(statistic=2.4312286347458874, pvalue=0.015983788401592251)

#### ('burger', 1) vs ('swipe', 3)

Ttest\_indResult(statistic=3.5315534086960496, pvalue=0.00053094839433830772)

#### ('burger', 1) vs ('swipe', 4)

Ttest\_indResult(statistic=2.215874978949087, pvalue=0.027866499438757488)

#### ('burger', 1) vs ('swipe', 5)

Ttest\_indResult(statistic=2.8283089411876623, pvalue=0.0052076221586708762)

#### ('burger', 2) vs ('burger', 3)

Ttest\_indResult(statistic=0.0, pvalue=1.0)

#### ('burger', 2) vs ('burger', 4)

Ttest\_indResult(statistic=-0.82537870096095911, pvalue=0.41015411439664728)

#### ('burger', 2) vs ('burger', 5)

Ttest\_indResult(statistic=-1.3566596213974287, pvalue=0.17678194158108454)

#### ('burger', 2) vs ('swipe', 1)

Ttest\_indResult(statistic=-0.68719540412208679, pvalue=0.49275308971484577)

#### ('burger', 2) vs ('swipe', 2)

Ttest\_indResult(statistic=1.0167030982209715, pvalue=0.31028623539588174)

#### ('burger', 2) vs ('swipe', 3)

Ttest\_indResult(statistic=2.2274529233560192, pvalue=0.02686863183496167)

#### ('burger', 2) vs ('swipe', 4)

Ttest\_indResult(statistic=0.78033142539281197, pvalue=0.43594053940311395)

#### ('burger', 2) vs ('swipe', 5)

Ttest\_indResult(statistic=1.4542927864169122, pvalue=0.14714672347976621)

#### ('burger', 3) vs ('burger', 4)

Ttest\_indResult(statistic=-0.82537870096095911, pvalue=0.41015411439664728)

#### ('burger', 3) vs ('burger', 5)

Ttest\_indResult(statistic=-1.3566596213974287, pvalue=0.17678194158108454)

#### ('burger', 3) vs ('swipe', 1)

Ttest\_indResult(statistic=-0.68719540412208691, pvalue=0.49275308971484599)

#### ('burger', 3) vs ('swipe', 2)

Ttest\_indResult(statistic=1.0167030982209715, pvalue=0.31028623539588174)

#### ('burger', 3) vs ('swipe', 3)

Ttest\_indResult(statistic=2.2274529233560192, pvalue=0.026868631834961684)

#### ('burger', 3) vs ('swipe', 4)

Ttest\_indResult(statistic=0.78033142539281197, pvalue=0.43594053940311339)

#### ('burger', 3) vs ('swipe', 5)

Ttest\_indResult(statistic=1.4542927864169122, pvalue=0.14714672347976621)

#### ('burger', 4) vs ('burger', 5)

Ttest\_indResult(statistic=-0.57912400691442567, pvalue=0.56316817234044769)

#### ('burger', 4) vs ('swipe', 1)

Ttest\_indResult(statistic=0.1830408456352626, pvalue=0.85491950188735677)

#### ('burger', 4) vs ('swipe', 2)

Ttest\_indResult(statistic=1.8876521394554662, pvalue=0.060369367164060092)

#### ('burger', 4) vs ('swipe', 3)

Ttest\_indResult(statistic=3.0477589618316396, pvalue=0.0026190549770261249)

#### ('burger', 4) vs ('swipe', 4)

Ttest\_indResult(statistic=1.6592223276634299, pvalue=0.098439184876363106)

#### ('burger', 4) vs ('swipe', 5)

Ttest\_indResult(statistic=2.3080061990353404, pvalue=0.021957393227192475)

#### ('burger', 5) vs ('swipe', 1)

Ttest\_indResult(statistic=0.80739517975463093, pvalue=0.42023551788635605)

#### ('burger', 5) vs ('swipe', 2)

Ttest\_indResult(statistic=2.4312286347458874, pvalue=0.015983788401592251)

#### ('burger', 5) vs ('swipe', 3)

Ttest\_indResult(statistic=3.5315534086960496, pvalue=0.00053094839433830772)

#### ('burger', 5) vs ('swipe', 4)

Ttest\_indResult(statistic=2.215874978949087, pvalue=0.027866499438757488)

#### ('burger', 5) vs ('swipe', 5)

Ttest\_indResult(statistic=2.8283089411876623, pvalue=0.0052076221586708762)

#### ('swipe', 1) vs ('swipe', 2)

Ttest\_indResult(statistic=1.7740264404232391, pvalue=0.077408728725552087)

#### ('swipe', 1) vs ('swipe', 3)

Ttest\_indResult(statistic=2.9590379368657991, pvalue=0.0034639370862902222)

#### ('swipe', 1) vs ('swipe', 4)

Ttest\_indResult(statistic=1.5390840856715888, pvalue=0.12514089473419432)

#### ('swipe', 1) vs ('swipe', 5)

Ttest\_indResult(statistic=2.2048134129200938, pvalue=0.028535852417557052)

#### ('swipe', 2) vs ('swipe', 3)

Ttest\_indResult(statistic=1.280041747845708, pvalue=0.20165292226882248)

#### ('swipe', 2) vs ('swipe', 4)

Ttest\_indResult(statistic=-0.24938402863057901, pvalue=0.80324845639334197)

#### ('swipe', 2) vs ('swipe', 5)

Ttest\_indResult(statistic=0.46261298892397296, pvalue=0.64400676703062332)

#### ('swipe', 3) vs ('swipe', 4)

Ttest\_indResult(statistic=-1.5243950537075324, pvalue=0.12863551731870207)

#### ('swipe', 3) vs ('swipe', 5)

Ttest\_indResult(statistic=-0.82168544483210404, pvalue=0.41197355678268388)

#### ('swipe', 4) vs ('swipe', 5)

Ttest\_indResult(statistic=0.7109532653097157, pvalue=0.47772206370287928)

### Global Burger vs Swipe per tid Tests \[success\]

#### burger vs swipe 1

Ttest\_indResult(statistic=-0.028285152780717485, pvalue=0.97746081014720443)

#### burger vs swipe 2

Ttest\_indResult(statistic=1.95549234878333, pvalue=0.052216567883136028)

#### burger vs swipe 3

Ttest\_indResult(statistic=3.1643004716025089, pvalue=0.0018713455894696909)

#### burger vs swipe 4

Ttest\_indResult(statistic=1.7105169556030884, pvalue=0.089017873436017358)

#### burger vs swipe 5

Ttest\_indResult(statistic=2.3988552989827197, pvalue=0.017594620657847271)

### Global Burger vs Global Swipe Test \[success\]

#### burger vs swipe

Ttest\_indResult(statistic=3.8996269795774503, pvalue=0.00010184696908914221)

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

###### swipe

count | 140.0 |\
mean | 6.83571428571 |\
std | 0.458504203722 |\
min | 5.0 |\
25% | 7.0 |\
50% | 7.0 |\
75% | 7.0 |\
max | 7.0 |

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

###### ('burger', 2)

count | 22.0 |\
mean | 6.90909090909 |\
std | 0.294244943168 |\
min | 6.0 |\
25% | 7.0 |\
50% | 7.0 |\
75% | 7.0 |\
max | 7.0 |

###### ('burger', 3)

count | 22.0 |\
mean | 6.77272727273 |\
std | 0.751621623515 |\
min | 4.0 |\
25% | 7.0 |\
50% | 7.0 |\
75% | 7.0 |\
max | 7.0 |

###### ('burger', 4)

count | 22.0 |\
mean | 6.90909090909 |\
std | 0.294244943168 |\
min | 6.0 |\
25% | 7.0 |\
50% | 7.0 |\
75% | 7.0 |\
max | 7.0 |

###### ('burger', 5)

count | 22.0 |\
mean | 6.95454545455 |\
std | 0.213200716356 |\
min | 6.0 |\
25% | 7.0 |\
50% | 7.0 |\
75% | 7.0 |\
max | 7.0 |

###### ('swipe', 1)

count | 28.0 |\
mean | 6.85714285714 |\
std | 0.448395139423 |\
min | 5.0 |\
25% | 7.0 |\
50% | 7.0 |\
75% | 7.0 |\
max | 7.0 |

###### ('swipe', 2)

count | 28.0 |\
mean | 6.92857142857 |\
std | 0.262265264156 |\
min | 6.0 |\
25% | 7.0 |\
50% | 7.0 |\
75% | 7.0 |\
max | 7.0 |

###### ('swipe', 3)

count | 28.0 |\
mean | 6.82142857143 |\
std | 0.475594865606 |\
min | 5.0 |\
25% | 7.0 |\
50% | 7.0 |\
75% | 7.0 |\
max | 7.0 |

###### ('swipe', 4)

count | 28.0 |\
mean | 6.82142857143 |\
std | 0.475594865606 |\
min | 5.0 |\
25% | 7.0 |\
50% | 7.0 |\
75% | 7.0 |\
max | 7.0 |

###### ('swipe', 5)

count | 28.0 |\
mean | 6.75 |\
std | 0.585314097381 |\
min | 5.0 |\
25% | 7.0 |\
50% | 7.0 |\
75% | 7.0 |\
max | 7.0 |

#### Cross-compare Tests per tid \[result\]

##### ('burger', 1) vs ('burger', 2)

Ttest\_indResult(statistic=1.4491376746189426, pvalue=0.16206871193916272)

##### ('burger', 1) vs ('burger', 3)

Ttest\_indResult(statistic=1.4182715723279398, pvalue=0.17078161271838718)

##### ('burger', 1) vs ('burger', 4)

Ttest\_indResult(statistic=1.4491376746189426, pvalue=0.16206871193916272)

##### ('burger', 1) vs ('burger', 5)

Ttest\_indResult(statistic=1.0000000000000089, pvalue=0.32869468323645945)

##### ('burger', 1) vs ('swipe', 1)

Ttest\_indResult(statistic=1.6858544608470538, pvalue=0.1033481555997189)

##### ('burger', 1) vs ('swipe', 2)

Ttest\_indResult(statistic=1.4411533842457791, pvalue=0.16103934953023244)

##### ('burger', 1) vs ('swipe', 3)

Ttest\_indResult(statistic=1.9867985355975688, pvalue=0.057179118127154482)

##### ('burger', 1) vs ('swipe', 4)

Ttest\_indResult(statistic=1.9867985355975688, pvalue=0.057179118127154482)

##### ('burger', 1) vs ('swipe', 5)

Ttest\_indResult(statistic=2.2601124105026518, pvalue=0.03208842174489044)

##### ('burger', 2) vs ('burger', 3)

Ttest\_indResult(statistic=0.79240581569306312, pvalue=0.434959083634744)

##### ('burger', 2) vs ('burger', 4)

Ttest\_indResult(statistic=0.0, pvalue=1.0)

##### ('burger', 2) vs ('burger', 5)

Ttest\_indResult(statistic=-0.58673869403846191, pvalue=0.56082327307745816)

##### ('burger', 2) vs ('swipe', 1)

Ttest\_indResult(statistic=0.49271170229567274, pvalue=0.62452609288904781)

##### ('burger', 2) vs ('swipe', 2)

Ttest\_indResult(statistic=-0.24365889171012692, pvalue=0.80866695186899662)

##### ('burger', 2) vs ('swipe', 3)

Ttest\_indResult(statistic=0.79978792158211109, pvalue=0.42796667468869776)

##### ('burger', 2) vs ('swipe', 4)

Ttest\_indResult(statistic=0.79978792158211109, pvalue=0.42796667468869776)

##### ('burger', 2) vs ('swipe', 5)

Ttest\_indResult(statistic=1.2510600541476802, pvalue=0.2178987002569478)

##### ('burger', 3) vs ('burger', 4)

Ttest\_indResult(statistic=-0.79240581569306312, pvalue=0.434959083634744)

##### ('burger', 3) vs ('burger', 5)

Ttest\_indResult(statistic=-1.0915536458196295, pvalue=0.28570930736987338)

##### ('burger', 3) vs ('swipe', 1)

Ttest\_indResult(statistic=-0.46568478226137766, pvalue=0.64455504483952952)

##### ('burger', 3) vs ('swipe', 2)

Ttest\_indResult(statistic=-0.92910316007448612, pvalue=0.36170919252817291)

##### ('burger', 3) vs ('swipe', 3)

Ttest\_indResult(statistic=-0.26506842102661687, pvalue=0.7925715578816479)

##### ('burger', 3) vs ('swipe', 4)

Ttest\_indResult(statistic=-0.26506842102661687, pvalue=0.7925715578816479)

##### ('burger', 3) vs ('swipe', 5)

Ttest\_indResult(statistic=0.11672011558286063, pvalue=0.90768224442657708)

##### ('burger', 4) vs ('burger', 5)

Ttest\_indResult(statistic=-0.58673869403846191, pvalue=0.56082327307745816)

##### ('burger', 4) vs ('swipe', 1)

Ttest\_indResult(statistic=0.49271170229567274, pvalue=0.62452609288904781)

##### ('burger', 4) vs ('swipe', 2)

Ttest\_indResult(statistic=-0.24365889171012692, pvalue=0.80866695186899662)

##### ('burger', 4) vs ('swipe', 3)

Ttest\_indResult(statistic=0.79978792158211109, pvalue=0.42796667468869776)

##### ('burger', 4) vs ('swipe', 4)

Ttest\_indResult(statistic=0.79978792158211109, pvalue=0.42796667468869776)

##### ('burger', 4) vs ('swipe', 5)

Ttest\_indResult(statistic=1.2510600541476802, pvalue=0.2178987002569478)

##### ('burger', 5) vs ('swipe', 1)

Ttest\_indResult(statistic=1.0129210828495314, pvalue=0.31711639921326906)

##### ('burger', 5) vs ('swipe', 2)

Ttest\_indResult(statistic=0.38622696788057731, pvalue=0.70103791654914316)

##### ('burger', 5) vs ('swipe', 3)

Ttest\_indResult(statistic=1.3216640957475614, pvalue=0.193927451557106)

##### ('burger', 5) vs ('swipe', 4)

Ttest\_indResult(statistic=1.3216640957475614, pvalue=0.193927451557106)

##### ('burger', 5) vs ('swipe', 5)

Ttest\_indResult(statistic=1.7104014031978396, pvalue=0.095898470850199258)

##### ('swipe', 1) vs ('swipe', 2)

Ttest\_indResult(statistic=-0.72760687510900546, pvalue=0.47074919343997945)

##### ('swipe', 1) vs ('swipe', 3)

Ttest\_indResult(statistic=0.28912165479145496, pvalue=0.77359920204510002)

##### ('swipe', 1) vs ('swipe', 4)

Ttest\_indResult(statistic=0.28912165479145496, pvalue=0.77359920204510002)

##### ('swipe', 1) vs ('swipe', 5)

Ttest\_indResult(statistic=0.76892189194508209, pvalue=0.44551595328148408)

##### ('swipe', 2) vs ('swipe', 3)

Ttest\_indResult(statistic=1.0438803085865349, pvalue=0.30250767106524179)

##### ('swipe', 2) vs ('swipe', 4)

Ttest\_indResult(statistic=1.0438803085865349, pvalue=0.30250767106524179)

##### ('swipe', 2) vs ('swipe', 5)

Ttest\_indResult(statistic=1.4732338600612171, pvalue=0.14905035503113803)

##### ('swipe', 3) vs ('swipe', 4)

Ttest\_indResult(statistic=0.0, pvalue=1.0)

##### ('swipe', 3) vs ('swipe', 5)

Ttest\_indResult(statistic=0.50116144175073229, pvalue=0.61837946822394008)

##### ('swipe', 4) vs ('swipe', 5)

Ttest\_indResult(statistic=0.50116144175073229, pvalue=0.61837946822394008)

#### Global Burger vs Swipe per tid Tests \[result\]

##### burger vs swipe 1

Ttest\_indResult(statistic=0.55997233123865175, pvalue=0.57874985452460637)

##### burger vs swipe 2

Ttest\_indResult(statistic=-0.31266159062439741, pvalue=0.75558308779702033)

##### burger vs swipe 3

Ttest\_indResult(statistic=0.89922333067579296, pvalue=0.37433593164182521)

##### burger vs swipe 4

Ttest\_indResult(statistic=0.89922333067579296, pvalue=0.37433593164182521)

##### burger vs swipe 5

Ttest\_indResult(statistic=1.3611501176257312, pvalue=0.18254059625123423)

#### Global Burger vs Global Swipe Test \[result\]

##### burger vs swipe

Ttest\_indResult(statistic=1.3562601440255169, pvalue=0.17626116218076363)

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

###### swipe

count | 140.0 |\
mean | 2.86428571429 |\
std | 2.12964925773 |\
min | 1.0 |\
25% | 1.0 |\
50% | 2.0 |\
75% | 4.0 |\
max | 7.0 |

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

###### ('burger', 2)

count | 22.0 |\
mean | 1.77272727273 |\
std | 1.87545088374 |\
min | 1.0 |\
25% | 1.0 |\
50% | 1.0 |\
75% | 1.0 |\
max | 7.0 |

###### ('burger', 3)

count | 22.0 |\
mean | 2.0 |\
std | 1.74574312189 |\
min | 1.0 |\
25% | 1.0 |\
50% | 1.0 |\
75% | 2.0 |\
max | 6.0 |

###### ('burger', 4)

count | 22.0 |\
mean | 1.77272727273 |\
std | 1.54092792643 |\
min | 1.0 |\
25% | 1.0 |\
50% | 1.0 |\
75% | 1.0 |\
max | 6.0 |

###### ('burger', 5)

count | 22.0 |\
mean | 1.95454545455 |\
std | 1.98751514465 |\
min | 1.0 |\
25% | 1.0 |\
50% | 1.0 |\
75% | 1.0 |\
max | 7.0 |

###### ('swipe', 1)

count | 28.0 |\
mean | 2.75 |\
std | 2.36682315602 |\
min | 1.0 |\
25% | 1.0 |\
50% | 1.0 |\
75% | 4.25 |\
max | 7.0 |

###### ('swipe', 2)

count | 28.0 |\
mean | 2.67857142857 |\
std | 2.21198036674 |\
min | 1.0 |\
25% | 1.0 |\
50% | 1.0 |\
75% | 4.0 |\
max | 7.0 |

###### ('swipe', 3)

count | 28.0 |\
mean | 2.82142857143 |\
std | 2.16116517662 |\
min | 1.0 |\
25% | 1.0 |\
50% | 2.0 |\
75% | 4.0 |\
max | 7.0 |

###### ('swipe', 4)

count | 28.0 |\
mean | 2.85714285714 |\
std | 1.87999774851 |\
min | 1.0 |\
25% | 1.0 |\
50% | 3.0 |\
75% | 4.0 |\
max | 7.0 |

###### ('swipe', 5)

count | 28.0 |\
mean | 3.21428571429 |\
std | 2.11445015806 |\
min | 1.0 |\
25% | 1.0 |\
50% | 3.0 |\
75% | 4.0 |\
max | 7.0 |

#### Cross-compare Tests per tid \[result\]

##### ('burger', 1) vs ('burger', 2)

Ttest\_indResult(statistic=0.31010458564086002, pvalue=0.75802244540869279)

##### ('burger', 1) vs ('burger', 3)

Ttest\_indResult(statistic=-0.080051859907446427, pvalue=0.93658374072558803)

##### ('burger', 1) vs ('burger', 4)

Ttest\_indResult(statistic=0.33657671342337503, pvalue=0.73822512878677493)

##### ('burger', 1) vs ('burger', 5)

Ttest\_indResult(statistic=0.0, pvalue=1.0)

##### ('burger', 1) vs ('swipe', 1)

Ttest\_indResult(statistic=-1.2837421053733327, pvalue=0.2054375873090272)

##### ('burger', 1) vs ('swipe', 2)

Ttest\_indResult(statistic=-1.2090139880073498, pvalue=0.23271472223326703)

##### ('burger', 1) vs ('swipe', 3)

Ttest\_indResult(statistic=-1.463852065048149, pvalue=0.14995179579288434)

##### ('burger', 1) vs ('swipe', 4)

Ttest\_indResult(statistic=-1.6208185434680238, pvalue=0.11224980129520724)

##### ('burger', 1) vs ('swipe', 5)

Ttest\_indResult(statistic=-2.1492165095182081, pvalue=0.03688815104511671)

##### ('burger', 2) vs ('burger', 3)

Ttest\_indResult(statistic=-0.41604800757760851, pvalue=0.6795040084428422)

##### ('burger', 2) vs ('burger', 4)

Ttest\_indResult(statistic=0.0, pvalue=1.0)

##### ('burger', 2) vs ('burger', 5)

Ttest\_indResult(statistic=-0.31207579904219773, pvalue=0.75653217927135352)

##### ('burger', 2) vs ('swipe', 1)

Ttest\_indResult(statistic=-1.6289142640148464, pvalue=0.10987883761813257)

##### ('burger', 2) vs ('swipe', 2)

Ttest\_indResult(statistic=-1.5659419487889481, pvalue=0.12397500203185813)

##### ('burger', 2) vs ('swipe', 3)

Ttest\_indResult(statistic=-1.8347896616603989, pvalue=0.072806163662061316)

##### ('burger', 2) vs ('swipe', 4)

Ttest\_indResult(statistic=-2.0273655509871724, pvalue=0.048533888623595652)

##### ('burger', 2) vs ('swipe', 5)

Ttest\_indResult(statistic=-2.550121168647193, pvalue=0.014070036183701212)

##### ('burger', 3) vs ('burger', 4)

Ttest\_indResult(statistic=0.45779999816880002, pvalue=0.64949206222919309)

##### ('burger', 3) vs ('burger', 5)

Ttest\_indResult(statistic=0.08059475790364122, pvalue=0.93615340884054188)

##### ('burger', 3) vs ('swipe', 1)

Ttest\_indResult(statistic=-1.2889066290162134, pvalue=0.20362802550896689)

##### ('burger', 3) vs ('swipe', 2)

Ttest\_indResult(statistic=-1.2123668735785071, pvalue=0.23130618790625015)

##### ('burger', 3) vs ('swipe', 3)

Ttest\_indResult(statistic=-1.4865530860485299, pvalue=0.14367932916113879)

##### ('burger', 3) vs ('swipe', 4)

Ttest\_indResult(statistic=-1.665827282358026, pvalue=0.10245606821048929)

##### ('burger', 3) vs ('swipe', 5)

Ttest\_indResult(statistic=-2.2236416215700405, pvalue=0.030927460331272798)

##### ('burger', 4) vs ('burger', 5)

Ttest\_indResult(statistic=-0.33910136104054245, pvalue=0.73632757197468268)

##### ('burger', 4) vs ('swipe', 1)

Ttest\_indResult(statistic=-1.7609344102128832, pvalue=0.084815434369215556)

##### ('burger', 4) vs ('swipe', 2)

Ttest\_indResult(statistic=-1.7037658302714056, pvalue=0.09497299007775549)

##### ('burger', 4) vs ('swipe', 3)

Ttest\_indResult(statistic=-2.0007469881640132, pvalue=0.051138917909208527)

##### ('burger', 4) vs ('swipe', 4)

Ttest\_indResult(statistic=-2.2409958289424603, pvalue=0.029698757129413455)

##### ('burger', 4) vs ('swipe', 5)

Ttest\_indResult(statistic=-2.7866677954802945, pvalue=0.0076168232047276047)

##### ('burger', 5) vs ('swipe', 1)

Ttest\_indResult(statistic=-1.2910409183090523, pvalue=0.20290434875885618)

##### ('burger', 5) vs ('swipe', 2)

Ttest\_indResult(statistic=-1.2163777102367443, pvalue=0.22990419438692747)

##### ('burger', 5) vs ('swipe', 3)

Ttest\_indResult(statistic=-1.4729715892618513, pvalue=0.14745914516885314)

##### ('burger', 5) vs ('swipe', 4)

Ttest\_indResult(statistic=-1.6322512563257097, pvalue=0.10976494840900448)

##### ('burger', 5) vs ('swipe', 5)

Ttest\_indResult(statistic=-2.1628863874669357, pvalue=0.035735733189624176)

##### ('swipe', 1) vs ('swipe', 2)

Ttest\_indResult(statistic=0.11667176816723937, pvalue=0.90755497563889476)

##### ('swipe', 1) vs ('swipe', 3)

Ttest\_indResult(statistic=-0.11792698212695876, pvalue=0.90656666165487043)

##### ('swipe', 1) vs ('swipe', 4)

Ttest\_indResult(statistic=-0.18756785365546197, pvalue=0.85195435322794189)

##### ('swipe', 1) vs ('swipe', 5)

Ttest\_indResult(statistic=-0.77408790290137819, pvalue=0.44229719902179665)

##### ('swipe', 2) vs ('swipe', 3)

Ttest\_indResult(statistic=-0.24444025311801382, pvalue=0.80781680136158207)

##### ('swipe', 2) vs ('swipe', 4)

Ttest\_indResult(statistic=-0.32549781971440689, pvalue=0.74609483697056533)

##### ('swipe', 2) vs ('swipe', 5)

Ttest\_indResult(statistic=-0.92637576511926945, pvalue=0.35838094161896383)

##### ('swipe', 3) vs ('swipe', 4)

Ttest\_indResult(statistic=-0.065975241937917109, pvalue=0.94764585285887681)

##### ('swipe', 3) vs ('swipe', 5)

Ttest\_indResult(statistic=-0.68754973774649286, pvalue=0.49468042451910721)

##### ('swipe', 4) vs ('swipe', 5)

Ttest\_indResult(statistic=-0.66793226421816831, pvalue=0.50706047845662638)

#### Global Burger vs Swipe per tid Tests \[result\]

##### burger vs swipe 1

Ttest\_indResult(statistic=-1.7920485696152606, pvalue=0.081668377626223213)

##### burger vs swipe 2

Ttest\_indResult(statistic=-1.7418063441047225, pvalue=0.089916422412057356)

##### burger vs swipe 3

Ttest\_indResult(statistic=-2.0988468236683779, pvalue=0.042676536020284629)

##### burger vs swipe 4

Ttest\_indResult(statistic=-2.446535421195474, pvalue=0.018837342914925163)

##### burger vs swipe 5

Ttest\_indResult(statistic=-3.0406465555493165, pvalue=0.0042798608827830081)

#### Global Burger vs Global Swipe Test \[result\]

##### burger vs swipe

Ttest\_indResult(statistic=-3.9046179737739855, pvalue=0.00012188835447452269)

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

###### swipe

count | 28.0 |\
mean | 1.53571428571 |\
std | 1.29048204766 |\
min | 1.0 |\
25% | 1.0 |\
50% | 1.0 |\
75% | 1.25 |\
max | 7.0 |

#### Global Burger vs Global Swipe Test \[result\]

##### burger vs swipe

Ttest\_indResult(statistic=-0.10751543495766284, pvalue=0.9148292292550424)

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

###### swipe

count | 28.0 |\
mean | 1.67857142857 |\
std | 1.18801332542 |\
min | 1.0 |\
25% | 1.0 |\
50% | 1.0 |\
75% | 2.0 |\
max | 6.0 |

#### Global Burger vs Global Swipe Test \[result\]

##### burger vs swipe

Ttest\_indResult(statistic=1.2353085848140299, pvalue=0.22501281363206999)

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

###### swipe

count | 28.0 |\
mean | 1.75 |\
std | 1.37773297418 |\
min | 1.0 |\
25% | 1.0 |\
50% | 1.0 |\
75% | 2.0 |\
max | 7.0 |

#### Global Burger vs Global Swipe Test \[result\]

##### burger vs swipe

Ttest\_indResult(statistic=-1.8942147514189334, pvalue=0.066878319737774167)

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

###### swipe

count | 28.0 |\
mean | 4.5 |\
std | 1.45296631451 |\
min | 1.0 |\
25% | 4.0 |\
50% | 4.0 |\
75% | 5.25 |\
max | 7.0 |

#### Global Burger vs Global Swipe Test \[result\]

##### burger vs swipe

Ttest\_indResult(statistic=1.4151306918873736, pvalue=0.16442349507017537)
