#!/usr/bin/perl

use strict;
use warnings;

#--- Day 2: Corruption Checksum ---
#
#As you walk through the door, a glowing humanoid shape yells in your direction. "You there! Your state appears to be idle. Come help us repair the corruption in this spreadsheet - if we take another millisecond, we'll have to display an hourglass cursor!"
#
#The spreadsheet consists of rows of apparently-random numbers. To make sure the recovery process is on the right track, they need you to calculate the spreadsheet's checksum. For each row, determine the difference between the largest value and the smallest value; the checksum is the sum of all of these differences.
#
#For example, given the following spreadsheet:
#
#5 1 9 5
#7 5 3
#2 4 6 8
#The first row's largest and smallest values are 9 and 1, and their difference is 8.
#The second row's largest and smallest values are 7 and 3, and their difference is 4.
#The third row's difference is 6.
#In this example, the spreadsheet's checksum would be 8 + 4 + 6 = 18.
#
#What is the checksum for the spreadsheet in your puzzle input?
#
#--- Part Two ---
#
#"Great work; looks like we're on the right track after all. Here's a star for your effort." However, the program seems a little worried. Can programs be worried?
#
#"Based on what we're seeing, it looks like all the User wanted is some information about the evenly divisible values in the spreadsheet. Unfortunately, none of us are equipped for that kind of calculation - most of us specialize in bitwise operations."
#
#It sounds like the goal is to find the only two numbers in each row where one evenly divides the other - that is, where the result of the division operation is a whole number. They would like you to find those numbers on each line, divide them, and add up each line's result.
#
#For example, given the following spreadsheet:
#
#5 9 2 8
#9 4 7 3
#3 8 6 5
#In the first row, the only two numbers that evenly divide are 8 and 2; the result of this division is 4.
#In the second row, the two numbers are 9 and 3; the result is 3.
#In the third row, the result is 2.
#In this example, the sum of the results would be 4 + 3 + 2 = 9.
#
#What is the sum of each row's result in your puzzle input?

my $cs = 0;

LINE: while (my $line = <DATA>) {
  chomp $line;
  my @a = split( / +/, $line );
  for (my $x = 0; $x < @a; $x++) {
    for (my $y = $x + 1; $y < @a; $y++) {
      if (($a[$x] % $a[$y]) * ($a[$y] % $a[$x]) == 0) {
        $cs += int($a[$x] / $a[$y]) + int($a[$y] / $a[$x]);
        next LINE;
      }
    }
  }
}

print "$cs\n";

__DATA__
1640 590 93 958 73 1263 1405 1363 737 712 1501 390 68 1554 959 79
4209 128 131 2379 2568 2784 2133 145 3618 1274 3875 158 1506 3455 1621 3799
206 1951 2502 2697 2997 74 76 78 1534 81 2775 2059 3026 77 2600 3067
373 1661 94 102 2219 1967 1856 417 1594 75 100 2251 2200 1825 1291 1021
57 72 51 1101 1303 60 1227 421 970 1058 138 333 1320 1302 402 1210
4833 5427 179 3934 4533 5124 4832 2088 94 200 199 1114 4151 1795 208 3036
759 876 110 79 1656 1691 185 544 616 312 757 1712 92 97 1513 1683
1250 1186 284 107 1190 1233 573 1181 1041 655 132 547 395 146 119 515
505 1726 79 180 86 1941 1597 1785 1608 1692 968 1177 94 184 91 31
1366 2053 1820 1570 70 506 53 415 717 1263 82 366 74 1255 2020 1985
2365 5585 2285 4424 5560 3188 3764 187 88 223 1544 5023 4013 5236 214 196
1487 1305 1359 1615 6579 2623 4591 150 5030 188 146 4458 5724 5828 1960 221
3114 688 3110 334 1921 153 4083 131 2234 3556 3573 3764 127 919 3293 104
1008 78 1196 607 135 1409 296 475 915 157 1419 1304 153 423 163 704
235 4935 4249 3316 1202 221 1835 380 249 1108 1922 5607 4255 238 211 3973
1738 207 179 137 226 907 1468 1341 1582 1430 851 213 393 1727 1389 632
