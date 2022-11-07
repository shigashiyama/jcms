input_file=data_source/ASPEC/ASPEC-JE/train/train-1.txt 
out_dir=text/org
work_dir=text/tmp/ASPEC

input_file2=$work_dir/ASPEC-JE_train-1.txt
echo "Converting ASPEC data (This will take some time.)"
sed -e 's/ ||| /'$'\t/g' $input_file | cut -f2,4 > $input_file2

echo "Extracting sentences for each domain"
grep '^B' $input_file2 | cut -f2 | head -1001 | awk '!a[$0]++' > $out_dir/ASPEC-JE-PHY.txt   # B: 物理学
grep '^C' $input_file2 | cut -f2 | head -1700 | awk '!a[$0]++' > $out_dir/ASPEC-JE-CHE-B.txt # C: 基礎化学
grep '^X' $input_file2 | cut -f2 | head -750  | awk '!a[$0]++' > $out_dir/ASPEC-JE-CHE-E.txt # X: 化学工学
grep '^Y' $input_file2 | cut -f2 | head -950  | awk '!a[$0]++' > $out_dir/ASPEC-JE-CHE-I.txt # Y: 化学工業
grep '^D' $input_file2 | cut -f2 | head -800  | awk '!a[$0]++' > $out_dir/ASPEC-JE-ETH.txt   # D: 宇宙・地球の科学
grep '^E' $input_file2 | cut -f2 | head -1000 | awk '!a[$0]++' > $out_dir/ASPEC-JE-BIO.txt   # E: 生物科学
grep '^F' $input_file2 | cut -f2 | head -900  | awk '!a[$0]++' > $out_dir/ASPEC-JE-AGR.txt   # F: 農林水産
grep '^G' $input_file2 | cut -f2 | head -1319 | awk '!a[$0]++' > $out_dir/ASPEC-JE-MED.txt   # G: 医学
grep '^I' $input_file2 | cut -f2 | head -1500 | awk '!a[$0]++' > $out_dir/ASPEC-JE-SYS.txt   # I: システム・制御工学
grep '^J' $input_file2 | cut -f2 | head -900  | awk '!a[$0]++' > $out_dir/ASPEC-JE-INF.txt   # J: 情報工学
grep '^K' $input_file2 | cut -f2 | head -1501 | awk '!a[$0]++' > $out_dir/ASPEC-JE-MAN.txt   # K: 経営工学
grep '^L' $input_file2 | cut -f2 | head -1360 | awk '!a[$0]++' > $out_dir/ASPEC-JE-ENE.txt   # L: エネルギー工学
grep '^M' $input_file2 | cut -f2 | head -800  | awk '!a[$0]++' > $out_dir/ASPEC-JE-NUC.txt   # M: 原子力工学
grep '^N' $input_file2 | cut -f2 | head -2002 | awk '!a[$0]++' > $out_dir/ASPEC-JE-ELC.txt   # N: 電気工学
grep '^P' $input_file2 | cut -f2 | head -1502 | awk '!a[$0]++' > $out_dir/ASPEC-JE-THM.txt   # P: 熱工学，応用熱力学
grep '^Q' $input_file2 | cut -f2 | head -1752 | awk '!a[$0]++' > $out_dir/ASPEC-JE-MEC.txt   # Q: 機械工学
grep '^R' $input_file2 | cut -f2 | head -1704 | awk '!a[$0]++' > $out_dir/ASPEC-JE-CON.txt   # R: 建設工学
grep '^S' $input_file2 | cut -f2 | head -870  | awk '!a[$0]++' > $out_dir/ASPEC-JE-ENV.txt   # S: 環境工学
grep '^T' $input_file2 | cut -f2 | head -1431 | awk '!a[$0]++' > $out_dir/ASPEC-JE-TRA.txt   # T: 運輸交通工学
grep '^U' $input_file2 | cut -f2 | head -640  | awk '!a[$0]++' > $out_dir/ASPEC-JE-MIN.txt   # U: 鉱山工学
