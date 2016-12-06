#!/usr/bin/perl

use strict;
use warnings;

#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91  99.
#
#Find the largest palindrome made from the product of two 3-digit numbers.

my $max = 0;
my $tmp;
my $i;
my $j;
for ( $i = 999; $i >= 101; $i-- ) {
  for ( $j = $i ; $j >=101; $j-- ) {
    $tmp = $i * $j;
    if ( $tmp == reverse $tmp ) {
      $max = $tmp > $max ? $tmp : $max;
#      print "$tmp = $i * $j\n";
    }
  }
}

print "Max is $max.\n";
