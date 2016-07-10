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

Using normality test: normaltest

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

normaltest\
NormaltestResult(statistic=76.823862390019315, pvalue=2.079266912942909e-17)

##### swipe

count | 140.0 |\
mean | 5105.28428571 |\
std | 1878.17462417 |\
min | 1941.8 |\
25% | 3672.2 |\
50% | 4950.3 |\
75% | 6415.4 |\
max | 10211.0 |

normaltest\
NormaltestResult(statistic=4.1262168679871163, pvalue=0.1270584027578627)

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

normaltest\
NormaltestResult(statistic=5.4950917433178086, pvalue=0.064084941050891631)

##### ('burger', 2)

count | 22.0 |\
mean | 4855.64545455 |\
std | 1865.02294323 |\
min | 3348.4 |\
25% | 3808.65 |\
50% | 4359.2 |\
75% | 4578.85 |\
max | 11598.2 |

normaltest\
NormaltestResult(statistic=28.296271253133376, pvalue=7.1703898419210531e-07)

##### ('burger', 3)

count | 22.0 |\
mean | 4923.24545455 |\
std | 1382.21854785 |\
min | 3571.0 |\
25% | 4064.05 |\
50% | 4597.1 |\
75% | 5142.0 |\
max | 8840.8 |

normaltest\
NormaltestResult(statistic=16.239339715682625, pvalue=0.00029762690341199154)

##### ('burger', 4)

count | 22.0 |\
mean | 4455.94545455 |\
std | 905.444160792 |\
min | 3286.4 |\
25% | 3905.6 |\
50% | 4331.4 |\
75% | 4714.1 |\
max | 7063.4 |

normaltest\
NormaltestResult(statistic=9.3359233468656129, pvalue=0.0093913927560497004)

##### ('burger', 5)

count | 22.0 |\
mean | 5073.72727273 |\
std | 820.671220162 |\
min | 3920.4 |\
25% | 4413.7 |\
50% | 5098.7 |\
75% | 5444.1 |\
max | 6927.6 |

normaltest\
NormaltestResult(statistic=1.0240505652669714, pvalue=0.59928063626132155)

##### ('swipe', 1)

count | 28.0 |\
mean | 2770.21428571 |\
std | 883.229726299 |\
min | 1941.8 |\
25% | 2296.25 |\
50% | 2554.1 |\
75% | 2865.6 |\
max | 6413.4 |

normaltest\
NormaltestResult(statistic=40.210028501523979, pvalue=1.8556807060464479e-09)

##### ('swipe', 2)

count | 28.0 |\
mean | 4204.86428571 |\
std | 1330.36827878 |\
min | 3202.4 |\
25% | 3635.95 |\
50% | 3765.6 |\
75% | 4341.1 |\
max | 10211.0 |

normaltest\
NormaltestResult(statistic=50.183283335215393, pvalue=1.2671805020588637e-11)

##### ('swipe', 3)

count | 28.0 |\
mean | 5175.67857143 |\
std | 889.237003511 |\
min | 3899.8 |\
25% | 4701.9 |\
50% | 4908.9 |\
75% | 5396.35 |\
max | 7508.4 |

normaltest\
NormaltestResult(statistic=9.4275154863943342, pvalue=0.0089710034377580416)

##### ('swipe', 4)

count | 28.0 |\
mean | 6123.01428571 |\
std | 1000.60964517 |\
min | 4474.6 |\
25% | 5388.2 |\
50% | 6092.4 |\
75% | 6559.75 |\
max | 9004.2 |

normaltest\
NormaltestResult(statistic=6.0922522821566361, pvalue=0.047542741994770842)

##### ('swipe', 5)

count | 28.0 |\
mean | 7252.65 |\
std | 1209.06568841 |\
min | 5476.8 |\
25% | 6350.65 |\
50% | 7014.5 |\
75% | 7972.85 |\
max | 9742.0 |

normaltest\
NormaltestResult(statistic=1.8115899346271727, pvalue=0.40422041532329878)

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

MannwhitneyuResult(statistic=6.0, pvalue=1.9015268435477013e-09)

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

MannwhitneyuResult(statistic=124.0, pvalue=0.00016767696076002179)

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

MannwhitneyuResult(statistic=177.0, pvalue=0.00021989622033020476)

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

normaltest\
NormaltestResult(statistic=68.459419887611048, pvalue=1.3621528840605701e-15)

##### swipe

count | 140.0 |\
mean | 0.934285714286 |\
std | 0.105783427849 |\
min | 0.6 |\
25% | 0.8 |\
50% | 1.0 |\
75% | 1.0 |\
max | 1.0 |

normaltest\
NormaltestResult(statistic=30.683850175565183, pvalue=2.173134430069827e-07)

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

normaltest\
NormaltestResult(statistic=55.867295667147665, pvalue=7.3887485384486275e-13)

##### ('burger', 2)

count | 22.0 |\
mean | 0.963636363636 |\
std | 0.0789542033952 |\
min | 0.8 |\
25% | 1.0 |\
50% | 1.0 |\
75% | 1.0 |\
max | 1.0 |

normaltest\
NormaltestResult(statistic=11.761207015205065, pvalue=0.0027930991097338811)

##### ('burger', 3)

count | 22.0 |\
mean | 0.963636363636 |\
std | 0.0789542033952 |\
min | 0.8 |\
25% | 1.0 |\
50% | 1.0 |\
75% | 1.0 |\
max | 1.0 |

normaltest\
NormaltestResult(statistic=11.761207015205118, pvalue=0.002793099109733807)

##### ('burger', 4)

count | 22.0 |\
mean | 0.981818181818 |\
std | 0.0588489886336 |\
min | 0.8 |\
25% | 1.0 |\
50% | 1.0 |\
75% | 1.0 |\
max | 1.0 |

normaltest\
NormaltestResult(statistic=32.977747192506733, pvalue=6.9019718607633975e-08)

##### ('burger', 5)

count | 22.0 |\
mean | 0.990909090909 |\
std | 0.0426401432711 |\
min | 0.8 |\
25% | 1.0 |\
50% | 1.0 |\
75% | 1.0 |\
max | 1.0 |

normaltest\
NormaltestResult(statistic=55.867295667147665, pvalue=7.3887485384486275e-13)

##### ('swipe', 1)

count | 28.0 |\
mean | 0.978571428571 |\
std | 0.0629940788349 |\
min | 0.8 |\
25% | 1.0 |\
50% | 1.0 |\
75% | 1.0 |\
max | 1.0 |

normaltest\
NormaltestResult(statistic=30.230322102932696, pvalue=2.7262706131404123e-07)

##### ('swipe', 2)

count | 28.0 |\
mean | 0.935714285714 |\
std | 0.0951189731211 |\
min | 0.8 |\
25% | 0.8 |\
50% | 1.0 |\
75% | 1.0 |\
max | 1.0 |

normaltest\
NormaltestResult(statistic=13.850854641882318, pvalue=0.0009824831927910632)

##### ('swipe', 3)

count | 28.0 |\
mean | 0.892857142857 |\
std | 0.138586973437 |\
min | 0.6 |\
25% | 0.8 |\
50% | 1.0 |\
75% | 1.0 |\
max | 1.0 |

normaltest\
NormaltestResult(statistic=4.3703066280619502, pvalue=0.11246049056138591)

##### ('swipe', 4)

count | 28.0 |\
mean | 0.942857142857 |\
std | 0.0920087412456 |\
min | 0.8 |\
25% | 0.8 |\
50% | 1.0 |\
75% | 1.0 |\
max | 1.0 |

normaltest\
NormaltestResult(statistic=8.1469969468004297, pvalue=0.017017748104058518)

##### ('swipe', 5)

count | 28.0 |\
mean | 0.921428571429 |\
std | 0.113389341903 |\
min | 0.6 |\
25% | 0.8 |\
50% | 1.0 |\
75% | 1.0 |\
max | 1.0 |

normaltest\
NormaltestResult(statistic=6.1681726236411034, pvalue=0.045771835985766236)

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

normaltest\
NormaltestResult(statistic=153.41323829366706, pvalue=4.861145039338043e-34)

###### swipe

count | 140.0 |\
mean | 6.83571428571 |\
std | 0.458504203722 |\
min | 5.0 |\
25% | 7.0 |\
50% | 7.0 |\
75% | 7.0 |\
max | 7.0 |

normaltest\
NormaltestResult(statistic=101.53235210749389, pvalue=8.9645784582099588e-23)

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

normaltest\
NormaltestResult(statistic=1.0828149152562685, pvalue=0.58192863582398746)

###### ('burger', 2)

count | 22.0 |\
mean | 6.90909090909 |\
std | 0.294244943168 |\
min | 6.0 |\
25% | 7.0 |\
50% | 7.0 |\
75% | 7.0 |\
max | 7.0 |

normaltest\
NormaltestResult(statistic=32.977747192506648, pvalue=6.901971860763698e-08)

###### ('burger', 3)

count | 22.0 |\
mean | 6.77272727273 |\
std | 0.751621623515 |\
min | 4.0 |\
25% | 7.0 |\
50% | 7.0 |\
75% | 7.0 |\
max | 7.0 |

normaltest\
NormaltestResult(statistic=37.132620570418851, pvalue=8.6447789726675352e-09)

###### ('burger', 4)

count | 22.0 |\
mean | 6.90909090909 |\
std | 0.294244943168 |\
min | 6.0 |\
25% | 7.0 |\
50% | 7.0 |\
75% | 7.0 |\
max | 7.0 |

normaltest\
NormaltestResult(statistic=32.977747192506648, pvalue=6.901971860763698e-08)

###### ('burger', 5)

count | 22.0 |\
mean | 6.95454545455 |\
std | 0.213200716356 |\
min | 6.0 |\
25% | 7.0 |\
50% | 7.0 |\
75% | 7.0 |\
max | 7.0 |

normaltest\
NormaltestResult(statistic=55.867295667147516, pvalue=7.3887485384492e-13)

###### ('swipe', 1)

count | 28.0 |\
mean | 6.85714285714 |\
std | 0.448395139423 |\
min | 5.0 |\
25% | 7.0 |\
50% | 7.0 |\
75% | 7.0 |\
max | 7.0 |

normaltest\
NormaltestResult(statistic=43.18815831051505, pvalue=4.1861094680904202e-10)

###### ('swipe', 2)

count | 28.0 |\
mean | 6.92857142857 |\
std | 0.262265264156 |\
min | 6.0 |\
25% | 7.0 |\
50% | 7.0 |\
75% | 7.0 |\
max | 7.0 |

normaltest\
NormaltestResult(statistic=44.203532340976452, pvalue=2.5195612001886847e-10)

###### ('swipe', 3)

count | 28.0 |\
mean | 6.82142857143 |\
std | 0.475594865606 |\
min | 5.0 |\
25% | 7.0 |\
50% | 7.0 |\
75% | 7.0 |\
max | 7.0 |

normaltest\
NormaltestResult(statistic=34.427175981240801, pvalue=3.3437494037083985e-08)

###### ('swipe', 4)

count | 28.0 |\
mean | 6.82142857143 |\
std | 0.475594865606 |\
min | 5.0 |\
25% | 7.0 |\
50% | 7.0 |\
75% | 7.0 |\
max | 7.0 |

normaltest\
NormaltestResult(statistic=34.427175981240801, pvalue=3.3437494037083985e-08)

###### ('swipe', 5)

count | 28.0 |\
mean | 6.75 |\
std | 0.585314097381 |\
min | 5.0 |\
25% | 7.0 |\
50% | 7.0 |\
75% | 7.0 |\
max | 7.0 |

normaltest\
NormaltestResult(statistic=24.938342419703677, pvalue=3.843330652607647e-06)

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

normaltest\
NormaltestResult(statistic=41.10183363779808, pvalue=1.1880924265582291e-09)

###### swipe

count | 140.0 |\
mean | 2.86428571429 |\
std | 2.12964925773 |\
min | 1.0 |\
25% | 1.0 |\
50% | 2.0 |\
75% | 4.0 |\
max | 7.0 |

normaltest\
NormaltestResult(statistic=18.788553344848623, pvalue=8.3198879945244137e-05)

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

normaltest\
NormaltestResult(statistic=14.852104558574464, pvalue=0.00059553387888821891)

###### ('burger', 2)

count | 22.0 |\
mean | 1.77272727273 |\
std | 1.87545088374 |\
min | 1.0 |\
25% | 1.0 |\
50% | 1.0 |\
75% | 1.0 |\
max | 7.0 |

normaltest\
NormaltestResult(statistic=20.210686165265589, pvalue=4.08606491047461e-05)

###### ('burger', 3)

count | 22.0 |\
mean | 2.0 |\
std | 1.74574312189 |\
min | 1.0 |\
25% | 1.0 |\
50% | 1.0 |\
75% | 2.0 |\
max | 6.0 |

normaltest\
NormaltestResult(statistic=9.2076296409072071, pvalue=0.010013562844574659)

###### ('burger', 4)

count | 22.0 |\
mean | 1.77272727273 |\
std | 1.54092792643 |\
min | 1.0 |\
25% | 1.0 |\
50% | 1.0 |\
75% | 1.0 |\
max | 6.0 |

normaltest\
NormaltestResult(statistic=13.258524513028126, pvalue=0.0013211373870855303)

###### ('burger', 5)

count | 22.0 |\
mean | 1.95454545455 |\
std | 1.98751514465 |\
min | 1.0 |\
25% | 1.0 |\
50% | 1.0 |\
75% | 1.0 |\
max | 7.0 |

normaltest\
NormaltestResult(statistic=13.11454314032791, pvalue=0.0014197541301194895)

###### ('swipe', 1)

count | 28.0 |\
mean | 2.75 |\
std | 2.36682315602 |\
min | 1.0 |\
25% | 1.0 |\
50% | 1.0 |\
75% | 4.25 |\
max | 7.0 |

normaltest\
NormaltestResult(statistic=5.6255405651946386, pvalue=0.060038438357067736)

###### ('swipe', 2)

count | 28.0 |\
mean | 2.67857142857 |\
std | 2.21198036674 |\
min | 1.0 |\
25% | 1.0 |\
50% | 1.0 |\
75% | 4.0 |\
max | 7.0 |

normaltest\
NormaltestResult(statistic=4.9857181545995557, pvalue=0.082673259115518136)

###### ('swipe', 3)

count | 28.0 |\
mean | 2.82142857143 |\
std | 2.16116517662 |\
min | 1.0 |\
25% | 1.0 |\
50% | 2.0 |\
75% | 4.0 |\
max | 7.0 |

normaltest\
NormaltestResult(statistic=4.8948691150333712, pvalue=0.086515251945615837)

###### ('swipe', 4)

count | 28.0 |\
mean | 2.85714285714 |\
std | 1.87999774851 |\
min | 1.0 |\
25% | 1.0 |\
50% | 3.0 |\
75% | 4.0 |\
max | 7.0 |

normaltest\
NormaltestResult(statistic=3.2631829602951457, pvalue=0.19561800409388738)

###### ('swipe', 5)

count | 28.0 |\
mean | 3.21428571429 |\
std | 2.11445015806 |\
min | 1.0 |\
25% | 1.0 |\
50% | 3.0 |\
75% | 4.0 |\
max | 7.0 |

normaltest\
NormaltestResult(statistic=2.7864677335567007, pvalue=0.24827112927752484)

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

normaltest\
NormaltestResult(statistic=26.197588687579557, pvalue=2.0476979566055249e-06)

###### swipe

count | 28.0 |\
mean | 1.53571428571 |\
std | 1.29048204766 |\
min | 1.0 |\
25% | 1.0 |\
50% | 1.0 |\
75% | 1.25 |\
max | 7.0 |

normaltest\
NormaltestResult(statistic=43.488260518740518, pvalue=3.6028336850503621e-10)

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

normaltest\
NormaltestResult(statistic=4.9137570390411183, pvalue=0.085702051156163167)

###### swipe

count | 28.0 |\
mean | 1.67857142857 |\
std | 1.18801332542 |\
min | 1.0 |\
25% | 1.0 |\
50% | 1.0 |\
75% | 2.0 |\
max | 6.0 |

normaltest\
NormaltestResult(statistic=28.457743224410187, pvalue=6.6142342997665578e-07)

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

normaltest\
NormaltestResult(statistic=7.0141044989524168, pvalue=0.029985173100470022)

###### swipe

count | 28.0 |\
mean | 1.75 |\
std | 1.37773297418 |\
min | 1.0 |\
25% | 1.0 |\
50% | 1.0 |\
75% | 2.0 |\
max | 7.0 |

normaltest\
NormaltestResult(statistic=30.833945386464563, pvalue=2.0160153368124402e-07)

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

normaltest\
NormaltestResult(statistic=4.4344935502051488, pvalue=0.1089085461474571)

###### swipe

count | 28.0 |\
mean | 4.5 |\
std | 1.45296631451 |\
min | 1.0 |\
25% | 4.0 |\
50% | 4.0 |\
75% | 5.25 |\
max | 7.0 |

normaltest\
NormaltestResult(statistic=0.29622233841262957, pvalue=0.86233524448851595)

#### Global Burger vs Global Swipe Test (result)

##### burger vs swipe

Ttest\_indResult(statistic=1.4151306918873736, pvalue=0.16442349507017537)
