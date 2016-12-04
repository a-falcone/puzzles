#!/usr/bin/perl

use strict;
use warnings;

#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
#Find the sum of all the even-valued terms in the sequence which do not exceed four million.

my $sum = 0;
my $f1 = 1;
my $f2 = 1;

while ( $f1 < 4000000 ) {

  $sum += $f1 if ( $f1 % 2 == 0 );
  my $tmp = $f1;
  $f1 += $f2;
  $f2 = $tmp;

}

print "$sum\n";
