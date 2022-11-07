# download and decompress "ntcir8_patmt_ntc8-patmt-train.tgz" as "ntc8-patmt-train"

input_file=data_source/NTCIR_PatentMT/ntc8-patmt-train/ntc8/pat-2003-2005.txt
out_dir=text/org

head -1107 $input_file | nkf -w | sed -e 's/ ||| /\t/g' | cut -f3 | \
    python script/to_zen.py -s | awk '!a[$0]++' \
    > $out_dir/NTCIR-PAT.txt
