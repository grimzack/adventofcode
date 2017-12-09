# aoc_2.1.py

puzzle_input = "1208	412	743	57	1097	53	71	1029	719	133	258	69	1104	373	367	365\n\
4011	4316	1755	4992	228	240	3333	208	247	3319	4555	717	1483	4608	1387	3542\n\
675	134	106	115	204	437	1035	1142	195	1115	569	140	1133	190	701	1016\n\
4455	2184	5109	221	3794	246	5214	4572	3571	3395	2054	5050	216	878	237	3880\n\
4185	5959	292	2293	118	5603	2167	5436	3079	167	243	256	5382	207	5258	4234\n\
94	402	126	1293	801	1604	1481	1292	1428	1051	345	1510	1417	684	133	119\n\
120	1921	115	3188	82	334	366	3467	103	863	3060	2123	3429	1974	557	3090\n\
53	446	994	71	872	898	89	982	957	789	1040	100	133	82	84	791\n\
2297	733	575	2896	1470	169	2925	1901	195	2757	1627	1216	148	3037	392	221\n\
1343	483	67	1655	57	71	1562	447	58	1561	889	1741	1338	88	1363	560\n\
2387	3991	3394	6300	2281	6976	234	204	6244	854	1564	210	195	7007	3773	3623\n\
1523	77	1236	1277	112	171	70	1198	86	1664	1767	75	315	143	1450	1610\n\
168	2683	1480	200	1666	1999	3418	2177	156	430	2959	3264	2989	136	110	3526\n\
8702	6973	203	4401	8135	7752	1704	8890	182	9315	255	229	6539	647	6431	6178\n\
2290	157	2759	3771	4112	2063	153	3538	3740	130	3474	1013	180	2164	170	189\n\
525	1263	146	954	188	232	1019	918	268	172	1196	1091	1128	234	650	420"

test_input_1 = "5	1	9	5\n7	5	3\n2	4	6	8"

def checksum_calculator(input_str):
	# Input comes in as a string, parse it into a list of strings.
	rows = input_str.split("\n")

	rows_nums_only = []
	for i in range(len(rows)):
		rows_nums_only.append(rows[i].split("\t"))

	usable_data = []
	for i in range(len(rows_nums_only)):
		row_data = []
		for number in rows_nums_only[i]:
			row_data.append(int(number))
		usable_data.append(row_data)

	sum_of_differences = 0
	for row in usable_data:
		row_difference = 0
		row_max = row[0]
		row_min = row[0]
		# Go through each row and find the minimum and maximum
		for number in row:
			if number > row_max:
				row_max = number
			if number < row_min:
				row_min = number
		# Compute the difference of max and min
		row_difference = row_max - row_min
		# Add it to the sum
		sum_of_differences += row_difference

	print sum_of_differences

checksum_calculator(puzzle_input)