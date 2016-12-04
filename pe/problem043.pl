#!/usr/bin/perl

use strict;
use warnings;

#The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.
#
#Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
#
#  * d2d3d4=406 is divisible by 2
#  * d3d4d5=063 is divisible by 3
#  * d4d5d6=635 is divisible by 5
#  * d5d6d7=357 is divisible by 7
#  * d6d7d8=572 is divisible by 11
#  * d7d8d9=728 is divisible by 13
#  * d8d9d10=289 is divisible by 17
#
#Find the sum of all 0 to 9 pandigital numbers with this property.

my $answer = 0;
my $tmp;

for ( my $d8 = 17; $d8 < 999; $d8 += 17 ) {
  next if $d8 =~ /(.).*\1/;
  $d8 = "0"."$d8" if $d8 < 100;
  for ( my $d7 = 0; $d7 < 10; $d7++ ) {
    $tmp = "$d7$d8";
    next if $tmp =~ /(.).*\1/;
    $tmp =~ s/^0|.$//g;
    next if $tmp % 13 != 0;
    foreach my $d6 ( 0, 5 ) {
      $tmp = "$d6$d7$d8";
      next if $tmp =~ /(.).*\1/;
      $tmp =~ s/^0|..$//g;
      next if $tmp % 11 != 0;
      for ( my $d5 = 0; $d5 < 10; $d5++ ) {
        next if "$d5$d6$d7$d8" =~ /(.).*\1/;
        $tmp = "$d5$d6$d7";
        $tmp =~ s/^0|//;
        next if $tmp % 7 != 0;
        foreach my $d4 ( 0, 2, 4, 6, 8 ) {
          next if "$d4$d5$d6$d7$d8" =~ /(.).*\1/;
          for ( my $d3 = 0; $d3 < 10; $d3++ ) {
            next if "$d3$d4$d5$d6$d7$d8" =~ /(.).*\1/;
            $tmp = "$d3$d4$d5";
            $tmp =~ s/^0//g;
            next if $tmp % 3 != 0;
            for ( my $d2 = 0; $d2 < 10; $d2++ ) {
              next if "$d2$d3$d4$d5$d6$d7$d8" =~ /(.).*\1/;
              for ( my $d1 = 0; $d1 < 10; $d1++ ) {
                next if "$d1$d2$d3$d4$d5$d6$d7$d8" =~ /(.).*\1/;
                my $tmp = "$d1$d2$d3$d4$d5$d6$d7$d8";
                $tmp =~ s/^0//g;
                $answer += "$tmp";
              }
            }
          }
        }
      }
    }
  }
}

print "$answer\n";
