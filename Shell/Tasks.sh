#!/bin/bash

#Task - 1
# ping multiple servers and checking if they are up or down
servers=(192.168.1.16 192.168.1.20 "google.com")
for server in "${servers[@]}"; do
    ping -c 1 -W 1 $server &>/dev/null
    if [[ $? -eq 0 ]]; then
        echo "$server is up"
    else
        echo "$server is down"
    fi
done

# Task -2
# Calculate percentage of partition used by a specific directory
#!/bin/bash
dirs=("/home" "/var" "/tmp" "/tmp")
for dir in "${dirs[@]}"; do
    output=$(sudo du -sb "$dir" | awk -v total=$(df -B1 "$dir" | tail -1 | awk '{print $2}') '{printf "%.2f%%\n", ($1/total)*100}')
    echo "$dir --> $output used"
done 

# Task -3
# Add "Mr." Prefix to Names
#!/bin/bash
names=("John" "Tom" "David")
for name in "${names[@]}"; do
    echo "Mr.$name" >> new_names.txt
done

# Task -4
# Countdown Timer
#!/bin/bash
read -p "Enter a number: " n
while (( n >= 0 )); do
    if (( n != 0 ));then
        echo $n
        sleep 1
        (( n-- ))
    else
        echo "Time's up"
        break
    fi
done

# Task -5
# do a while loop to check the RAM usage every 5 seconds and print a message if it exceeds 40.5%
#!/bin/bash
while true; do
ram=$(free | awk '/Mem:/ {printf("%.2f"), $3/$2 * 100}')
if [ "$(echo "$ram <= 40.5" | bc -l)" -eq 1 ]; then
    echo "RAM usage is safe: $ram"
else
    echo "High RAM usage: $ram"
fi
sleep 5
done
