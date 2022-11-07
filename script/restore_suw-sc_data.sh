mask_dir=suw-sc/mask
text_dir=text/org
out_dir=suw-sc/proc
for file in `ls $text_dir`; do
    name=`basename $file`
    name=${name%.*}
    python script/restore.py $mask_dir/${name}.mask $text_dir/${name}.txt > $out_dir/${name}.txt
done
