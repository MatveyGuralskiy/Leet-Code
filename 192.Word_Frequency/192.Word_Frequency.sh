#!/bin/bash
#--------------LEET CODE---------------
#192. Word Frequency

#Solution of Matvey Guralskiy
#https://github.com/MatveyGuralskiy

#-----------------------------------------------
#Write a bash script to calculate the 
#frequency
#of each word in a text file words.txt.

#For simplicity sake, you may assume:

#words.txt contains only lowercase characters and space ' ' characters.
#Each word must consist of lowercase characters only.
#Words are separated by one or more whitespace characters.
#xample:

#Assume that words.txt has the following content:

#the day is sunny the the
#the sunny is is
#Your script should output the following, sorted by descending frequency:

#the 4
#is 3
#sunny 2
#day 1
#Note:

#Don't worry about handling ties, it is guaranteed that each word's frequency count is unique.
#Could you write it in one-line using Unix pipes?
#----------------------------------------------

awk '{
    # NF- contains the number of fields (words) in the current line. 
    for (i=1; i<=NF; i++) {
        count[$i]++;
    }
}
END {
    for (word in count) {
        print word, count[word];
    }
}' words.txt | sort -k2,2nr