
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

| Split by Navigation, Pid, Tid, apply `mean` combine!

Drop jid and pid columns

| Computing efficiency task $1000 *                       mean_success/mean_time_ms$

Using normality test: normaltest

## Demographics

### age

|  |age |
| -|--- |
| count|50.0 |
| mean|24.1 |
| std|2.90144228737 |
| min|20.0 |
| 25%|22.0 |
| 50%|24.0 |
| 75%|25.0 |
| max|35.0 |

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

|  |efficiency |
| -|---------- |
| count|110.0 |
| mean|0.223055228972 |
| std|0.0500230406763 |
| min|0.068976220448 |
| 25%|0.190058286882 |
| 50%|0.22691177807 |
| 75%|0.25700334919 |
| max|0.336157052575 |

| normaltest
| NormaltestResult(statistic=4.771761427618066, pvalue=0.092007911247545662)

##### swipe

|  |efficiency |
| -|---------- |
| count|140.0 |
| mean|0.215488934466 |
| std|0.100837665235 |
| min|0.0783468808148 |
| 25%|0.140770307033 |
| 50%|0.186047319425 |
| 75%|0.267820085532 |
| max|0.514986095375 |

| normaltest
| NormaltestResult(statistic=21.611661929265029, pvalue=2.0280900748269049e-05)

#### Repeated measures (efficiency)

##### burger

| KruskalResult(statistic=21.228960676540432, pvalue=0.00028522628404656868)
| FriedmanchisquareResult(statistic=30.509090909090901, pvalue=3.8548715779974447e-06)

##### swipe

| KruskalResult(statistic=91.910160660008614, pvalue=5.1718364795390112e-19)
| FriedmanchisquareResult(statistic=80.628571428571377, pvalue=1.2818240657137304e-16)

#### Descriptions per tid (efficiency)

##### ('burger', 1)

|  |efficiency |
| -|---------- |
| count|22.0 |
| mean|0.259627939777 |
| std|0.03615089292 |
| min|0.189458527528 |
| 25%|0.242800150862 |
| 50%|0.263092621632 |
| 75%|0.281021933116 |
| max|0.336157052575 |

| normaltest
| NormaltestResult(statistic=0.20268737597716502, pvalue=0.90362241534079546)

##### ('burger', 2)

|  |efficiency |
| -|---------- |
| count|22.0 |
| mean|0.218885902709 |
| std|0.0617582924756 |
| min|0.068976220448 |
| 25%|0.175369392634 |
| 50%|0.229429832866 |
| 75%|0.262567057042 |
| max|0.298650101541 |

| normaltest
| NormaltestResult(statistic=2.8677330362290436, pvalue=0.2383854164873315)

##### ('burger', 3)

|  |efficiency |
| -|---------- |
| count|22.0 |
| mean|0.207954767299 |
| std|0.0501700789335 |
| min|0.0904895484572 |
| 25%|0.177580422745 |
| 50%|0.214082948414 |
| 75%|0.246063771629 |
| max|0.280033604032 |

| normaltest
| NormaltestResult(statistic=1.7984339571775487, pvalue=0.40688813716037808)

##### ('burger', 4)

|  |efficiency |
| -|---------- |
| count|22.0 |
| mean|0.228578290867 |
| std|0.0445345887587 |
| min|0.113259903163 |
| 25%|0.21190614273 |
| 50%|0.227615297646 |
| 75%|0.251743012241 |
| max|0.304284323272 |

| normaltest
| NormaltestResult(statistic=2.3160697541755684, pvalue=0.31410282545206514)

##### ('burger', 5)

|  |efficiency |
| -|---------- |
| count|22.0 |
| mean|0.200229244208 |
| std|0.0336254251422 |
| min|0.144350135689 |
| 25%|0.177255912416 |
| 50%|0.196225661233 |
| 75%|0.22656990971 |
| max|0.255076012652 |

| normaltest
| NormaltestResult(statistic=1.5723484852844765, pvalue=0.45558442091815343)

##### ('swipe', 1)

|  |efficiency |
| -|---------- |
| count|28.0 |
| mean|0.376411637958 |
| std|0.0826782359999 |
| min|0.124738828079 |
| 25%|0.339208375025 |
| 50%|0.385810331212 |
| 75%|0.43554876804 |
| max|0.514986095375 |

| normaltest
| NormaltestResult(statistic=9.9372068077013189, pvalue=0.0069528515829475517)

##### ('swipe', 2)

|  |efficiency |
| -|---------- |
| count|28.0 |
| mean|0.235764444338 |
| std|0.0515833509387 |
| min|0.0783468808148 |
| 25%|0.214528622096 |
| 50%|0.250787488437 |
| 75%|0.270937446389 |
| max|0.305866519851 |

| normaltest
| NormaltestResult(statistic=11.365760575131674, pvalue=0.0034037405594077226)

##### ('swipe', 3)

|  |efficiency |
| -|---------- |
| count|28.0 |
| mean|0.176438327988 |
| std|0.0368031666814 |
| min|0.106547333653 |
| 25%|0.149048762852 |
| 50%|0.183800941036 |
| 75%|0.207357536463 |
| max|0.233165454206 |

| normaltest
| NormaltestResult(statistic=2.0647128368782415, pvalue=0.35616669318396116)

##### ('swipe', 4)

|  |efficiency |
| -|---------- |
| count|28.0 |
| mean|0.158462999373 |
| std|0.0321520787395 |
| min|0.0888474267564 |
| 25%|0.137780626155 |
| 50%|0.155438077528 |
| 75%|0.183456377089 |
| max|0.223483663344 |

| normaltest
| NormaltestResult(statistic=0.12655594049035332, pvalue=0.93868251161307126)

##### ('swipe', 5)

|  |efficiency |
| -|---------- |
| count|28.0 |
| mean|0.130367262672 |
| std|0.0267090785385 |
| min|0.0821186614658 |
| 25%|0.120638250545 |
| 50%|0.128225214081 |
| 75%|0.143514673291 |
| max|0.182588372772 |

| normaltest
| NormaltestResult(statistic=0.20145824064936479, pvalue=0.9041779231387197)

### Cross-compare Tests per tid (efficiency)

#### ('burger', 1) vs ('burger', 2)

{'n2': 22, 'test_result': Ttest_relResult(statistic=3.1400467644045085, pvalue=0.0049443978028402098), 'N': 44, 'n1': 22, 'df': 21, 'effect_size': 0.66946021956115787}

#### ('burger', 1) vs ('burger', 3)

{'n2': 22, 'test_result': Ttest_relResult(statistic=3.9836168083266799, pvalue=0.00067564806607191632), 'N': 44, 'n1': 22, 'df': 21, 'effect_size': 0.8493099572214986}

#### ('burger', 1) vs ('burger', 4)

{'n2': 22, 'test_result': Ttest_relResult(statistic=2.8165527849774352, pvalue=0.010338413955597564), 'N': 44, 'n1': 22, 'df': 21, 'effect_size': 0.60049107141057878}

#### ('burger', 1) vs ('burger', 5)

{'n2': 22, 'test_result': Ttest_relResult(statistic=8.8261650322279657, pvalue=1.6451903254595333e-08), 'N': 44, 'n1': 22, 'df': 21, 'effect_size': 1.8817447075438416}

#### ('burger', 1) vs ('swipe', 1)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=58.0, pvalue=5.4061503445428946e-07), 'effect_size': 0.81168831168831168, 'N': 50}

#### ('burger', 1) vs ('swipe', 2)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=233.0, pvalue=0.072691640416537293), 'effect_size': 0.24350649350649356, 'N': 50}

#### ('burger', 1) vs ('swipe', 3)

{'n2': 28, 'test_result': Ttest_indResult(statistic=8.0131642746175658, pvalue=3.0036765567743509e-10), 'N': 50, 'n1': 22, 'df': 45.605549072886376, 'effect_size': 2.2829620500029861}

#### ('burger', 1) vs ('swipe', 4)

{'n2': 28, 'test_result': Ttest_indResult(statistic=10.307733474302083, pvalue=3.9626211595999131e-13), 'N': 50, 'n1': 22, 'df': 42.458884481600464, 'effect_size': 2.9366881218094303}

#### ('burger', 1) vs ('swipe', 5)

{'n2': 28, 'test_result': Ttest_indResult(statistic=14.030061269834485, pvalue=1.6751765716561837e-16), 'N': 50, 'n1': 22, 'df': 37.509707823002977, 'effect_size': 3.9971846751859452}

#### ('burger', 2) vs ('burger', 3)

{'n2': 22, 'test_result': Ttest_relResult(statistic=1.17541673163024, pvalue=0.25298310480066288), 'N': 44, 'n1': 22, 'df': 21, 'effect_size': 0.25059968919993747}

#### ('burger', 2) vs ('burger', 4)

{'n2': 22, 'test_result': Ttest_relResult(statistic=-0.91478090125993261, pvalue=0.37069158497461707), 'N': 44, 'n1': 22, 'df': 21, 'effect_size': -0.19503194345704855}

#### ('burger', 2) vs ('burger', 5)

{'n2': 22, 'test_result': Ttest_relResult(statistic=1.7093607431380531, pvalue=0.10212210775377208), 'N': 44, 'n1': 22, 'df': 21, 'effect_size': 0.36443693494719148}

#### ('burger', 2) vs ('swipe', 1)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=42.0, pvalue=1.0574010189647895e-07), 'effect_size': 0.86363636363636365, 'N': 50}

#### ('burger', 2) vs ('swipe', 2)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=263.0, pvalue=0.19222905550361363), 'effect_size': 0.14610389610389607, 'N': 50}

#### ('burger', 2) vs ('swipe', 3)

{'n2': 28, 'test_result': Ttest_indResult(statistic=2.8505540361974759, pvalue=0.0075330728311379285), 'N': 50, 'n1': 22, 'df': 32.392545034300269, 'effect_size': 0.8121269529860301}

#### ('burger', 2) vs ('swipe', 4)

{'n2': 28, 'test_result': Ttest_indResult(statistic=4.1667258070177873, pvalue=0.00024295893165475588), 'N': 50, 'n1': 22, 'df': 29.84388793928602, 'effect_size': 1.1871061872924931}

#### ('burger', 2) vs ('swipe', 5)

{'n2': 28, 'test_result': Ttest_indResult(statistic=6.2773612390822446, pvalue=9.9419198495425322e-07), 'N': 50, 'n1': 22, 'df': 27.169372064223619, 'effect_size': 1.7884292636279995}

#### ('burger', 3) vs ('burger', 4)

{'n2': 22, 'test_result': Ttest_relResult(statistic=-2.4460095385965119, pvalue=0.023338332791632995), 'N': 44, 'n1': 22, 'df': 21, 'effect_size': -0.5214909858414325}

#### ('burger', 3) vs ('burger', 5)

{'n2': 22, 'test_result': Ttest_relResult(statistic=0.78458522971067601, pvalue=0.4414581754358432), 'N': 44, 'n1': 22, 'df': 21, 'effect_size': 0.16727413301634728}

#### ('burger', 3) vs ('swipe', 1)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=32.0, pvalue=3.634468651668778e-08), 'effect_size': 0.89610389610389607, 'N': 50}

#### ('burger', 3) vs ('swipe', 2)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=197.0, pvalue=0.015401027053631673), 'effect_size': 0.36038961038961037, 'N': 50}

#### ('burger', 3) vs ('swipe', 3)

{'n2': 28, 'test_result': Ttest_indResult(statistic=2.470189187096973, pvalue=0.018195085242505033), 'N': 50, 'n1': 22, 'df': 37.322733521049877, 'effect_size': 0.70376045931483877}

#### ('burger', 3) vs ('swipe', 4)

{'n2': 28, 'test_result': Ttest_indResult(statistic=4.0231808100500288, pvalue=0.00030313523132898115), 'N': 50, 'n1': 22, 'df': 33.987304407263395, 'effect_size': 1.1462100107866362}

#### ('burger', 3) vs ('swipe', 5)

{'n2': 28, 'test_result': Ttest_indResult(statistic=6.5599551896199069, pvalue=2.8434885910251012e-07), 'N': 50, 'n1': 22, 'df': 30.228298418120758, 'effect_size': 1.8689406873961953}

#### ('burger', 4) vs ('burger', 5)

{'n2': 22, 'test_result': Ttest_relResult(statistic=2.7959221711584767, pvalue=0.010828183767257568), 'N': 44, 'n1': 22, 'df': 21, 'effect_size': 0.59609260976552092}

#### ('burger', 4) vs ('swipe', 1)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=40.0, pvalue=8.565787191672169e-08), 'effect_size': 0.87012987012987009, 'N': 50}

#### ('burger', 4) vs ('swipe', 2)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=262.0, pvalue=0.18693288210180464), 'effect_size': 0.14935064935064934, 'N': 50}

#### ('burger', 4) vs ('swipe', 3)

{'n2': 28, 'test_result': Ttest_indResult(statistic=4.430023567415585, pvalue=6.9900388209403688e-05), 'N': 50, 'n1': 22, 'df': 40.510976522970402, 'effect_size': 1.2621200986811547}

#### ('burger', 4) vs ('swipe', 4)

{'n2': 28, 'test_result': Ttest_indResult(statistic=6.2199825165556213, pvalue=3.1960770384704573e-07), 'N': 50, 'n1': 22, 'df': 36.907897952812725, 'effect_size': 1.7720819828888703}

#### ('burger', 4) vs ('swipe', 5)

{'n2': 28, 'test_result': Ttest_indResult(statistic=9.1332813540710109, pvalue=1.7051757569924315e-10), 'N': 50, 'n1': 22, 'df': 32.52632637459962, 'effect_size': 2.6020850201949877}

#### ('burger', 5) vs ('swipe', 1)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=30.0, pvalue=2.9224626895523775e-08), 'effect_size': 0.90259740259740262, 'N': 50}

#### ('burger', 5) vs ('swipe', 2)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=149.0, pvalue=0.0009750243017655867), 'effect_size': 0.51623376623376616, 'N': 50}

#### ('burger', 5) vs ('swipe', 3)

{'n2': 28, 'test_result': Ttest_indResult(statistic=2.3818550602659152, pvalue=0.021339025726255848), 'N': 50, 'n1': 22, 'df': 46.852508622129029, 'effect_size': 0.67859393927802347}

#### ('burger', 5) vs ('swipe', 4)

{'n2': 28, 'test_result': Ttest_indResult(statistic=4.4443766050942699, pvalue=5.8417405173783915e-05), 'N': 50, 'n1': 22, 'df': 44.248400605855807, 'effect_size': 1.2662092998006793}

#### ('burger', 5) vs ('swipe', 5)

{'n2': 28, 'test_result': Ttest_indResult(statistic=7.9681513334901224, pvalue=9.6399894615656076e-10), 'N': 50, 'n1': 22, 'df': 39.442494949086644, 'effect_size': 2.2701377982054178}

#### ('swipe', 1) vs ('swipe', 2)

{'n1': 28, 'n2': 28, 'test_result': WilcoxonResult(statistic=3.0, pvalue=5.2564133258508337e-06), 'effect_size': 0.0019126554032515141, 'N': 56}

#### ('swipe', 1) vs ('swipe', 3)

{'n1': 28, 'n2': 28, 'test_result': WilcoxonResult(statistic=0.0, pvalue=3.7896194415808708e-06), 'effect_size': 0.0, 'N': 56}

#### ('swipe', 1) vs ('swipe', 4)

{'n1': 28, 'n2': 28, 'test_result': WilcoxonResult(statistic=1.0, pvalue=4.2284088472460966e-06), 'effect_size': 0.00063755180108383803, 'N': 56}

#### ('swipe', 1) vs ('swipe', 5)

{'n1': 28, 'n2': 28, 'test_result': WilcoxonResult(statistic=0.0, pvalue=3.7896194415808708e-06), 'effect_size': 0.0, 'N': 56}

#### ('swipe', 2) vs ('swipe', 3)

{'n1': 28, 'n2': 28, 'test_result': WilcoxonResult(statistic=30.0, pvalue=8.1666493089205386e-05), 'effect_size': 0.01912655403251514, 'N': 56}

#### ('swipe', 2) vs ('swipe', 4)

{'n1': 28, 'n2': 28, 'test_result': WilcoxonResult(statistic=16.0, pvalue=2.0602777134809463e-05), 'effect_size': 0.010200828817341408, 'N': 56}

#### ('swipe', 2) vs ('swipe', 5)

{'n1': 28, 'n2': 28, 'test_result': WilcoxonResult(statistic=5.0, pvalue=6.5213205645443688e-06), 'effect_size': 0.0031877590054191903, 'N': 56}

#### ('swipe', 3) vs ('swipe', 4)

{'n2': 28, 'test_result': Ttest_relResult(statistic=2.0977040344080686, pvalue=0.04542748458455511), 'N': 56, 'n1': 28, 'df': 27, 'effect_size': 0.39642879994718772}

#### ('swipe', 3) vs ('swipe', 5)

{'n2': 28, 'test_result': Ttest_relResult(statistic=5.0744024279604449, pvalue=2.493775482784069e-05), 'N': 56, 'n1': 28, 'df': 27, 'effect_size': 0.9589719197604063}

#### ('swipe', 4) vs ('swipe', 5)

{'n2': 28, 'test_result': Ttest_relResult(statistic=4.1324585768793005, pvalue=0.00031147549191696151), 'N': 56, 'n1': 28, 'df': 27, 'effect_size': 0.78096126412132294}

### Global Burger vs Swipe per tid Tests (efficiency)

#### burger vs swipe 1

{'n1': 110, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=202.0, pvalue=7.1491176304337561e-13), 'effect_size': 0.86883116883116884, 'N': 138}

#### burger vs swipe 2

{'n1': 110, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=1254.0, pvalue=0.065327534078559346), 'effect_size': 0.18571428571428572, 'N': 138}

#### burger vs swipe 3

{'n2': 28, 'test_result': Ttest_indResult(statistic=5.5276510400502614, pvalue=9.0622300016681276e-07), 'N': 138, 'n1': 110, 'df': 55.333617103825162, 'effect_size': 1.1700510299170281}

#### burger vs swipe 4

{'n2': 28, 'test_result': Ttest_indResult(statistic=8.3619818317844903, pvalue=7.0554228434676112e-12), 'N': 138, 'n1': 110, 'df': 64.460648478482284, 'effect_size': 1.7700005632660121}

#### burger vs swipe 5

{'n2': 28, 'test_result': Ttest_indResult(statistic=13.346985621733216, pvalue=3.9194832679581521e-22), 'N': 138, 'n1': 110, 'df': 80.786408371513843, 'effect_size': 2.8251881603681546}

### Global Burger vs Global Swipe Test (efficiency)

#### burger vs swipe

{'n1': 110, 'n2': 140, 'test_result': MannwhitneyuResult(statistic=5992.0, pvalue=0.0013125763723938479), 'effect_size': 0.2218181818181818, 'N': 250}

## Effectiveness by Tasks

### Descriptions (effectiveness)

#### Global Descriptions (effectiveness)

##### burger

|  |effectiveness |
| -|------------- |
| count|110.0 |
| mean|0.978181818182 |
| std|0.0626360071457 |
| min|0.8 |
| 25%|1.0 |
| 50%|1.0 |
| 75%|1.0 |
| max|1.0 |

| normaltest
| NormaltestResult(statistic=68.459419887611048, pvalue=1.3621528840605701e-15)

##### swipe

|  |effectiveness |
| -|------------- |
| count|140.0 |
| mean|0.934285714286 |
| std|0.105783427849 |
| min|0.6 |
| 25%|0.8 |
| 50%|1.0 |
| 75%|1.0 |
| max|1.0 |

| normaltest
| NormaltestResult(statistic=30.683850175565183, pvalue=2.173134430069827e-07)

#### Repeated measures (effectiveness)

##### burger

| KruskalResult(statistic=4.2636054421768179, pvalue=0.37150463698880992)
| FriedmanchisquareResult(statistic=5.1111111111109082, pvalue=0.276085623834601)

##### swipe

| KruskalResult(statistic=8.4325646925437621, pvalue=0.076957851331098878)
| FriedmanchisquareResult(statistic=8.7192429022081477, pvalue=0.068513251264267688)

#### Descriptions per tid (effectiveness)

##### ('burger', 1)

|  |effectiveness |
| -|------------- |
| count|22.0 |
| mean|0.990909090909 |
| std|0.0426401432711 |
| min|0.8 |
| 25%|1.0 |
| 50%|1.0 |
| 75%|1.0 |
| max|1.0 |

| normaltest
| NormaltestResult(statistic=55.867295667147665, pvalue=7.3887485384486275e-13)

##### ('burger', 2)

|  |effectiveness |
| -|------------- |
| count|22.0 |
| mean|0.963636363636 |
| std|0.0789542033952 |
| min|0.8 |
| 25%|1.0 |
| 50%|1.0 |
| 75%|1.0 |
| max|1.0 |

| normaltest
| NormaltestResult(statistic=11.761207015205065, pvalue=0.0027930991097338811)

##### ('burger', 3)

|  |effectiveness |
| -|------------- |
| count|22.0 |
| mean|0.963636363636 |
| std|0.0789542033952 |
| min|0.8 |
| 25%|1.0 |
| 50%|1.0 |
| 75%|1.0 |
| max|1.0 |

| normaltest
| NormaltestResult(statistic=11.761207015205118, pvalue=0.002793099109733807)

##### ('burger', 4)

|  |effectiveness |
| -|------------- |
| count|22.0 |
| mean|0.981818181818 |
| std|0.0588489886336 |
| min|0.8 |
| 25%|1.0 |
| 50%|1.0 |
| 75%|1.0 |
| max|1.0 |

| normaltest
| NormaltestResult(statistic=32.977747192506733, pvalue=6.9019718607633975e-08)

##### ('burger', 5)

|  |effectiveness |
| -|------------- |
| count|22.0 |
| mean|0.990909090909 |
| std|0.0426401432711 |
| min|0.8 |
| 25%|1.0 |
| 50%|1.0 |
| 75%|1.0 |
| max|1.0 |

| normaltest
| NormaltestResult(statistic=55.867295667147665, pvalue=7.3887485384486275e-13)

##### ('swipe', 1)

|  |effectiveness |
| -|------------- |
| count|28.0 |
| mean|0.978571428571 |
| std|0.0629940788349 |
| min|0.8 |
| 25%|1.0 |
| 50%|1.0 |
| 75%|1.0 |
| max|1.0 |

| normaltest
| NormaltestResult(statistic=30.230322102932696, pvalue=2.7262706131404123e-07)

##### ('swipe', 2)

|  |effectiveness |
| -|------------- |
| count|28.0 |
| mean|0.935714285714 |
| std|0.0951189731211 |
| min|0.8 |
| 25%|0.8 |
| 50%|1.0 |
| 75%|1.0 |
| max|1.0 |

| normaltest
| NormaltestResult(statistic=13.850854641882318, pvalue=0.0009824831927910632)

##### ('swipe', 3)

|  |effectiveness |
| -|------------- |
| count|28.0 |
| mean|0.892857142857 |
| std|0.138586973437 |
| min|0.6 |
| 25%|0.8 |
| 50%|1.0 |
| 75%|1.0 |
| max|1.0 |

| normaltest
| NormaltestResult(statistic=4.3703066280619502, pvalue=0.11246049056138591)

##### ('swipe', 4)

|  |effectiveness |
| -|------------- |
| count|28.0 |
| mean|0.942857142857 |
| std|0.0920087412456 |
| min|0.8 |
| 25%|0.8 |
| 50%|1.0 |
| 75%|1.0 |
| max|1.0 |

| normaltest
| NormaltestResult(statistic=8.1469969468004297, pvalue=0.017017748104058518)

##### ('swipe', 5)

|  |effectiveness |
| -|------------- |
| count|28.0 |
| mean|0.921428571429 |
| std|0.113389341903 |
| min|0.6 |
| 25%|0.8 |
| 50%|1.0 |
| 75%|1.0 |
| max|1.0 |

| normaltest
| NormaltestResult(statistic=6.1681726236411034, pvalue=0.045771835985766236)

### Cross-compare Tests per tid (effectiveness)

#### ('burger', 1) vs ('burger', 2)

{'n1': 22, 'n2': 22, 'test_result': WilcoxonResult(statistic=3.0, pvalue=0.17971249487899976), 'effect_size': 0.0030975735673722249, 'N': 44}

#### ('burger', 1) vs ('burger', 3)

{'n1': 22, 'n2': 22, 'test_result': WilcoxonResult(statistic=3.0, pvalue=0.17971249487899976), 'effect_size': 0.0030975735673722249, 'N': 44}

#### ('burger', 1) vs ('burger', 4)

{'n1': 22, 'n2': 22, 'test_result': WilcoxonResult(statistic=2.0, pvalue=0.5637028616507731), 'effect_size': 0.0020650490449148169, 'N': 44}

#### ('burger', 1) vs ('burger', 5)

{'n1': 22, 'n2': 22, 'test_result': '=== All pairs were equal ===', 'effect_size': '=== All pairs were equal ===', 'N': 44}

#### ('burger', 1) vs ('swipe', 1)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=289.0, pvalue=0.22085511431458626), 'effect_size': 0.061688311688311681, 'N': 50}

#### ('burger', 1) vs ('swipe', 2)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=223.0, pvalue=0.0085809342731982628), 'effect_size': 0.27597402597402598, 'N': 50}

#### ('burger', 1) vs ('swipe', 3)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=188.5, pvalue=0.0011982167922993706), 'effect_size': 0.38798701298701299, 'N': 50}

#### ('burger', 1) vs ('swipe', 4)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=234.0, pvalue=0.015452252565939647), 'effect_size': 0.24025974025974028, 'N': 50}

#### ('burger', 1) vs ('swipe', 5)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=211.5, pvalue=0.0045566881958452573), 'effect_size': 0.31331168831168832, 'N': 50}

#### ('burger', 2) vs ('burger', 3)

{'n1': 22, 'n2': 22, 'test_result': WilcoxonResult(statistic=5.0, pvalue=1.0), 'effect_size': 0.0051626226122870418, 'N': 44}

#### ('burger', 2) vs ('burger', 4)

{'n1': 22, 'n2': 22, 'test_result': WilcoxonResult(statistic=0.0, pvalue=0.15729920705028502), 'effect_size': 0.0, 'N': 44}

#### ('burger', 2) vs ('burger', 5)

{'n1': 22, 'n2': 22, 'test_result': WilcoxonResult(statistic=3.0, pvalue=0.17971249487899976), 'effect_size': 0.0030975735673722249, 'N': 44}

#### ('burger', 2) vs ('swipe', 1)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=285.0, pvalue=0.23222527082050248), 'effect_size': 0.074675324675324672, 'N': 50}

#### ('burger', 2) vs ('swipe', 2)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=265.0, pvalue=0.13717816505985114), 'effect_size': 0.13961038961038963, 'N': 50}

#### ('burger', 2) vs ('swipe', 3)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=226.0, pvalue=0.025658789178159933), 'effect_size': 0.26623376623376627, 'N': 50}

#### ('burger', 2) vs ('swipe', 4)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=276.0, pvalue=0.20268150101021792), 'effect_size': 0.10389610389610393, 'N': 50}

#### ('burger', 2) vs ('swipe', 5)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=252.0, pvalue=0.082343202897603662), 'effect_size': 0.18181818181818177, 'N': 50}

#### ('burger', 3) vs ('burger', 4)

{'n1': 22, 'n2': 22, 'test_result': WilcoxonResult(statistic=2.5, pvalue=0.31731050786291415), 'effect_size': 0.0025813113061435209, 'N': 44}

#### ('burger', 3) vs ('burger', 5)

{'n1': 22, 'n2': 22, 'test_result': WilcoxonResult(statistic=3.0, pvalue=0.17971249487899976), 'effect_size': 0.0030975735673722249, 'N': 44}

#### ('burger', 3) vs ('swipe', 1)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=285.0, pvalue=0.23222527082050248), 'effect_size': 0.074675324675324672, 'N': 50}

#### ('burger', 3) vs ('swipe', 2)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=265.0, pvalue=0.13717816505985114), 'effect_size': 0.13961038961038963, 'N': 50}

#### ('burger', 3) vs ('swipe', 3)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=226.0, pvalue=0.025658789178159933), 'effect_size': 0.26623376623376627, 'N': 50}

#### ('burger', 3) vs ('swipe', 4)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=276.0, pvalue=0.20268150101021792), 'effect_size': 0.10389610389610393, 'N': 50}

#### ('burger', 3) vs ('swipe', 5)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=252.0, pvalue=0.082343202897603662), 'effect_size': 0.18181818181818177, 'N': 50}

#### ('burger', 4) vs ('burger', 5)

{'n1': 22, 'n2': 22, 'test_result': WilcoxonResult(statistic=2.0, pvalue=0.5637028616507731), 'effect_size': 0.0020650490449148169, 'N': 44}

#### ('burger', 4) vs ('swipe', 1)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=303.0, pvalue=0.43281068947535356), 'effect_size': 0.016233766233766267, 'N': 50}

#### ('burger', 4) vs ('swipe', 2)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=237.0, pvalue=0.027429809187369383), 'effect_size': 0.23051948051948057, 'N': 50}

#### ('burger', 4) vs ('swipe', 3)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=201.0, pvalue=0.0040041913682163349), 'effect_size': 0.34740259740259738, 'N': 50}

#### ('burger', 4) vs ('swipe', 4)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=248.0, pvalue=0.046661220530755103), 'effect_size': 0.19480519480519476, 'N': 50}

#### ('burger', 4) vs ('swipe', 5)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=225.0, pvalue=0.014890923602395365), 'effect_size': 0.26948051948051943, 'N': 50}

#### ('burger', 5) vs ('swipe', 1)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=289.0, pvalue=0.22085511431458626), 'effect_size': 0.061688311688311681, 'N': 50}

#### ('burger', 5) vs ('swipe', 2)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=223.0, pvalue=0.0085809342731982628), 'effect_size': 0.27597402597402598, 'N': 50}

#### ('burger', 5) vs ('swipe', 3)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=188.5, pvalue=0.0011982167922993706), 'effect_size': 0.38798701298701299, 'N': 50}

#### ('burger', 5) vs ('swipe', 4)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=234.0, pvalue=0.015452252565939647), 'effect_size': 0.24025974025974028, 'N': 50}

#### ('burger', 5) vs ('swipe', 5)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=211.5, pvalue=0.0045566881958452573), 'effect_size': 0.31331168831168832, 'N': 50}

#### ('swipe', 1) vs ('swipe', 2)

{'n1': 28, 'n2': 28, 'test_result': WilcoxonResult(statistic=4.5, pvalue=0.033894853524689246), 'effect_size': 0.0028689831048772712, 'N': 56}

#### ('swipe', 1) vs ('swipe', 3)

{'n1': 28, 'n2': 28, 'test_result': WilcoxonResult(statistic=5.0, pvalue=0.0050991474349813982), 'effect_size': 0.0031877590054191903, 'N': 56}

#### ('swipe', 1) vs ('swipe', 4)

{'n1': 28, 'n2': 28, 'test_result': WilcoxonResult(statistic=18.0, pvalue=0.13166801602281422), 'effect_size': 0.011475932419509085, 'N': 56}

#### ('swipe', 1) vs ('swipe', 5)

{'n1': 28, 'n2': 28, 'test_result': WilcoxonResult(statistic=11.0, pvalue=0.032509444645719511), 'effect_size': 0.0070130698119222189, 'N': 56}

#### ('swipe', 2) vs ('swipe', 3)

{'n1': 28, 'n2': 28, 'test_result': WilcoxonResult(statistic=30.0, pvalue=0.13458487139107694), 'effect_size': 0.01912655403251514, 'N': 56}

#### ('swipe', 2) vs ('swipe', 4)

{'n1': 28, 'n2': 28, 'test_result': WilcoxonResult(statistic=42.0, pvalue=0.7815112949987133), 'effect_size': 0.026777175645521199, 'N': 56}

#### ('swipe', 2) vs ('swipe', 5)

{'n1': 28, 'n2': 28, 'test_result': WilcoxonResult(statistic=52.5, pvalue=0.63735188823393707), 'effect_size': 0.033471469556901501, 'N': 56}

#### ('swipe', 3) vs ('swipe', 4)

{'n1': 28, 'n2': 28, 'test_result': WilcoxonResult(statistic=35.0, pvalue=0.068594778422537167), 'effect_size': 0.022314313037934332, 'N': 56}

#### ('swipe', 3) vs ('swipe', 5)

{'n1': 28, 'n2': 28, 'test_result': WilcoxonResult(statistic=58.0, pvalue=0.35511621808512916), 'effect_size': 0.036978004462862604, 'N': 56}

#### ('swipe', 4) vs ('swipe', 5)

{'n1': 28, 'n2': 28, 'test_result': WilcoxonResult(statistic=30.0, pvalue=0.43857802608099983), 'effect_size': 0.01912655403251514, 'N': 56}

### Global Burger vs Swipe per tid Tests (effectiveness)

#### burger vs swipe 1

{'n1': 110, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=1537.0, pvalue=0.49020683242704011), 'effect_size': 0.0019480519480519209, 'N': 138}

#### burger vs swipe 2

{'n1': 110, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=1213.0, pvalue=0.0027313254754476467), 'effect_size': 0.21233766233766238, 'N': 138}

#### burger vs swipe 3

{'n1': 110, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=1030.0, pvalue=2.0615949541882224e-05), 'effect_size': 0.33116883116883122, 'N': 138}

#### burger vs swipe 4

{'n1': 110, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=1268.0, pvalue=0.0092023144768541426), 'effect_size': 0.17662337662337657, 'N': 138}

#### burger vs swipe 5

{'n1': 110, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=1152.0, pvalue=0.00061159598135044442), 'effect_size': 0.25194805194805192, 'N': 138}

### Global Burger vs Global Swipe Test (effectiveness)

#### burger vs swipe

{'n1': 110, 'n2': 140, 'test_result': MannwhitneyuResult(statistic=6206.0, pvalue=0.00011462735661581992), 'effect_size': 0.19402597402597399, 'N': 250}

## Task Questionnaires

### Task Question 0

#### Descriptions (result)

##### Global Descriptions (result)

###### burger

|  |result |
| -|------ |
| count|110.0 |
| mean|6.90909090909 |
| std|0.395976427467 |
| min|4.0 |
| 25%|7.0 |
| 50%|7.0 |
| 75%|7.0 |
| max|7.0 |

| normaltest
| NormaltestResult(statistic=153.41323829366706, pvalue=4.861145039338043e-34)

###### swipe

|  |result |
| -|------ |
| count|140.0 |
| mean|6.83571428571 |
| std|0.458504203722 |
| min|5.0 |
| 25%|7.0 |
| 50%|7.0 |
| 75%|7.0 |
| max|7.0 |

| normaltest
| NormaltestResult(statistic=101.53235210749389, pvalue=8.9645784582099588e-23)

##### Repeated measures (result)

###### burger

| KruskalResult(statistic=2.4526192106750853, pvalue=0.65313967433502973)
| FriedmanchisquareResult(statistic=3.3103448275862144, pvalue=0.50729488262873967)

###### swipe

| KruskalResult(statistic=1.7694225721785437, pvalue=0.77807166799688021)
| FriedmanchisquareResult(statistic=5.0958904109588801, pvalue=0.27759929640181424)

##### Descriptions per tid (result)

###### ('burger', 1)

|  |result |
| -|------ |
| count|22.0 |
| mean|7.0 |
| std|0.0 |
| min|7.0 |
| 25%|7.0 |
| 50%|7.0 |
| 75%|7.0 |
| max|7.0 |

| normaltest
| NormaltestResult(statistic=1.0828149152562685, pvalue=0.58192863582398746)

###### ('burger', 2)

|  |result |
| -|------ |
| count|22.0 |
| mean|6.90909090909 |
| std|0.294244943168 |
| min|6.0 |
| 25%|7.0 |
| 50%|7.0 |
| 75%|7.0 |
| max|7.0 |

| normaltest
| NormaltestResult(statistic=32.977747192506648, pvalue=6.901971860763698e-08)

###### ('burger', 3)

|  |result |
| -|------ |
| count|22.0 |
| mean|6.77272727273 |
| std|0.751621623515 |
| min|4.0 |
| 25%|7.0 |
| 50%|7.0 |
| 75%|7.0 |
| max|7.0 |

| normaltest
| NormaltestResult(statistic=37.132620570418851, pvalue=8.6447789726675352e-09)

###### ('burger', 4)

|  |result |
| -|------ |
| count|22.0 |
| mean|6.90909090909 |
| std|0.294244943168 |
| min|6.0 |
| 25%|7.0 |
| 50%|7.0 |
| 75%|7.0 |
| max|7.0 |

| normaltest
| NormaltestResult(statistic=32.977747192506648, pvalue=6.901971860763698e-08)

###### ('burger', 5)

|  |result |
| -|------ |
| count|22.0 |
| mean|6.95454545455 |
| std|0.213200716356 |
| min|6.0 |
| 25%|7.0 |
| 50%|7.0 |
| 75%|7.0 |
| max|7.0 |

| normaltest
| NormaltestResult(statistic=55.867295667147516, pvalue=7.3887485384492e-13)

###### ('swipe', 1)

|  |result |
| -|------ |
| count|28.0 |
| mean|6.85714285714 |
| std|0.448395139423 |
| min|5.0 |
| 25%|7.0 |
| 50%|7.0 |
| 75%|7.0 |
| max|7.0 |

| normaltest
| NormaltestResult(statistic=43.18815831051505, pvalue=4.1861094680904202e-10)

###### ('swipe', 2)

|  |result |
| -|------ |
| count|28.0 |
| mean|6.92857142857 |
| std|0.262265264156 |
| min|6.0 |
| 25%|7.0 |
| 50%|7.0 |
| 75%|7.0 |
| max|7.0 |

| normaltest
| NormaltestResult(statistic=44.203532340976452, pvalue=2.5195612001886847e-10)

###### ('swipe', 3)

|  |result |
| -|------ |
| count|28.0 |
| mean|6.82142857143 |
| std|0.475594865606 |
| min|5.0 |
| 25%|7.0 |
| 50%|7.0 |
| 75%|7.0 |
| max|7.0 |

| normaltest
| NormaltestResult(statistic=34.427175981240801, pvalue=3.3437494037083985e-08)

###### ('swipe', 4)

|  |result |
| -|------ |
| count|28.0 |
| mean|6.82142857143 |
| std|0.475594865606 |
| min|5.0 |
| 25%|7.0 |
| 50%|7.0 |
| 75%|7.0 |
| max|7.0 |

| normaltest
| NormaltestResult(statistic=34.427175981240801, pvalue=3.3437494037083985e-08)

###### ('swipe', 5)

|  |result |
| -|------ |
| count|28.0 |
| mean|6.75 |
| std|0.585314097381 |
| min|5.0 |
| 25%|7.0 |
| 50%|7.0 |
| 75%|7.0 |
| max|7.0 |

| normaltest
| NormaltestResult(statistic=24.938342419703677, pvalue=3.843330652607647e-06)

#### Cross-compare Tests per tid (result)

##### ('burger', 1) vs ('burger', 2)

{'n1': 22, 'n2': 22, 'test_result': WilcoxonResult(statistic=0.0, pvalue=0.15729920705028502), 'effect_size': 0.0, 'N': 44}

##### ('burger', 1) vs ('burger', 3)

{'n1': 22, 'n2': 22, 'test_result': WilcoxonResult(statistic=0.0, pvalue=0.17971249487899976), 'effect_size': 0.0, 'N': 44}

##### ('burger', 1) vs ('burger', 4)

{'n1': 22, 'n2': 22, 'test_result': WilcoxonResult(statistic=0.0, pvalue=0.15729920705028502), 'effect_size': 0.0, 'N': 44}

##### ('burger', 1) vs ('burger', 5)

{'n1': 22, 'n2': 22, 'test_result': WilcoxonResult(statistic=0.0, pvalue=0.31731050786291415), 'effect_size': 0.0, 'N': 44}

##### ('burger', 1) vs ('swipe', 1)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=275.0, pvalue=0.061389171314485569), 'effect_size': 0.1071428571428571, 'N': 50}

##### ('burger', 1) vs ('swipe', 2)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=286.0, pvalue=0.10790037602663682), 'effect_size': 0.071428571428571397, 'N': 50}

##### ('burger', 1) vs ('swipe', 3)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=264.0, pvalue=0.035323810007342034), 'effect_size': 0.1428571428571429, 'N': 50}

##### ('burger', 1) vs ('swipe', 4)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=264.0, pvalue=0.035323810007342034), 'effect_size': 0.1428571428571429, 'N': 50}

##### ('burger', 1) vs ('swipe', 5)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=253.0, pvalue=0.020341356769343476), 'effect_size': 0.1785714285714286, 'N': 50}

##### ('burger', 2) vs ('burger', 3)

{'n1': 22, 'n2': 22, 'test_result': WilcoxonResult(statistic=3.0, pvalue=0.46145098783336069), 'effect_size': 0.0030975735673722249, 'N': 44}

##### ('burger', 2) vs ('burger', 4)

{'n1': 22, 'n2': 22, 'test_result': WilcoxonResult(statistic=5.0, pvalue=1.0), 'effect_size': 0.0051626226122870418, 'N': 44}

##### ('burger', 2) vs ('burger', 5)

{'n1': 22, 'n2': 22, 'test_result': WilcoxonResult(statistic=2.0, pvalue=0.5637028616507731), 'effect_size': 0.0020650490449148169, 'N': 44}

##### ('burger', 2) vs ('swipe', 1)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=302.0, pvalue=0.41814383343092509), 'effect_size': 0.019480519480519431, 'N': 50}

##### ('burger', 2) vs ('swipe', 2)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=302.0, pvalue=0.40954587077471732), 'effect_size': 0.019480519480519431, 'N': 50}

##### ('burger', 2) vs ('swipe', 3)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=291.0, pvalue=0.28360268156813595), 'effect_size': 0.055194805194805241, 'N': 50}

##### ('burger', 2) vs ('swipe', 4)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=291.0, pvalue=0.28360268156813595), 'effect_size': 0.055194805194805241, 'N': 50}

##### ('burger', 2) vs ('swipe', 5)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=279.0, pvalue=0.1776214834950835), 'effect_size': 0.094155844155844104, 'N': 50}

##### ('burger', 3) vs ('burger', 4)

{'n1': 22, 'n2': 22, 'test_result': WilcoxonResult(statistic=1.5, pvalue=0.41421617824252521), 'effect_size': 0.0015487867836861124, 'N': 44}

##### ('burger', 3) vs ('burger', 5)

{'n1': 22, 'n2': 22, 'test_result': WilcoxonResult(statistic=0.0, pvalue=0.17971249487899976), 'effect_size': 0.0, 'N': 44}

##### ('burger', 3) vs ('swipe', 1)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=305.5, pvalue=0.47007151426311133), 'effect_size': 0.008116883116883078, 'N': 50}

##### ('burger', 3) vs ('swipe', 2)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=300.0, pvalue=0.37768095297605236), 'effect_size': 0.025974025974025983, 'N': 50}

##### ('burger', 3) vs ('swipe', 3)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=295.5, pvalue=0.3388315325050939), 'effect_size': 0.040584415584415612, 'N': 50}

##### ('burger', 3) vs ('swipe', 4)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=295.5, pvalue=0.3388315325050939), 'effect_size': 0.040584415584415612, 'N': 50}

##### ('burger', 3) vs ('swipe', 5)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=285.0, pvalue=0.23293475501797717), 'effect_size': 0.074675324675324672, 'N': 50}

##### ('burger', 4) vs ('burger', 5)

{'n1': 22, 'n2': 22, 'test_result': WilcoxonResult(statistic=0.0, pvalue=0.31731050786291415), 'effect_size': 0.0, 'N': 44}

##### ('burger', 4) vs ('swipe', 1)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=302.0, pvalue=0.41814383343092509), 'effect_size': 0.019480519480519431, 'N': 50}

##### ('burger', 4) vs ('swipe', 2)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=302.0, pvalue=0.40954587077471732), 'effect_size': 0.019480519480519431, 'N': 50}

##### ('burger', 4) vs ('swipe', 3)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=291.0, pvalue=0.28360268156813595), 'effect_size': 0.055194805194805241, 'N': 50}

##### ('burger', 4) vs ('swipe', 4)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=291.0, pvalue=0.28360268156813595), 'effect_size': 0.055194805194805241, 'N': 50}

##### ('burger', 4) vs ('swipe', 5)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=279.0, pvalue=0.1776214834950835), 'effect_size': 0.094155844155844104, 'N': 50}

##### ('burger', 5) vs ('swipe', 1)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=288.5, pvalue=0.21488485789583234), 'effect_size': 0.063311688311688319, 'N': 50}

##### ('burger', 5) vs ('swipe', 2)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=300.0, pvalue=0.36081607462259746), 'effect_size': 0.025974025974025983, 'N': 50}

##### ('burger', 5) vs ('swipe', 3)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=277.5, pvalue=0.12983938884427548), 'effect_size': 0.099025974025974017, 'N': 50}

##### ('burger', 5) vs ('swipe', 4)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=277.5, pvalue=0.12983938884427548), 'effect_size': 0.099025974025974017, 'N': 50}

##### ('burger', 5) vs ('swipe', 5)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=266.0, pvalue=0.07519977300947886), 'effect_size': 0.13636363636363635, 'N': 50}

##### ('swipe', 1) vs ('swipe', 2)

{'n1': 28, 'n2': 28, 'test_result': WilcoxonResult(statistic=1.5, pvalue=0.41421617824252521), 'effect_size': 0.00095632770162575704, 'N': 56}

##### ('swipe', 1) vs ('swipe', 3)

{'n1': 28, 'n2': 28, 'test_result': WilcoxonResult(statistic=2.0, pvalue=0.5637028616507731), 'effect_size': 0.0012751036021676761, 'N': 56}

##### ('swipe', 1) vs ('swipe', 4)

{'n1': 28, 'n2': 28, 'test_result': WilcoxonResult(statistic=2.0, pvalue=0.5637028616507731), 'effect_size': 0.0012751036021676761, 'N': 56}

##### ('swipe', 1) vs ('swipe', 5)

{'n1': 28, 'n2': 28, 'test_result': WilcoxonResult(statistic=0.0, pvalue=0.083264516663550406), 'effect_size': 0.0, 'N': 56}

##### ('swipe', 2) vs ('swipe', 3)

{'n1': 28, 'n2': 28, 'test_result': WilcoxonResult(statistic=2.0, pvalue=0.25683925795785656), 'effect_size': 0.0012751036021676761, 'N': 56}

##### ('swipe', 2) vs ('swipe', 4)

{'n1': 28, 'n2': 28, 'test_result': WilcoxonResult(statistic=2.0, pvalue=0.25683925795785656), 'effect_size': 0.0012751036021676761, 'N': 56}

##### ('swipe', 2) vs ('swipe', 5)

{'n1': 28, 'n2': 28, 'test_result': WilcoxonResult(statistic=0.0, pvalue=0.058781721355358862), 'effect_size': 0.0, 'N': 56}

##### ('swipe', 3) vs ('swipe', 4)

{'n1': 28, 'n2': 28, 'test_result': '=== All pairs were equal ===', 'effect_size': '=== All pairs were equal ===', 'N': 56}

##### ('swipe', 3) vs ('swipe', 5)

{'n1': 28, 'n2': 28, 'test_result': WilcoxonResult(statistic=1.5, pvalue=0.41421617824252521), 'effect_size': 0.00095632770162575704, 'N': 56}

##### ('swipe', 4) vs ('swipe', 5)

{'n1': 28, 'n2': 28, 'test_result': WilcoxonResult(statistic=1.5, pvalue=0.41421617824252521), 'effect_size': 0.00095632770162575704, 'N': 56}

#### Global Burger vs Swipe per tid Tests (result)

##### burger vs swipe 1

{'n1': 110, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=1473.0, pvalue=0.21665236926243431), 'effect_size': 0.043506493506493493, 'N': 138}

##### burger vs swipe 2

{'n1': 110, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=1530.0, pvalue=0.45320928415997419), 'effect_size': 0.0064935064935064402, 'N': 138}

##### burger vs swipe 3

{'n1': 110, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=1419.0, pvalue=0.087083010808927386), 'effect_size': 0.078571428571428625, 'N': 138}

##### burger vs swipe 4

{'n1': 110, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=1419.0, pvalue=0.087083010808927386), 'effect_size': 0.078571428571428625, 'N': 138}

##### burger vs swipe 5

{'n1': 110, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=1362.0, pvalue=0.027199345369874211), 'effect_size': 0.11558441558441557, 'N': 138}

#### Global Burger vs Global Swipe Test (result)

##### burger vs swipe

{'n1': 110, 'n2': 140, 'test_result': MannwhitneyuResult(statistic=7203.0, pvalue=0.046318608676750285), 'effect_size': 0.064545454545454573, 'N': 250}

### Task Question 1

#### Descriptions (result)

##### Global Descriptions (result)

###### burger

|  |result |
| -|------ |
| count|110.0 |
| mean|1.89090909091 |
| std|1.80897585981 |
| min|1.0 |
| 25%|1.0 |
| 50%|1.0 |
| 75%|1.0 |
| max|7.0 |

| normaltest
| NormaltestResult(statistic=41.10183363779808, pvalue=1.1880924265582291e-09)

###### swipe

|  |result |
| -|------ |
| count|140.0 |
| mean|2.86428571429 |
| std|2.12964925773 |
| min|1.0 |
| 25%|1.0 |
| 50%|2.0 |
| 75%|4.0 |
| max|7.0 |

| normaltest
| NormaltestResult(statistic=18.788553344848623, pvalue=8.3198879945244137e-05)

##### Repeated measures (result)

###### burger

| KruskalResult(statistic=0.78069084963312274, pvalue=0.94101782074422269)
| FriedmanchisquareResult(statistic=2.7575757575757125, pvalue=0.59917784877228941)

###### swipe

| KruskalResult(statistic=2.0615941350657225, pvalue=0.72443103796977781)
| FriedmanchisquareResult(statistic=5.4968553459119409, pvalue=0.24000603548291879)

##### Descriptions per tid (result)

###### ('burger', 1)

|  |result |
| -|------ |
| count|22.0 |
| mean|1.95454545455 |
| std|2.01133153544 |
| min|1.0 |
| 25%|1.0 |
| 50%|1.0 |
| 75%|1.0 |
| max|7.0 |

| normaltest
| NormaltestResult(statistic=14.852104558574464, pvalue=0.00059553387888821891)

###### ('burger', 2)

|  |result |
| -|------ |
| count|22.0 |
| mean|1.77272727273 |
| std|1.87545088374 |
| min|1.0 |
| 25%|1.0 |
| 50%|1.0 |
| 75%|1.0 |
| max|7.0 |

| normaltest
| NormaltestResult(statistic=20.210686165265589, pvalue=4.08606491047461e-05)

###### ('burger', 3)

|  |result |
| -|------ |
| count|22.0 |
| mean|2.0 |
| std|1.74574312189 |
| min|1.0 |
| 25%|1.0 |
| 50%|1.0 |
| 75%|2.0 |
| max|6.0 |

| normaltest
| NormaltestResult(statistic=9.2076296409072071, pvalue=0.010013562844574659)

###### ('burger', 4)

|  |result |
| -|------ |
| count|22.0 |
| mean|1.77272727273 |
| std|1.54092792643 |
| min|1.0 |
| 25%|1.0 |
| 50%|1.0 |
| 75%|1.0 |
| max|6.0 |

| normaltest
| NormaltestResult(statistic=13.258524513028126, pvalue=0.0013211373870855303)

###### ('burger', 5)

|  |result |
| -|------ |
| count|22.0 |
| mean|1.95454545455 |
| std|1.98751514465 |
| min|1.0 |
| 25%|1.0 |
| 50%|1.0 |
| 75%|1.0 |
| max|7.0 |

| normaltest
| NormaltestResult(statistic=13.11454314032791, pvalue=0.0014197541301194895)

###### ('swipe', 1)

|  |result |
| -|------ |
| count|28.0 |
| mean|2.75 |
| std|2.36682315602 |
| min|1.0 |
| 25%|1.0 |
| 50%|1.0 |
| 75%|4.25 |
| max|7.0 |

| normaltest
| NormaltestResult(statistic=5.6255405651946386, pvalue=0.060038438357067736)

###### ('swipe', 2)

|  |result |
| -|------ |
| count|28.0 |
| mean|2.67857142857 |
| std|2.21198036674 |
| min|1.0 |
| 25%|1.0 |
| 50%|1.0 |
| 75%|4.0 |
| max|7.0 |

| normaltest
| NormaltestResult(statistic=4.9857181545995557, pvalue=0.082673259115518136)

###### ('swipe', 3)

|  |result |
| -|------ |
| count|28.0 |
| mean|2.82142857143 |
| std|2.16116517662 |
| min|1.0 |
| 25%|1.0 |
| 50%|2.0 |
| 75%|4.0 |
| max|7.0 |

| normaltest
| NormaltestResult(statistic=4.8948691150333712, pvalue=0.086515251945615837)

###### ('swipe', 4)

|  |result |
| -|------ |
| count|28.0 |
| mean|2.85714285714 |
| std|1.87999774851 |
| min|1.0 |
| 25%|1.0 |
| 50%|3.0 |
| 75%|4.0 |
| max|7.0 |

| normaltest
| NormaltestResult(statistic=3.2631829602951457, pvalue=0.19561800409388738)

###### ('swipe', 5)

|  |result |
| -|------ |
| count|28.0 |
| mean|3.21428571429 |
| std|2.11445015806 |
| min|1.0 |
| 25%|1.0 |
| 50%|3.0 |
| 75%|4.0 |
| max|7.0 |

| normaltest
| NormaltestResult(statistic=2.7864677335567007, pvalue=0.24827112927752484)

#### Cross-compare Tests per tid (result)

##### ('burger', 1) vs ('burger', 2)

{'n1': 22, 'n2': 22, 'test_result': WilcoxonResult(statistic=7.5, pvalue=1.0), 'effect_size': 0.0077439339184305631, 'N': 44}

##### ('burger', 1) vs ('burger', 3)

{'n1': 22, 'n2': 22, 'test_result': WilcoxonResult(statistic=14.0, pvalue=0.56869370493349436), 'effect_size': 0.014455343314403717, 'N': 44}

##### ('burger', 1) vs ('burger', 4)

{'n1': 22, 'n2': 22, 'test_result': WilcoxonResult(statistic=6.0, pvalue=0.68027954733445029), 'effect_size': 0.0061951471347444498, 'N': 44}

##### ('burger', 1) vs ('burger', 5)

{'n1': 22, 'n2': 22, 'test_result': WilcoxonResult(statistic=5.0, pvalue=1.0), 'effect_size': 0.0051626226122870418, 'N': 44}

##### ('burger', 1) vs ('swipe', 1)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=247.5, pvalue=0.082098002975044604), 'effect_size': 0.1964285714285714, 'N': 50}

##### ('burger', 1) vs ('swipe', 2)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=241.5, pvalue=0.066396878662638464), 'effect_size': 0.21590909090909094, 'N': 50}

##### ('burger', 1) vs ('swipe', 3)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=213.5, pvalue=0.020092875062028004), 'effect_size': 0.30681818181818177, 'N': 50}

##### ('burger', 1) vs ('swipe', 4)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=198.5, pvalue=0.010019521264436585), 'effect_size': 0.35551948051948057, 'N': 50}

##### ('burger', 1) vs ('swipe', 5)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=192.0, pvalue=0.0068101408106697112), 'effect_size': 0.37662337662337664, 'N': 50}

##### ('burger', 2) vs ('burger', 3)

{'n1': 22, 'n2': 22, 'test_result': WilcoxonResult(statistic=6.5, pvalue=0.39510806859049219), 'effect_size': 0.0067114093959731542, 'N': 44}

##### ('burger', 2) vs ('burger', 4)

{'n1': 22, 'n2': 22, 'test_result': WilcoxonResult(statistic=10.5, pvalue=1.0), 'effect_size': 0.010841507485802787, 'N': 44}

##### ('burger', 2) vs ('burger', 5)

{'n1': 22, 'n2': 22, 'test_result': WilcoxonResult(statistic=9.0, pvalue=0.73888268036352733), 'effect_size': 0.0092927207021166747, 'N': 44}

##### ('burger', 2) vs ('swipe', 1)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=232.5, pvalue=0.038182542965196922), 'effect_size': 0.24512987012987009, 'N': 50}

##### ('burger', 2) vs ('swipe', 2)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=225.5, pvalue=0.028699028147674787), 'effect_size': 0.2678571428571429, 'N': 50}

##### ('burger', 2) vs ('swipe', 3)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=194.5, pvalue=0.0062373933525989578), 'effect_size': 0.36850649350649356, 'N': 50}

##### ('burger', 2) vs ('swipe', 4)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=179.5, pvalue=0.0028888514521789059), 'effect_size': 0.41720779220779225, 'N': 50}

##### ('burger', 2) vs ('swipe', 5)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=173.0, pvalue=0.001845925801493757), 'effect_size': 0.43831168831168832, 'N': 50}

##### ('burger', 3) vs ('burger', 4)

{'n1': 22, 'n2': 22, 'test_result': WilcoxonResult(statistic=9.0, pvalue=0.3885437838475907), 'effect_size': 0.0092927207021166747, 'N': 44}

##### ('burger', 3) vs ('burger', 5)

{'n1': 22, 'n2': 22, 'test_result': WilcoxonResult(statistic=13.0, pvalue=0.86456930168674195), 'effect_size': 0.013422818791946308, 'N': 44}

##### ('burger', 3) vs ('swipe', 1)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=260.5, pvalue=0.14603135541294709), 'effect_size': 0.15422077922077926, 'N': 50}

##### ('burger', 3) vs ('swipe', 2)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=256.0, pvalue=0.12750985422970523), 'effect_size': 0.16883116883116878, 'N': 50}

##### ('burger', 3) vs ('swipe', 3)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=230.0, pvalue=0.049115891184390158), 'effect_size': 0.25324675324675328, 'N': 50}

##### ('burger', 3) vs ('swipe', 4)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=215.0, pvalue=0.026326679220802538), 'effect_size': 0.30194805194805197, 'N': 50}

##### ('burger', 3) vs ('swipe', 5)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=203.5, pvalue=0.014613622667340618), 'effect_size': 0.3392857142857143, 'N': 50}

##### ('burger', 4) vs ('burger', 5)

{'n1': 22, 'n2': 22, 'test_result': WilcoxonResult(statistic=1.5, pvalue=0.19364643126922065), 'effect_size': 0.0015487867836861124, 'N': 44}

##### ('burger', 4) vs ('swipe', 1)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=238.5, pvalue=0.054909704407618581), 'effect_size': 0.22564935064935066, 'N': 50}

##### ('burger', 4) vs ('swipe', 2)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=233.0, pvalue=0.044870412680933683), 'effect_size': 0.24350649350649356, 'N': 50}

##### ('burger', 4) vs ('swipe', 3)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=209.0, pvalue=0.015775210433546256), 'effect_size': 0.3214285714285714, 'N': 50}

##### ('burger', 4) vs ('swipe', 4)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=192.5, pvalue=0.0070352388832014452), 'effect_size': 0.375, 'N': 50}

##### ('burger', 4) vs ('swipe', 5)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=183.5, pvalue=0.0040067153811422793), 'effect_size': 0.40422077922077926, 'N': 50}

##### ('burger', 5) vs ('swipe', 1)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=246.0, pvalue=0.077014874525015403), 'effect_size': 0.20129870129870131, 'N': 50}

##### ('burger', 5) vs ('swipe', 2)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=240.5, pvalue=0.063535812872022673), 'effect_size': 0.2191558441558441, 'N': 50}

##### ('burger', 5) vs ('swipe', 3)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=211.5, pvalue=0.01809715117525822), 'effect_size': 0.31331168831168832, 'N': 50}

##### ('burger', 5) vs ('swipe', 4)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=198.5, pvalue=0.010033737896491264), 'effect_size': 0.35551948051948057, 'N': 50}

##### ('burger', 5) vs ('swipe', 5)

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=190.5, pvalue=0.0062419441538161761), 'effect_size': 0.38149350649350644, 'N': 50}

##### ('swipe', 1) vs ('swipe', 2)

{'n2': 28, 'test_result': Ttest_relResult(statistic=0.18569533817705183, pvalue=0.8540717092857345), 'N': 56, 'n1': 28, 'df': 27, 'effect_size': 0.035093120317179816}

##### ('swipe', 1) vs ('swipe', 3)

{'n2': 28, 'test_result': Ttest_relResult(statistic=-0.25384865729693323, pvalue=0.80153564704995517), 'N': 56, 'n1': 28, 'df': 27, 'effect_size': -0.047972886989667646}

##### ('swipe', 1) vs ('swipe', 4)

{'n2': 28, 'test_result': Ttest_relResult(statistic=-0.2825869881107243, pvalue=0.77964854494580593), 'N': 56, 'n1': 28, 'df': 27, 'effect_size': -0.05340392102026733}

##### ('swipe', 1) vs ('swipe', 5)

{'n2': 28, 'test_result': Ttest_relResult(statistic=-1.2118660185275947, pvalue=0.23606280739392285), 'N': 56, 'n1': 28, 'df': 27, 'effect_size': -0.22902115052528635}

##### ('swipe', 2) vs ('swipe', 3)

{'n2': 28, 'test_result': Ttest_relResult(statistic=-0.53737329062387895, pvalue=0.5954113366515259), 'N': 56, 'n1': 28, 'df': 27, 'effect_size': -0.10155400629994435}

##### ('swipe', 2) vs ('swipe', 4)

{'n2': 28, 'test_result': Ttest_relResult(statistic=-0.50083542247063328, pvalue=0.62054550807787923), 'N': 56, 'n1': 28, 'df': 27, 'effect_size': -0.094648998259233286}

##### ('swipe', 2) vs ('swipe', 5)

{'n2': 28, 'test_result': Ttest_relResult(statistic=-1.5616592479102798, pvalue=0.13001443262320639), 'N': 56, 'n1': 28, 'df': 27, 'effect_size': -0.29512585732819752}

##### ('swipe', 3) vs ('swipe', 4)

{'n2': 28, 'test_result': Ttest_relResult(statistic=-0.11824716716574642, pvalue=0.90674715458336475), 'N': 56, 'n1': 28, 'df': 27, 'effect_size': -0.022346614111317671}

##### ('swipe', 3) vs ('swipe', 5)

{'n2': 28, 'test_result': Ttest_relResult(statistic=-1.4607872576624297, pvalue=0.15561417089917387), 'N': 56, 'n1': 28, 'df': 27, 'effect_size': -0.27606284301048722}

##### ('swipe', 4) vs ('swipe', 5)

{'n2': 28, 'test_result': Ttest_relResult(statistic=-1.2048289933537484, pvalue=0.23872409198062031), 'N': 56, 'n1': 28, 'df': 27, 'effect_size': -0.22769127776959361}

#### Global Burger vs Swipe per tid Tests (result)

##### burger vs swipe 1

{'n1': 110, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=1225.0, pvalue=0.017143625211004959), 'effect_size': 0.20454545454545459, 'N': 138}

##### burger vs swipe 2

{'n1': 110, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=1196.5, pvalue=0.011075983661422355), 'effect_size': 0.22305194805194806, 'N': 138}

##### burger vs swipe 3

{'n1': 110, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=1058.5, pvalue=0.00087828638876744818), 'effect_size': 0.31266233766233764, 'N': 138}

##### burger vs swipe 4

{'n1': 110, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=984.0, pvalue=0.00018652482417813029), 'effect_size': 0.36103896103896105, 'N': 138}

##### burger vs swipe 5

{'n1': 110, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=942.5, pvalue=6.5526352124271008e-05), 'effect_size': 0.38798701298701299, 'N': 138}

#### Global Burger vs Global Swipe Test (result)

##### burger vs swipe

{'n1': 110, 'n2': 140, 'test_result': MannwhitneyuResult(statistic=5406.5, pvalue=2.9062055593999374e-06), 'effect_size': 0.29785714285714282, 'N': 250}

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

#### 0 Description

|  |result |
| -|------ |
| count|50.0 |
| mean|1.52 |
| std|1.18218062089 |
| min|1.0 |
| 25%|1.0 |
| 50%|1.0 |
| 75%|1.75 |
| max|7.0 |

#### Descriptions (result)

##### Global Descriptions (result)

###### burger

|  |result |
| -|------ |
| count|22.0 |
| mean|1.5 |
| std|1.05785047102 |
| min|1.0 |
| 25%|1.0 |
| 50%|1.0 |
| 75%|1.75 |
| max|5.0 |

| normaltest
| NormaltestResult(statistic=26.197588687579557, pvalue=2.0476979566055249e-06)

###### swipe

|  |result |
| -|------ |
| count|28.0 |
| mean|1.53571428571 |
| std|1.29048204766 |
| min|1.0 |
| 25%|1.0 |
| 50%|1.0 |
| 75%|1.25 |
| max|7.0 |

| normaltest
| NormaltestResult(statistic=43.488260518740518, pvalue=3.6028336850503621e-10)

#### Global Burger vs Global Swipe Test (result)

##### burger vs swipe

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=302.5, pvalue=0.44941800310214225), 'effect_size': 0.017857142857142905, 'N': 50}

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

#### 1 Description

|  |result |
| -|------ |
| count|50.0 |
| mean|1.92 |
| std|1.49611742418 |
| min|1.0 |
| 25%|1.0 |
| 50%|1.0 |
| 75%|2.0 |
| max|6.0 |

#### Descriptions (result)

##### Global Descriptions (result)

###### burger

|  |result |
| -|------ |
| count|22.0 |
| mean|2.22727272727 |
| std|1.79766563398 |
| min|1.0 |
| 25%|1.0 |
| 50%|1.0 |
| 75%|3.5 |
| max|6.0 |

| normaltest
| NormaltestResult(statistic=4.9137570390411183, pvalue=0.085702051156163167)

###### swipe

|  |result |
| -|------ |
| count|28.0 |
| mean|1.67857142857 |
| std|1.18801332542 |
| min|1.0 |
| 25%|1.0 |
| 50%|1.0 |
| 75%|2.0 |
| max|6.0 |

| normaltest
| NormaltestResult(statistic=28.457743224410187, pvalue=6.6142342997665578e-07)

#### Global Burger vs Global Swipe Test (result)

##### burger vs swipe

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=281.0, pvalue=0.27788843237866634), 'effect_size': 0.087662337662337664, 'N': 50}

### Final Question 2

#### Just counts grouped by Results

| Navigation burger answered 1 stars:                                 17
| Navigation burger answered 2 stars:                                 5
| Navigation swipe answered 1 stars:                                 18
| Navigation swipe answered 2 stars:                                 5
| Navigation swipe answered 3 stars:                                 2
| Navigation swipe answered 4 stars:                                 2
| Navigation swipe answered 7 stars:                                 1

#### 2 Description

|  |result |
| -|------ |
| count|50.0 |
| mean|1.52 |
| std|1.09246024539 |
| min|1.0 |
| 25%|1.0 |
| 50%|1.0 |
| 75%|2.0 |
| max|7.0 |

#### Descriptions (result)

##### Global Descriptions (result)

###### burger

|  |result |
| -|------ |
| count|22.0 |
| mean|1.22727272727 |
| std|0.428932027229 |
| min|1.0 |
| 25%|1.0 |
| 50%|1.0 |
| 75%|1.0 |
| max|2.0 |

| normaltest
| NormaltestResult(statistic=7.0141044989524168, pvalue=0.029985173100470022)

###### swipe

|  |result |
| -|------ |
| count|28.0 |
| mean|1.75 |
| std|1.37773297418 |
| min|1.0 |
| 25%|1.0 |
| 50%|1.0 |
| 75%|2.0 |
| max|7.0 |

| normaltest
| NormaltestResult(statistic=30.833945386464563, pvalue=2.0160153368124402e-07)

#### Global Burger vs Global Swipe Test (result)

##### burger vs swipe

{'n1': 22, 'n2': 28, 'test_result': MannwhitneyuResult(statistic=255.5, pvalue=0.10358134878107761), 'effect_size': 0.17045454545454541, 'N': 50}

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

#### 3 Description

|  |result |
| -|------ |
| count|50.0 |
| mean|4.78 |
| std|1.56869892794 |
| min|1.0 |
| 25%|4.0 |
| 50%|5.0 |
| 75%|6.0 |
| max|7.0 |

#### Descriptions (result)

##### Global Descriptions (result)

###### burger

|  |result |
| -|------ |
| count|22.0 |
| mean|5.13636363636 |
| std|1.67034226733 |
| min|2.0 |
| 25%|3.25 |
| 50%|5.5 |
| 75%|6.75 |
| max|7.0 |

| normaltest
| NormaltestResult(statistic=4.4344935502051488, pvalue=0.1089085461474571)

###### swipe

|  |result |
| -|------ |
| count|28.0 |
| mean|4.5 |
| std|1.45296631451 |
| min|1.0 |
| 25%|4.0 |
| 50%|4.0 |
| 75%|5.25 |
| max|7.0 |

| normaltest
| NormaltestResult(statistic=0.29622233841262957, pvalue=0.86233524448851595)

#### Global Burger vs Global Swipe Test (result)

##### burger vs swipe

{'n2': 28, 'test_result': Ttest_indResult(statistic=1.4151306918873736, pvalue=0.16442349507017537), 'N': 50, 'n1': 22, 'df': 41.879320839518563, 'effect_size': 0.40317277353302849}
