
# Analysis

## Preprocessing

* experiment_results.csv
* task_questionnaire_results.csv
* final_questionnaire_results.csv
* demographic_data_fixed.csv

Dropping Task ID 0 (Training)

Asserting Absolute Distance Values!

| Dataset Validation:
| dict_items([('pid', True)])

| Adding success column based on
| `opt_interactions == interactions`
| in order to measure effectiveness.

| Aggregating Task Groups

| Computing efficiency over task mean_success/time_ms

Using normality test: shapiro

## Demographics

### age

| count | 50.0 |
| mean | 24.1 |
| std | 2.90144228737 |
| min | 20.0 |
| 25% | 22.0 |
| 50% | 24.0 |
| 75% | 25.0 |
| max | 35.0 |

### sex

| ('f', 29)
| ('m', 21)

### job

| ('Agrarwissenschaften', 5)
| ('Agribusiness', 1)
| ('Betriebswirtschaftslehre', 1)
| ('Biochemie', 1)
| ('Biologie', 1)
| ('Ernährungs- und Verbraucherökonomie', 2)
| ('Finanzmathematik', 2)
| ('Informatik / Nachhilfelehrer', 1)
| ('Mathemathik / Chemie', 1)
| ('Mathemathik / Deutsch / Psychologie', 1)
| ('Mathemathik / Geologie', 1)
| ('Mathemathik / Geschichte', 1)
| ('Mathemathik / Philosophie', 1)
| ('Mathemathik / Physik', 1)
| ('Mathemathik / Sport', 1)
| ('Mathematik', 4)
| ('Mathematik / Informatik', 1)
| ('Mathematik / Spanisch', 1)
| ('Medizin', 1)
| ('Musikwissenschaft / Philosophie', 1)
| ('Physik', 1)
| ('Politikwissenschaft / Ur- und Frühgeschichte', 1)
| ('Psychologie', 4)
| ('Rechtswissenschaften', 1)
| ('Soziologie / Pädagogik', 1)
| ('Volkswirtschaftslehre', 3)
| ('Wirtschaftsinformatik', 6)
| ('Wirtschaftsingenieur', 2)
| ('Wirtschaftswissenschaften Profil: Handelslehrer', 1)

### smartphone

| ('None', 1)
| ('android', 37)
| ('nodroid', 12)

### comments

| ('Ich zweifle die Aussagekraft der Studie an, da die Navigation nur aus „Wischen nach links“ und „Wischen nach rechts“ besteht.', 1)
| ('Menü-Steuerung: nur 5/7 Steine da: Menü zum Ausklappen. besser: dauerhaft ausgeklappt - >1 Klick statt 2', 1)
| ('Samsung', 1)
| ('man könnte die Bedienung noch vereinfachen, indem man durch wischen von Tür zu Tür kann', 1)
| ('schön kurz :)', 1)

## Efficiency by Tasks

### Descriptions (efficiency)

#### Global Descriptions (efficiency)

##### burger

| count | 110.0 |
| mean | 0.000223055228972 |
| std | 5.00230406763e-05 |
| min | 6.8976220448e-05 |
| 25% | 0.000190058286882 |
| 50% | 0.00022691177807 |
| 75% | 0.00025700334919 |
| max | 0.000336157052575 |

| shapiro
| (0.982802152633667, 0.16857866942882538)

##### swipe

| count | 140.0 |
| mean | 0.000215488934466 |
| std | 0.000100837665235 |
| min | 7.83468808148e-05 |
| 25% | 0.000140770307033 |
| 50% | 0.000186047319425 |
| 75% | 0.000267820085532 |
| max | 0.000514986095375 |

| shapiro
| (0.8906473517417908, 9.997179084564323e-09)

#### Repeated measures (efficiency)

##### burger

| KruskalResult(statistic=21.228960676540432, pvalue=0.00028522628404656868)
| FriedmanchisquareResult(statistic=30.509090909090901, pvalue=3.8548715779974447e-06)

##### swipe

| KruskalResult(statistic=91.910160660008614, pvalue=5.1718364795390112e-19)
| FriedmanchisquareResult(statistic=80.628571428571377, pvalue=1.2818240657137304e-16)

#### Descriptions per tid (efficiency)

##### ('burger', 1)

| count | 22.0 |
| mean | 0.000259627939777 |
| std | 3.615089292e-05 |
| min | 0.000189458527528 |
| 25% | 0.000242800150862 |
| 50% | 0.000263092621632 |
| 75% | 0.000281021933116 |
| max | 0.000336157052575 |

| shapiro
| (0.9797267913818359, 0.9116690158843994)

##### ('burger', 2)

| count | 22.0 |
| mean | 0.000218885902709 |
| std | 6.17582924756e-05 |
| min | 6.8976220448e-05 |
| 25% | 0.000175369392634 |
| 50% | 0.000229429832866 |
| 75% | 0.000262567057042 |
| max | 0.000298650101541 |

| shapiro
| (0.9300148487091064, 0.12278413027524948)

##### ('burger', 3)

| count | 22.0 |
| mean | 0.000207954767299 |
| std | 5.01700789335e-05 |
| min | 9.04895484572e-05 |
| 25% | 0.000177580422745 |
| 50% | 0.000214082948414 |
| 75% | 0.000246063771629 |
| max | 0.000280033604032 |

| shapiro
| (0.9594278335571289, 0.47779956459999084)

##### ('burger', 4)

| count | 22.0 |
| mean | 0.000228578290867 |
| std | 4.45345887587e-05 |
| min | 0.000113259903163 |
| 25% | 0.00021190614273 |
| 50% | 0.000227615297646 |
| 75% | 0.000251743012241 |
| max | 0.000304284323272 |

| shapiro
| (0.957809567451477, 0.4463127553462982)

##### ('burger', 5)

| count | 22.0 |
| mean | 0.000200229244208 |
| std | 3.36254251422e-05 |
| min | 0.000144350135689 |
| 25% | 0.000177255912416 |
| 50% | 0.000196225661233 |
| 75% | 0.00022656990971 |
| max | 0.000255076012652 |

| shapiro
| (0.9565545916557312, 0.4229239225387573)

##### ('swipe', 1)

| count | 28.0 |
| mean | 0.000376411637958 |
| std | 8.26782359999e-05 |
| min | 0.000124738828079 |
| 25% | 0.000339208375025 |
| 50% | 0.000385810331212 |
| 75% | 0.00043554876804 |
| max | 0.000514986095375 |

| shapiro
| (0.9320521354675293, 0.06946226954460144)

##### ('swipe', 2)

| count | 28.0 |
| mean | 0.000235764444338 |
| std | 5.15833509387e-05 |
| min | 7.83468808148e-05 |
| 25% | 0.000214528622096 |
| 50% | 0.000250787488437 |
| 75% | 0.000270937446389 |
| max | 0.000305866519851 |

| shapiro
| (0.8996769189834595, 0.011243239976465702)

##### ('swipe', 3)

| count | 28.0 |
| mean | 0.000176438327988 |
| std | 3.68031666814e-05 |
| min | 0.000106547333653 |
| 25% | 0.000149048762852 |
| 50% | 0.000183800941036 |
| 75% | 0.000207357536463 |
| max | 0.000233165454206 |

| shapiro
| (0.9592776298522949, 0.3351445198059082)

##### ('swipe', 4)

| count | 28.0 |
| mean | 0.000158462999373 |
| std | 3.21520787395e-05 |
| min | 8.88474267564e-05 |
| 25% | 0.000137780626155 |
| 50% | 0.000155438077528 |
| 75% | 0.000183456377089 |
| max | 0.000223483663344 |

| shapiro
| (0.9860241413116455, 0.9621396660804749)

##### ('swipe', 5)

| count | 28.0 |
| mean | 0.000130367262672 |
| std | 2.67090785385e-05 |
| min | 8.21186614658e-05 |
| 25% | 0.000120638250545 |
| 50% | 0.000128225214081 |
| 75% | 0.000143514673291 |
| max | 0.000182588372772 |

| shapiro
| (0.957489550113678, 0.303546667098999)

### Cross-compare Tests per tid (efficiency)

#### ('burger', 1) vs ('burger', 2)

{'n2': 22, 'N': 44, 'effect_size': 0.94675972197265923, 'n1': 22, 'test_result': Ttest_relResult(statistic=3.1400467644045076, pvalue=0.0049443978028402202)}

#### ('burger', 1) vs ('burger', 3)

{'n2': 22, 'N': 44, 'effect_size': 1.2011056601611565, 'n1': 22, 'test_result': Ttest_relResult(statistic=3.9836168083266799, pvalue=0.00067564806607191632)}

#### ('burger', 1) vs ('burger', 4)

{'n2': 22, 'N': 44, 'effect_size': 0.84922261727279102, 'n1': 22, 'test_result': Ttest_relResult(statistic=2.8165527849774343, pvalue=0.010338413955597585)}

#### ('burger', 1) vs ('burger', 5)

{'n2': 22, 'N': 44, 'effect_size': 2.6611888863322934, 'n1': 22, 'test_result': Ttest_relResult(statistic=8.8261650322279621, pvalue=1.6451903254595449e-08)}

#### ('burger', 1) vs ('swipe', 1)

{'n2': 28, 'N': 50, 'effect_size': -1.9097298327149146, 'n1': 22, 'test_result': Ttest_indResult(statistic=-6.7031245086454758, pvalue=5.6381782972874844e-08)}

#### ('burger', 1) vs ('swipe', 2)

{'n2': 28, 'N': 50, 'effect_size': 0.24350649350649356, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=233.0, pvalue=0.072691640416537293)}

#### ('burger', 1) vs ('swipe', 3)

{'n2': 28, 'N': 50, 'effect_size': 2.2829620500029861, 'n1': 22, 'test_result': Ttest_indResult(statistic=8.0131642746175658, pvalue=3.0036765567743514e-10)}

#### ('burger', 1) vs ('swipe', 4)

{'n2': 28, 'N': 50, 'effect_size': 2.9366881218094312, 'n1': 22, 'test_result': Ttest_indResult(statistic=10.307733474302086, pvalue=3.9626211595998718e-13)}

#### ('burger', 1) vs ('swipe', 5)

{'n2': 28, 'N': 50, 'effect_size': 3.9971846751859443, 'n1': 22, 'test_result': Ttest_indResult(statistic=14.030061269834484, pvalue=1.6751765716561832e-16)}

#### ('burger', 2) vs ('burger', 3)

{'n2': 22, 'N': 44, 'effect_size': 0.35440147919303427, 'n1': 22, 'test_result': Ttest_relResult(statistic=1.1754167316302409, pvalue=0.25298310480066266)}

#### ('burger', 2) vs ('burger', 4)

{'n2': 22, 'N': 44, 'effect_size': -0.27581681953294063, 'n1': 22, 'test_result': Ttest_relResult(statistic=-0.91478090125993228, pvalue=0.37069158497461718)}

#### ('burger', 2) vs ('burger', 5)

{'n2': 22, 'N': 44, 'effect_size': 0.51539165603199966, 'n1': 22, 'test_result': Ttest_relResult(statistic=1.7093607431380531, pvalue=0.10212210775377208)}

#### ('burger', 2) vs ('swipe', 1)

{'n2': 28, 'N': 50, 'effect_size': -2.1964344153980893, 'n1': 22, 'test_result': Ttest_indResult(statistic=-7.7094535097442671, pvalue=6.1460659425242285e-10)}

#### ('burger', 2) vs ('swipe', 2)

{'n2': 28, 'N': 50, 'effect_size': 0.14610389610389607, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=263.0, pvalue=0.19222905550361363)}

#### ('burger', 2) vs ('swipe', 3)

{'n2': 28, 'N': 50, 'effect_size': 0.81212695298602966, 'n1': 22, 'test_result': Ttest_indResult(statistic=2.8505540361974746, pvalue=0.007533072831137938)}

#### ('burger', 2) vs ('swipe', 4)

{'n2': 28, 'N': 50, 'effect_size': 1.1871061872924935, 'n1': 22, 'test_result': Ttest_indResult(statistic=4.1667258070177891, pvalue=0.00024295893165475523)}

#### ('burger', 2) vs ('swipe', 5)

{'n2': 28, 'N': 50, 'effect_size': 1.7884292636279993, 'n1': 22, 'test_result': Ttest_indResult(statistic=6.2773612390822437, pvalue=9.9419198495425703e-07)}

#### ('burger', 3) vs ('burger', 4)

{'n2': 22, 'N': 44, 'effect_size': -0.7374996248322695, 'n1': 22, 'test_result': Ttest_relResult(statistic=-2.4460095385965119, pvalue=0.023338332791632995)}

#### ('burger', 3) vs ('burger', 5)

{'n2': 22, 'N': 44, 'effect_size': 0.23656134754591943, 'n1': 22, 'test_result': Ttest_relResult(statistic=0.7845852297106759, pvalue=0.4414581754358432)}

#### ('burger', 3) vs ('swipe', 1)

{'n2': 28, 'N': 50, 'effect_size': -2.5346208780888531, 'n1': 22, 'test_result': Ttest_indResult(statistic=-8.8964831763080934, pvalue=1.6380584716166247e-11)}

#### ('burger', 3) vs ('swipe', 2)

{'n2': 28, 'N': 50, 'effect_size': 0.36038961038961037, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=197.0, pvalue=0.015401027053631673)}

#### ('burger', 3) vs ('swipe', 3)

{'n2': 28, 'N': 50, 'effect_size': 0.70376045931483799, 'n1': 22, 'test_result': Ttest_indResult(statistic=2.4701891870969703, pvalue=0.018195085242505141)}

#### ('burger', 3) vs ('swipe', 4)

{'n2': 28, 'N': 50, 'effect_size': 1.1462100107866364, 'n1': 22, 'test_result': Ttest_indResult(statistic=4.0231808100500297, pvalue=0.00030313523132897963)}

#### ('burger', 3) vs ('swipe', 5)

{'n2': 28, 'N': 50, 'effect_size': 1.8689406873961947, 'n1': 22, 'test_result': Ttest_indResult(statistic=6.5599551896199042, pvalue=2.8434885910251271e-07)}

#### ('burger', 4) vs ('burger', 5)

{'n2': 22, 'N': 44, 'effect_size': 0.84300225316077237, 'n1': 22, 'test_result': Ttest_relResult(statistic=2.7959221711584763, pvalue=0.010828183767257584)}

#### ('burger', 4) vs ('swipe', 1)

{'n2': 28, 'N': 50, 'effect_size': -2.3036145286208791, 'n1': 22, 'test_result': Ttest_indResult(statistic=-8.0856541803709217, pvalue=3.5438757244842358e-10)}

#### ('burger', 4) vs ('swipe', 2)

{'n2': 28, 'N': 50, 'effect_size': 0.14935064935064934, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=262.0, pvalue=0.18693288210180464)}

#### ('burger', 4) vs ('swipe', 3)

{'n2': 28, 'N': 50, 'effect_size': 1.2621200986811529, 'n1': 22, 'test_result': Ttest_indResult(statistic=4.4300235674155788, pvalue=6.9900388209405247e-05)}

#### ('burger', 4) vs ('swipe', 4)

{'n2': 28, 'N': 50, 'effect_size': 1.7720819828888696, 'n1': 22, 'test_result': Ttest_indResult(statistic=6.2199825165556186, pvalue=3.19607703847048e-07)}

#### ('burger', 4) vs ('swipe', 5)

{'n2': 28, 'N': 50, 'effect_size': 2.6020850201949859, 'n1': 22, 'test_result': Ttest_indResult(statistic=9.1332813540710038, pvalue=1.7051757569924614e-10)}

#### ('burger', 5) vs ('swipe', 1)

{'n2': 28, 'N': 50, 'effect_size': -2.9198423468617594, 'n1': 22, 'test_result': Ttest_indResult(statistic=-10.248605044204549, pvalue=2.0453619521585734e-12)}

#### ('burger', 5) vs ('swipe', 2)

{'n2': 28, 'N': 50, 'effect_size': 0.51623376623376616, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=149.0, pvalue=0.0009750243017655867)}

#### ('burger', 5) vs ('swipe', 3)

{'n2': 28, 'N': 50, 'effect_size': 0.67859393927802314, 'n1': 22, 'test_result': Ttest_indResult(statistic=2.3818550602659139, pvalue=0.0213390257262559)}

#### ('burger', 5) vs ('swipe', 4)

{'n2': 28, 'N': 50, 'effect_size': 1.2662092998006802, 'n1': 22, 'test_result': Ttest_indResult(statistic=4.4443766050942735, pvalue=5.8417405173783372e-05)}

#### ('burger', 5) vs ('swipe', 5)

{'n2': 28, 'N': 50, 'effect_size': 2.2701377982054174, 'n1': 22, 'test_result': Ttest_indResult(statistic=7.9681513334901197, pvalue=9.6399894615656428e-10)}

#### ('swipe', 1) vs ('swipe', 2)

{'n2': 28, 'N': 56, 'effect_size': 0.0019126554032515141, 'n1': 28, 'test_result': WilcoxonResult(statistic=3.0, pvalue=5.2564133258508337e-06)}

#### ('swipe', 1) vs ('swipe', 3)

{'n2': 28, 'N': 56, 'effect_size': 3.4860559225484686, 'n1': 28, 'test_result': Ttest_relResult(statistic=13.043626893310524, pvalue=3.5969964456561752e-13)}

#### ('swipe', 1) vs ('swipe', 4)

{'n2': 28, 'N': 56, 'effect_size': 3.8799222428390125, 'n1': 28, 'test_result': Ttest_relResult(statistic=14.517339720027108, pvalue=2.8328302970398919e-14)}

#### ('swipe', 1) vs ('swipe', 5)

{'n2': 28, 'N': 56, 'effect_size': 4.5968919124502001, 'n1': 28, 'test_result': Ttest_relResult(statistic=17.199994580420682, pvalue=4.4867434987762781e-16)}

#### ('swipe', 2) vs ('swipe', 3)

{'n2': 28, 'N': 56, 'effect_size': 0.01912655403251514, 'n1': 28, 'test_result': WilcoxonResult(statistic=30.0, pvalue=8.1666493089205386e-05)}

#### ('swipe', 2) vs ('swipe', 4)

{'n2': 28, 'N': 56, 'effect_size': 0.010200828817341408, 'n1': 28, 'test_result': WilcoxonResult(statistic=16.0, pvalue=2.0602777134809463e-05)}

#### ('swipe', 2) vs ('swipe', 5)

{'n2': 28, 'N': 56, 'effect_size': 0.0031877590054191903, 'n1': 28, 'test_result': WilcoxonResult(statistic=5.0, pvalue=6.5213205645443688e-06)}

#### ('swipe', 3) vs ('swipe', 4)

{'n2': 28, 'N': 56, 'effect_size': 0.5606349854006033, 'n1': 28, 'test_result': Ttest_relResult(statistic=2.0977040344080682, pvalue=0.045427484584555158)}

#### ('swipe', 3) vs ('swipe', 5)

{'n2': 28, 'N': 56, 'effect_size': 1.3561910948601303, 'n1': 28, 'test_result': Ttest_relResult(statistic=5.0744024279604458, pvalue=2.493775482784069e-05)}

#### ('swipe', 4) vs ('swipe', 5)

{'n2': 28, 'N': 56, 'effect_size': 1.104446011408412, 'n1': 28, 'test_result': Ttest_relResult(statistic=4.1324585768793014, pvalue=0.00031147549191696031)}

### Global Burger vs Swipe per tid Tests (efficiency)

#### burger vs swipe 1

{'n2': 28, 'N': 138, 'effect_size': -1.9870466939513425, 'n1': 110, 'test_result': Ttest_indResult(statistic=-9.3873689639224196, pvalue=9.7956596089962241e-11)}

#### burger vs swipe 2

{'n2': 28, 'N': 138, 'effect_size': 0.18571428571428572, 'n1': 110, 'test_result': MannwhitneyuResult(statistic=1254.0, pvalue=0.065327534078559346)}

#### burger vs swipe 3

{'n2': 28, 'N': 138, 'effect_size': 1.1700510299170295, 'n1': 110, 'test_result': Ttest_indResult(statistic=5.5276510400502676, pvalue=9.0622300016679275e-07)}

#### burger vs swipe 4

{'n2': 28, 'N': 138, 'effect_size': 1.770000563266015, 'n1': 110, 'test_result': Ttest_indResult(statistic=8.3619818317845045, pvalue=7.0554228434671516e-12)}

#### burger vs swipe 5

{'n2': 28, 'N': 138, 'effect_size': 2.8251881603681559, 'n1': 110, 'test_result': Ttest_indResult(statistic=13.346985621733221, pvalue=3.9194832679580957e-22)}

### Global Burger vs Global Swipe Test (efficiency)

#### burger vs swipe

{'n2': 140, 'N': 250, 'effect_size': 0.2218181818181818, 'n1': 110, 'test_result': MannwhitneyuResult(statistic=5992.0, pvalue=0.0013125763723938479)}

## Task Questionnaires

### Task Question 0

#### Descriptions (result)

##### Global Descriptions (result)

###### burger

| count | 110.0 |
| mean | 6.90909090909 |
| std | 0.395976427467 |
| min | 4.0 |
| 25% | 7.0 |
| 50% | 7.0 |
| 75% | 7.0 |
| max | 7.0 |

| shapiro
| (0.24518823623657227, 2.9252628439826945e-21)

###### swipe

| count | 140.0 |
| mean | 6.83571428571 |
| std | 0.458504203722 |
| min | 5.0 |
| 25% | 7.0 |
| 50% | 7.0 |
| 75% | 7.0 |
| max | 7.0 |

| shapiro
| (0.39919018745422363, 1.5329055243220379e-21)

##### Repeated measures (result)

###### burger

| KruskalResult(statistic=2.4526192106750853, pvalue=0.65313967433502973)
| FriedmanchisquareResult(statistic=3.3103448275862144, pvalue=0.50729488262873967)

###### swipe

| KruskalResult(statistic=1.7694225721785437, pvalue=0.77807166799688021)
| FriedmanchisquareResult(statistic=5.0958904109588801, pvalue=0.27759929640181424)

##### Descriptions per tid (result)

###### ('burger', 1)

| count | 22.0 |
| mean | 7.0 |
| std | 0.0 |
| min | 7.0 |
| 25% | 7.0 |
| 50% | 7.0 |
| 75% | 7.0 |
| max | 7.0 |

| shapiro
| (1.0, 1.0)

###### ('burger', 2)

| count | 22.0 |
| mean | 6.90909090909 |
| std | 0.294244943168 |
| min | 6.0 |
| 25% | 7.0 |
| 50% | 7.0 |
| 75% | 7.0 |
| max | 7.0 |

| shapiro
| (0.3322211503982544, 4.875188253095075e-09)

###### ('burger', 3)

| count | 22.0 |
| mean | 6.77272727273 |
| std | 0.751621623515 |
| min | 4.0 |
| 25% | 7.0 |
| 50% | 7.0 |
| 75% | 7.0 |
| max | 7.0 |

| shapiro
| (0.3419651389122009, 5.8100124711302215e-09)

###### ('burger', 4)

| count | 22.0 |
| mean | 6.90909090909 |
| std | 0.294244943168 |
| min | 6.0 |
| 25% | 7.0 |
| 50% | 7.0 |
| 75% | 7.0 |
| max | 7.0 |

| shapiro
| (0.3322211503982544, 4.875188253095075e-09)

###### ('burger', 5)

| count | 22.0 |
| mean | 6.95454545455 |
| std | 0.213200716356 |
| min | 6.0 |
| 25% | 7.0 |
| 50% | 7.0 |
| 75% | 7.0 |
| max | 7.0 |

| shapiro
| (0.22147256135940552, 7.41695094230721e-10)

###### ('swipe', 1)

| count | 28.0 |
| mean | 6.85714285714 |
| std | 0.448395139423 |
| min | 5.0 |
| 25% | 7.0 |
| 50% | 7.0 |
| 75% | 7.0 |
| max | 7.0 |

| shapiro
| (0.365678608417511, 6.050620560138498e-10)

###### ('swipe', 2)

| count | 28.0 |
| mean | 6.92857142857 |
| std | 0.262265264156 |
| min | 6.0 |
| 25% | 7.0 |
| 50% | 7.0 |
| 75% | 7.0 |
| max | 7.0 |

| shapiro
| (0.2873581051826477, 1.3197647141804936e-10)

###### ('swipe', 3)

| count | 28.0 |
| mean | 6.82142857143 |
| std | 0.475594865606 |
| min | 5.0 |
| 25% | 7.0 |
| 50% | 7.0 |
| 75% | 7.0 |
| max | 7.0 |

| shapiro
| (0.43253177404403687, 2.463778070449507e-09)

###### ('swipe', 4)

| count | 28.0 |
| mean | 6.82142857143 |
| std | 0.475594865606 |
| min | 5.0 |
| 25% | 7.0 |
| 50% | 7.0 |
| 75% | 7.0 |
| max | 7.0 |

| shapiro
| (0.43253177404403687, 2.463778070449507e-09)

###### ('swipe', 5)

| count | 28.0 |
| mean | 6.75 |
| std | 0.585314097381 |
| min | 5.0 |
| 25% | 7.0 |
| 50% | 7.0 |
| 75% | 7.0 |
| max | 7.0 |

| shapiro
| (0.48425883054733276, 7.892020370547925e-09)

#### Cross-compare Tests per tid (result)

##### ('burger', 1) vs ('burger', 2)

{'n2': 22, 'N': 44, 'effect_size': 0.0, 'n1': 22, 'test_result': WilcoxonResult(statistic=0.0, pvalue=0.15729920705028502)}

##### ('burger', 1) vs ('burger', 3)

{'n2': 22, 'N': 44, 'effect_size': 0.0, 'n1': 22, 'test_result': WilcoxonResult(statistic=0.0, pvalue=0.17971249487899976)}

##### ('burger', 1) vs ('burger', 4)

{'n2': 22, 'N': 44, 'effect_size': 0.0, 'n1': 22, 'test_result': WilcoxonResult(statistic=0.0, pvalue=0.15729920705028502)}

##### ('burger', 1) vs ('burger', 5)

{'n2': 22, 'N': 44, 'effect_size': 0.0, 'n1': 22, 'test_result': WilcoxonResult(statistic=0.0, pvalue=0.31731050786291415)}

##### ('burger', 1) vs ('swipe', 1)

{'n2': 28, 'N': 50, 'effect_size': 0.1071428571428571, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=275.0, pvalue=0.061389171314485569)}

##### ('burger', 1) vs ('swipe', 2)

{'n2': 28, 'N': 50, 'effect_size': 0.071428571428571397, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=286.0, pvalue=0.10790037602663682)}

##### ('burger', 1) vs ('swipe', 3)

{'n2': 28, 'N': 50, 'effect_size': 0.1428571428571429, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=264.0, pvalue=0.035323810007342034)}

##### ('burger', 1) vs ('swipe', 4)

{'n2': 28, 'N': 50, 'effect_size': 0.1428571428571429, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=264.0, pvalue=0.035323810007342034)}

##### ('burger', 1) vs ('swipe', 5)

{'n2': 28, 'N': 50, 'effect_size': 0.1785714285714286, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=253.0, pvalue=0.020341356769343476)}

##### ('burger', 2) vs ('burger', 3)

{'n2': 22, 'N': 44, 'effect_size': 0.0030975735673722249, 'n1': 22, 'test_result': WilcoxonResult(statistic=3.0, pvalue=0.46145098783336069)}

##### ('burger', 2) vs ('burger', 4)

{'n2': 22, 'N': 44, 'effect_size': 0.0051626226122870418, 'n1': 22, 'test_result': WilcoxonResult(statistic=5.0, pvalue=1.0)}

##### ('burger', 2) vs ('burger', 5)

{'n2': 22, 'N': 44, 'effect_size': 0.0020650490449148169, 'n1': 22, 'test_result': WilcoxonResult(statistic=2.0, pvalue=0.5637028616507731)}

##### ('burger', 2) vs ('swipe', 1)

{'n2': 28, 'N': 50, 'effect_size': 0.019480519480519431, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=302.0, pvalue=0.41814383343092509)}

##### ('burger', 2) vs ('swipe', 2)

{'n2': 28, 'N': 50, 'effect_size': 0.019480519480519431, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=302.0, pvalue=0.40954587077471732)}

##### ('burger', 2) vs ('swipe', 3)

{'n2': 28, 'N': 50, 'effect_size': 0.055194805194805241, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=291.0, pvalue=0.28360268156813595)}

##### ('burger', 2) vs ('swipe', 4)

{'n2': 28, 'N': 50, 'effect_size': 0.055194805194805241, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=291.0, pvalue=0.28360268156813595)}

##### ('burger', 2) vs ('swipe', 5)

{'n2': 28, 'N': 50, 'effect_size': 0.094155844155844104, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=279.0, pvalue=0.1776214834950835)}

##### ('burger', 3) vs ('burger', 4)

{'n2': 22, 'N': 44, 'effect_size': 0.0015487867836861124, 'n1': 22, 'test_result': WilcoxonResult(statistic=1.5, pvalue=0.41421617824252521)}

##### ('burger', 3) vs ('burger', 5)

{'n2': 22, 'N': 44, 'effect_size': 0.0, 'n1': 22, 'test_result': WilcoxonResult(statistic=0.0, pvalue=0.17971249487899976)}

##### ('burger', 3) vs ('swipe', 1)

{'n2': 28, 'N': 50, 'effect_size': 0.008116883116883078, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=305.5, pvalue=0.47007151426311133)}

##### ('burger', 3) vs ('swipe', 2)

{'n2': 28, 'N': 50, 'effect_size': 0.025974025974025983, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=300.0, pvalue=0.37768095297605236)}

##### ('burger', 3) vs ('swipe', 3)

{'n2': 28, 'N': 50, 'effect_size': 0.040584415584415612, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=295.5, pvalue=0.3388315325050939)}

##### ('burger', 3) vs ('swipe', 4)

{'n2': 28, 'N': 50, 'effect_size': 0.040584415584415612, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=295.5, pvalue=0.3388315325050939)}

##### ('burger', 3) vs ('swipe', 5)

{'n2': 28, 'N': 50, 'effect_size': 0.074675324675324672, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=285.0, pvalue=0.23293475501797717)}

##### ('burger', 4) vs ('burger', 5)

{'n2': 22, 'N': 44, 'effect_size': 0.0, 'n1': 22, 'test_result': WilcoxonResult(statistic=0.0, pvalue=0.31731050786291415)}

##### ('burger', 4) vs ('swipe', 1)

{'n2': 28, 'N': 50, 'effect_size': 0.019480519480519431, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=302.0, pvalue=0.41814383343092509)}

##### ('burger', 4) vs ('swipe', 2)

{'n2': 28, 'N': 50, 'effect_size': 0.019480519480519431, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=302.0, pvalue=0.40954587077471732)}

##### ('burger', 4) vs ('swipe', 3)

{'n2': 28, 'N': 50, 'effect_size': 0.055194805194805241, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=291.0, pvalue=0.28360268156813595)}

##### ('burger', 4) vs ('swipe', 4)

{'n2': 28, 'N': 50, 'effect_size': 0.055194805194805241, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=291.0, pvalue=0.28360268156813595)}

##### ('burger', 4) vs ('swipe', 5)

{'n2': 28, 'N': 50, 'effect_size': 0.094155844155844104, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=279.0, pvalue=0.1776214834950835)}

##### ('burger', 5) vs ('swipe', 1)

{'n2': 28, 'N': 50, 'effect_size': 0.063311688311688319, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=288.5, pvalue=0.21488485789583234)}

##### ('burger', 5) vs ('swipe', 2)

{'n2': 28, 'N': 50, 'effect_size': 0.025974025974025983, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=300.0, pvalue=0.36081607462259746)}

##### ('burger', 5) vs ('swipe', 3)

{'n2': 28, 'N': 50, 'effect_size': 0.099025974025974017, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=277.5, pvalue=0.12983938884427548)}

##### ('burger', 5) vs ('swipe', 4)

{'n2': 28, 'N': 50, 'effect_size': 0.099025974025974017, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=277.5, pvalue=0.12983938884427548)}

##### ('burger', 5) vs ('swipe', 5)

{'n2': 28, 'N': 50, 'effect_size': 0.13636363636363635, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=266.0, pvalue=0.07519977300947886)}

##### ('swipe', 1) vs ('swipe', 2)

{'n2': 28, 'N': 56, 'effect_size': 0.00095632770162575704, 'n1': 28, 'test_result': WilcoxonResult(statistic=1.5, pvalue=0.41421617824252521)}

##### ('swipe', 1) vs ('swipe', 3)

{'n2': 28, 'N': 56, 'effect_size': 0.0012751036021676761, 'n1': 28, 'test_result': WilcoxonResult(statistic=2.0, pvalue=0.5637028616507731)}

##### ('swipe', 1) vs ('swipe', 4)

{'n2': 28, 'N': 56, 'effect_size': 0.0012751036021676761, 'n1': 28, 'test_result': WilcoxonResult(statistic=2.0, pvalue=0.5637028616507731)}

##### ('swipe', 1) vs ('swipe', 5)

{'n2': 28, 'N': 56, 'effect_size': 0.0, 'n1': 28, 'test_result': WilcoxonResult(statistic=0.0, pvalue=0.083264516663550406)}

##### ('swipe', 2) vs ('swipe', 3)

{'n2': 28, 'N': 56, 'effect_size': 0.0012751036021676761, 'n1': 28, 'test_result': WilcoxonResult(statistic=2.0, pvalue=0.25683925795785656)}

##### ('swipe', 2) vs ('swipe', 4)

{'n2': 28, 'N': 56, 'effect_size': 0.0012751036021676761, 'n1': 28, 'test_result': WilcoxonResult(statistic=2.0, pvalue=0.25683925795785656)}

##### ('swipe', 2) vs ('swipe', 5)

{'n2': 28, 'N': 56, 'effect_size': 0.0, 'n1': 28, 'test_result': WilcoxonResult(statistic=0.0, pvalue=0.058781721355358862)}

##### ('swipe', 3) vs ('swipe', 4)

{'n2': 28, 'N': 56, 'effect_size': '=== All pairs were equal ===', 'n1': 28, 'test_result': '=== All pairs were equal ==='}

##### ('swipe', 3) vs ('swipe', 5)

{'n2': 28, 'N': 56, 'effect_size': 0.00095632770162575704, 'n1': 28, 'test_result': WilcoxonResult(statistic=1.5, pvalue=0.41421617824252521)}

##### ('swipe', 4) vs ('swipe', 5)

{'n2': 28, 'N': 56, 'effect_size': 0.00095632770162575704, 'n1': 28, 'test_result': WilcoxonResult(statistic=1.5, pvalue=0.41421617824252521)}

#### Global Burger vs Swipe per tid Tests (result)

##### burger vs swipe 1

{'n2': 28, 'N': 138, 'effect_size': 0.043506493506493493, 'n1': 110, 'test_result': MannwhitneyuResult(statistic=1473.0, pvalue=0.21665236926243431)}

##### burger vs swipe 2

{'n2': 28, 'N': 138, 'effect_size': 0.0064935064935064402, 'n1': 110, 'test_result': MannwhitneyuResult(statistic=1530.0, pvalue=0.45320928415997419)}

##### burger vs swipe 3

{'n2': 28, 'N': 138, 'effect_size': 0.078571428571428625, 'n1': 110, 'test_result': MannwhitneyuResult(statistic=1419.0, pvalue=0.087083010808927386)}

##### burger vs swipe 4

{'n2': 28, 'N': 138, 'effect_size': 0.078571428571428625, 'n1': 110, 'test_result': MannwhitneyuResult(statistic=1419.0, pvalue=0.087083010808927386)}

##### burger vs swipe 5

{'n2': 28, 'N': 138, 'effect_size': 0.11558441558441557, 'n1': 110, 'test_result': MannwhitneyuResult(statistic=1362.0, pvalue=0.027199345369874211)}

#### Global Burger vs Global Swipe Test (result)

##### burger vs swipe

{'n2': 140, 'N': 250, 'effect_size': 0.064545454545454573, 'n1': 110, 'test_result': MannwhitneyuResult(statistic=7203.0, pvalue=0.046318608676750285)}

### Task Question 1

#### Descriptions (result)

##### Global Descriptions (result)

###### burger

| count | 110.0 |
| mean | 1.89090909091 |
| std | 1.80897585981 |
| min | 1.0 |
| 25% | 1.0 |
| 50% | 1.0 |
| 75% | 1.0 |
| max | 7.0 |

| shapiro
| (0.5440710783004761, 6.783648646543276e-17)

###### swipe

| count | 140.0 |
| mean | 2.86428571429 |
| std | 2.12964925773 |
| min | 1.0 |
| 25% | 1.0 |
| 50% | 2.0 |
| 75% | 4.0 |
| max | 7.0 |

| shapiro
| (0.799676775932312, 1.4816165872302833e-12)

##### Repeated measures (result)

###### burger

| KruskalResult(statistic=0.78069084963312274, pvalue=0.94101782074422269)
| FriedmanchisquareResult(statistic=2.7575757575757125, pvalue=0.59917784877228941)

###### swipe

| KruskalResult(statistic=2.0615941350657225, pvalue=0.72443103796977781)
| FriedmanchisquareResult(statistic=5.4968553459119409, pvalue=0.24000603548291879)

##### Descriptions per tid (result)

###### ('burger', 1)

| count | 22.0 |
| mean | 1.95454545455 |
| std | 2.01133153544 |
| min | 1.0 |
| 25% | 1.0 |
| 50% | 1.0 |
| 75% | 1.0 |
| max | 7.0 |

| shapiro
| (0.5299234390258789, 2.541320327509311e-07)

###### ('burger', 2)

| count | 22.0 |
| mean | 1.77272727273 |
| std | 1.87545088374 |
| min | 1.0 |
| 25% | 1.0 |
| 50% | 1.0 |
| 75% | 1.0 |
| max | 7.0 |

| shapiro
| (0.4611632227897644, 5.790687396256544e-08)

###### ('burger', 3)

| count | 22.0 |
| mean | 2.0 |
| std | 1.74574312189 |
| min | 1.0 |
| 25% | 1.0 |
| 50% | 1.0 |
| 75% | 2.0 |
| max | 6.0 |

| shapiro
| (0.6260440349578857, 2.5660463052190607e-06)

###### ('burger', 4)

| count | 22.0 |
| mean | 1.77272727273 |
| std | 1.54092792643 |
| min | 1.0 |
| 25% | 1.0 |
| 50% | 1.0 |
| 75% | 1.0 |
| max | 6.0 |

| shapiro
| (0.5682213306427002, 6.146745477053628e-07)

###### ('burger', 5)

| count | 22.0 |
| mean | 1.95454545455 |
| std | 1.98751514465 |
| min | 1.0 |
| 25% | 1.0 |
| 50% | 1.0 |
| 75% | 1.0 |
| max | 7.0 |

| shapiro
| (0.5327657461166382, 2.7092326604361006e-07)

###### ('swipe', 1)

| count | 28.0 |
| mean | 2.75 |
| std | 2.36682315602 |
| min | 1.0 |
| 25% | 1.0 |
| 50% | 1.0 |
| 75% | 4.25 |
| max | 7.0 |

| shapiro
| (0.7217938303947449, 5.8795612858375534e-06)

###### ('swipe', 2)

| count | 28.0 |
| mean | 2.67857142857 |
| std | 2.21198036674 |
| min | 1.0 |
| 25% | 1.0 |
| 50% | 1.0 |
| 75% | 4.0 |
| max | 7.0 |

| shapiro
| (0.7506808042526245, 1.617231646378059e-05)

###### ('swipe', 3)

| count | 28.0 |
| mean | 2.82142857143 |
| std | 2.16116517662 |
| min | 1.0 |
| 25% | 1.0 |
| 50% | 2.0 |
| 75% | 4.0 |
| max | 7.0 |

| shapiro
| (0.7865198850631714, 6.232791929505765e-05)

###### ('swipe', 4)

| count | 28.0 |
| mean | 2.85714285714 |
| std | 1.87999774851 |
| min | 1.0 |
| 25% | 1.0 |
| 50% | 3.0 |
| 75% | 4.0 |
| max | 7.0 |

| shapiro
| (0.8642818927764893, 0.0018409639596939087)

###### ('swipe', 5)

| count | 28.0 |
| mean | 3.21428571429 |
| std | 2.11445015806 |
| min | 1.0 |
| 25% | 1.0 |
| 50% | 3.0 |
| 75% | 4.0 |
| max | 7.0 |

| shapiro
| (0.8491970896720886, 0.0009006079635582864)

#### Cross-compare Tests per tid (result)

##### ('burger', 1) vs ('burger', 2)

{'n2': 22, 'N': 44, 'effect_size': 0.0077439339184305631, 'n1': 22, 'test_result': WilcoxonResult(statistic=7.5, pvalue=1.0)}

##### ('burger', 1) vs ('burger', 3)

{'n2': 22, 'N': 44, 'effect_size': 0.014455343314403717, 'n1': 22, 'test_result': WilcoxonResult(statistic=14.0, pvalue=0.56869370493349436)}

##### ('burger', 1) vs ('burger', 4)

{'n2': 22, 'N': 44, 'effect_size': 0.0061951471347444498, 'n1': 22, 'test_result': WilcoxonResult(statistic=6.0, pvalue=0.68027954733445029)}

##### ('burger', 1) vs ('burger', 5)

{'n2': 22, 'N': 44, 'effect_size': 0.0051626226122870418, 'n1': 22, 'test_result': WilcoxonResult(statistic=5.0, pvalue=1.0)}

##### ('burger', 1) vs ('swipe', 1)

{'n2': 28, 'N': 50, 'effect_size': 0.1964285714285714, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=247.5, pvalue=0.082098002975044604)}

##### ('burger', 1) vs ('swipe', 2)

{'n2': 28, 'N': 50, 'effect_size': 0.21590909090909094, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=241.5, pvalue=0.066396878662638464)}

##### ('burger', 1) vs ('swipe', 3)

{'n2': 28, 'N': 50, 'effect_size': 0.30681818181818177, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=213.5, pvalue=0.020092875062028004)}

##### ('burger', 1) vs ('swipe', 4)

{'n2': 28, 'N': 50, 'effect_size': 0.35551948051948057, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=198.5, pvalue=0.010019521264436585)}

##### ('burger', 1) vs ('swipe', 5)

{'n2': 28, 'N': 50, 'effect_size': 0.37662337662337664, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=192.0, pvalue=0.0068101408106697112)}

##### ('burger', 2) vs ('burger', 3)

{'n2': 22, 'N': 44, 'effect_size': 0.0067114093959731542, 'n1': 22, 'test_result': WilcoxonResult(statistic=6.5, pvalue=0.39510806859049219)}

##### ('burger', 2) vs ('burger', 4)

{'n2': 22, 'N': 44, 'effect_size': 0.010841507485802787, 'n1': 22, 'test_result': WilcoxonResult(statistic=10.5, pvalue=1.0)}

##### ('burger', 2) vs ('burger', 5)

{'n2': 22, 'N': 44, 'effect_size': 0.0092927207021166747, 'n1': 22, 'test_result': WilcoxonResult(statistic=9.0, pvalue=0.73888268036352733)}

##### ('burger', 2) vs ('swipe', 1)

{'n2': 28, 'N': 50, 'effect_size': 0.24512987012987009, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=232.5, pvalue=0.038182542965196922)}

##### ('burger', 2) vs ('swipe', 2)

{'n2': 28, 'N': 50, 'effect_size': 0.2678571428571429, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=225.5, pvalue=0.028699028147674787)}

##### ('burger', 2) vs ('swipe', 3)

{'n2': 28, 'N': 50, 'effect_size': 0.36850649350649356, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=194.5, pvalue=0.0062373933525989578)}

##### ('burger', 2) vs ('swipe', 4)

{'n2': 28, 'N': 50, 'effect_size': 0.41720779220779225, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=179.5, pvalue=0.0028888514521789059)}

##### ('burger', 2) vs ('swipe', 5)

{'n2': 28, 'N': 50, 'effect_size': 0.43831168831168832, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=173.0, pvalue=0.001845925801493757)}

##### ('burger', 3) vs ('burger', 4)

{'n2': 22, 'N': 44, 'effect_size': 0.0092927207021166747, 'n1': 22, 'test_result': WilcoxonResult(statistic=9.0, pvalue=0.3885437838475907)}

##### ('burger', 3) vs ('burger', 5)

{'n2': 22, 'N': 44, 'effect_size': 0.013422818791946308, 'n1': 22, 'test_result': WilcoxonResult(statistic=13.0, pvalue=0.86456930168674195)}

##### ('burger', 3) vs ('swipe', 1)

{'n2': 28, 'N': 50, 'effect_size': 0.15422077922077926, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=260.5, pvalue=0.14603135541294709)}

##### ('burger', 3) vs ('swipe', 2)

{'n2': 28, 'N': 50, 'effect_size': 0.16883116883116878, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=256.0, pvalue=0.12750985422970523)}

##### ('burger', 3) vs ('swipe', 3)

{'n2': 28, 'N': 50, 'effect_size': 0.25324675324675328, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=230.0, pvalue=0.049115891184390158)}

##### ('burger', 3) vs ('swipe', 4)

{'n2': 28, 'N': 50, 'effect_size': 0.30194805194805197, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=215.0, pvalue=0.026326679220802538)}

##### ('burger', 3) vs ('swipe', 5)

{'n2': 28, 'N': 50, 'effect_size': 0.3392857142857143, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=203.5, pvalue=0.014613622667340618)}

##### ('burger', 4) vs ('burger', 5)

{'n2': 22, 'N': 44, 'effect_size': 0.0015487867836861124, 'n1': 22, 'test_result': WilcoxonResult(statistic=1.5, pvalue=0.19364643126922065)}

##### ('burger', 4) vs ('swipe', 1)

{'n2': 28, 'N': 50, 'effect_size': 0.22564935064935066, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=238.5, pvalue=0.054909704407618581)}

##### ('burger', 4) vs ('swipe', 2)

{'n2': 28, 'N': 50, 'effect_size': 0.24350649350649356, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=233.0, pvalue=0.044870412680933683)}

##### ('burger', 4) vs ('swipe', 3)

{'n2': 28, 'N': 50, 'effect_size': 0.3214285714285714, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=209.0, pvalue=0.015775210433546256)}

##### ('burger', 4) vs ('swipe', 4)

{'n2': 28, 'N': 50, 'effect_size': 0.375, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=192.5, pvalue=0.0070352388832014452)}

##### ('burger', 4) vs ('swipe', 5)

{'n2': 28, 'N': 50, 'effect_size': 0.40422077922077926, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=183.5, pvalue=0.0040067153811422793)}

##### ('burger', 5) vs ('swipe', 1)

{'n2': 28, 'N': 50, 'effect_size': 0.20129870129870131, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=246.0, pvalue=0.077014874525015403)}

##### ('burger', 5) vs ('swipe', 2)

{'n2': 28, 'N': 50, 'effect_size': 0.2191558441558441, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=240.5, pvalue=0.063535812872022673)}

##### ('burger', 5) vs ('swipe', 3)

{'n2': 28, 'N': 50, 'effect_size': 0.31331168831168832, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=211.5, pvalue=0.01809715117525822)}

##### ('burger', 5) vs ('swipe', 4)

{'n2': 28, 'N': 50, 'effect_size': 0.35551948051948057, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=198.5, pvalue=0.010033737896491264)}

##### ('burger', 5) vs ('swipe', 5)

{'n2': 28, 'N': 50, 'effect_size': 0.38149350649350644, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=190.5, pvalue=0.0062419441538161761)}

##### ('swipe', 1) vs ('swipe', 2)

{'n2': 28, 'N': 56, 'effect_size': 0.032196365954733824, 'n1': 28, 'test_result': WilcoxonResult(statistic=50.5, pvalue=0.89924291781309873)}

##### ('swipe', 1) vs ('swipe', 3)

{'n2': 28, 'N': 56, 'effect_size': 0.020720433535224736, 'n1': 28, 'test_result': WilcoxonResult(statistic=32.5, pvalue=0.34939652545601385)}

##### ('swipe', 1) vs ('swipe', 4)

{'n2': 28, 'N': 56, 'effect_size': 0.025820847943895442, 'n1': 28, 'test_result': WilcoxonResult(statistic=40.5, pvalue=0.44742990778151448)}

##### ('swipe', 1) vs ('swipe', 5)

{'n2': 28, 'N': 56, 'effect_size': 0.021676761236850493, 'n1': 28, 'test_result': WilcoxonResult(statistic=34.0, pvalue=0.13211241836284676)}

##### ('swipe', 2) vs ('swipe', 3)

{'n2': 28, 'N': 56, 'effect_size': 0.01912655403251514, 'n1': 28, 'test_result': WilcoxonResult(statistic=30.0, pvalue=0.4727619557115964)}

##### ('swipe', 2) vs ('swipe', 4)

{'n2': 28, 'N': 56, 'effect_size': 0.042715970672617148, 'n1': 28, 'test_result': WilcoxonResult(statistic=67.0, pvalue=0.6485210682667949)}

##### ('swipe', 2) vs ('swipe', 5)

{'n2': 28, 'N': 56, 'effect_size': 0.025183296142811604, 'n1': 28, 'test_result': WilcoxonResult(statistic=39.5, pvalue=0.1354274987516664)}

##### ('swipe', 3) vs ('swipe', 4)

{'n2': 28, 'N': 56, 'effect_size': 0.038253108065030281, 'n1': 28, 'test_result': WilcoxonResult(statistic=60.0, pvalue=0.66730491249962687)}

##### ('swipe', 3) vs ('swipe', 5)

{'n2': 28, 'N': 56, 'effect_size': 0.016576346828179791, 'n1': 28, 'test_result': WilcoxonResult(statistic=26.0, pvalue=0.16753962672004419)}

##### ('swipe', 4) vs ('swipe', 5)

{'n2': 28, 'N': 56, 'effect_size': 0.016576346828179791, 'n1': 28, 'test_result': WilcoxonResult(statistic=26.0, pvalue=0.30026522383277554)}

#### Global Burger vs Swipe per tid Tests (result)

##### burger vs swipe 1

{'n2': 28, 'N': 138, 'effect_size': 0.20454545454545459, 'n1': 110, 'test_result': MannwhitneyuResult(statistic=1225.0, pvalue=0.017143625211004959)}

##### burger vs swipe 2

{'n2': 28, 'N': 138, 'effect_size': 0.22305194805194806, 'n1': 110, 'test_result': MannwhitneyuResult(statistic=1196.5, pvalue=0.011075983661422355)}

##### burger vs swipe 3

{'n2': 28, 'N': 138, 'effect_size': 0.31266233766233764, 'n1': 110, 'test_result': MannwhitneyuResult(statistic=1058.5, pvalue=0.00087828638876744818)}

##### burger vs swipe 4

{'n2': 28, 'N': 138, 'effect_size': 0.36103896103896105, 'n1': 110, 'test_result': MannwhitneyuResult(statistic=984.0, pvalue=0.00018652482417813029)}

##### burger vs swipe 5

{'n2': 28, 'N': 138, 'effect_size': 0.38798701298701299, 'n1': 110, 'test_result': MannwhitneyuResult(statistic=942.5, pvalue=6.5526352124271008e-05)}

#### Global Burger vs Global Swipe Test (result)

##### burger vs swipe

{'n2': 140, 'N': 250, 'effect_size': 0.29785714285714282, 'n1': 110, 'test_result': MannwhitneyuResult(statistic=5406.5, pvalue=2.9062055593999374e-06)}

## Final Questionnaires

### Final Question 0

#### Just counts grouped by Results

| Navigation burger answered 1 stars:                                 16
| Navigation burger answered 2 stars:                                 4
| Navigation burger answered 4 stars:                                 1
| Navigation burger answered 5 stars:                                 1
| Navigation swipe answered 1 stars:                                 21
| Navigation swipe answered 2 stars:                                 4
| Navigation swipe answered 3 stars:                                 1
| Navigation swipe answered 4 stars:                                 1
| Navigation swipe answered 7 stars:                                 1

#### Descriptions (result)

##### Global Descriptions (result)

###### burger

| count | 22.0 |
| mean | 1.5 |
| std | 1.05785047102 |
| min | 1.0 |
| 25% | 1.0 |
| 50% | 1.0 |
| 75% | 1.75 |
| max | 5.0 |

| shapiro
| (0.5448707342147827, 3.567666624348931e-07)

###### swipe

| count | 28.0 |
| mean | 1.53571428571 |
| std | 1.29048204766 |
| min | 1.0 |
| 25% | 1.0 |
| 50% | 1.0 |
| 75% | 1.25 |
| max | 7.0 |

| shapiro
| (0.4864434003829956, 8.3034956688266e-09)

#### Global Burger vs Global Swipe Test (result)

##### burger vs swipe

{'n2': 28, 'N': 50, 'effect_size': 0.017857142857142905, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=302.5, pvalue=0.44941800310214225)}

### Final Question 1

#### Just counts grouped by Results

| Navigation burger answered 1 stars:                                 13
| Navigation burger answered 2 stars:                                 3
| Navigation burger answered 4 stars:                                 1
| Navigation burger answered 5 stars:                                 4
| Navigation burger answered 6 stars:                                 1
| Navigation swipe answered 1 stars:                                 17
| Navigation swipe answered 2 stars:                                 8
| Navigation swipe answered 4 stars:                                 2
| Navigation swipe answered 6 stars:                                 1

#### Descriptions (result)

##### Global Descriptions (result)

###### burger

| count | 22.0 |
| mean | 2.22727272727 |
| std | 1.79766563398 |
| min | 1.0 |
| 25% | 1.0 |
| 50% | 1.0 |
| 75% | 3.5 |
| max | 6.0 |

| shapiro
| (0.6886584758758545, 1.4087103409110568e-05)

###### swipe

| count | 28.0 |
| mean | 1.67857142857 |
| std | 1.18801332542 |
| min | 1.0 |
| 25% | 1.0 |
| 50% | 1.0 |
| 75% | 2.0 |
| max | 6.0 |

| shapiro
| (0.6186860203742981, 2.4386196173509234e-07)

#### Global Burger vs Global Swipe Test (result)

##### burger vs swipe

{'n2': 28, 'N': 50, 'effect_size': 0.087662337662337664, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=281.0, pvalue=0.27788843237866634)}

### Final Question 2

#### Just counts grouped by Results

| Navigation burger answered 1 stars:                                 17
| Navigation burger answered 2 stars:                                 5
| Navigation swipe answered 1 stars:                                 18
| Navigation swipe answered 2 stars:                                 5
| Navigation swipe answered 3 stars:                                 2
| Navigation swipe answered 4 stars:                                 2
| Navigation swipe answered 7 stars:                                 1

#### Descriptions (result)

##### Global Descriptions (result)

###### burger

| count | 22.0 |
| mean | 1.22727272727 |
| std | 0.428932027229 |
| min | 1.0 |
| 25% | 1.0 |
| 50% | 1.0 |
| 75% | 1.0 |
| max | 2.0 |

| shapiro
| (0.5222699642181396, 2.1416671813767607e-07)

###### swipe

| count | 28.0 |
| mean | 1.75 |
| std | 1.37773297418 |
| min | 1.0 |
| 25% | 1.0 |
| 50% | 1.0 |
| 75% | 2.0 |
| max | 7.0 |

| shapiro
| (0.6172786951065063, 2.343947329563889e-07)

#### Global Burger vs Global Swipe Test (result)

##### burger vs swipe

{'n2': 28, 'N': 50, 'effect_size': 0.17045454545454541, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=255.5, pvalue=0.10358134878107761)}

### Final Question 3

#### Just counts grouped by Results

| Navigation burger answered 2 stars:                                 1
| Navigation burger answered 3 stars:                                 5
| Navigation burger answered 4 stars:                                 1
| Navigation burger answered 5 stars:                                 4
| Navigation burger answered 6 stars:                                 5
| Navigation burger answered 7 stars:                                 6
| Navigation swipe answered 1 stars:                                 1
| Navigation swipe answered 2 stars:                                 1
| Navigation swipe answered 3 stars:                                 3
| Navigation swipe answered 4 stars:                                 11
| Navigation swipe answered 5 stars:                                 5
| Navigation swipe answered 6 stars:                                 4
| Navigation swipe answered 7 stars:                                 3

#### Descriptions (result)

##### Global Descriptions (result)

###### burger

| count | 22.0 |
| mean | 5.13636363636 |
| std | 1.67034226733 |
| min | 2.0 |
| 25% | 3.25 |
| 50% | 5.5 |
| 75% | 6.75 |
| max | 7.0 |

| shapiro
| (0.8708899021148682, 0.008132589980959892)

###### swipe

| count | 28.0 |
| mean | 4.5 |
| std | 1.45296631451 |
| min | 1.0 |
| 25% | 4.0 |
| 50% | 4.0 |
| 75% | 5.25 |
| max | 7.0 |

| shapiro
| (0.9325721859931946, 0.07159832864999771)

#### Global Burger vs Global Swipe Test (result)

##### burger vs swipe

{'n2': 28, 'N': 50, 'effect_size': 0.22564935064935066, 'n1': 22, 'test_result': MannwhitneyuResult(statistic=238.5, pvalue=0.084899251911718931)}
