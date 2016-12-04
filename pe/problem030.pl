#!/usr/bin/perl

use strict;
use warnings;

#Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#
#  1634 = 1^4 + 6^4 + 3^4 + 4^4
#  8208 = 8^4 + 2^4 + 0^4 + 8^4
#  9474 = 9^4 + 4^4 + 7^4 + 4^4
#
#  As 1 = 14 is not a sum it is not included.
#
#  The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
#  Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

my $answer = 0;

for ( my $i = 10; $i < 5 * 9**5; $i++ ) {
  my $sum = 0;
  foreach ( split //, $i ) {
    $sum += $_**5;
  }
  $answer += $i if $i == $sum;
}

print "$answer\n";
