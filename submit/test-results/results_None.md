
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

No normality test, *Forcing t-test*!

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

### Cross-compare Tests per tid (efficiency)

#### ('burger', 1) vs ('burger', 2)

{'effect_size': 0.66946021956115787, 'n1': 22, 'N': 44, 'test_result': Ttest_relResult(statistic=3.1400467644045085, pvalue=0.0049443978028402098), 'n2': 22, 'df': 21}

#### ('burger', 1) vs ('burger', 3)

{'effect_size': 0.8493099572214986, 'n1': 22, 'N': 44, 'test_result': Ttest_relResult(statistic=3.9836168083266799, pvalue=0.00067564806607191632), 'n2': 22, 'df': 21}

#### ('burger', 1) vs ('burger', 4)

{'effect_size': 0.60049107141057878, 'n1': 22, 'N': 44, 'test_result': Ttest_relResult(statistic=2.8165527849774352, pvalue=0.010338413955597564), 'n2': 22, 'df': 21}

#### ('burger', 1) vs ('burger', 5)

{'effect_size': 1.8817447075438416, 'n1': 22, 'N': 44, 'test_result': Ttest_relResult(statistic=8.8261650322279657, pvalue=1.6451903254595333e-08), 'n2': 22, 'df': 21}

#### ('burger', 1) vs ('swipe', 1)

{'effect_size': -1.9097298327149146, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=-6.7031245086454758, pvalue=5.6381782972874956e-08), 'n2': 28, 'df': 38.785742202473031}

#### ('burger', 1) vs ('swipe', 2)

{'effect_size': 0.54708801247960148, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=1.920271130511056, pvalue=0.06084394453973696), 'n2': 28, 'df': 47.461440359463033}

#### ('burger', 1) vs ('swipe', 3)

{'effect_size': 2.2829620500029861, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=8.0131642746175658, pvalue=3.0036765567743509e-10), 'n2': 28, 'df': 45.605549072886376}

#### ('burger', 1) vs ('swipe', 4)

{'effect_size': 2.9366881218094303, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=10.307733474302083, pvalue=3.9626211595999131e-13), 'n2': 28, 'df': 42.458884481600464}

#### ('burger', 1) vs ('swipe', 5)

{'effect_size': 3.9971846751859452, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=14.030061269834485, pvalue=1.6751765716561837e-16), 'n2': 28, 'df': 37.509707823002977}

#### ('burger', 2) vs ('burger', 3)

{'effect_size': 0.25059968919993747, 'n1': 22, 'N': 44, 'test_result': Ttest_relResult(statistic=1.17541673163024, pvalue=0.25298310480066288), 'n2': 22, 'df': 21}

#### ('burger', 2) vs ('burger', 4)

{'effect_size': -0.19503194345704855, 'n1': 22, 'N': 44, 'test_result': Ttest_relResult(statistic=-0.91478090125993261, pvalue=0.37069158497461707), 'n2': 22, 'df': 21}

#### ('burger', 2) vs ('burger', 5)

{'effect_size': 0.36443693494719148, 'n1': 22, 'N': 44, 'test_result': Ttest_relResult(statistic=1.7093607431380531, pvalue=0.10212210775377208), 'n2': 22, 'df': 21}

#### ('burger', 2) vs ('swipe', 1)

{'effect_size': -2.1964344153980879, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=-7.7094535097442627, pvalue=6.1460659425243401e-10), 'n2': 28, 'df': 47.903652892032788}

#### ('burger', 2) vs ('swipe', 2)

{'effect_size': -0.29352169691926894, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=-1.0302569749573955, pvalue=0.30895874574764653), 'n2': 28, 'df': 40.797596378640058}

#### ('burger', 2) vs ('swipe', 3)

{'effect_size': 0.8121269529860301, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=2.8505540361974759, pvalue=0.0075330728311379285), 'n2': 28, 'df': 32.392545034300269}

#### ('burger', 2) vs ('swipe', 4)

{'effect_size': 1.1871061872924931, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=4.1667258070177873, pvalue=0.00024295893165475588), 'n2': 28, 'df': 29.84388793928602}

#### ('burger', 2) vs ('swipe', 5)

{'effect_size': 1.7884292636279995, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=6.2773612390822446, pvalue=9.9419198495425322e-07), 'n2': 28, 'df': 27.169372064223619}

#### ('burger', 3) vs ('burger', 4)

{'effect_size': -0.5214909858414325, 'n1': 22, 'N': 44, 'test_result': Ttest_relResult(statistic=-2.4460095385965119, pvalue=0.023338332791632995), 'n2': 22, 'df': 21}

#### ('burger', 3) vs ('burger', 5)

{'effect_size': 0.16727413301634728, 'n1': 22, 'N': 44, 'test_result': Ttest_relResult(statistic=0.78458522971067601, pvalue=0.4414581754358432), 'n2': 22, 'df': 21}

#### ('burger', 3) vs ('swipe', 1)

{'effect_size': -2.5346208780888522, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=-8.8964831763080898, pvalue=1.638058471616648e-11), 'n2': 28, 'df': 45.413055852663888}

#### ('burger', 3) vs ('swipe', 2)

{'effect_size': -0.54746947139065949, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=-1.921610045854971, pvalue=0.060890407860921245), 'n2': 28, 'df': 45.798346041116126}

#### ('burger', 3) vs ('swipe', 3)

{'effect_size': 0.70376045931483877, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=2.470189187096973, pvalue=0.018195085242505033), 'n2': 28, 'df': 37.322733521049877}

#### ('burger', 3) vs ('swipe', 4)

{'effect_size': 1.1462100107866362, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=4.0231808100500288, pvalue=0.00030313523132898115), 'n2': 28, 'df': 33.987304407263395}

#### ('burger', 3) vs ('swipe', 5)

{'effect_size': 1.8689406873961953, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=6.5599551896199069, pvalue=2.8434885910251012e-07), 'n2': 28, 'df': 30.228298418120758}

#### ('burger', 4) vs ('burger', 5)

{'effect_size': 0.59609260976552092, 'n1': 22, 'N': 44, 'test_result': Ttest_relResult(statistic=2.7959221711584767, pvalue=0.010828183767257568), 'n2': 22, 'df': 21}

#### ('burger', 4) vs ('swipe', 1)

{'effect_size': -2.3036145286208778, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=-8.0856541803709163, pvalue=3.5438757244843004e-10), 'n2': 28, 'df': 43.071161614293338}

#### ('burger', 4) vs ('swipe', 2)

{'effect_size': -0.15045008208176169, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=-0.52807764493907217, pvalue=0.59990243168577306), 'n2': 28, 'df': 47.530062536302886}

#### ('burger', 4) vs ('swipe', 3)

{'effect_size': 1.2621200986811547, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=4.430023567415585, pvalue=6.9900388209403688e-05), 'n2': 28, 'df': 40.510976522970402}

#### ('burger', 4) vs ('swipe', 4)

{'effect_size': 1.7720819828888703, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=6.2199825165556213, pvalue=3.1960770384704573e-07), 'n2': 28, 'df': 36.907897952812725}

#### ('burger', 4) vs ('swipe', 5)

{'effect_size': 2.6020850201949877, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=9.1332813540710109, pvalue=1.7051757569924315e-10), 'n2': 28, 'df': 32.52632637459962}

#### ('burger', 5) vs ('swipe', 1)

{'effect_size': -2.919842346861758, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=-10.248605044204545, pvalue=2.045361952158588e-12), 'n2': 28, 'df': 37.431678148502876}

#### ('burger', 5) vs ('swipe', 2)

{'effect_size': -0.83665629981403178, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=-2.9366516941421579, pvalue=0.0051414786529753878), 'n2': 28, 'df': 46.583490458425899}

#### ('burger', 5) vs ('swipe', 3)

{'effect_size': 0.67859393927802347, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=2.3818550602659152, pvalue=0.021339025726255848), 'n2': 28, 'df': 46.852508622129029}

#### ('burger', 5) vs ('swipe', 4)

{'effect_size': 1.2662092998006793, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=4.4443766050942699, pvalue=5.8417405173783915e-05), 'n2': 28, 'df': 44.248400605855807}

#### ('burger', 5) vs ('swipe', 5)

{'effect_size': 2.2701377982054178, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=7.9681513334901224, pvalue=9.6399894615656076e-10), 'n2': 28, 'df': 39.442494949086644}

#### ('swipe', 1) vs ('swipe', 2)

{'effect_size': 1.6921201725332735, 'n1': 28, 'N': 56, 'test_result': Ttest_relResult(statistic=8.9538583299174999, pvalue=1.4377672965886051e-09), 'n2': 28, 'df': 27}

#### ('swipe', 1) vs ('swipe', 3)

{'effect_size': 2.465013782429549, 'n1': 28, 'N': 56, 'test_result': Ttest_relResult(statistic=13.043626893310529, pvalue=3.5969964456561358e-13), 'n2': 28, 'df': 27}

#### ('swipe', 1) vs ('swipe', 4)

{'effect_size': 2.743519328387984, 'n1': 28, 'N': 56, 'test_result': Ttest_relResult(statistic=14.517339720027108, pvalue=2.8328302970398919e-14), 'n2': 28, 'df': 27}

#### ('swipe', 1) vs ('swipe', 5)

{'effect_size': 3.2504934436751336, 'n1': 28, 'N': 56, 'test_result': Ttest_relResult(statistic=17.199994580420682, pvalue=4.4867434987762781e-16), 'n2': 28, 'df': 27}

#### ('swipe', 2) vs ('swipe', 3)

{'effect_size': 1.1377702099935221, 'n1': 28, 'N': 56, 'test_result': Ttest_relResult(statistic=6.0205140495611911, pvalue=2.0043561530050876e-06), 'n2': 28, 'df': 27}

#### ('swipe', 2) vs ('swipe', 4)

{'effect_size': 1.3859931582541019, 'n1': 28, 'N': 56, 'test_result': Ttest_relResult(statistic=7.3339864311546856, pvalue=6.8802917453985944e-08), 'n2': 28, 'df': 27}

#### ('swipe', 2) vs ('swipe', 5)

{'effect_size': 1.8185545723959244, 'n1': 28, 'N': 56, 'test_result': Ttest_relResult(statistic=9.6228862883180462, pvalue=3.2178913431071324e-10), 'n2': 28, 'df': 27}

#### ('swipe', 3) vs ('swipe', 4)

{'effect_size': 0.39642879994718772, 'n1': 28, 'N': 56, 'test_result': Ttest_relResult(statistic=2.0977040344080686, pvalue=0.04542748458455511), 'n2': 28, 'df': 27}

#### ('swipe', 3) vs ('swipe', 5)

{'effect_size': 0.9589719197604063, 'n1': 28, 'N': 56, 'test_result': Ttest_relResult(statistic=5.0744024279604449, pvalue=2.493775482784069e-05), 'n2': 28, 'df': 27}

#### ('swipe', 4) vs ('swipe', 5)

{'effect_size': 0.78096126412132294, 'n1': 28, 'N': 56, 'test_result': Ttest_relResult(statistic=4.1324585768793005, pvalue=0.00031147549191696151), 'n2': 28, 'df': 27}

### Global Burger vs Swipe per tid Tests (efficiency)

#### burger vs swipe 1

{'effect_size': -1.9870466939513429, 'n1': 110, 'N': 138, 'test_result': Ttest_indResult(statistic=-9.3873689639224214, pvalue=9.7956596089961892e-11), 'n2': 28, 'df': 32.196906556146352}

#### burger vs swipe 2

{'effect_size': -0.24788502211622654, 'n1': 110, 'N': 138, 'test_result': Ttest_indResult(statistic=-1.1710787523607482, pvalue=0.24834596113607729), 'n2': 28, 'df': 40.893196760276176}

#### burger vs swipe 3

{'effect_size': 1.1700510299170281, 'n1': 110, 'N': 138, 'test_result': Ttest_indResult(statistic=5.5276510400502614, pvalue=9.0622300016681276e-07), 'n2': 28, 'df': 55.333617103825162}

#### burger vs swipe 4

{'effect_size': 1.7700005632660121, 'n1': 110, 'N': 138, 'test_result': Ttest_indResult(statistic=8.3619818317844903, pvalue=7.0554228434676112e-12), 'n2': 28, 'df': 64.460648478482284}

#### burger vs swipe 5

{'effect_size': 2.8251881603681546, 'n1': 110, 'N': 138, 'test_result': Ttest_indResult(statistic=13.346985621733216, pvalue=3.9194832679581521e-22), 'n2': 28, 'df': 80.786408371513843}

### Global Burger vs Global Swipe Test (efficiency)

#### burger vs swipe

{'effect_size': 0.098711489643317329, 'n1': 110, 'N': 250, 'test_result': Ttest_indResult(statistic=0.77474371527385055, pvalue=0.43935007376708934), 'n2': 140, 'df': 213.05432217924604}

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

### Cross-compare Tests per tid (effectiveness)

#### ('burger', 1) vs ('burger', 2)

{'effect_size': 0.29164791418864128, 'n1': 22, 'N': 44, 'test_result': Ttest_relResult(statistic=1.3679499730300344, pvalue=0.1857887709669136), 'n2': 22, 'df': 21}

#### ('burger', 1) vs ('burger', 3)

{'effect_size': 0.29164791418864128, 'n1': 22, 'N': 44, 'test_result': Ttest_relResult(statistic=1.3679499730300344, pvalue=0.1857887709669136), 'n2': 22, 'df': 21}

#### ('burger', 1) vs ('burger', 4)

{'effect_size': 0.12118298018003469, 'n1': 22, 'N': 44, 'test_result': Ttest_relResult(statistic=0.56839856005880507, pvalue=0.57579272855240249), 'n2': 22, 'df': 21}

#### ('burger', 1) vs ('burger', 5)

{'effect_size': nan, 'n1': 22, 'N': 44, 'test_result': Ttest_relResult(statistic=nan, pvalue=nan), 'n2': 22, 'df': 21}

#### ('burger', 1) vs ('swipe', 1)

{'effect_size': 0.23466433176906615, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=0.82366846170589003, pvalue=0.41428064209770366), 'n2': 28, 'df': 47.08496053303012}

#### ('burger', 1) vs ('swipe', 2)

{'effect_size': 0.78064001159627316, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=2.7400353204522681, pvalue=0.0091946014470773128), 'n2': 28, 'df': 39.274267272770743}

#### ('burger', 1) vs ('swipe', 3)

{'effect_size': 1.0076384489725929, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=3.5367966020406145, pvalue=0.0012166207287807747), 'n2': 28, 'df': 33.276977869806174}

#### ('burger', 1) vs ('swipe', 4)

{'effect_size': 0.69772160053299137, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=2.4489928787964925, pvalue=0.018809724953796), 'n2': 28, 'df': 39.941129628992769}

#### ('burger', 1) vs ('swipe', 5)

{'effect_size': 0.85040706574694769, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=2.9849166866864385, pvalue=0.005066877024676052), 'n2': 28, 'df': 36.090509045076026}

#### ('burger', 2) vs ('burger', 3)

{'effect_size': 0.0, 'n1': 22, 'N': 44, 'test_result': Ttest_relResult(statistic=0.0, pvalue=1.0), 'n2': 22, 'df': 21}

#### ('burger', 2) vs ('burger', 4)

{'effect_size': -0.30895719032666236, 'n1': 22, 'N': 44, 'test_result': Ttest_relResult(statistic=-1.4491376746189439, pvalue=0.16206871193916239), 'n2': 22, 'df': 21}

#### ('burger', 2) vs ('burger', 5)

{'effect_size': -0.29164791418864128, 'n1': 22, 'N': 44, 'test_result': Ttest_relResult(statistic=-1.3679499730300344, pvalue=0.1857887709669136), 'n2': 22, 'df': 21}

#### ('burger', 2) vs ('swipe', 1)

{'effect_size': -0.20638031994173572, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=-0.72439198309892927, pvalue=0.47308750654179754), 'n2': 28, 'df': 39.562600702212336}

#### ('burger', 2) vs ('swipe', 2)

{'effect_size': 0.32302291280978401, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=1.13380582248701, pvalue=0.26252717192400138), 'n2': 28, 'df': 47.828479613444102}

#### ('burger', 2) vs ('swipe', 3)

{'effect_size': 0.64769813858798198, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=2.2734112399558835, pvalue=0.027911615554138184), 'n2': 28, 'df': 44.213704391296204}

#### ('burger', 2) vs ('swipe', 4)

{'effect_size': 0.24461760596562426, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=0.85860431235098866, pvalue=0.39486327780313391), 'n2': 28, 'df': 47.58569507601031}

#### ('burger', 2) vs ('swipe', 5)

{'effect_size': 0.44129430695846589, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=1.5489367311677702, pvalue=0.12804879993894061), 'n2': 28, 'df': 47.398184235865926}

#### ('burger', 3) vs ('burger', 4)

{'effect_size': -0.21320071635561041, 'n1': 22, 'N': 44, 'test_result': Ttest_relResult(statistic=-1.0, pvalue=0.32869468323646367), 'n2': 22, 'df': 21}

#### ('burger', 3) vs ('burger', 5)

{'effect_size': -0.29164791418864128, 'n1': 22, 'N': 44, 'test_result': Ttest_relResult(statistic=-1.3679499730300344, pvalue=0.1857887709669136), 'n2': 22, 'df': 21}

#### ('burger', 3) vs ('swipe', 1)

{'effect_size': -0.20638031994173414, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=-0.72439198309892372, pvalue=0.47308750654180076), 'n2': 28, 'df': 39.562600702212336}

#### ('burger', 3) vs ('swipe', 2)

{'effect_size': 0.32302291280978518, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=1.1338058224870142, pvalue=0.26252717192399971), 'n2': 28, 'df': 47.828479613444102}

#### ('burger', 3) vs ('swipe', 3)

{'effect_size': 0.64769813858798297, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=2.273411239955887, pvalue=0.027911615554137945), 'n2': 28, 'df': 44.213704391296204}

#### ('burger', 3) vs ('swipe', 4)

{'effect_size': 0.24461760596562554, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=0.8586043123509931, pvalue=0.39486327780313146), 'n2': 28, 'df': 47.58569507601031}

#### ('burger', 3) vs ('swipe', 5)

{'effect_size': 0.44129430695846694, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=1.548936731167774, pvalue=0.12804879993893969), 'n2': 28, 'df': 47.398184235865926}

#### ('burger', 4) vs ('burger', 5)

{'effect_size': -0.12118298018003469, 'n1': 22, 'N': 44, 'test_result': Ttest_relResult(statistic=-0.56839856005880507, pvalue=0.57579272855240249), 'n2': 22, 'df': 21}

#### ('burger', 4) vs ('swipe', 1)

{'effect_size': 0.053481730884926533, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=0.18772011355652787, pvalue=0.85191261940051899), 'n2': 28, 'df': 46.511882640896744}

#### ('burger', 4) vs ('swipe', 2)

{'effect_size': 0.59918933090885751, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=2.1031460160122153, pvalue=0.040982538230155942), 'n2': 28, 'df': 45.753689548912838}

#### ('burger', 4) vs ('swipe', 3)

{'effect_size': 0.8727465727132796, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=3.063328037911023, pvalue=0.0039982893426720014), 'n2': 28, 'df': 38.226137222589209}

#### ('burger', 4) vs ('swipe', 4)

{'effect_size': 0.51767700677424922, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=1.8170389194463148, pvalue=0.075687083399407801), 'n2': 28, 'df': 46.298217179902764}

#### ('burger', 4) vs ('swipe', 5)

{'effect_size': 0.69287422335247306, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=2.4319786539439705, pvalue=0.019328473504723491), 'n2': 28, 'df': 42.294644211025989}

#### ('burger', 5) vs ('swipe', 1)

{'effect_size': 0.23466433176906615, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=0.82366846170589003, pvalue=0.41428064209770366), 'n2': 28, 'df': 47.08496053303012}

#### ('burger', 5) vs ('swipe', 2)

{'effect_size': 0.78064001159627316, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=2.7400353204522681, pvalue=0.0091946014470773128), 'n2': 28, 'df': 39.274267272770743}

#### ('burger', 5) vs ('swipe', 3)

{'effect_size': 1.0076384489725929, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=3.5367966020406145, pvalue=0.0012166207287807747), 'n2': 28, 'df': 33.276977869806174}

#### ('burger', 5) vs ('swipe', 4)

{'effect_size': 0.69772160053299137, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=2.4489928787964925, pvalue=0.018809724953796), 'n2': 28, 'df': 39.941129628992769}

#### ('burger', 5) vs ('swipe', 5)

{'effect_size': 0.85040706574694769, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=2.9849166866864385, pvalue=0.005066877024676052), 'n2': 28, 'df': 36.090509045076026}

#### ('swipe', 1) vs ('swipe', 2)

{'effect_size': 0.42970973450348038, 'n1': 28, 'N': 56, 'test_result': Ttest_relResult(statistic=2.2738101868796008, pvalue=0.031143927701852654), 'n2': 28, 'df': 27}

#### ('swipe', 1) vs ('swipe', 3)

{'effect_size': 0.62105900340811859, 'n1': 28, 'N': 56, 'test_result': Ttest_relResult(statistic=3.286335345030996, pvalue=0.0028163139346924671), 'n2': 28, 'df': 27}

#### ('swipe', 1) vs ('swipe', 4)

{'effect_size': 0.29186341048270625, 'n1': 28, 'N': 56, 'test_result': Ttest_relResult(statistic=1.5443960018728058, pvalue=0.13413370332412661), 'n2': 28, 'df': 27}

#### ('swipe', 1) vs ('swipe', 5)

{'effect_size': 0.43376642344069183, 'n1': 28, 'N': 56, 'test_result': Ttest_relResult(statistic=2.2952761670280175, pvalue=0.029714387495799355), 'n2': 28, 'df': 27}

#### ('swipe', 2) vs ('swipe', 3)

{'effect_size': 0.25738810551251956, 'n1': 28, 'N': 56, 'test_result': Ttest_relResult(statistic=1.3619698352243597, pvalue=0.18446343063393097), 'n2': 28, 'df': 27}

#### ('swipe', 2) vs ('swipe', 4)

{'effect_size': -0.051540609955803708, 'n1': 28, 'N': 56, 'test_result': Ttest_relResult(statistic=-0.27272727272727271, pvalue=0.78713793632384976), 'n2': 28, 'df': 27}

#### ('swipe', 2) vs ('swipe', 5)

{'effect_size': 0.087831006565367992, 'n1': 28, 'N': 56, 'test_result': Ttest_relResult(statistic=0.46475800154489011, pvalue=0.64583105923673334), 'n2': 28, 'df': 27}

#### ('swipe', 3) vs ('swipe', 4)

{'effect_size': -0.31277162108561218, 'n1': 28, 'N': 56, 'test_result': Ttest_relResult(statistic=-1.6550318531021115, pvalue=0.10949774875264846), 'n2': 28, 'df': 27}

#### ('swipe', 3) vs ('swipe', 5)

{'effect_size': -0.14720510145392723, 'n1': 28, 'N': 56, 'test_result': Ttest_relResult(statistic=-0.77893618033424816, pvalue=0.44279119248126331), 'n2': 28, 'df': 27}

#### ('swipe', 4) vs ('swipe', 5)

{'effect_size': 0.14531257883714099, 'n1': 28, 'N': 56, 'test_result': Ttest_relResult(statistic=0.76892189194508498, pvalue=0.44861400074734215), 'n2': 28, 'df': 27}

### Global Burger vs Swipe per tid Tests (effectiveness)

#### burger vs swipe 1

{'effect_size': -0.0061919983429827991, 'n1': 110, 'N': 138, 'test_result': Ttest_indResult(statistic=-0.029252746423380799, pvalue=0.97680275053100574), 'n2': 28, 'df': 41.646274215071564}

#### burger vs swipe 2

{'effect_size': 0.47456730807128411, 'n1': 110, 'N': 138, 'test_result': Ttest_indResult(statistic=2.2419897995561002, pvalue=0.031762405354738295), 'n2': 28, 'df': 33.189150709706816}

#### burger vs swipe 3

{'effect_size': 0.67233918280951432, 'n1': 110, 'N': 138, 'test_result': Ttest_indResult(statistic=3.1763199109248252, pvalue=0.0034532804986949521), 'n2': 28, 'df': 29.860774566923141}

#### burger vs swipe 4

{'effect_size': 0.40670365410079579, 'n1': 110, 'N': 138, 'test_result': Ttest_indResult(statistic=1.9213827594698381, pvalue=0.063192249558969904), 'n2': 28, 'df': 33.629945690624162}

#### burger vs swipe 5

{'effect_size': 0.54003040866087293, 'n1': 110, 'N': 138, 'test_result': Ttest_indResult(statistic=2.5512559484732256, pvalue=0.015832395055001371), 'n2': 28, 'df': 31.310433179797702}

### Global Burger vs Global Swipe Test (effectiveness)

#### burger vs swipe

{'effect_size': 0.5201935300606596, 'n1': 110, 'N': 250, 'test_result': Ttest_indResult(statistic=4.0827736426313646, pvalue=6.1281992339985695e-05), 'n2': 140, 'df': 231.85456841341124}

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

#### Cross-compare Tests per tid (result)

##### ('burger', 1) vs ('burger', 2)

{'effect_size': 0.30895719032666236, 'n1': 22, 'N': 44, 'test_result': Ttest_relResult(statistic=1.4491376746189439, pvalue=0.16206871193916239), 'n2': 22, 'df': 21}

##### ('burger', 1) vs ('burger', 3)

{'effect_size': 0.30237651520711439, 'n1': 22, 'N': 44, 'test_result': Ttest_relResult(statistic=1.4182715723279382, pvalue=0.1707816127183879), 'n2': 22, 'df': 21}

##### ('burger', 1) vs ('burger', 4)

{'effect_size': 0.30895719032666236, 'n1': 22, 'N': 44, 'test_result': Ttest_relResult(statistic=1.4491376746189439, pvalue=0.16206871193916239), 'n2': 22, 'df': 21}

##### ('burger', 1) vs ('burger', 5)

{'effect_size': 0.21320071635561041, 'n1': 22, 'N': 44, 'test_result': Ttest_relResult(statistic=0.99999999999999989, pvalue=0.32869468323646389), 'n2': 22, 'df': 21}

##### ('burger', 1) vs ('swipe', 1)

{'effect_size': 0.48030236546295596, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=1.6858544608470538, pvalue=0.1033481555997189), 'n2': 28, 'df': 27.000000000000007}

##### ('burger', 1) vs ('swipe', 2)

{'effect_size': 0.41058667608851773, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=1.4411533842457791, pvalue=0.16103934953023244), 'n2': 28, 'df': 26.999999999999993}

##### ('burger', 1) vs ('swipe', 3)

{'effect_size': 0.56604176606465861, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=1.9867985355975688, pvalue=0.057179118127154482), 'n2': 28, 'df': 27.0}

##### ('burger', 1) vs ('swipe', 4)

{'effect_size': 0.56604176606465861, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=1.9867985355975688, pvalue=0.057179118127154482), 'n2': 28, 'df': 27.0}

##### ('burger', 1) vs ('swipe', 5)

{'effect_size': 0.64390928291116023, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=2.2601124105026518, pvalue=0.03208842174489044), 'n2': 28, 'df': 27.000000000000004}

##### ('burger', 2) vs ('burger', 3)

{'effect_size': 0.16359387723719587, 'n1': 22, 'N': 44, 'test_result': Ttest_relResult(statistic=0.76732330000396298, pvalue=0.45143092243104099), 'n2': 22, 'df': 21}

##### ('burger', 2) vs ('burger', 4)

{'effect_size': 0.0, 'n1': 22, 'N': 44, 'test_result': Ttest_relResult(statistic=0.0, pvalue=1.0), 'n2': 22, 'df': 21}

##### ('burger', 2) vs ('burger', 5)

{'effect_size': -0.12118298018003472, 'n1': 22, 'N': 44, 'test_result': Ttest_relResult(statistic=-0.56839856005880518, pvalue=0.57579272855240227), 'n2': 22, 'df': 21}

##### ('burger', 2) vs ('swipe', 1)

{'effect_size': 0.14037427405506098, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=0.49271170229567274, pvalue=0.62452609288904781), 'n2': 28, 'df': 46.678533060555651}

##### ('burger', 2) vs ('swipe', 2)

{'effect_size': -0.069418769397006405, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=-0.24365889171012692, pvalue=0.80866695186899662), 'n2': 28, 'df': 42.514901642794264}

##### ('burger', 2) vs ('swipe', 3)

{'effect_size': 0.22786073147238273, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=0.79978792158211109, pvalue=0.42796667468869776), 'n2': 28, 'df': 45.753689548912831}

##### ('burger', 2) vs ('swipe', 4)

{'effect_size': 0.22786073147238273, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=0.79978792158211109, pvalue=0.42796667468869776), 'n2': 28, 'df': 45.753689548912831}

##### ('burger', 2) vs ('swipe', 5)

{'effect_size': 0.35642881239073876, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=1.2510600541476802, pvalue=0.2178987002569478), 'n2': 28, 'df': 41.625329367674269}

##### ('burger', 3) vs ('burger', 4)

{'effect_size': -0.19201784934589022, 'n1': 22, 'N': 44, 'test_result': Ttest_relResult(statistic=-0.90064354673936453, pvalue=0.37799097909168333), 'n2': 22, 'df': 21}

##### ('burger', 3) vs ('burger', 5)

{'effect_size': -0.27361708674793644, 'n1': 22, 'N': 44, 'test_result': Ttest_relResult(statistic=-1.2833778958394957, pvalue=0.2133419606752297), 'n2': 22, 'df': 21}

##### ('burger', 3) vs ('swipe', 1)

{'effect_size': -0.13267426558746895, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=-0.46568478226137766, pvalue=0.64455504483952952), 'n2': 28, 'df': 32.415229334774999}

##### ('burger', 3) vs ('swipe', 2)

{'effect_size': -0.26470282928139927, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=-0.92910316007448612, pvalue=0.36170919252817291), 'n2': 28, 'df': 25.031888735183646}

##### ('burger', 3) vs ('swipe', 3)

{'effect_size': -0.075518375153598188, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=-0.26506842102661687, pvalue=0.7925715578816479), 'n2': 28, 'df': 33.697146607252122}

##### ('burger', 3) vs ('swipe', 4)

{'effect_size': -0.075518375153598188, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=-0.26506842102661687, pvalue=0.7925715578816479), 'n2': 28, 'df': 33.697146607252122}

##### ('burger', 3) vs ('swipe', 5)

{'effect_size': 0.033253729140645921, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=0.11672011558286063, pvalue=0.90768224442657708), 'n2': 28, 'df': 38.909196327468443}

##### ('burger', 4) vs ('burger', 5)

{'effect_size': -0.21320071635561041, 'n1': 22, 'N': 44, 'test_result': Ttest_relResult(statistic=-0.99999999999999989, pvalue=0.32869468323646389), 'n2': 22, 'df': 21}

##### ('burger', 4) vs ('swipe', 1)

{'effect_size': 0.14037427405506098, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=0.49271170229567274, pvalue=0.62452609288904781), 'n2': 28, 'df': 46.678533060555651}

##### ('burger', 4) vs ('swipe', 2)

{'effect_size': -0.069418769397006405, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=-0.24365889171012692, pvalue=0.80866695186899662), 'n2': 28, 'df': 42.514901642794264}

##### ('burger', 4) vs ('swipe', 3)

{'effect_size': 0.22786073147238273, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=0.79978792158211109, pvalue=0.42796667468869776), 'n2': 28, 'df': 45.753689548912831}

##### ('burger', 4) vs ('swipe', 4)

{'effect_size': 0.22786073147238273, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=0.79978792158211109, pvalue=0.42796667468869776), 'n2': 28, 'df': 45.753689548912831}

##### ('burger', 4) vs ('swipe', 5)

{'effect_size': 0.35642881239073876, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=1.2510600541476802, pvalue=0.2178987002569478), 'n2': 28, 'df': 41.625329367674269}

##### ('burger', 5) vs ('swipe', 1)

{'effect_size': 0.28858267627413325, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=1.0129210828495314, pvalue=0.31711639921326906), 'n2': 28, 'df': 40.465604241992374}

##### ('burger', 5) vs ('swipe', 2)

{'effect_size': 0.11003661975982165, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=0.38622696788057731, pvalue=0.70103791654914316), 'n2': 28, 'df': 47.92717840005146}

##### ('burger', 5) vs ('swipe', 3)

{'effect_size': 0.37654400559349555, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=1.3216640957475614, pvalue=0.193927451557106), 'n2': 28, 'df': 39.27426727277075}

##### ('burger', 5) vs ('swipe', 4)

{'effect_size': 0.37654400559349555, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=1.3216640957475614, pvalue=0.193927451557106), 'n2': 28, 'df': 39.27426727277075}

##### ('burger', 5) vs ('swipe', 5)

{'effect_size': 0.48729582471449862, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=1.7104014031978396, pvalue=0.095898470850199258), 'n2': 28, 'df': 35.58393287131743}

##### ('swipe', 1) vs ('swipe', 2)

{'effect_size': -0.15335958973297431, 'n1': 28, 'N': 56, 'test_result': Ttest_relResult(statistic=-0.81150267120068909, pvalue=0.42417364208211739), 'n2': 28, 'df': 27}

##### ('swipe', 1) vs ('swipe', 3)

{'effect_size': 0.1077863635721933, 'n1': 28, 'N': 56, 'test_result': Ttest_relResult(statistic=0.57035182547203012, pvalue=0.57315533458734902), 'n2': 28, 'df': 27}

##### ('swipe', 1) vs ('swipe', 4)

{'effect_size': 0.1077863635721933, 'n1': 28, 'N': 56, 'test_result': Ttest_relResult(statistic=0.57035182547203012, pvalue=0.57315533458734902), 'n2': 28, 'df': 27}

##### ('swipe', 1) vs ('swipe', 5)

{'effect_size': 0.34016802570830451, 'n1': 28, 'N': 56, 'test_result': Ttest_relResult(statistic=1.8, pvalue=0.083044921447959233), 'n2': 28, 'df': 27}

##### ('swipe', 2) vs ('swipe', 3)

{'effect_size': 0.215428579534056, 'n1': 28, 'N': 56, 'test_result': Ttest_relResult(statistic=1.1399408934860222, pvalue=0.26432288019972711), 'n2': 28, 'df': 27}

##### ('swipe', 2) vs ('swipe', 4)

{'effect_size': 0.215428579534056, 'n1': 28, 'N': 56, 'test_result': Ttest_relResult(statistic=1.1399408934860222, pvalue=0.26432288019972711), 'n2': 28, 'df': 27}

##### ('swipe', 2) vs ('swipe', 5)

{'effect_size': 0.37546963074131917, 'n1': 28, 'N': 56, 'test_result': Ttest_relResult(statistic=1.9867985355975659, pvalue=0.057179118127154788), 'n2': 28, 'df': 27}

##### ('swipe', 3) vs ('swipe', 4)

{'effect_size': nan, 'n1': 28, 'N': 56, 'test_result': Ttest_relResult(statistic=nan, pvalue=nan), 'n2': 28, 'df': 27}

##### ('swipe', 3) vs ('swipe', 5)

{'effect_size': 0.15335958973297431, 'n1': 28, 'N': 56, 'test_result': Ttest_relResult(statistic=0.81150267120068909, pvalue=0.42417364208211739), 'n2': 28, 'df': 27}

##### ('swipe', 4) vs ('swipe', 5)

{'effect_size': 0.15335958973297431, 'n1': 28, 'N': 56, 'test_result': Ttest_relResult(statistic=0.81150267120068909, pvalue=0.42417364208211739), 'n2': 28, 'df': 27}

#### Global Burger vs Swipe per tid Tests (result)

##### burger vs swipe 1

{'effect_size': 0.11853067390536037, 'n1': 110, 'N': 138, 'test_result': Ttest_indResult(statistic=0.55997233123865175, pvalue=0.57874985452460637), 'n2': 28, 'df': 38.408590297522736}

##### burger vs swipe 2

{'effect_size': -0.06618182180368716, 'n1': 110, 'N': 138, 'test_result': Ttest_indResult(statistic=-0.31266159062439741, pvalue=0.75558308779702033), 'n2': 28, 'df': 62.234421968088661}

##### burger vs swipe 3

{'effect_size': 0.19034073905162166, 'n1': 110, 'N': 138, 'test_result': Ttest_indResult(statistic=0.89922333067579296, pvalue=0.37433593164182521), 'n2': 28, 'df': 37.083136983495038}

##### burger vs swipe 4

{'effect_size': 0.19034073905162166, 'n1': 110, 'N': 138, 'test_result': Ttest_indResult(statistic=0.89922333067579296, pvalue=0.37433593164182521), 'n2': 28, 'df': 37.083136983495038}

##### burger vs swipe 5

{'effect_size': 0.28811787963105384, 'n1': 110, 'N': 138, 'test_result': Ttest_indResult(statistic=1.3611501176257312, pvalue=0.18254059625123423), 'n2': 28, 'df': 33.544677628509355}

#### Global Burger vs Global Swipe Test (result)

##### burger vs swipe

{'effect_size': 0.17280354331534853, 'n1': 110, 'N': 250, 'test_result': Ttest_indResult(statistic=1.3562601440255169, pvalue=0.17626116218076363), 'n2': 140, 'df': 245.75199938633483}

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

#### Cross-compare Tests per tid (result)

##### ('burger', 1) vs ('burger', 2)

{'effect_size': 0.13295400586957762, 'n1': 22, 'N': 44, 'test_result': Ttest_relResult(statistic=0.62360956446232363, pvalue=0.53959920616515578), 'n2': 22, 'df': 21}

##### ('burger', 1) vs ('burger', 3)

{'effect_size': -0.025456396896192779, 'n1': 22, 'N': 44, 'test_result': Ttest_relResult(statistic=-0.11940108519022286, pvalue=0.90609248698339373), 'n2': 22, 'df': 21}

##### ('burger', 1) vs ('burger', 4)

{'effect_size': 0.12118298018003472, 'n1': 22, 'N': 44, 'test_result': Ttest_relResult(statistic=0.56839856005880518, pvalue=0.57579272855240227), 'n2': 22, 'df': 21}

##### ('burger', 1) vs ('burger', 5)

{'effect_size': 0.0, 'n1': 22, 'N': 44, 'test_result': Ttest_relResult(statistic=0.0, pvalue=1.0), 'n2': 22, 'df': 21}

##### ('burger', 1) vs ('swipe', 1)

{'effect_size': -0.36573997588463569, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=-1.2837421053733327, pvalue=0.2054375873090272), 'n2': 28, 'df': 47.667575416968432}

##### ('burger', 1) vs ('swipe', 2)

{'effect_size': -0.34444982755270848, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=-1.2090139880073498, pvalue=0.23271472223326703), 'n2': 28, 'df': 46.920593391153176}

##### ('burger', 1) vs ('swipe', 3)

{'effect_size': -0.41705356296129625, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=-1.463852065048149, pvalue=0.14995179579288434), 'n2': 28, 'df': 46.57265245558154}

##### ('burger', 1) vs ('swipe', 4)

{'effect_size': -0.46177353887521688, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=-1.6208185434680238, pvalue=0.11224980129520724), 'n2': 28, 'df': 43.707666454689033}

##### ('burger', 1) vs ('swipe', 5)

{'effect_size': -0.61231488090316488, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=-2.1492165095182081, pvalue=0.03688815104511671), 'n2': 28, 'df': 46.206561810348745}

##### ('burger', 2) vs ('burger', 3)

{'effect_size': -0.17391210417696717, 'n1': 22, 'N': 44, 'test_result': Ttest_relResult(statistic=-0.81572007425570092, pvalue=0.42381641720650809), 'n2': 22, 'df': 21}

##### ('burger', 2) vs ('burger', 4)

{'effect_size': 0.0, 'n1': 22, 'N': 44, 'test_result': Ttest_relResult(statistic=0.0, pvalue=1.0), 'n2': 22, 'df': 21}

##### ('burger', 2) vs ('burger', 5)

{'effect_size': -0.15399810070180364, 'n1': 22, 'N': 44, 'test_result': Ttest_relResult(statistic=-0.72231511851461538, pvalue=0.47806803198115067), 'n2': 22, 'df': 21}

##### ('burger', 2) vs ('swipe', 1)

{'effect_size': -0.46408002132614695, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=-1.6289142640148464, pvalue=0.10987883761813257), 'n2': 28, 'df': 47.9913124558378}

##### ('burger', 2) vs ('swipe', 2)

{'effect_size': -0.44613911796579342, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=-1.5659419487889481, pvalue=0.12397500203185813), 'n2': 28, 'df': 47.685525414509769}

##### ('burger', 2) vs ('swipe', 3)

{'effect_size': -0.52273421881250781, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=-1.8347896616603989, pvalue=0.072806163662061316), 'n2': 28, 'df': 47.480446678333088}

##### ('burger', 2) vs ('swipe', 4)

{'effect_size': -0.57759936721227423, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=-2.0273655509871724, pvalue=0.048533888623595652), 'n2': 28, 'df': 45.291768555758196}

##### ('burger', 2) vs ('swipe', 5)

{'effect_size': -0.7265331960523993, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=-2.550121168647193, pvalue=0.014070036183701212), 'n2': 28, 'df': 47.242477361105024}

##### ('burger', 3) vs ('burger', 4)

{'effect_size': 0.20479161839774845, 'n1': 22, 'N': 44, 'test_result': Ttest_relResult(statistic=0.96055783441254516, pvalue=0.34770479176718427), 'n2': 22, 'df': 21}

##### ('burger', 3) vs ('burger', 5)

{'effect_size': 0.032548869678754512, 'n1': 22, 'N': 44, 'test_result': Ttest_relResult(statistic=0.15266773130566913, pvalue=0.88011767262008023), 'n2': 22, 'df': 21}

##### ('burger', 3) vs ('swipe', 1)

{'effect_size': -0.36721135611334099, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=-1.2889066290162134, pvalue=0.20362802550896689), 'n2': 28, 'df': 47.843495880541269}

##### ('burger', 3) vs ('swipe', 2)

{'effect_size': -0.34540506948393923, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=-1.2123668735785071, pvalue=0.23130618790625015), 'n2': 28, 'df': 47.99569879327052}

##### ('burger', 3) vs ('swipe', 3)

{'effect_size': -0.42352111655986063, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=-1.4865530860485299, pvalue=0.14367932916113879), 'n2': 28, 'df': 47.948929091062439}

##### ('burger', 3) vs ('swipe', 4)

{'effect_size': -0.47459659344928179, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=-1.665827282358026, pvalue=0.10245606821048929), 'n2': 28, 'df': 46.608085124245342}

##### ('burger', 3) vs ('swipe', 5)

{'effect_size': -0.63351870258441478, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=-2.2236416215700405, pvalue=0.030927460331272798), 'n2': 28, 'df': 47.85778083492422}

##### ('burger', 4) vs ('burger', 5)

{'effect_size': -0.27361708674793639, 'n1': 22, 'N': 44, 'test_result': Ttest_relResult(statistic=-1.2833778958394955, pvalue=0.21334196067522973), 'n2': 22, 'df': 21}

##### ('burger', 4) vs ('swipe', 1)

{'effect_size': -0.50169275123868184, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=-1.7609344102128832, pvalue=0.084815434369215556), 'n2': 28, 'df': 46.565383072420282}

##### ('burger', 4) vs ('swipe', 2)

{'effect_size': -0.48540534042490763, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=-1.7037658302714056, pvalue=0.09497299007775549), 'n2': 28, 'df': 47.402752323541641}

##### ('burger', 4) vs ('swipe', 3)

{'effect_size': -0.57001570030263848, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=-2.0007469881640132, pvalue=0.051138917909208527), 'n2': 28, 'df': 47.614210617056905}

##### ('burger', 4) vs ('swipe', 4)

{'effect_size': -0.6384629412748174, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=-2.2409958289424603, pvalue=0.029698757129413455), 'n2': 28, 'df': 47.893187281978172}

##### ('burger', 4) vs ('swipe', 5)

{'effect_size': -0.79392567093610711, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=-2.7866677954802945, pvalue=0.0076168232047276047), 'n2': 28, 'df': 47.773184620417567}

##### ('burger', 5) vs ('swipe', 1)

{'effect_size': -0.3678194182086999, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=-1.2910409183090523, pvalue=0.20290434875885618), 'n2': 28, 'df': 47.755647354791428}

##### ('burger', 5) vs ('swipe', 2)

{'effect_size': -0.34654776262808462, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=-1.2163777102367443, pvalue=0.22990419438692747), 'n2': 28, 'df': 47.081512542372259}

##### ('burger', 5) vs ('swipe', 3)

{'effect_size': -0.41965172855237409, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=-1.4729715892618513, pvalue=0.14745914516885314), 'n2': 28, 'df': 46.75648935374295}

##### ('burger', 5) vs ('swipe', 4)

{'effect_size': -0.46503073524461536, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=-1.6322512563257097, pvalue=0.10976494840900448), 'n2': 28, 'df': 43.993914902720441}

##### ('burger', 5) vs ('swipe', 5)

{'effect_size': -0.61620944883108963, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=-2.1628863874669357, pvalue=0.035735733189624176), 'n2': 28, 'df': 46.410640594005613}

##### ('swipe', 1) vs ('swipe', 2)

{'effect_size': 0.035093120317179816, 'n1': 28, 'N': 56, 'test_result': Ttest_relResult(statistic=0.18569533817705183, pvalue=0.8540717092857345), 'n2': 28, 'df': 27}

##### ('swipe', 1) vs ('swipe', 3)

{'effect_size': -0.047972886989667646, 'n1': 28, 'N': 56, 'test_result': Ttest_relResult(statistic=-0.25384865729693323, pvalue=0.80153564704995517), 'n2': 28, 'df': 27}

##### ('swipe', 1) vs ('swipe', 4)

{'effect_size': -0.05340392102026733, 'n1': 28, 'N': 56, 'test_result': Ttest_relResult(statistic=-0.2825869881107243, pvalue=0.77964854494580593), 'n2': 28, 'df': 27}

##### ('swipe', 1) vs ('swipe', 5)

{'effect_size': -0.22902115052528635, 'n1': 28, 'N': 56, 'test_result': Ttest_relResult(statistic=-1.2118660185275947, pvalue=0.23606280739392285), 'n2': 28, 'df': 27}

##### ('swipe', 2) vs ('swipe', 3)

{'effect_size': -0.10155400629994435, 'n1': 28, 'N': 56, 'test_result': Ttest_relResult(statistic=-0.53737329062387895, pvalue=0.5954113366515259), 'n2': 28, 'df': 27}

##### ('swipe', 2) vs ('swipe', 4)

{'effect_size': -0.094648998259233286, 'n1': 28, 'N': 56, 'test_result': Ttest_relResult(statistic=-0.50083542247063328, pvalue=0.62054550807787923), 'n2': 28, 'df': 27}

##### ('swipe', 2) vs ('swipe', 5)

{'effect_size': -0.29512585732819752, 'n1': 28, 'N': 56, 'test_result': Ttest_relResult(statistic=-1.5616592479102798, pvalue=0.13001443262320639), 'n2': 28, 'df': 27}

##### ('swipe', 3) vs ('swipe', 4)

{'effect_size': -0.022346614111317671, 'n1': 28, 'N': 56, 'test_result': Ttest_relResult(statistic=-0.11824716716574642, pvalue=0.90674715458336475), 'n2': 28, 'df': 27}

##### ('swipe', 3) vs ('swipe', 5)

{'effect_size': -0.27606284301048722, 'n1': 28, 'N': 56, 'test_result': Ttest_relResult(statistic=-1.4607872576624297, pvalue=0.15561417089917387), 'n2': 28, 'df': 27}

##### ('swipe', 4) vs ('swipe', 5)

{'effect_size': -0.22769127776959361, 'n1': 28, 'N': 56, 'test_result': Ttest_relResult(statistic=-1.2048289933537484, pvalue=0.23872409198062031), 'n2': 28, 'df': 27}

#### Global Burger vs Swipe per tid Tests (result)

##### burger vs swipe 1

{'effect_size': -0.3793271788228888, 'n1': 110, 'N': 138, 'test_result': Ttest_indResult(statistic=-1.7920485696152606, pvalue=0.081668377626223213), 'n2': 28, 'df': 35.4325064294745}

##### burger vs swipe 2

{'effect_size': -0.36869228756835798, 'n1': 110, 'N': 138, 'test_result': Ttest_indResult(statistic=-1.7418063441047225, pvalue=0.089916422412057356), 'n2': 28, 'df': 36.712069747533576}

##### burger vs swipe 3

{'effect_size': -0.44426789424264002, 'n1': 110, 'N': 138, 'test_result': Ttest_indResult(statistic=-2.0988468236683779, pvalue=0.042676536020284629), 'n2': 28, 'df': 37.196208525266002}

##### burger vs swipe 4

{'effect_size': -0.51786396582520622, 'n1': 110, 'N': 138, 'test_result': Ttest_indResult(statistic=-2.446535421195474, pvalue=0.018837342914925163), 'n2': 28, 'df': 40.666690450571501}

##### burger vs swipe 5

{'effect_size': -0.64362088130327999, 'n1': 110, 'N': 138, 'test_result': Ttest_indResult(statistic=-3.0406465555493165, pvalue=0.0042798608827830081), 'n2': 28, 'df': 37.674013279441489}

#### Global Burger vs Global Swipe Test (result)

##### burger vs swipe

{'effect_size': -0.4974943959926959, 'n1': 110, 'N': 250, 'test_result': Ttest_indResult(statistic=-3.9046179737739855, pvalue=0.00012188835447452269), 'n2': 140, 'df': 246.46345878761642}

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

#### Global Burger vs Global Swipe Test (result)

##### burger vs swipe

{'effect_size': -0.03063130236520992, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=-0.10751543495766284, pvalue=0.9148292292550424), 'n2': 28, 'df': 47.892694076399025}

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

#### Global Burger vs Global Swipe Test (result)

##### burger vs swipe

{'effect_size': 0.35194119607736601, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=1.2353085848140299, pvalue=0.22501281363206999), 'n2': 28, 'df': 34.706650521379885}

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

#### Global Burger vs Global Swipe Test (result)

##### burger vs swipe

{'effect_size': -0.53966451252512859, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=-1.8942147514189334, pvalue=0.066878319737774167), 'n2': 28, 'df': 33.418574529686872}

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

#### Global Burger vs Global Swipe Test (result)

##### burger vs swipe

{'effect_size': 0.40317277353302849, 'n1': 22, 'N': 50, 'test_result': Ttest_indResult(statistic=1.4151306918873736, pvalue=0.16442349507017537), 'n2': 28, 'df': 41.879320839518563}
