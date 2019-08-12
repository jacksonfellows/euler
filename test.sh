#!/bin/bash
get () {
	awk -F "$1" "\$1 == $2 {print \$2}" $3
}

is_number () {
	re='^-?[0-9]+$'
	[[ $1 =~ $re ]]
}
export -f is_number

check () {
	runner=$1; file=$2; ans=$3
	res=$($runner $file 2> /dev/null | tail -n 1)
	if ! is_number "$res"; then
		echo $file: result \""$res"\" is not a number
	elif (( "$res" != "$ans" )); then
		echo $file: failed \("$res" != "$ans"\)
	else
		echo $file: passed \("$res" == "$ans"\)
	fi
}
export -f check

test_file () {
	file=$1; past=$2
	base=$(basename "$file")
	ext=${base##*.}
	runner=$(get ":" "\"$ext\"" "$past/runners.txt")
	if [ -z "$runner" ]; then
		echo $file: extension $ext has no runner
		continue
	fi
	num=${base%%_*}
	if ! is_number $num; then
		echo $file: problem number \""$num"\" is not a number
		continue
	fi
	ans=$(get " " "$num" "$past/answers.txt")
	if [ -z "$ans" ]; then
		echo $file: problem number $num has no answer \(yet!\)
		continue
	fi
	if ! timeout 1m bash -c "check '$runner' '$file' '$ans'"; then
		echo $file: timed out
	fi
}

test_dir () {
	dir=$1
	echo Testing directory $dir
	past=$(pwd)
	cd $dir
	for file in $(find * -type f -depth 0); do
		test_file "$file" "$past"
	done
	cd $past
}

if [ -z $* ]; then
	args="*/"
else
	args="$*"
fi

for name in $args; do
	if [ -d "$name" ]; then
		test_dir "$name"
	else
		test_file "$name" "$(pwd)"
	fi
	# TODO: add coverage report
done
