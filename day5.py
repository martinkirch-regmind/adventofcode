test_input = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

input = """645,570 -> 517,570
100,409 -> 200,409
945,914 -> 98,67
22,934 -> 22,681
935,781 -> 524,370
750,304 -> 854,408
974,27 -> 26,975
529,58 -> 979,58
979,515 -> 550,944
925,119 -> 17,119
178,594 -> 45,461
252,366 -> 92,206
25,593 -> 250,593
956,34 -> 21,969
200,671 -> 200,369
628,614 -> 628,637
697,428 -> 237,428
554,40 -> 554,949
927,197 -> 469,197
504,779 -> 593,868
227,882 -> 227,982
56,905 -> 56,81
438,874 -> 566,746
989,73 -> 113,949
82,36 -> 616,570
670,423 -> 670,873
100,435 -> 291,435
242,81 -> 978,817
367,335 -> 367,332
890,584 -> 116,584
572,192 -> 572,561
391,516 -> 391,559
525,62 -> 525,540
787,540 -> 812,515
749,732 -> 423,406
745,911 -> 694,911
805,18 -> 972,18
701,565 -> 280,144
930,92 -> 129,893
15,989 -> 970,34
409,920 -> 409,345
192,743 -> 312,863
724,12 -> 29,707
323,664 -> 323,897
161,423 -> 391,653
59,363 -> 250,554
407,676 -> 19,288
449,585 -> 449,301
914,798 -> 914,806
917,401 -> 288,401
588,800 -> 647,800
897,883 -> 897,276
115,606 -> 41,532
692,482 -> 777,482
428,736 -> 69,736
405,44 -> 405,632
198,482 -> 198,620
988,816 -> 988,598
254,461 -> 186,393
560,783 -> 208,783
856,766 -> 215,125
182,30 -> 569,30
504,242 -> 656,242
393,929 -> 131,929
597,359 -> 26,930
502,690 -> 255,443
149,608 -> 149,748
293,662 -> 622,662
697,154 -> 697,228
587,804 -> 983,804
715,63 -> 715,709
496,831 -> 23,358
461,48 -> 68,441
927,565 -> 595,565
972,350 -> 689,350
728,438 -> 728,221
173,134 -> 173,804
720,368 -> 121,368
690,66 -> 201,66
218,680 -> 841,680
80,792 -> 80,467
624,319 -> 624,461
248,348 -> 532,64
357,260 -> 505,408
296,814 -> 13,531
819,216 -> 819,932
696,233 -> 696,840
219,93 -> 868,93
537,63 -> 905,63
777,940 -> 777,84
286,133 -> 286,735
969,967 -> 969,823
254,222 -> 859,827
426,728 -> 426,388
854,561 -> 854,363
755,861 -> 755,947
570,754 -> 439,754
333,351 -> 333,828
436,693 -> 436,262
982,987 -> 172,177
267,178 -> 267,270
218,201 -> 747,730
811,602 -> 829,584
602,659 -> 766,659
536,544 -> 483,597
280,881 -> 547,881
584,125 -> 129,125
386,210 -> 757,210
605,855 -> 605,668
19,985 -> 988,16
980,655 -> 836,655
73,189 -> 267,383
621,645 -> 533,645
36,12 -> 255,231
538,889 -> 130,481
921,217 -> 921,724
873,59 -> 873,311
76,918 -> 970,24
694,448 -> 694,983
573,891 -> 573,337
796,358 -> 403,358
532,928 -> 351,928
123,717 -> 123,446
874,714 -> 874,886
350,458 -> 728,458
798,140 -> 798,242
832,406 -> 864,406
188,55 -> 188,641
903,376 -> 509,376
50,954 -> 989,15
42,294 -> 25,294
544,273 -> 974,273
804,756 -> 103,55
398,184 -> 570,12
82,179 -> 902,179
461,728 -> 905,284
429,241 -> 26,241
128,715 -> 207,715
239,545 -> 934,545
978,769 -> 978,576
250,77 -> 515,77
521,533 -> 521,434
955,844 -> 314,203
144,601 -> 702,43
313,784 -> 339,784
388,692 -> 805,275
540,872 -> 540,72
971,19 -> 17,973
816,540 -> 386,540
933,246 -> 560,619
800,600 -> 387,187
272,791 -> 129,934
908,133 -> 110,931
759,191 -> 910,40
420,479 -> 749,150
604,946 -> 804,946
633,404 -> 771,266
948,974 -> 948,734
735,198 -> 105,828
889,653 -> 889,688
157,172 -> 822,837
206,670 -> 297,670
50,122 -> 792,864
656,664 -> 27,664
966,33 -> 523,33
985,40 -> 101,924
394,367 -> 574,547
440,573 -> 268,573
159,989 -> 159,130
867,123 -> 867,891
316,153 -> 316,249
680,59 -> 773,152
52,928 -> 52,182
128,595 -> 225,595
508,719 -> 591,719
595,447 -> 709,333
930,783 -> 283,136
366,236 -> 283,236
820,512 -> 381,951
135,450 -> 135,766
750,838 -> 534,838
259,304 -> 626,671
414,631 -> 916,129
193,862 -> 901,154
362,595 -> 362,209
377,215 -> 377,499
723,16 -> 577,16
335,238 -> 790,693
670,266 -> 871,65
288,313 -> 213,313
48,423 -> 592,967
960,323 -> 911,323
177,182 -> 177,235
773,918 -> 757,918
216,432 -> 147,432
808,500 -> 656,500
205,451 -> 776,451
598,985 -> 598,608
193,253 -> 241,205
912,384 -> 912,532
214,194 -> 214,738
508,356 -> 508,792
16,372 -> 30,372
384,854 -> 986,252
361,569 -> 851,569
923,550 -> 923,441
271,257 -> 318,304
651,345 -> 651,397
885,14 -> 929,14
199,547 -> 925,547
803,176 -> 104,875
840,302 -> 197,945
971,743 -> 355,127
684,951 -> 684,292
58,867 -> 58,953
351,187 -> 351,831
701,413 -> 701,728
482,159 -> 134,159
118,52 -> 950,884
115,968 -> 115,137
437,739 -> 627,929
653,153 -> 549,153
604,504 -> 560,460
538,865 -> 840,563
114,876 -> 114,124
152,899 -> 925,126
973,224 -> 973,387
492,360 -> 861,729
927,902 -> 108,83
754,678 -> 754,647
526,671 -> 423,671
675,608 -> 243,608
147,241 -> 147,242
456,770 -> 456,665
953,50 -> 102,901
415,869 -> 415,733
979,533 -> 169,533
336,385 -> 336,18
927,176 -> 927,587
370,317 -> 933,880
450,349 -> 450,103
755,235 -> 408,235
342,55 -> 931,55
417,707 -> 887,237
141,95 -> 131,85
776,209 -> 590,23
39,732 -> 469,302
743,602 -> 743,358
473,439 -> 473,545
270,290 -> 270,640
904,963 -> 949,963
71,91 -> 956,976
865,757 -> 276,757
59,72 -> 966,979
46,184 -> 788,926
360,833 -> 561,833
120,452 -> 528,452
704,927 -> 158,381
140,481 -> 140,350
929,920 -> 929,342
328,381 -> 328,866
897,389 -> 227,389
341,614 -> 29,614
609,327 -> 609,582
727,858 -> 727,941
349,536 -> 349,500
280,959 -> 259,959
973,637 -> 832,637
161,255 -> 979,255
512,826 -> 149,826
308,769 -> 22,769
60,692 -> 60,262
787,31 -> 753,31
932,166 -> 932,127
514,77 -> 514,646
535,434 -> 535,979
838,799 -> 838,332
565,956 -> 565,477
74,195 -> 274,195
916,715 -> 907,715
721,655 -> 721,542
180,784 -> 928,784
16,128 -> 313,128
23,330 -> 23,704
530,723 -> 530,88
869,272 -> 765,376
878,185 -> 353,185
72,800 -> 514,800
319,117 -> 307,117
436,405 -> 496,345
327,459 -> 641,145
358,309 -> 661,612
60,225 -> 811,976
113,130 -> 794,130
559,950 -> 32,423
626,110 -> 626,319
50,39 -> 989,978
257,627 -> 799,627
581,843 -> 581,493
869,18 -> 208,18
184,395 -> 184,263
454,888 -> 165,599
637,920 -> 637,544
170,982 -> 273,982
98,354 -> 668,924
32,409 -> 32,925
154,175 -> 273,294
425,896 -> 870,451
198,319 -> 615,736
170,582 -> 170,712
141,645 -> 141,639
482,768 -> 486,768
940,969 -> 24,53
680,360 -> 959,360
315,905 -> 315,96
22,666 -> 22,247
722,40 -> 722,714
585,31 -> 585,21
479,254 -> 307,254
291,182 -> 291,855
684,698 -> 402,698
20,984 -> 988,16
256,424 -> 17,663
825,380 -> 820,385
254,622 -> 254,315
98,855 -> 98,694
220,719 -> 220,117
615,653 -> 656,694
427,12 -> 427,745
20,64 -> 828,872
739,203 -> 434,203
546,576 -> 130,160
730,835 -> 299,835
927,512 -> 927,586
411,192 -> 868,192
917,630 -> 678,630
620,588 -> 620,26
786,488 -> 486,488
746,640 -> 251,145
585,556 -> 585,119
977,202 -> 762,202
587,244 -> 587,877
693,479 -> 693,859
59,816 -> 59,475
191,941 -> 878,254
150,920 -> 926,144
856,397 -> 856,739
380,965 -> 549,796
637,323 -> 909,595
848,219 -> 304,763
123,146 -> 589,146
546,122 -> 651,122
131,711 -> 814,28
727,274 -> 296,274
101,546 -> 479,168
508,517 -> 615,410
492,115 -> 492,250
212,65 -> 770,623
118,938 -> 857,199
623,843 -> 98,843
86,153 -> 701,768
81,98 -> 81,604
173,313 -> 173,533
792,396 -> 792,242
975,985 -> 10,20
762,661 -> 726,661
216,327 -> 216,122
446,658 -> 98,658
85,184 -> 314,184
165,750 -> 313,750
729,583 -> 729,640
382,36 -> 382,326
487,32 -> 225,32
389,722 -> 582,915
954,965 -> 86,965
747,376 -> 747,96
254,259 -> 254,482
149,256 -> 149,871
893,207 -> 708,22
195,907 -> 195,82
342,686 -> 457,571
647,469 -> 468,469
150,525 -> 832,525
90,907 -> 90,31
389,554 -> 389,318
138,327 -> 138,310
861,126 -> 861,549
355,583 -> 355,534
591,182 -> 181,592
73,84 -> 897,908
326,989 -> 425,989
835,688 -> 724,799
844,493 -> 844,974
172,436 -> 172,12
536,933 -> 48,445
192,531 -> 287,531
286,547 -> 80,547
929,795 -> 697,795
790,681 -> 433,681
692,229 -> 731,229
377,667 -> 14,304
535,226 -> 116,645
338,861 -> 338,343
668,160 -> 853,160
188,157 -> 667,636
62,934 -> 951,45
948,820 -> 978,820
860,884 -> 157,884
794,251 -> 783,251
317,381 -> 591,655
459,876 -> 459,307
146,822 -> 903,65
374,739 -> 891,739
619,575 -> 973,929
544,351 -> 544,124
300,335 -> 818,335
158,220 -> 418,480
107,953 -> 988,953
304,753 -> 543,753
948,95 -> 140,903
832,451 -> 526,145
966,34 -> 402,598
72,123 -> 716,123
336,294 -> 84,294
116,605 -> 116,889
700,742 -> 700,217
551,554 -> 973,554
684,181 -> 66,799
86,949 -> 86,173
834,361 -> 834,942
508,668 -> 627,549
213,695 -> 704,695
260,979 -> 868,371
825,435 -> 825,67
956,854 -> 66,854
390,444 -> 697,444
360,450 -> 720,810
153,514 -> 794,514
253,261 -> 253,298
925,679 -> 925,499
391,282 -> 441,282
86,366 -> 779,366
687,312 -> 687,629
304,172 -> 732,600
571,518 -> 263,518
814,252 -> 118,252
108,920 -> 108,162
154,965 -> 928,191
635,875 -> 635,947
986,31 -> 47,970
746,35 -> 746,636
735,849 -> 334,448
826,510 -> 906,590
834,745 -> 834,949
843,401 -> 564,122
179,212 -> 179,32
354,906 -> 233,906
593,439 -> 196,42
707,446 -> 242,446
511,84 -> 511,406
109,299 -> 100,290
410,79 -> 410,784
806,923 -> 54,171
592,83 -> 592,189
413,28 -> 413,469
17,844 -> 17,691
130,419 -> 205,344
374,247 -> 849,247
650,344 -> 653,344
563,942 -> 563,726
771,966 -> 450,966
499,693 -> 788,693
962,458 -> 962,356
28,683 -> 765,683
432,546 -> 432,708
519,974 -> 176,974
797,744 -> 280,227
505,228 -> 547,228
401,366 -> 401,754
356,470 -> 123,470
57,909 -> 229,909
343,880 -> 539,880
221,851 -> 221,297
520,677 -> 894,677
216,805 -> 688,805
158,901 -> 847,901
98,129 -> 98,969
793,203 -> 210,786
852,855 -> 135,138
944,90 -> 103,931
691,768 -> 583,768
784,617 -> 637,764
222,160 -> 819,757
145,982 -> 145,216
837,355 -> 99,355
324,121 -> 324,14
773,851 -> 773,413
778,550 -> 686,458
81,56 -> 338,313
356,512 -> 356,441"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def step_to(self, other):
        vector = (other.x - self.x, other.y - self.y)
        if vector[0] != 0 and vector[1] != 0 and abs(vector[0]) != abs(vector[1]):
            raise ValueError()

        return ((vector[0] // abs(vector[0])) if vector[0] != 0 else 0, (vector[1] // abs(vector[1])) if vector[1] != 0 else 0)
    
    def move(self, vector):
        return Point(self.x + vector[0], self.y + vector[1])
    
    def __eq__(self, __o: object) -> bool:
        return (self.x == __o.x) and (self.y == __o.y)

segments = []
max_x = 0
max_y = 0
for line in input.split("\n"):
    segment = line.split("->")
    start = Point(*[int(x) for x in segment[0].split(',')])
    end   = Point(*[int(x) for x in segment[1].split(',')])
    max_x = max(max_x, start.x, end.x)
    max_y = max(max_y, start.y, end.y)
    segments.append((start, end))

print(f"max_x {max_x}, max_y {max_y}")

diagram = [[0] * (max_y+1) for i in range(max_x+1)]

for segment in segments:
    current = segment[0]
    try:
        vector = current.step_to(segment[1])
    except ValueError:
        continue
    diagram[current.x][current.y] += 1
    while current != segment[1]:
        current = current.move(vector)
        diagram[current.x][current.y] += 1

dangerous = 0
for line in diagram:
    #print(line)
    for point in line:
        if point >= 2:
            dangerous += 1

print(dangerous)
