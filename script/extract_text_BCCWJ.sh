input_dir=data_source/BCCWJ/Disk4/TSV_SUW_OT
out_dir=text/org
work_dir=text/tmp/BCCWJ

declare -A vals=(
    ["OL"]=38627
    ["OM"]=36710
    ["OP"]=24289
    ["OT"]=17839
    ["OV"]=16043
)

for name in ${!vals[@]}; do
    echo "Extracting $name sentences"

    paste <(head -${vals["$name"]} $input_dir/$name/$name.txt | cut -f10,23) \
          <(head -${vals["$name"]} $input_dir/$name/$name.txt | cut -f17-19) | \
        sed -z 's/\nB/\n\nB/g' | cut -f2- | grep -v 'ｈｔｔｐ' \
        > $work_dir/${name}_a_seg.txt

    if [ $name = "OV" ]; then
        cp $work_dir/${name}_a_seg.txt $work_dir/${name}_seg.txt

    elif [ $name = "OT" ]; then
        head -${vals["$name"]} $input_dir/$name/$name.txt | cut -f10,17,23 | \
            sed -z 's/\nB/\n\nB/g' | cut -f2,3 | tr '\t' '_' | \
            python script/to_chars.py -tword -s -n | awk 'a[$0]++' | \
            sort -u > $work_dir/${name}_b.txt

        python script/remove_dup_bccwj_data.py $work_dir/${name}_a_seg.txt \
               $work_dir/${name}_b.txt use_pos > $work_dir/${name}_seg.txt

    else
        head -${vals["$name"]} $input_dir/$name/$name.txt | cut -f10,23 | \
            sed -z 's/\nB/\n\nB/g' | cut -f2 | \
            python script/to_chars.py -traw -s -n | grep -v 'ｈｔｔｐ' |
            awk 'a[$0]++' | sort -u > $work_dir/${name}_b.txt

        python script/remove_dup_bccwj_data.py $work_dir/${name}_a_seg.txt \
               $work_dir/${name}_b.txt > $work_dir/${name}_seg.txt
    fi
           
    cut -f1 $work_dir/${name}_seg.txt | python script/to_chars.py -traw -s -n \
        > $out_dir/BCCWJ-${name}.txt
done
