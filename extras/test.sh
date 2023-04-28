first_line=$(head -n 1 FileHistory.txt)
echo "$first_line"
second_line=$(head -n 2 FileHistory.txt | tail -n 1)
echo "$second_line"