input_file=data_source/NTCIR_MedNLP2/ntcir11_mednlp_mednlp2sub.xml
out_dir=text/org
work_dir=text/tmp/NTCIR_MedNLP2

cat $input_file | sed -z 's/\n/\$\n/g' | sed -z 's/</\n</g' | \
    sed -z 's/>/>\n/g' | grep -v '<' | sed -z 's/\n//g' | tr '$' '\n' | \
    sed -e 's/\t//g' | grep -v '^$' > $work_dir/NTCIR-MED_a.txt
awk '!a[$0]++' $work_dir/NTCIR-MED_a.txt | \
    python script/to_zen.py -s -t > $out_dir/NTCIR-MED.txt
