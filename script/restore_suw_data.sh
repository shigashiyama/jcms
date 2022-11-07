in_dir=suw-sc/proc
out_dir=suw/proc
for file in `ls $in_dir`; do
    python script/merge_separated_conjsuf.py $in_dir/$file > $out_dir/$file
done
