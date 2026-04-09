#!/bin/bash

# for loop
fruits=("apples" "orange" "banana" "lemon" "kiwi")

for fruit in ${fruits[@]}; do
    echo "i like $fruit"
done

for (( i=1;i<5;i=i+1 )); do
    echo $i
done

# functions
deposit() {
read -p "Enter the amount: " amount
((balance=balance+amount))
clear
echo "amount deposited was $amount and new balance is $balance"
}
withdrawl() {
read -p "Enter the amount: " amount
((balance=balance-amount))
clear
echo "amount deposited was $amount and new balance is $balance"
}
exit() {
    echo "exiting the program"
    break
}

# case loops
balance=1000
while true; do
echo "press 1 for deposit"
echo "press 2 for withdrawl"
echo "press 3 for exit"

read -p "please enter your choice in number: " choice

case $choice in
1) 
deposit $1;;
2)
withdrawl $1;;
3)
exit;;
esac
done
