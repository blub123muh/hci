Analysis
========

Preprocessing
-------------

-   experiment\_results.csv
-   task\_questionnaire\_results.csv
-   final\_questionnaire\_results.csv
-   demographic\_data\_fixed.csv

Dropping Task ID 0 (Training)

Asserting Absolute Distance Values!

Dataset Validation:\
dict\_items(\[('pid', True)\])

Adding success column based on\
`opt_interactions == interactions`\
in order to measure effectiveness.

Aggregating Task Groups

Using normality test: shapiro

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

### Descriptions (time\_ms)

#### Global Descriptions (time\_ms)

##### burger

count | 110.0 |\
mean | 4638.11818182 |\
std | 1251.30839042 |\
min | 2974.8 |\
25% | 3871.7 |\
50% | 4375.3 |\
75% | 5029.45 |\
max | 11598.2 |

shapiro\
(0.802947998046875, 7.877890007002009e-11)

##### swipe

count | 140.0 |\
mean | 5105.28428571 |\
std | 1878.17462417 |\
min | 1941.8 |\
25% | 3672.2 |\
50% | 4950.3 |\
75% | 6415.4 |\
max | 10211.0 |

shapiro\
(0.9749319553375244, 0.011162536218762398)

#### Repeated measures (time\_ms)

##### burger

friedmanchisquare\
FriedmanchisquareResult(statistic=32.618181818181824,
pvalue=1.4299671878258814e-06)

##### swipe

friedmanchisquare\
FriedmanchisquareResult(statistic=99.0, pvalue=1.6058853045998598e-20)

#### Descriptions per tid (time\_ms)

##### ('burger', 1)

count | 22.0 |\
mean | 3882.02727273 |\
std | 527.012396332 |\
min | 2974.8 |\
25% | 3558.45 |\
50% | 3802.0 |\
75% | 4053.1 |\
max | 5278.2 |

shapiro\
(0.9460052847862244, 0.26264825463294983)

##### ('burger', 2)

count | 22.0 |\
mean | 4855.64545455 |\
std | 1865.02294323 |\
min | 3348.4 |\
25% | 3808.65 |\
50% | 4359.2 |\
75% | 4578.85 |\
max | 11598.2 |

shapiro\
(0.7007542848587036, 2.0007397324661724e-05)

##### ('burger', 3)

count | 22.0 |\
mean | 4923.24545455 |\
std | 1382.21854785 |\
min | 3571.0 |\
25% | 4064.05 |\
50% | 4597.1 |\
75% | 5142.0 |\
max | 8840.8 |

shapiro\
(0.7784804701805115, 0.00023477213107980788)

##### ('burger', 4)

count | 22.0 |\
mean | 4455.94545455 |\
std | 905.444160792 |\
min | 3286.4 |\
25% | 3905.6 |\
50% | 4331.4 |\
75% | 4714.1 |\
max | 7063.4 |

shapiro\
(0.9076412916183472, 0.042384739965200424)

##### ('burger', 5)

count | 22.0 |\
mean | 5073.72727273 |\
std | 820.671220162 |\
min | 3920.4 |\
25% | 4413.7 |\
50% | 5098.7 |\
75% | 5444.1 |\
max | 6927.6 |

shapiro\
(0.9563226103782654, 0.41870200634002686)

##### ('swipe', 1)

count | 28.0 |\
mean | 2770.21428571 |\
std | 883.229726299 |\
min | 1941.8 |\
25% | 2296.25 |\
50% | 2554.1 |\
75% | 2865.6 |\
max | 6413.4 |

shapiro\
(0.6596945524215698, 8.059980132202327e-07)

##### ('swipe', 2)

count | 28.0 |\
mean | 4204.86428571 |\
std | 1330.36827878 |\
min | 3202.4 |\
25% | 3635.95 |\
50% | 3765.6 |\
75% | 4341.1 |\
max | 10211.0 |

shapiro\
(0.5677787065505981, 6.146506592585865e-08)

##### ('swipe', 3)

count | 28.0 |\
mean | 5175.67857143 |\
std | 889.237003511 |\
min | 3899.8 |\
25% | 4701.9 |\
50% | 4908.9 |\
75% | 5396.35 |\
max | 7508.4 |

shapiro\
(0.8815559148788452, 0.004346329253166914)

##### ('swipe', 4)

count | 28.0 |\
mean | 6123.01428571 |\
std | 1000.60964517 |\
min | 4474.6 |\
25% | 5388.2 |\
50% | 6092.4 |\
75% | 6559.75 |\
max | 9004.2 |

shapiro\
(0.944583535194397, 0.1445537954568863)

##### ('swipe', 5)

count | 28.0 |\
mean | 7252.65 |\
std | 1209.06568841 |\
min | 5476.8 |\
25% | 6350.65 |\
50% | 7014.5 |\
75% | 7972.85 |\
max | 9742.0 |

shapiro\
(0.9483340978622437, 0.17988574504852295)

### Cross-compare Tests per tid (time\_ms)

#### ('burger', 1) vs ('burger', 2)

MannwhitneyuResult(statistic=151.0, pvalue=0.016817419210219058)

#### ('burger', 1) vs ('burger', 3)

MannwhitneyuResult(statistic=95.0, pvalue=0.00029221438038809819)

#### ('burger', 1) vs ('burger', 4)

MannwhitneyuResult(statistic=139.0, pvalue=0.0080653641686478112)

#### ('burger', 1) vs ('burger', 5)

Ttest\_indResult(statistic=-5.7310272087258207, pvalue=1.619575495038546e-06)

#### ('burger', 1) vs ('swipe', 1)

MannwhitneyuResult(statistic=49.0, pvalue=2.1843898538621358e-07)

#### ('burger', 1) vs ('swipe', 2)

MannwhitneyuResult(statistic=282.0, pvalue=0.30911023670878912)

#### ('burger', 1) vs ('swipe', 3)

MannwhitneyuResult(statistic=43.0, pvalue=1.1741801859588888e-07)

#### ('burger', 1) vs ('swipe', 4)

Ttest\_indResult(statistic=-10.188148275652745, pvalue=5.439990089157802e-13)

#### ('burger', 1) vs ('swipe', 5)

Ttest\_indResult(statistic=-13.237665385930107, pvalue=5.9225323858749191e-16)

#### ('burger', 2) vs ('burger', 3)

MannwhitneyuResult(statistic=195.0, pvalue=0.1375314960388796)

#### ('burger', 2) vs ('burger', 4)

MannwhitneyuResult(statistic=240.0, pvalue=0.48595656697665318)

#### ('burger', 2) vs ('burger', 5)

MannwhitneyuResult(statistic=160.0, pvalue=0.02787280707345783)

#### ('burger', 2) vs ('swipe', 1)

MannwhitneyuResult(statistic=35.0, pvalue=5.0265581070320699e-08)

#### ('burger', 2) vs ('swipe', 2)

MannwhitneyuResult(statistic=221.0, pvalue=0.045460175439921736)

#### ('burger', 2) vs ('swipe', 3)

MannwhitneyuResult(statistic=173.0, pvalue=0.0042858685698253926)

#### ('burger', 2) vs ('swipe', 4)

MannwhitneyuResult(statistic=114.0, pvalue=7.7855780297600262e-05)

#### ('burger', 2) vs ('swipe', 5)

MannwhitneyuResult(statistic=70.0, pvalue=1.7276174406690636e-06)

#### ('burger', 3) vs ('burger', 4)

MannwhitneyuResult(statistic=190.0, pvalue=0.11336211114805772)

#### ('burger', 3) vs ('burger', 5)

MannwhitneyuResult(statistic=180.0, pvalue=0.074430474150163767)

#### ('burger', 3) vs ('swipe', 1)

MannwhitneyuResult(statistic=30.0, pvalue=2.9224626895523775e-08)

#### ('burger', 3) vs ('swipe', 2)

MannwhitneyuResult(statistic=152.0, pvalue=0.0011864143494592009)

#### ('burger', 3) vs ('swipe', 3)

MannwhitneyuResult(statistic=203.0, pvalue=0.020558109931233946)

#### ('burger', 3) vs ('swipe', 4)

MannwhitneyuResult(statistic=105.0, pvalue=3.7841304344645438e-05)

#### ('burger', 3) vs ('swipe', 5)

MannwhitneyuResult(statistic=62.0, pvalue=8.0100475146483783e-07)

#### ('burger', 4) vs ('burger', 5)

MannwhitneyuResult(statistic=136.0, pvalue=0.0066364447880311464)

#### ('burger', 4) vs ('swipe', 1)

MannwhitneyuResult(statistic=37.0, pvalue=6.2280507570442701e-08)

#### ('burger', 4) vs ('swipe', 2)

MannwhitneyuResult(statistic=212.5, pvalue=0.031674649462165971)

#### ('burger', 4) vs ('swipe', 3)

MannwhitneyuResult(statistic=151.0, pvalue=0.0011116905748856589)

#### ('burger', 4) vs ('swipe', 4)

MannwhitneyuResult(statistic=58.0, pvalue=5.4061503445428946e-07)

#### ('burger', 4) vs ('swipe', 5)

MannwhitneyuResult(statistic=21.0, pvalue=1.0756098347672391e-08)

#### ('burger', 5) vs ('swipe', 1)

MannwhitneyuResult(statistic=29.0, pvalue=2.6191554910060229e-08)

#### ('burger', 5) vs ('swipe', 2)

MannwhitneyuResult(statistic=93.0, pvalue=1.381283064893737e-05)

#### ('burger', 5) vs ('swipe', 3)

MannwhitneyuResult(statistic=306.0, pvalue=0.48830623668427992)

#### ('burger', 5) vs ('swipe', 4)

Ttest\_indResult(statistic=-4.0728963297471577, pvalue=0.00017339525839808439)

#### ('burger', 5) vs ('swipe', 5)

Ttest\_indResult(statistic=-7.5712623152822953, pvalue=1.1021397421496496e-09)

#### ('swipe', 1) vs ('swipe', 2)

MannwhitneyuResult(statistic=54.0, pvalue=1.5960698242093411e-08)

#### ('swipe', 1) vs ('swipe', 3)

MannwhitneyuResult(statistic=31.0, pvalue=1.7371643979876513e-09)

#### ('swipe', 1) vs ('swipe', 4)

MannwhitneyuResult(statistic=18.0, pvalue=4.66457628014128e-10)

#### ('swipe', 1) vs ('swipe', 5)

MannwhitneyuResult(statistic=8.0, pvalue=1.6461154966355821e-10)

#### ('swipe', 2) vs ('swipe', 3)

MannwhitneyuResult(statistic=105.0, pvalue=1.3341483772913665e-06)

#### ('swipe', 2) vs ('swipe', 4)

MannwhitneyuResult(statistic=45.0, pvalue=6.8123663028551721e-09)

#### ('swipe', 2) vs ('swipe', 5)

MannwhitneyuResult(statistic=34.0, pvalue=2.3382222267736259e-09)

#### ('swipe', 3) vs ('swipe', 4)

MannwhitneyuResult(statistic=163.0, pvalue=9.0415384769806993e-05)

#### ('swipe', 3) vs ('swipe', 5)

MannwhitneyuResult(statistic=54.0, pvalue=1.5960698242093411e-08)

#### ('swipe', 4) vs ('swipe', 5)

Ttest\_indResult(statistic=-3.8087281736762768, pvalue=0.00036955600286607841)

### Global Burger vs Swipe per tid Tests (time\_ms)

#### burger vs swipe 1

MannwhitneyuResult(statistic=180.0, pvalue=3.0639459096717655e-13)

#### burger vs swipe 2

MannwhitneyuResult(statistic=1012.5, pvalue=0.0026345778537083492)

#### burger vs swipe 3

MannwhitneyuResult(statistic=876.0, pvalue=0.00022173012779323569)

#### burger vs swipe 4

MannwhitneyuResult(statistic=407.0, pvalue=1.0124366289475617e-09)

#### burger vs swipe 5

MannwhitneyuResult(statistic=186.0, pvalue=3.8655469327992148e-13)

### Global Burger vs Global Swipe Test (time\_ms)

#### burger vs swipe

MannwhitneyuResult(statistic=6436.5, pvalue=0.013029103088263865)

Effectiveness by Tasks
----------------------

### Descriptions (success)

#### Global Descriptions (success)

##### burger

count | 110.0 |\
mean | 0.978181818182 |\
std | 0.0626360071457 |\
min | 0.8 |\
25% | 1.0 |\
50% | 1.0 |\
75% | 1.0 |\
max | 1.0 |

shapiro\
(0.3595287799835205, 8.873730593883483e-20)

##### swipe

count | 140.0 |\
mean | 0.934285714286 |\
std | 0.105783427849 |\
min | 0.6 |\
25% | 0.8 |\
50% | 1.0 |\
75% | 1.0 |\
max | 1.0 |

shapiro\
(0.6147457361221313, 1.3754389831214409e-17)

#### Repeated measures (success)

##### burger

friedmanchisquare\
FriedmanchisquareResult(statistic=5.1111111111109082, pvalue=0.276085623834601)

##### swipe

friedmanchisquare\
FriedmanchisquareResult(statistic=8.7192429022081477,
pvalue=0.068513251264267688)

#### Descriptions per tid (success)

##### ('burger', 1)

count | 22.0 |\
mean | 0.990909090909 |\
std | 0.0426401432711 |\
min | 0.8 |\
25% | 1.0 |\
50% | 1.0 |\
75% | 1.0 |\
max | 1.0 |

shapiro\
(0.22147256135940552, 7.41695094230721e-10)

##### ('burger', 2)

count | 22.0 |\
mean | 0.963636363636 |\
std | 0.0789542033952 |\
min | 0.8 |\
25% | 1.0 |\
50% | 1.0 |\
75% | 1.0 |\
max | 1.0 |

shapiro\
(0.4735521674156189, 7.489492048762258e-08)

##### ('burger', 3)

count | 22.0 |\
mean | 0.963636363636 |\
std | 0.0789542033952 |\
min | 0.8 |\
25% | 1.0 |\
50% | 1.0 |\
75% | 1.0 |\
max | 1.0 |

shapiro\
(0.4735521674156189, 7.489492048762258e-08)

##### ('burger', 4)

count | 22.0 |\
mean | 0.981818181818 |\
std | 0.0588489886336 |\
min | 0.8 |\
25% | 1.0 |\
50% | 1.0 |\
75% | 1.0 |\
max | 1.0 |

shapiro\
(0.3322211503982544, 4.875188253095075e-09)

##### ('burger', 5)

count | 22.0 |\
mean | 0.990909090909 |\
std | 0.0426401432711 |\
min | 0.8 |\
25% | 1.0 |\
50% | 1.0 |\
75% | 1.0 |\
max | 1.0 |

shapiro\
(0.22147256135940552, 7.41695094230721e-10)

##### ('swipe', 1)

count | 28.0 |\
mean | 0.978571428571 |\
std | 0.0629940788349 |\
min | 0.8 |\
25% | 1.0 |\
50% | 1.0 |\
75% | 1.0 |\
max | 1.0 |

shapiro\
(0.36062484979629517, 5.463860475174442e-10)

##### ('swipe', 2)

count | 28.0 |\
mean | 0.935714285714 |\
std | 0.0951189731211 |\
min | 0.8 |\
25% | 0.8 |\
50% | 1.0 |\
75% | 1.0 |\
max | 1.0 |

shapiro\
(0.5905900597572327, 1.1246834219491575e-07)

##### ('swipe', 3)

count | 28.0 |\
mean | 0.892857142857 |\
std | 0.138586973437 |\
min | 0.6 |\
25% | 0.8 |\
50% | 1.0 |\
75% | 1.0 |\
max | 1.0 |

shapiro\
(0.7237528562545776, 6.2850517679180484e-06)

##### ('swipe', 4)

count | 28.0 |\
mean | 0.942857142857 |\
std | 0.0920087412456 |\
min | 0.8 |\
25% | 0.8 |\
50% | 1.0 |\
75% | 1.0 |\
max | 1.0 |

shapiro\
(0.5682951211929321, 6.229736015939125e-08)

##### ('swipe', 5)

count | 28.0 |\
mean | 0.921428571429 |\
std | 0.113389341903 |\
min | 0.6 |\
25% | 0.8 |\
50% | 1.0 |\
75% | 1.0 |\
max | 1.0 |

shapiro\
(0.6656765341758728, 9.664669278208748e-07)

### Cross-compare Tests per tid (success)

#### ('burger', 1) vs ('burger', 2)

MannwhitneyuResult(statistic=209.0, pvalue=0.082657036656833605)

#### ('burger', 1) vs ('burger', 3)

MannwhitneyuResult(statistic=209.0, pvalue=0.082657036656833605)

#### ('burger', 1) vs ('burger', 4)

MannwhitneyuResult(statistic=231.0, pvalue=0.28624482430604659)

#### ('burger', 1) vs ('burger', 5)

MannwhitneyuResult(statistic=242.0, pvalue=0.48702804541380829)

#### ('burger', 1) vs ('swipe', 1)

MannwhitneyuResult(statistic=289.0, pvalue=0.22085511431458626)

#### ('burger', 1) vs ('swipe', 2)

MannwhitneyuResult(statistic=223.0, pvalue=0.0085809342731982628)

#### ('burger', 1) vs ('swipe', 3)

MannwhitneyuResult(statistic=188.5, pvalue=0.0011982167922993706)

#### ('burger', 1) vs ('swipe', 4)

MannwhitneyuResult(statistic=234.0, pvalue=0.015452252565939647)

#### ('burger', 1) vs ('swipe', 5)

MannwhitneyuResult(statistic=211.5, pvalue=0.0045566881958452573)

#### ('burger', 2) vs ('burger', 3)

MannwhitneyuResult(statistic=242.0, pvalue=0.49299346911620229)

#### ('burger', 2) vs ('burger', 4)

MannwhitneyuResult(statistic=220.0, pvalue=0.1979923748749125)

#### ('burger', 2) vs ('burger', 5)

MannwhitneyuResult(statistic=209.0, pvalue=0.082657036656833605)

#### ('burger', 2) vs ('swipe', 1)

MannwhitneyuResult(statistic=285.0, pvalue=0.23222527082050248)

#### ('burger', 2) vs ('swipe', 2)

MannwhitneyuResult(statistic=265.0, pvalue=0.13717816505985114)

#### ('burger', 2) vs ('swipe', 3)

MannwhitneyuResult(statistic=226.0, pvalue=0.025658789178159933)

#### ('burger', 2) vs ('swipe', 4)

MannwhitneyuResult(statistic=276.0, pvalue=0.20268150101021792)

#### ('burger', 2) vs ('swipe', 5)

MannwhitneyuResult(statistic=252.0, pvalue=0.082343202897603662)

#### ('burger', 3) vs ('burger', 4)

MannwhitneyuResult(statistic=220.0, pvalue=0.1979923748749125)

#### ('burger', 3) vs ('burger', 5)

MannwhitneyuResult(statistic=209.0, pvalue=0.082657036656833605)

#### ('burger', 3) vs ('swipe', 1)

MannwhitneyuResult(statistic=285.0, pvalue=0.23222527082050248)

#### ('burger', 3) vs ('swipe', 2)

MannwhitneyuResult(statistic=265.0, pvalue=0.13717816505985114)

#### ('burger', 3) vs ('swipe', 3)

MannwhitneyuResult(statistic=226.0, pvalue=0.025658789178159933)

#### ('burger', 3) vs ('swipe', 4)

MannwhitneyuResult(statistic=276.0, pvalue=0.20268150101021792)

#### ('burger', 3) vs ('swipe', 5)

MannwhitneyuResult(statistic=252.0, pvalue=0.082343202897603662)

#### ('burger', 4) vs ('burger', 5)

MannwhitneyuResult(statistic=231.0, pvalue=0.28624482430604659)

#### ('burger', 4) vs ('swipe', 1)

MannwhitneyuResult(statistic=303.0, pvalue=0.43281068947535356)

#### ('burger', 4) vs ('swipe', 2)

MannwhitneyuResult(statistic=237.0, pvalue=0.027429809187369383)

#### ('burger', 4) vs ('swipe', 3)

MannwhitneyuResult(statistic=201.0, pvalue=0.0040041913682163349)

#### ('burger', 4) vs ('swipe', 4)

MannwhitneyuResult(statistic=248.0, pvalue=0.046661220530755103)

#### ('burger', 4) vs ('swipe', 5)

MannwhitneyuResult(statistic=225.0, pvalue=0.014890923602395365)

#### ('burger', 5) vs ('swipe', 1)

MannwhitneyuResult(statistic=289.0, pvalue=0.22085511431458626)

#### ('burger', 5) vs ('swipe', 2)

MannwhitneyuResult(statistic=223.0, pvalue=0.0085809342731982628)

#### ('burger', 5) vs ('swipe', 3)

MannwhitneyuResult(statistic=188.5, pvalue=0.0011982167922993706)

#### ('burger', 5) vs ('swipe', 4)

MannwhitneyuResult(statistic=234.0, pvalue=0.015452252565939647)

#### ('burger', 5) vs ('swipe', 5)

MannwhitneyuResult(statistic=211.5, pvalue=0.0045566881958452573)

#### ('swipe', 1) vs ('swipe', 2)

MannwhitneyuResult(statistic=308.0, pvalue=0.027116872472542033)

#### ('swipe', 1) vs ('swipe', 3)

MannwhitneyuResult(statistic=261.5, pvalue=0.0029312417003149235)

#### ('swipe', 1) vs ('swipe', 4)

MannwhitneyuResult(statistic=322.0, pvalue=0.048986402150609308)

#### ('swipe', 1) vs ('swipe', 5)

MannwhitneyuResult(statistic=292.5, pvalue=0.013462573580567237)

#### ('swipe', 2) vs ('swipe', 3)

MannwhitneyuResult(statistic=336.5, pvalue=0.14453634210230498)

#### ('swipe', 2) vs ('swipe', 4)

MannwhitneyuResult(statistic=378.0, pvalue=0.39060796901685718)

#### ('swipe', 2) vs ('swipe', 5)

MannwhitneyuResult(statistic=373.5, pvalue=0.36014486364075388)

#### ('swipe', 3) vs ('swipe', 4)

MannwhitneyuResult(statistic=324.0, pvalue=0.094081951374916539)

#### ('swipe', 3) vs ('swipe', 5)

MannwhitneyuResult(statistic=355.0, pvalue=0.24385317707370369)

#### ('swipe', 4) vs ('swipe', 5)

MannwhitneyuResult(statistic=360.0, pvalue=0.26255479890207617)

### Global Burger vs Swipe per tid Tests (success)

#### burger vs swipe 1

MannwhitneyuResult(statistic=1537.0, pvalue=0.49020683242704011)

#### burger vs swipe 2

MannwhitneyuResult(statistic=1213.0, pvalue=0.0027313254754476467)

#### burger vs swipe 3

MannwhitneyuResult(statistic=1030.0, pvalue=2.0615949541882224e-05)

#### burger vs swipe 4

MannwhitneyuResult(statistic=1268.0, pvalue=0.0092023144768541426)

#### burger vs swipe 5

MannwhitneyuResult(statistic=1152.0, pvalue=0.00061159598135044442)

### Global Burger vs Global Swipe Test (success)

#### burger vs swipe

MannwhitneyuResult(statistic=6206.0, pvalue=0.00011462735661581992)

Task Questionnaires
-------------------

### Task Question 0

#### Descriptions (result)

##### Global Descriptions (result)

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

##### Repeated measures (result)

###### burger

friedmanchisquare\
FriedmanchisquareResult(statistic=3.3103448275862144,
pvalue=0.50729488262873967)

###### swipe

friedmanchisquare\
FriedmanchisquareResult(statistic=5.0958904109588801,
pvalue=0.27759929640181424)

##### Descriptions per tid (result)

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

#### Cross-compare Tests per tid (result)

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

#### Global Burger vs Swipe per tid Tests (result)

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

#### Global Burger vs Global Swipe Test (result)

##### burger vs swipe

MannwhitneyuResult(statistic=7203.0, pvalue=0.046318608676750285)

### Task Question 1

#### Descriptions (result)

##### Global Descriptions (result)

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

##### Repeated measures (result)

###### burger

friedmanchisquare\
FriedmanchisquareResult(statistic=2.7575757575757125,
pvalue=0.59917784877228941)

###### swipe

friedmanchisquare\
FriedmanchisquareResult(statistic=5.4968553459119409,
pvalue=0.24000603548291879)

##### Descriptions per tid (result)

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

#### Cross-compare Tests per tid (result)

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

#### Global Burger vs Swipe per tid Tests (result)

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

#### Global Burger vs Global Swipe Test (result)

##### burger vs swipe

MannwhitneyuResult(statistic=5406.5, pvalue=2.9062055593999374e-06)

Final Questionnaires
--------------------

### Final Question 0

#### Descriptions (result)

##### Global Descriptions (result)

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

#### Global Burger vs Global Swipe Test (result)

##### burger vs swipe

MannwhitneyuResult(statistic=302.5, pvalue=0.44941800310214225)

### Final Question 1

#### Descriptions (result)

##### Global Descriptions (result)

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

#### Global Burger vs Global Swipe Test (result)

##### burger vs swipe

MannwhitneyuResult(statistic=281.0, pvalue=0.27788843237866634)

### Final Question 2

#### Descriptions (result)

##### Global Descriptions (result)

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

#### Global Burger vs Global Swipe Test (result)

##### burger vs swipe

MannwhitneyuResult(statistic=255.5, pvalue=0.10358134878107761)

### Final Question 3

#### Descriptions (result)

##### Global Descriptions (result)

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

#### Global Burger vs Global Swipe Test (result)

##### burger vs swipe

MannwhitneyuResult(statistic=238.5, pvalue=0.084899251911718931)
