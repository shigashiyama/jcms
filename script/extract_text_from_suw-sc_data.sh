in_dir=suw-sc/proc
out_dir=text/proc
for file in `ls $in_dir/*.txt`; do
    name=`basename $file`
    grep '^#' $file | sed -e 's/^# ID=[0-9]\+ TEXT=//g' > $out_dir/$name
done
