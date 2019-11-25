# Read from the file file.txt and output the tenth line to stdout.
line=$(cat file.txt | wc -l)
if [ "$line" -ge 10 ]; then
  cat file.txt | head -n 10 | tail -n 1 
fi

