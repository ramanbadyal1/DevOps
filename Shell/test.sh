#!/bin/bash
a=10
b=15

echo $((a == b))

# conditional statements:

read -p "Enter your age here: " age
if [[ $age -gt 18 ]]; then
    echo "you can vote"
else
    echo "you can not vote"
fi

age=100
is_citizen="no"

if [[ $age -gt 18 && $is_citizen == "yes" ]]; then
    echo "you can vote"
else
    echo "you are not old enough/citizen to vote"
fi

# discount calculator:

read -p "Enter purchase amount here: " amount

if [[ $amount -ge 5000 ]]; then
    echo "discount applied is 20%"
    bill=$(( amount - (amount * 20 / 100) ))
    echo "your bill is $bill"
elif [[ $amount -ge 2000 ]]; then
    bill=$(( amount - (amount * 10 / 100 )))
    echo "discount applied is 10%"
    echo "your bill is $bill"
else
    echo "no discount applied"
fi

# check the memory used by a system

disk_usage=$(df -h)
usage=$(echo $disk_usage | grep ' \/$')
number=$(echo $usage | awk '{print $8}')
limit=$(echo $number | sed 's/%//g')
if [[ $limit -ge 80 ]]; then
    echo "we dont have much room left"
else
    echo "we are fine"
fi
