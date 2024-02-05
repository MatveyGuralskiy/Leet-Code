#!/bin/bash
#--------------LEET CODE---------------
#193. Valid Phone Numbers

#Solution of Matvey Guralskiy
#https://github.com/MatveyGuralskiy

grep -e ^[0-9]{3}-[0-9]{3}-[0-9]{4}$ -e ^([0-9]{3}) [0-9]{3}-[0-9]{4}$ file.txt