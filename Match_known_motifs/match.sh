
query_pwm=$1
target_pwm=$2
output_folder=$3
T=$4

tomtom -o $output_folder $query_pwm $target_pwm 

python parse_tomtom.py $output_folder/tomtom.txt $query_pwm.matched.list $T 