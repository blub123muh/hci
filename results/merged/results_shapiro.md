
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

{'n2': 22, 'effect_size': 0.94675972197265923, 'test_result': Ttest_relResult(statistic=3.1400467644045076, pvalue=0.0049443978028402202), 'n1': 22, 'N': 44}

#### ('burger', 1) vs ('burger', 3)

{'n2': 22, 'effect_size': 1.2011056601611565, 'test_result': Ttest_relResult(statistic=3.9836168083266799, pvalue=0.00067564806607191632), 'n1': 22, 'N': 44}

#### ('burger', 1) vs ('burger', 4)

{'n2': 22, 'effect_size': 0.84922261727279102, 'test_result': Ttest_relResult(statistic=2.8165527849774343, pvalue=0.010338413955597585), 'n1': 22, 'N': 44}

#### ('burger', 1) vs ('burger', 5)

{'n2': 22, 'effect_size': 2.6611888863322934, 'test_result': Ttest_relResult(statistic=8.8261650322279621, pvalue=1.6451903254595449e-08), 'n1': 22, 'N': 44}

#### ('burger', 1) vs ('swipe', 1)

{'n2': 28, 'effect_size': -1.9097298327149146, 'test_result': Ttest_indResult(statistic=-6.7031245086454758, pvalue=5.6381782972874844e-08), 'n1': 22, 'N': 50}

#### ('burger', 1) vs ('swipe', 2)

{'n2': 28, 'effect_size': 0.24350649350649356, 'test_result': MannwhitneyuResult(statistic=233.0, pvalue=0.072691640416537293), 'n1': 22, 'N': 50}

#### ('burger', 1) vs ('swipe', 3)

{'n2': 28, 'effect_size': 2.2829620500029861, 'test_result': Ttest_indResult(statistic=8.0131642746175658, pvalue=3.0036765567743514e-10), 'n1': 22, 'N': 50}

#### ('burger', 1) vs ('swipe', 4)

{'n2': 28, 'effect_size': 2.9366881218094312, 'test_result': Ttest_indResult(statistic=10.307733474302086, pvalue=3.9626211595998718e-13), 'n1': 22, 'N': 50}

#### ('burger', 1) vs ('swipe', 5)

{'n2': 28, 'effect_size': 3.9971846751859443, 'test_result': Ttest_indResult(statistic=14.030061269834484, pvalue=1.6751765716561832e-16), 'n1': 22, 'N': 50}

#### ('burger', 2) vs ('burger', 3)

{'n2': 22, 'effect_size': 0.35440147919303427, 'test_result': Ttest_relResult(statistic=1.1754167316302409, pvalue=0.25298310480066266), 'n1': 22, 'N': 44}

#### ('burger', 2) vs ('burger', 4)

{'n2': 22, 'effect_size': -0.27581681953294063, 'test_result': Ttest_relResult(statistic=-0.91478090125993228, pvalue=0.37069158497461718), 'n1': 22, 'N': 44}

#### ('burger', 2) vs ('burger', 5)

{'n2': 22, 'effect_size': 0.51539165603199966, 'test_result': Ttest_relResult(statistic=1.7093607431380531, pvalue=0.10212210775377208), 'n1': 22, 'N': 44}

#### ('burger', 2) vs ('swipe', 1)

{'n2': 28, 'effect_size': -2.1964344153980893, 'test_result': Ttest_indResult(statistic=-7.7094535097442671, pvalue=6.1460659425242285e-10), 'n1': 22, 'N': 50}

#### ('burger', 2) vs ('swipe', 2)

{'n2': 28, 'effect_size': 0.14610389610389607, 'test_result': MannwhitneyuResult(statistic=263.0, pvalue=0.19222905550361363), 'n1': 22, 'N': 50}

#### ('burger', 2) vs ('swipe', 3)

{'n2': 28, 'effect_size': 0.81212695298602966, 'test_result': Ttest_indResult(statistic=2.8505540361974746, pvalue=0.007533072831137938), 'n1': 22, 'N': 50}

#### ('burger', 2) vs ('swipe', 4)

{'n2': 28, 'effect_size': 1.1871061872924935, 'test_result': Ttest_indResult(statistic=4.1667258070177891, pvalue=0.00024295893165475523), 'n1': 22, 'N': 50}

#### ('burger', 2) vs ('swipe', 5)

{'n2': 28, 'effect_size': 1.7884292636279993, 'test_result': Ttest_indResult(statistic=6.2773612390822437, pvalue=9.9419198495425703e-07), 'n1': 22, 'N': 50}

#### ('burger', 3) vs ('burger', 4)

{'n2': 22, 'effect_size': -0.7374996248322695, 'test_result': Ttest_relResult(statistic=-2.4460095385965119, pvalue=0.023338332791632995), 'n1': 22, 'N': 44}

#### ('burger', 3) vs ('burger', 5)

{'n2': 22, 'effect_size': 0.23656134754591943, 'test_result': Ttest_relResult(statistic=0.7845852297106759, pvalue=0.4414581754358432), 'n1': 22, 'N': 44}

#### ('burger', 3) vs ('swipe', 1)

{'n2': 28, 'effect_size': -2.5346208780888531, 'test_result': Ttest_indResult(statistic=-8.8964831763080934, pvalue=1.6380584716166247e-11), 'n1': 22, 'N': 50}

#### ('burger', 3) vs ('swipe', 2)

{'n2': 28, 'effect_size': 0.36038961038961037, 'test_result': MannwhitneyuResult(statistic=197.0, pvalue=0.015401027053631673), 'n1': 22, 'N': 50}

#### ('burger', 3) vs ('swipe', 3)

{'n2': 28, 'effect_size': 0.70376045931483799, 'test_result': Ttest_indResult(statistic=2.4701891870969703, pvalue=0.018195085242505141), 'n1': 22, 'N': 50}

#### ('burger', 3) vs ('swipe', 4)

{'n2': 28, 'effect_size': 1.1462100107866364, 'test_result': Ttest_indResult(statistic=4.0231808100500297, pvalue=0.00030313523132897963), 'n1': 22, 'N': 50}

#### ('burger', 3) vs ('swipe', 5)

{'n2': 28, 'effect_size': 1.8689406873961947, 'test_result': Ttest_indResult(statistic=6.5599551896199042, pvalue=2.8434885910251271e-07), 'n1': 22, 'N': 50}

#### ('burger', 4) vs ('burger', 5)

{'n2': 22, 'effect_size': 0.84300225316077237, 'test_result': Ttest_relResult(statistic=2.7959221711584763, pvalue=0.010828183767257584), 'n1': 22, 'N': 44}

#### ('burger', 4) vs ('swipe', 1)

{'n2': 28, 'effect_size': -2.3036145286208791, 'test_result': Ttest_indResult(statistic=-8.0856541803709217, pvalue=3.5438757244842358e-10), 'n1': 22, 'N': 50}

#### ('burger', 4) vs ('swipe', 2)

{'n2': 28, 'effect_size': 0.14935064935064934, 'test_result': MannwhitneyuResult(statistic=262.0, pvalue=0.18693288210180464), 'n1': 22, 'N': 50}

#### ('burger', 4) vs ('swipe', 3)

{'n2': 28, 'effect_size': 1.2621200986811529, 'test_result': Ttest_indResult(statistic=4.4300235674155788, pvalue=6.9900388209405247e-05), 'n1': 22, 'N': 50}

#### ('burger', 4) vs ('swipe', 4)

{'n2': 28, 'effect_size': 1.7720819828888696, 'test_result': Ttest_indResult(statistic=6.2199825165556186, pvalue=3.19607703847048e-07), 'n1': 22, 'N': 50}

#### ('burger', 4) vs ('swipe', 5)

{'n2': 28, 'effect_size': 2.6020850201949859, 'test_result': Ttest_indResult(statistic=9.1332813540710038, pvalue=1.7051757569924614e-10), 'n1': 22, 'N': 50}

#### ('burger', 5) vs ('swipe', 1)

{'n2': 28, 'effect_size': -2.9198423468617594, 'test_result': Ttest_indResult(statistic=-10.248605044204549, pvalue=2.0453619521585734e-12), 'n1': 22, 'N': 50}

#### ('burger', 5) vs ('swipe', 2)

{'n2': 28, 'effect_size': 0.51623376623376616, 'test_result': MannwhitneyuResult(statistic=149.0, pvalue=0.0009750243017655867), 'n1': 22, 'N': 50}

#### ('burger', 5) vs ('swipe', 3)

{'n2': 28, 'effect_size': 0.67859393927802314, 'test_result': Ttest_indResult(statistic=2.3818550602659139, pvalue=0.0213390257262559), 'n1': 22, 'N': 50}

#### ('burger', 5) vs ('swipe', 4)

{'n2': 28, 'effect_size': 1.2662092998006802, 'test_result': Ttest_indResult(statistic=4.4443766050942735, pvalue=5.8417405173783372e-05), 'n1': 22, 'N': 50}

#### ('burger', 5) vs ('swipe', 5)

{'n2': 28, 'effect_size': 2.2701377982054174, 'test_result': Ttest_indResult(statistic=7.9681513334901197, pvalue=9.6399894615656428e-10), 'n1': 22, 'N': 50}

#### ('swipe', 1) vs ('swipe', 2)

{'n2': 28, 'effect_size': 0.0019126554032515141, 'test_result': WilcoxonResult(statistic=3.0, pvalue=5.2564133258508337e-06), 'n1': 28, 'N': 56}

#### ('swipe', 1) vs ('swipe', 3)

{'n2': 28, 'effect_size': 3.4860559225484686, 'test_result': Ttest_relResult(statistic=13.043626893310524, pvalue=3.5969964456561752e-13), 'n1': 28, 'N': 56}

#### ('swipe', 1) vs ('swipe', 4)

{'n2': 28, 'effect_size': 3.8799222428390125, 'test_result': Ttest_relResult(statistic=14.517339720027108, pvalue=2.8328302970398919e-14), 'n1': 28, 'N': 56}

#### ('swipe', 1) vs ('swipe', 5)

{'n2': 28, 'effect_size': 4.5968919124502001, 'test_result': Ttest_relResult(statistic=17.199994580420682, pvalue=4.4867434987762781e-16), 'n1': 28, 'N': 56}

#### ('swipe', 2) vs ('swipe', 3)

{'n2': 28, 'effect_size': 0.01912655403251514, 'test_result': WilcoxonResult(statistic=30.0, pvalue=8.1666493089205386e-05), 'n1': 28, 'N': 56}

#### ('swipe', 2) vs ('swipe', 4)

{'n2': 28, 'effect_size': 0.010200828817341408, 'test_result': WilcoxonResult(statistic=16.0, pvalue=2.0602777134809463e-05), 'n1': 28, 'N': 56}

#### ('swipe', 2) vs ('swipe', 5)

{'n2': 28, 'effect_size': 0.0031877590054191903, 'test_result': WilcoxonResult(statistic=5.0, pvalue=6.5213205645443688e-06), 'n1': 28, 'N': 56}

#### ('swipe', 3) vs ('swipe', 4)

{'n2': 28, 'effect_size': 0.5606349854006033, 'test_result': Ttest_relResult(statistic=2.0977040344080682, pvalue=0.045427484584555158), 'n1': 28, 'N': 56}

#### ('swipe', 3) vs ('swipe', 5)

{'n2': 28, 'effect_size': 1.3561910948601303, 'test_result': Ttest_relResult(statistic=5.0744024279604458, pvalue=2.493775482784069e-05), 'n1': 28, 'N': 56}

#### ('swipe', 4) vs ('swipe', 5)

{'n2': 28, 'effect_size': 1.104446011408412, 'test_result': Ttest_relResult(statistic=4.1324585768793014, pvalue=0.00031147549191696031), 'n1': 28, 'N': 56}

### Global Burger vs Swipe per tid Tests (efficiency)

#### burger vs swipe 1

{'n2': 28, 'effect_size': -1.9870466939513425, 'test_result': Ttest_indResult(statistic=-9.3873689639224196, pvalue=9.7956596089962241e-11), 'n1': 110, 'N': 138}

#### burger vs swipe 2

{'n2': 28, 'effect_size': 0.18571428571428572, 'test_result': MannwhitneyuResult(statistic=1254.0, pvalue=0.065327534078559346), 'n1': 110, 'N': 138}

#### burger vs swipe 3

{'n2': 28, 'effect_size': 1.1700510299170295, 'test_result': Ttest_indResult(statistic=5.5276510400502676, pvalue=9.0622300016679275e-07), 'n1': 110, 'N': 138}

#### burger vs swipe 4

{'n2': 28, 'effect_size': 1.770000563266015, 'test_result': Ttest_indResult(statistic=8.3619818317845045, pvalue=7.0554228434671516e-12), 'n1': 110, 'N': 138}

#### burger vs swipe 5

{'n2': 28, 'effect_size': 2.8251881603681559, 'test_result': Ttest_indResult(statistic=13.346985621733221, pvalue=3.9194832679580957e-22), 'n1': 110, 'N': 138}

### Global Burger vs Global Swipe Test (efficiency)

#### burger vs swipe

{'n2': 140, 'effect_size': 0.2218181818181818, 'test_result': MannwhitneyuResult(statistic=5992.0, pvalue=0.0013125763723938479), 'n1': 110, 'N': 250}

## Effectiveness by Tasks

### Descriptions (effectiveness)

#### Global Descriptions (effectiveness)

##### burger

| count | 110.0 |
| mean | 0.978181818182 |
| std | 0.0626360071457 |
| min | 0.8 |
| 25% | 1.0 |
| 50% | 1.0 |
| 75% | 1.0 |
| max | 1.0 |

| shapiro
| (0.3595287799835205, 8.873730593883483e-20)

##### swipe

| count | 140.0 |
| mean | 0.934285714286 |
| std | 0.105783427849 |
| min | 0.6 |
| 25% | 0.8 |
| 50% | 1.0 |
| 75% | 1.0 |
| max | 1.0 |

| shapiro
| (0.6147457361221313, 1.3754389831214409e-17)

### Global Burger vs Global Swipe Test (effectiveness)

#### burger vs swipe

{'n2': 140, 'effect_size': 0.19402597402597399, 'test_result': MannwhitneyuResult(statistic=6206.0, pvalue=0.00011462735661581992), 'n1': 110, 'N': 250}

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

#### Global Burger vs Global Swipe Test (result)

##### burger vs swipe

{'n2': 140, 'effect_size': 0.064545454545454573, 'test_result': MannwhitneyuResult(statistic=7203.0, pvalue=0.046318608676750285), 'n1': 110, 'N': 250}

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

#### Global Burger vs Global Swipe Test (result)

##### burger vs swipe

{'n2': 140, 'effect_size': 0.29785714285714282, 'test_result': MannwhitneyuResult(statistic=5406.5, pvalue=2.9062055593999374e-06), 'n1': 110, 'N': 250}

## Final Questionnaires

### Final Question 0

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

{'n2': 28, 'effect_size': 0.017857142857142905, 'test_result': MannwhitneyuResult(statistic=302.5, pvalue=0.44941800310214225), 'n1': 22, 'N': 50}

### Final Question 1

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

{'n2': 28, 'effect_size': 0.087662337662337664, 'test_result': MannwhitneyuResult(statistic=281.0, pvalue=0.27788843237866634), 'n1': 22, 'N': 50}

### Final Question 2

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

{'n2': 28, 'effect_size': 0.17045454545454541, 'test_result': MannwhitneyuResult(statistic=255.5, pvalue=0.10358134878107761), 'n1': 22, 'N': 50}

### Final Question 3

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

{'n2': 28, 'effect_size': 0.22564935064935066, 'test_result': MannwhitneyuResult(statistic=238.5, pvalue=0.084899251911718931), 'n1': 22, 'N': 50}
