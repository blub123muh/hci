
# Analysis

## Preprocessing

* experiment_results.csv
* task_questionnaire_results.csv
* final_questionnaire_results.csv

Dropping Task ID 0 (Training)

Asserting Absolute Distance Values!

| Dataset Validation:
| dict_items([('pid', True)])

| Adding success column based on
| `opt_interactions == interactions`
| in order to measure effectiveness.

| Aggregating Task Groups

| Computing efficiency over task mean_success/time_ms
Index(['navigation', 'tid', 'distance', 'n_interactions', 'time_ms',
       'effectiveness', 'efficiency'],
      dtype='object')

No normality test, *Forcing t-test*!

## Efficiency by Tasks

### Descriptions (efficiency)

#### Global Descriptions (efficiency)

##### burger

| count | 90.0 |
| mean | 0.00025247160313 |
| std | 0.000129952969122 |
| min | 0.0 |
| 25% | 0.000177282270746 |
| 50% | 0.00022486851119 |
| 75% | 0.000298780118888 |
| max | 0.000688231245699 |

##### swipe

| count | 115.0 |
| mean | 0.000241224910254 |
| std | 9.55488291012e-05 |
| min | 0.0 |
| 25% | 0.000184988873979 |
| 50% | 0.000252908447142 |
| 75% | 0.000310752500022 |
| max | 0.0004158004158 |

#### Repeated measures (efficiency)

##### burger

| KruskalResult(statistic=4.2779458205508298, pvalue=0.36969487988915695)
| FriedmanchisquareResult(statistic=41.466970387243741, pvalue=2.151251397158931e-08)

##### swipe

| KruskalResult(statistic=14.014411200225428, pvalue=0.0072492028795708161)
| FriedmanchisquareResult(statistic=51.228571428571399, pvalue=1.9997323452054533e-10)

#### Descriptions per tid (efficiency)

##### ('burger', 1)

| count | 18.0 |
| mean | 0.000187980465019 |
| std | 8.17030693819e-05 |
| min | 0.0 |
| 25% | 0.000155539606315 |
| 50% | 0.000168901908363 |
| 75% | 0.000242856401943 |
| max | 0.000324254215305 |

##### ('burger', 2)

| count | 18.0 |
| mean | 0.000286058804246 |
| std | 0.000159372688254 |
| min | 0.00013104442406 |
| 25% | 0.000185216193142 |
| 50% | 0.000251569672547 |
| 75% | 0.000286654569534 |
| max | 0.000688231245699 |

##### ('burger', 3)

| count | 18.0 |
| mean | 0.000271311881898 |
| std | 0.000139259548257 |
| min | 0.0 |
| 25% | 0.000189076829709 |
| 50% | 0.000249675893128 |
| 75% | 0.000313583435126 |
| max | 0.000576701268743 |

##### ('burger', 4)

| count | 18.0 |
| mean | 0.000256766958278 |
| std | 8.98804575751e-05 |
| min | 0.000132961042415 |
| 25% | 0.000198384475186 |
| 50% | 0.000219880706498 |
| 75% | 0.00030139038476 |
| max | 0.000462534690102 |

##### ('burger', 5)

| count | 18.0 |
| mean | 0.00026023990621 |
| std | 0.000151023886768 |
| min | 0.0 |
| 25% | 0.000178214433262 |
| 50% | 0.000251548744268 |
| 75% | 0.000302959203749 |
| max | 0.000574052812859 |

##### ('swipe', 1)

| count | 23.0 |
| mean | 0.000163211841402 |
| std | 6.72068582153e-05 |
| min | 0.0 |
| 25% | 0.000140276544119 |
| 50% | 0.000168605631428 |
| 75% | 0.000206167312053 |
| max | 0.000275103163686 |

##### ('swipe', 2)

| count | 23.0 |
| mean | 0.000262014814162 |
| std | 0.000101173335834 |
| min | 0.0 |
| 25% | 0.000202946264472 |
| 50% | 0.000258933195236 |
| 75% | 0.00034092004926 |
| max | 0.000407664084794 |

##### ('swipe', 3)

| count | 23.0 |
| mean | 0.000269550479124 |
| std | 8.88727487449e-05 |
| min | 0.0 |
| 25% | 0.00022802502717 |
| 50% | 0.000287108814241 |
| 75% | 0.000323001493465 |
| max | 0.0004158004158 |

##### ('swipe', 4)

| count | 23.0 |
| mean | 0.000243497513587 |
| std | 9.97611200489e-05 |
| min | 0.0 |
| 25% | 0.000204507332406 |
| 50% | 0.000271591526344 |
| 75% | 0.000311677638769 |
| max | 0.000358037952023 |

##### ('swipe', 5)

| count | 23.0 |
| mean | 0.000267849902998 |
| std | 7.94008918311e-05 |
| min | 0.0 |
| 25% | 0.000227080097751 |
| 50% | 0.000270929287456 |
| 75% | 0.000320579861403 |
| max | 0.000370233246946 |

### Cross-compare Tests per tid (efficiency)

#### ('burger', 1) vs ('burger', 2)

Ttest_indResult(statistic=nan, pvalue=nan)

#### ('burger', 1) vs ('burger', 3)

Ttest_indResult(statistic=nan, pvalue=nan)

#### ('burger', 1) vs ('burger', 4)

Ttest_indResult(statistic=nan, pvalue=nan)

#### ('burger', 1) vs ('burger', 5)

Ttest_indResult(statistic=nan, pvalue=nan)

#### ('burger', 1) vs ('swipe', 1)

Ttest_indResult(statistic=nan, pvalue=nan)

#### ('burger', 1) vs ('swipe', 2)

Ttest_indResult(statistic=nan, pvalue=nan)

#### ('burger', 1) vs ('swipe', 3)

Ttest_indResult(statistic=nan, pvalue=nan)

#### ('burger', 1) vs ('swipe', 4)

Ttest_indResult(statistic=nan, pvalue=nan)

#### ('burger', 1) vs ('swipe', 5)

Ttest_indResult(statistic=nan, pvalue=nan)

#### ('burger', 2) vs ('burger', 3)

Ttest_indResult(statistic=nan, pvalue=nan)

#### ('burger', 2) vs ('burger', 4)

Ttest_indResult(statistic=nan, pvalue=nan)

#### ('burger', 2) vs ('burger', 5)

Ttest_indResult(statistic=nan, pvalue=nan)

#### ('burger', 2) vs ('swipe', 1)

Ttest_indResult(statistic=nan, pvalue=nan)

#### ('burger', 2) vs ('swipe', 2)

Ttest_indResult(statistic=nan, pvalue=nan)

#### ('burger', 2) vs ('swipe', 3)

Ttest_indResult(statistic=nan, pvalue=nan)

#### ('burger', 2) vs ('swipe', 4)

Ttest_indResult(statistic=nan, pvalue=nan)

#### ('burger', 2) vs ('swipe', 5)

Ttest_indResult(statistic=nan, pvalue=nan)

#### ('burger', 3) vs ('burger', 4)

Ttest_indResult(statistic=nan, pvalue=nan)

#### ('burger', 3) vs ('burger', 5)

Ttest_indResult(statistic=nan, pvalue=nan)

#### ('burger', 3) vs ('swipe', 1)

Ttest_indResult(statistic=nan, pvalue=nan)

#### ('burger', 3) vs ('swipe', 2)

Ttest_indResult(statistic=nan, pvalue=nan)

#### ('burger', 3) vs ('swipe', 3)

Ttest_indResult(statistic=nan, pvalue=nan)

#### ('burger', 3) vs ('swipe', 4)

Ttest_indResult(statistic=nan, pvalue=nan)

#### ('burger', 3) vs ('swipe', 5)

Ttest_indResult(statistic=nan, pvalue=nan)

#### ('burger', 4) vs ('burger', 5)

Ttest_indResult(statistic=nan, pvalue=nan)

#### ('burger', 4) vs ('swipe', 1)

Ttest_indResult(statistic=nan, pvalue=nan)

#### ('burger', 4) vs ('swipe', 2)

Ttest_indResult(statistic=nan, pvalue=nan)

#### ('burger', 4) vs ('swipe', 3)

Ttest_indResult(statistic=nan, pvalue=nan)

#### ('burger', 4) vs ('swipe', 4)

Ttest_indResult(statistic=nan, pvalue=nan)

#### ('burger', 4) vs ('swipe', 5)

Ttest_indResult(statistic=nan, pvalue=nan)

#### ('burger', 5) vs ('swipe', 1)

Ttest_indResult(statistic=nan, pvalue=nan)

#### ('burger', 5) vs ('swipe', 2)

Ttest_indResult(statistic=nan, pvalue=nan)

#### ('burger', 5) vs ('swipe', 3)

Ttest_indResult(statistic=nan, pvalue=nan)

#### ('burger', 5) vs ('swipe', 4)

Ttest_indResult(statistic=nan, pvalue=nan)

#### ('burger', 5) vs ('swipe', 5)

Ttest_indResult(statistic=nan, pvalue=nan)

#### ('swipe', 1) vs ('swipe', 2)

Ttest_indResult(statistic=nan, pvalue=nan)

#### ('swipe', 1) vs ('swipe', 3)

Ttest_indResult(statistic=nan, pvalue=nan)

#### ('swipe', 1) vs ('swipe', 4)

Ttest_indResult(statistic=nan, pvalue=nan)

#### ('swipe', 1) vs ('swipe', 5)

Ttest_indResult(statistic=nan, pvalue=nan)

#### ('swipe', 2) vs ('swipe', 3)

Ttest_indResult(statistic=nan, pvalue=nan)

#### ('swipe', 2) vs ('swipe', 4)

Ttest_indResult(statistic=nan, pvalue=nan)

#### ('swipe', 2) vs ('swipe', 5)

Ttest_indResult(statistic=nan, pvalue=nan)

#### ('swipe', 3) vs ('swipe', 4)

Ttest_indResult(statistic=nan, pvalue=nan)

#### ('swipe', 3) vs ('swipe', 5)

Ttest_indResult(statistic=nan, pvalue=nan)

#### ('swipe', 4) vs ('swipe', 5)

Ttest_indResult(statistic=nan, pvalue=nan)

### Global Burger vs Swipe per tid Tests (efficiency)

#### burger vs swipe 1

Ttest_indResult(statistic=nan, pvalue=nan)

#### burger vs swipe 2

Ttest_indResult(statistic=nan, pvalue=nan)

#### burger vs swipe 3

Ttest_indResult(statistic=nan, pvalue=nan)

#### burger vs swipe 4

Ttest_indResult(statistic=nan, pvalue=nan)

#### burger vs swipe 5

Ttest_indResult(statistic=nan, pvalue=nan)

### Global Burger vs Global Swipe Test (efficiency)

#### burger vs swipe

Ttest_indResult(statistic=nan, pvalue=nan)

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

##### swipe

| count | 140.0 |
| mean | 0.934285714286 |
| std | 0.105783427849 |
| min | 0.6 |
| 25% | 0.8 |
| 50% | 1.0 |
| 75% | 1.0 |
| max | 1.0 |

#### Repeated measures (effectiveness)

##### burger

| KruskalResult(statistic=4.2636054421768179, pvalue=0.37150463698880992)
| FriedmanchisquareResult(statistic=5.1111111111109082, pvalue=0.276085623834601)

##### swipe

| KruskalResult(statistic=8.4325646925437621, pvalue=0.076957851331098878)
| FriedmanchisquareResult(statistic=8.7192429022081477, pvalue=0.068513251264267688)

#### Descriptions per tid (effectiveness)

##### ('burger', 1)

| count | 22.0 |
| mean | 0.990909090909 |
| std | 0.0426401432711 |
| min | 0.8 |
| 25% | 1.0 |
| 50% | 1.0 |
| 75% | 1.0 |
| max | 1.0 |

##### ('burger', 2)

| count | 22.0 |
| mean | 0.963636363636 |
| std | 0.0789542033952 |
| min | 0.8 |
| 25% | 1.0 |
| 50% | 1.0 |
| 75% | 1.0 |
| max | 1.0 |

##### ('burger', 3)

| count | 22.0 |
| mean | 0.963636363636 |
| std | 0.0789542033952 |
| min | 0.8 |
| 25% | 1.0 |
| 50% | 1.0 |
| 75% | 1.0 |
| max | 1.0 |

##### ('burger', 4)

| count | 22.0 |
| mean | 0.981818181818 |
| std | 0.0588489886336 |
| min | 0.8 |
| 25% | 1.0 |
| 50% | 1.0 |
| 75% | 1.0 |
| max | 1.0 |

##### ('burger', 5)

| count | 22.0 |
| mean | 0.990909090909 |
| std | 0.0426401432711 |
| min | 0.8 |
| 25% | 1.0 |
| 50% | 1.0 |
| 75% | 1.0 |
| max | 1.0 |

##### ('swipe', 1)

| count | 28.0 |
| mean | 0.978571428571 |
| std | 0.0629940788349 |
| min | 0.8 |
| 25% | 1.0 |
| 50% | 1.0 |
| 75% | 1.0 |
| max | 1.0 |

##### ('swipe', 2)

| count | 28.0 |
| mean | 0.935714285714 |
| std | 0.0951189731211 |
| min | 0.8 |
| 25% | 0.8 |
| 50% | 1.0 |
| 75% | 1.0 |
| max | 1.0 |

##### ('swipe', 3)

| count | 28.0 |
| mean | 0.892857142857 |
| std | 0.138586973437 |
| min | 0.6 |
| 25% | 0.8 |
| 50% | 1.0 |
| 75% | 1.0 |
| max | 1.0 |

##### ('swipe', 4)

| count | 28.0 |
| mean | 0.942857142857 |
| std | 0.0920087412456 |
| min | 0.8 |
| 25% | 0.8 |
| 50% | 1.0 |
| 75% | 1.0 |
| max | 1.0 |

##### ('swipe', 5)

| count | 28.0 |
| mean | 0.921428571429 |
| std | 0.113389341903 |
| min | 0.6 |
| 25% | 0.8 |
| 50% | 1.0 |
| 75% | 1.0 |
| max | 1.0 |

### Cross-compare Tests per tid (effectiveness)

#### ('burger', 1) vs ('burger', 2)

Ttest_indResult(statistic=1.4255728899344782, pvalue=0.16358780899480721)

#### ('burger', 1) vs ('burger', 3)

Ttest_indResult(statistic=1.4255728899344722, pvalue=0.1635878089948089)

#### ('burger', 1) vs ('burger', 4)

Ttest_indResult(statistic=0.5867386940384649, pvalue=0.56082327307745627)

#### ('burger', 1) vs ('burger', 5)

Ttest_indResult(statistic=0.0, pvalue=1.0)

#### ('burger', 1) vs ('swipe', 1)

Ttest_indResult(statistic=0.82366846170589003, pvalue=0.41428064209770366)

#### ('burger', 1) vs ('swipe', 2)

Ttest_indResult(statistic=2.7400353204522681, pvalue=0.0091946014470773128)

#### ('burger', 1) vs ('swipe', 3)

Ttest_indResult(statistic=3.5367966020406145, pvalue=0.0012166207287807747)

#### ('burger', 1) vs ('swipe', 4)

Ttest_indResult(statistic=2.4489928787964925, pvalue=0.018809724953796)

#### ('burger', 1) vs ('swipe', 5)

Ttest_indResult(statistic=2.9849166866864385, pvalue=0.005066877024676052)

#### ('burger', 2) vs ('burger', 3)

Ttest_indResult(statistic=-4.6637076279086357e-15, pvalue=0.99999999999999623)

#### ('burger', 2) vs ('burger', 4)

Ttest_indResult(statistic=-0.86602540378444448, pvalue=0.39179588482667327)

#### ('burger', 2) vs ('burger', 5)

Ttest_indResult(statistic=-1.4255728899344782, pvalue=0.16358780899480721)

#### ('burger', 2) vs ('swipe', 1)

Ttest_indResult(statistic=-0.72439198309892927, pvalue=0.47308750654179754)

#### ('burger', 2) vs ('swipe', 2)

Ttest_indResult(statistic=1.13380582248701, pvalue=0.26252717192400138)

#### ('burger', 2) vs ('swipe', 3)

Ttest_indResult(statistic=2.2734112399558835, pvalue=0.027911615554138184)

#### ('burger', 2) vs ('swipe', 4)

Ttest_indResult(statistic=0.85860431235098866, pvalue=0.39486327780313391)

#### ('burger', 2) vs ('swipe', 5)

Ttest_indResult(statistic=1.5489367311677702, pvalue=0.12804879993894061)

#### ('burger', 3) vs ('burger', 4)

Ttest_indResult(statistic=-0.86602540378443904, pvalue=0.39179588482667649)

#### ('burger', 3) vs ('burger', 5)

Ttest_indResult(statistic=-1.4255728899344722, pvalue=0.1635878089948089)

#### ('burger', 3) vs ('swipe', 1)

Ttest_indResult(statistic=-0.72439198309892372, pvalue=0.47308750654180076)

#### ('burger', 3) vs ('swipe', 2)

Ttest_indResult(statistic=1.1338058224870142, pvalue=0.26252717192399971)

#### ('burger', 3) vs ('swipe', 3)

Ttest_indResult(statistic=2.273411239955887, pvalue=0.027911615554137945)

#### ('burger', 3) vs ('swipe', 4)

Ttest_indResult(statistic=0.8586043123509931, pvalue=0.39486327780313146)

#### ('burger', 3) vs ('swipe', 5)

Ttest_indResult(statistic=1.548936731167774, pvalue=0.12804879993893969)

#### ('burger', 4) vs ('burger', 5)

Ttest_indResult(statistic=-0.5867386940384649, pvalue=0.56082327307745627)

#### ('burger', 4) vs ('swipe', 1)

Ttest_indResult(statistic=0.18772011355652787, pvalue=0.85191261940051899)

#### ('burger', 4) vs ('swipe', 2)

Ttest_indResult(statistic=2.1031460160122153, pvalue=0.040982538230155942)

#### ('burger', 4) vs ('swipe', 3)

Ttest_indResult(statistic=3.063328037911023, pvalue=0.0039982893426720014)

#### ('burger', 4) vs ('swipe', 4)

Ttest_indResult(statistic=1.8170389194463148, pvalue=0.075687083399407801)

#### ('burger', 4) vs ('swipe', 5)

Ttest_indResult(statistic=2.4319786539439705, pvalue=0.019328473504723491)

#### ('burger', 5) vs ('swipe', 1)

Ttest_indResult(statistic=0.82366846170589003, pvalue=0.41428064209770366)

#### ('burger', 5) vs ('swipe', 2)

Ttest_indResult(statistic=2.7400353204522681, pvalue=0.0091946014470773128)

#### ('burger', 5) vs ('swipe', 3)

Ttest_indResult(statistic=3.5367966020406145, pvalue=0.0012166207287807747)

#### ('burger', 5) vs ('swipe', 4)

Ttest_indResult(statistic=2.4489928787964925, pvalue=0.018809724953796)

#### ('burger', 5) vs ('swipe', 5)

Ttest_indResult(statistic=2.9849166866864385, pvalue=0.005066877024676052)

#### ('swipe', 1) vs ('swipe', 2)

Ttest_indResult(statistic=1.9877674693472367, pvalue=0.052697890488069769)

#### ('swipe', 1) vs ('swipe', 3)

Ttest_indResult(statistic=2.9793811989685222, pvalue=0.0050312636920862601)

#### ('swipe', 1) vs ('swipe', 4)

Ttest_indResult(statistic=1.694798048598096, pvalue=0.096626471720385576)

#### ('swipe', 1) vs ('swipe', 5)

Ttest_indResult(statistic=2.3310860696574305, pvalue=0.024596655054722923)

#### ('swipe', 2) vs ('swipe', 3)

Ttest_indResult(statistic=1.3491570401925495, pvalue=0.18364057349667903)

#### ('swipe', 2) vs ('swipe', 4)

Ttest_indResult(statistic=-0.28560636718891863, pvalue=0.77627353626500772)

#### ('swipe', 2) vs ('swipe', 5)

Ttest_indResult(statistic=0.51075391845524742, pvalue=0.61166797783873916)

#### ('swipe', 3) vs ('swipe', 4)

Ttest_indResult(statistic=-1.5904831691285086, pvalue=0.11844067281091235)

#### ('swipe', 3) vs ('swipe', 5)

Ttest_indResult(statistic=-0.84431705367635057, pvalue=0.40236278952334648)

#### ('swipe', 4) vs ('swipe', 5)

Ttest_indResult(statistic=0.77651636653311584, pvalue=0.44097544120891707)

### Global Burger vs Swipe per tid Tests (effectiveness)

#### burger vs swipe 1

Ttest_indResult(statistic=-0.029252746423380799, pvalue=0.97680275053100574)

#### burger vs swipe 2

Ttest_indResult(statistic=2.2419897995561002, pvalue=0.031762405354738295)

#### burger vs swipe 3

Ttest_indResult(statistic=3.1763199109248252, pvalue=0.0034532804986949521)

#### burger vs swipe 4

Ttest_indResult(statistic=1.9213827594698381, pvalue=0.063192249558969904)

#### burger vs swipe 5

Ttest_indResult(statistic=2.5512559484732256, pvalue=0.015832395055001371)

### Global Burger vs Global Swipe Test (effectiveness)

#### burger vs swipe

Ttest_indResult(statistic=4.0827736426313646, pvalue=6.1281992339985695e-05)

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

###### swipe

| count | 140.0 |
| mean | 6.83571428571 |
| std | 0.458504203722 |
| min | 5.0 |
| 25% | 7.0 |
| 50% | 7.0 |
| 75% | 7.0 |
| max | 7.0 |

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

###### ('burger', 2)

| count | 22.0 |
| mean | 6.90909090909 |
| std | 0.294244943168 |
| min | 6.0 |
| 25% | 7.0 |
| 50% | 7.0 |
| 75% | 7.0 |
| max | 7.0 |

###### ('burger', 3)

| count | 22.0 |
| mean | 6.77272727273 |
| std | 0.751621623515 |
| min | 4.0 |
| 25% | 7.0 |
| 50% | 7.0 |
| 75% | 7.0 |
| max | 7.0 |

###### ('burger', 4)

| count | 22.0 |
| mean | 6.90909090909 |
| std | 0.294244943168 |
| min | 6.0 |
| 25% | 7.0 |
| 50% | 7.0 |
| 75% | 7.0 |
| max | 7.0 |

###### ('burger', 5)

| count | 22.0 |
| mean | 6.95454545455 |
| std | 0.213200716356 |
| min | 6.0 |
| 25% | 7.0 |
| 50% | 7.0 |
| 75% | 7.0 |
| max | 7.0 |

###### ('swipe', 1)

| count | 28.0 |
| mean | 6.85714285714 |
| std | 0.448395139423 |
| min | 5.0 |
| 25% | 7.0 |
| 50% | 7.0 |
| 75% | 7.0 |
| max | 7.0 |

###### ('swipe', 2)

| count | 28.0 |
| mean | 6.92857142857 |
| std | 0.262265264156 |
| min | 6.0 |
| 25% | 7.0 |
| 50% | 7.0 |
| 75% | 7.0 |
| max | 7.0 |

###### ('swipe', 3)

| count | 28.0 |
| mean | 6.82142857143 |
| std | 0.475594865606 |
| min | 5.0 |
| 25% | 7.0 |
| 50% | 7.0 |
| 75% | 7.0 |
| max | 7.0 |

###### ('swipe', 4)

| count | 28.0 |
| mean | 6.82142857143 |
| std | 0.475594865606 |
| min | 5.0 |
| 25% | 7.0 |
| 50% | 7.0 |
| 75% | 7.0 |
| max | 7.0 |

###### ('swipe', 5)

| count | 28.0 |
| mean | 6.75 |
| std | 0.585314097381 |
| min | 5.0 |
| 25% | 7.0 |
| 50% | 7.0 |
| 75% | 7.0 |
| max | 7.0 |

#### Cross-compare Tests per tid (result)

##### ('burger', 1) vs ('burger', 2)

Ttest_indResult(statistic=1.4491376746189426, pvalue=0.16206871193916272)

##### ('burger', 1) vs ('burger', 3)

Ttest_indResult(statistic=1.4182715723279398, pvalue=0.17078161271838718)

##### ('burger', 1) vs ('burger', 4)

Ttest_indResult(statistic=1.4491376746189426, pvalue=0.16206871193916272)

##### ('burger', 1) vs ('burger', 5)

Ttest_indResult(statistic=1.0000000000000089, pvalue=0.32869468323645945)

##### ('burger', 1) vs ('swipe', 1)

Ttest_indResult(statistic=1.6858544608470538, pvalue=0.1033481555997189)

##### ('burger', 1) vs ('swipe', 2)

Ttest_indResult(statistic=1.4411533842457791, pvalue=0.16103934953023244)

##### ('burger', 1) vs ('swipe', 3)

Ttest_indResult(statistic=1.9867985355975688, pvalue=0.057179118127154482)

##### ('burger', 1) vs ('swipe', 4)

Ttest_indResult(statistic=1.9867985355975688, pvalue=0.057179118127154482)

##### ('burger', 1) vs ('swipe', 5)

Ttest_indResult(statistic=2.2601124105026518, pvalue=0.03208842174489044)

##### ('burger', 2) vs ('burger', 3)

Ttest_indResult(statistic=0.79240581569306312, pvalue=0.434959083634744)

##### ('burger', 2) vs ('burger', 4)

Ttest_indResult(statistic=0.0, pvalue=1.0)

##### ('burger', 2) vs ('burger', 5)

Ttest_indResult(statistic=-0.58673869403846191, pvalue=0.56082327307745816)

##### ('burger', 2) vs ('swipe', 1)

Ttest_indResult(statistic=0.49271170229567274, pvalue=0.62452609288904781)

##### ('burger', 2) vs ('swipe', 2)

Ttest_indResult(statistic=-0.24365889171012692, pvalue=0.80866695186899662)

##### ('burger', 2) vs ('swipe', 3)

Ttest_indResult(statistic=0.79978792158211109, pvalue=0.42796667468869776)

##### ('burger', 2) vs ('swipe', 4)

Ttest_indResult(statistic=0.79978792158211109, pvalue=0.42796667468869776)

##### ('burger', 2) vs ('swipe', 5)

Ttest_indResult(statistic=1.2510600541476802, pvalue=0.2178987002569478)

##### ('burger', 3) vs ('burger', 4)

Ttest_indResult(statistic=-0.79240581569306312, pvalue=0.434959083634744)

##### ('burger', 3) vs ('burger', 5)

Ttest_indResult(statistic=-1.0915536458196295, pvalue=0.28570930736987338)

##### ('burger', 3) vs ('swipe', 1)

Ttest_indResult(statistic=-0.46568478226137766, pvalue=0.64455504483952952)

##### ('burger', 3) vs ('swipe', 2)

Ttest_indResult(statistic=-0.92910316007448612, pvalue=0.36170919252817291)

##### ('burger', 3) vs ('swipe', 3)

Ttest_indResult(statistic=-0.26506842102661687, pvalue=0.7925715578816479)

##### ('burger', 3) vs ('swipe', 4)

Ttest_indResult(statistic=-0.26506842102661687, pvalue=0.7925715578816479)

##### ('burger', 3) vs ('swipe', 5)

Ttest_indResult(statistic=0.11672011558286063, pvalue=0.90768224442657708)

##### ('burger', 4) vs ('burger', 5)

Ttest_indResult(statistic=-0.58673869403846191, pvalue=0.56082327307745816)

##### ('burger', 4) vs ('swipe', 1)

Ttest_indResult(statistic=0.49271170229567274, pvalue=0.62452609288904781)

##### ('burger', 4) vs ('swipe', 2)

Ttest_indResult(statistic=-0.24365889171012692, pvalue=0.80866695186899662)

##### ('burger', 4) vs ('swipe', 3)

Ttest_indResult(statistic=0.79978792158211109, pvalue=0.42796667468869776)

##### ('burger', 4) vs ('swipe', 4)

Ttest_indResult(statistic=0.79978792158211109, pvalue=0.42796667468869776)

##### ('burger', 4) vs ('swipe', 5)

Ttest_indResult(statistic=1.2510600541476802, pvalue=0.2178987002569478)

##### ('burger', 5) vs ('swipe', 1)

Ttest_indResult(statistic=1.0129210828495314, pvalue=0.31711639921326906)

##### ('burger', 5) vs ('swipe', 2)

Ttest_indResult(statistic=0.38622696788057731, pvalue=0.70103791654914316)

##### ('burger', 5) vs ('swipe', 3)

Ttest_indResult(statistic=1.3216640957475614, pvalue=0.193927451557106)

##### ('burger', 5) vs ('swipe', 4)

Ttest_indResult(statistic=1.3216640957475614, pvalue=0.193927451557106)

##### ('burger', 5) vs ('swipe', 5)

Ttest_indResult(statistic=1.7104014031978396, pvalue=0.095898470850199258)

##### ('swipe', 1) vs ('swipe', 2)

Ttest_indResult(statistic=-0.72760687510900546, pvalue=0.47074919343997945)

##### ('swipe', 1) vs ('swipe', 3)

Ttest_indResult(statistic=0.28912165479145496, pvalue=0.77359920204510002)

##### ('swipe', 1) vs ('swipe', 4)

Ttest_indResult(statistic=0.28912165479145496, pvalue=0.77359920204510002)

##### ('swipe', 1) vs ('swipe', 5)

Ttest_indResult(statistic=0.76892189194508209, pvalue=0.44551595328148408)

##### ('swipe', 2) vs ('swipe', 3)

Ttest_indResult(statistic=1.0438803085865349, pvalue=0.30250767106524179)

##### ('swipe', 2) vs ('swipe', 4)

Ttest_indResult(statistic=1.0438803085865349, pvalue=0.30250767106524179)

##### ('swipe', 2) vs ('swipe', 5)

Ttest_indResult(statistic=1.4732338600612171, pvalue=0.14905035503113803)

##### ('swipe', 3) vs ('swipe', 4)

Ttest_indResult(statistic=0.0, pvalue=1.0)

##### ('swipe', 3) vs ('swipe', 5)

Ttest_indResult(statistic=0.50116144175073229, pvalue=0.61837946822394008)

##### ('swipe', 4) vs ('swipe', 5)

Ttest_indResult(statistic=0.50116144175073229, pvalue=0.61837946822394008)

#### Global Burger vs Swipe per tid Tests (result)

##### burger vs swipe 1

Ttest_indResult(statistic=0.55997233123865175, pvalue=0.57874985452460637)

##### burger vs swipe 2

Ttest_indResult(statistic=-0.31266159062439741, pvalue=0.75558308779702033)

##### burger vs swipe 3

Ttest_indResult(statistic=0.89922333067579296, pvalue=0.37433593164182521)

##### burger vs swipe 4

Ttest_indResult(statistic=0.89922333067579296, pvalue=0.37433593164182521)

##### burger vs swipe 5

Ttest_indResult(statistic=1.3611501176257312, pvalue=0.18254059625123423)

#### Global Burger vs Global Swipe Test (result)

##### burger vs swipe

Ttest_indResult(statistic=1.3562601440255169, pvalue=0.17626116218076363)

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

###### swipe

| count | 140.0 |
| mean | 2.86428571429 |
| std | 2.12964925773 |
| min | 1.0 |
| 25% | 1.0 |
| 50% | 2.0 |
| 75% | 4.0 |
| max | 7.0 |

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

###### ('burger', 2)

| count | 22.0 |
| mean | 1.77272727273 |
| std | 1.87545088374 |
| min | 1.0 |
| 25% | 1.0 |
| 50% | 1.0 |
| 75% | 1.0 |
| max | 7.0 |

###### ('burger', 3)

| count | 22.0 |
| mean | 2.0 |
| std | 1.74574312189 |
| min | 1.0 |
| 25% | 1.0 |
| 50% | 1.0 |
| 75% | 2.0 |
| max | 6.0 |

###### ('burger', 4)

| count | 22.0 |
| mean | 1.77272727273 |
| std | 1.54092792643 |
| min | 1.0 |
| 25% | 1.0 |
| 50% | 1.0 |
| 75% | 1.0 |
| max | 6.0 |

###### ('burger', 5)

| count | 22.0 |
| mean | 1.95454545455 |
| std | 1.98751514465 |
| min | 1.0 |
| 25% | 1.0 |
| 50% | 1.0 |
| 75% | 1.0 |
| max | 7.0 |

###### ('swipe', 1)

| count | 28.0 |
| mean | 2.75 |
| std | 2.36682315602 |
| min | 1.0 |
| 25% | 1.0 |
| 50% | 1.0 |
| 75% | 4.25 |
| max | 7.0 |

###### ('swipe', 2)

| count | 28.0 |
| mean | 2.67857142857 |
| std | 2.21198036674 |
| min | 1.0 |
| 25% | 1.0 |
| 50% | 1.0 |
| 75% | 4.0 |
| max | 7.0 |

###### ('swipe', 3)

| count | 28.0 |
| mean | 2.82142857143 |
| std | 2.16116517662 |
| min | 1.0 |
| 25% | 1.0 |
| 50% | 2.0 |
| 75% | 4.0 |
| max | 7.0 |

###### ('swipe', 4)

| count | 28.0 |
| mean | 2.85714285714 |
| std | 1.87999774851 |
| min | 1.0 |
| 25% | 1.0 |
| 50% | 3.0 |
| 75% | 4.0 |
| max | 7.0 |

###### ('swipe', 5)

| count | 28.0 |
| mean | 3.21428571429 |
| std | 2.11445015806 |
| min | 1.0 |
| 25% | 1.0 |
| 50% | 3.0 |
| 75% | 4.0 |
| max | 7.0 |

#### Cross-compare Tests per tid (result)

##### ('burger', 1) vs ('burger', 2)

Ttest_indResult(statistic=0.31010458564086002, pvalue=0.75802244540869279)

##### ('burger', 1) vs ('burger', 3)

Ttest_indResult(statistic=-0.080051859907446427, pvalue=0.93658374072558803)

##### ('burger', 1) vs ('burger', 4)

Ttest_indResult(statistic=0.33657671342337503, pvalue=0.73822512878677493)

##### ('burger', 1) vs ('burger', 5)

Ttest_indResult(statistic=0.0, pvalue=1.0)

##### ('burger', 1) vs ('swipe', 1)

Ttest_indResult(statistic=-1.2837421053733327, pvalue=0.2054375873090272)

##### ('burger', 1) vs ('swipe', 2)

Ttest_indResult(statistic=-1.2090139880073498, pvalue=0.23271472223326703)

##### ('burger', 1) vs ('swipe', 3)

Ttest_indResult(statistic=-1.463852065048149, pvalue=0.14995179579288434)

##### ('burger', 1) vs ('swipe', 4)

Ttest_indResult(statistic=-1.6208185434680238, pvalue=0.11224980129520724)

##### ('burger', 1) vs ('swipe', 5)

Ttest_indResult(statistic=-2.1492165095182081, pvalue=0.03688815104511671)

##### ('burger', 2) vs ('burger', 3)

Ttest_indResult(statistic=-0.41604800757760851, pvalue=0.6795040084428422)

##### ('burger', 2) vs ('burger', 4)

Ttest_indResult(statistic=0.0, pvalue=1.0)

##### ('burger', 2) vs ('burger', 5)

Ttest_indResult(statistic=-0.31207579904219773, pvalue=0.75653217927135352)

##### ('burger', 2) vs ('swipe', 1)

Ttest_indResult(statistic=-1.6289142640148464, pvalue=0.10987883761813257)

##### ('burger', 2) vs ('swipe', 2)

Ttest_indResult(statistic=-1.5659419487889481, pvalue=0.12397500203185813)

##### ('burger', 2) vs ('swipe', 3)

Ttest_indResult(statistic=-1.8347896616603989, pvalue=0.072806163662061316)

##### ('burger', 2) vs ('swipe', 4)

Ttest_indResult(statistic=-2.0273655509871724, pvalue=0.048533888623595652)

##### ('burger', 2) vs ('swipe', 5)

Ttest_indResult(statistic=-2.550121168647193, pvalue=0.014070036183701212)

##### ('burger', 3) vs ('burger', 4)

Ttest_indResult(statistic=0.45779999816880002, pvalue=0.64949206222919309)

##### ('burger', 3) vs ('burger', 5)

Ttest_indResult(statistic=0.08059475790364122, pvalue=0.93615340884054188)

##### ('burger', 3) vs ('swipe', 1)

Ttest_indResult(statistic=-1.2889066290162134, pvalue=0.20362802550896689)

##### ('burger', 3) vs ('swipe', 2)

Ttest_indResult(statistic=-1.2123668735785071, pvalue=0.23130618790625015)

##### ('burger', 3) vs ('swipe', 3)

Ttest_indResult(statistic=-1.4865530860485299, pvalue=0.14367932916113879)

##### ('burger', 3) vs ('swipe', 4)

Ttest_indResult(statistic=-1.665827282358026, pvalue=0.10245606821048929)

##### ('burger', 3) vs ('swipe', 5)

Ttest_indResult(statistic=-2.2236416215700405, pvalue=0.030927460331272798)

##### ('burger', 4) vs ('burger', 5)

Ttest_indResult(statistic=-0.33910136104054245, pvalue=0.73632757197468268)

##### ('burger', 4) vs ('swipe', 1)

Ttest_indResult(statistic=-1.7609344102128832, pvalue=0.084815434369215556)

##### ('burger', 4) vs ('swipe', 2)

Ttest_indResult(statistic=-1.7037658302714056, pvalue=0.09497299007775549)

##### ('burger', 4) vs ('swipe', 3)

Ttest_indResult(statistic=-2.0007469881640132, pvalue=0.051138917909208527)

##### ('burger', 4) vs ('swipe', 4)

Ttest_indResult(statistic=-2.2409958289424603, pvalue=0.029698757129413455)

##### ('burger', 4) vs ('swipe', 5)

Ttest_indResult(statistic=-2.7866677954802945, pvalue=0.0076168232047276047)

##### ('burger', 5) vs ('swipe', 1)

Ttest_indResult(statistic=-1.2910409183090523, pvalue=0.20290434875885618)

##### ('burger', 5) vs ('swipe', 2)

Ttest_indResult(statistic=-1.2163777102367443, pvalue=0.22990419438692747)

##### ('burger', 5) vs ('swipe', 3)

Ttest_indResult(statistic=-1.4729715892618513, pvalue=0.14745914516885314)

##### ('burger', 5) vs ('swipe', 4)

Ttest_indResult(statistic=-1.6322512563257097, pvalue=0.10976494840900448)

##### ('burger', 5) vs ('swipe', 5)

Ttest_indResult(statistic=-2.1628863874669357, pvalue=0.035735733189624176)

##### ('swipe', 1) vs ('swipe', 2)

Ttest_indResult(statistic=0.11667176816723937, pvalue=0.90755497563889476)

##### ('swipe', 1) vs ('swipe', 3)

Ttest_indResult(statistic=-0.11792698212695876, pvalue=0.90656666165487043)

##### ('swipe', 1) vs ('swipe', 4)

Ttest_indResult(statistic=-0.18756785365546197, pvalue=0.85195435322794189)

##### ('swipe', 1) vs ('swipe', 5)

Ttest_indResult(statistic=-0.77408790290137819, pvalue=0.44229719902179665)

##### ('swipe', 2) vs ('swipe', 3)

Ttest_indResult(statistic=-0.24444025311801382, pvalue=0.80781680136158207)

##### ('swipe', 2) vs ('swipe', 4)

Ttest_indResult(statistic=-0.32549781971440689, pvalue=0.74609483697056533)

##### ('swipe', 2) vs ('swipe', 5)

Ttest_indResult(statistic=-0.92637576511926945, pvalue=0.35838094161896383)

##### ('swipe', 3) vs ('swipe', 4)

Ttest_indResult(statistic=-0.065975241937917109, pvalue=0.94764585285887681)

##### ('swipe', 3) vs ('swipe', 5)

Ttest_indResult(statistic=-0.68754973774649286, pvalue=0.49468042451910721)

##### ('swipe', 4) vs ('swipe', 5)

Ttest_indResult(statistic=-0.66793226421816831, pvalue=0.50706047845662638)

#### Global Burger vs Swipe per tid Tests (result)

##### burger vs swipe 1

Ttest_indResult(statistic=-1.7920485696152606, pvalue=0.081668377626223213)

##### burger vs swipe 2

Ttest_indResult(statistic=-1.7418063441047225, pvalue=0.089916422412057356)

##### burger vs swipe 3

Ttest_indResult(statistic=-2.0988468236683779, pvalue=0.042676536020284629)

##### burger vs swipe 4

Ttest_indResult(statistic=-2.446535421195474, pvalue=0.018837342914925163)

##### burger vs swipe 5

Ttest_indResult(statistic=-3.0406465555493165, pvalue=0.0042798608827830081)

#### Global Burger vs Global Swipe Test (result)

##### burger vs swipe

Ttest_indResult(statistic=-3.9046179737739855, pvalue=0.00012188835447452269)

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

###### swipe

| count | 28.0 |
| mean | 1.53571428571 |
| std | 1.29048204766 |
| min | 1.0 |
| 25% | 1.0 |
| 50% | 1.0 |
| 75% | 1.25 |
| max | 7.0 |

#### Global Burger vs Global Swipe Test (result)

##### burger vs swipe

Ttest_indResult(statistic=-0.10751543495766284, pvalue=0.9148292292550424)

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

###### swipe

| count | 28.0 |
| mean | 1.67857142857 |
| std | 1.18801332542 |
| min | 1.0 |
| 25% | 1.0 |
| 50% | 1.0 |
| 75% | 2.0 |
| max | 6.0 |

#### Global Burger vs Global Swipe Test (result)

##### burger vs swipe

Ttest_indResult(statistic=1.2353085848140299, pvalue=0.22501281363206999)

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

###### swipe

| count | 28.0 |
| mean | 1.75 |
| std | 1.37773297418 |
| min | 1.0 |
| 25% | 1.0 |
| 50% | 1.0 |
| 75% | 2.0 |
| max | 7.0 |

#### Global Burger vs Global Swipe Test (result)

##### burger vs swipe

Ttest_indResult(statistic=-1.8942147514189334, pvalue=0.066878319737774167)

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

###### swipe

| count | 28.0 |
| mean | 4.5 |
| std | 1.45296631451 |
| min | 1.0 |
| 25% | 4.0 |
| 50% | 4.0 |
| 75% | 5.25 |
| max | 7.0 |

#### Global Burger vs Global Swipe Test (result)

##### burger vs swipe

Ttest_indResult(statistic=1.4151306918873736, pvalue=0.16442349507017537)
