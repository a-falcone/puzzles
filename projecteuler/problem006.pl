#!/usr/bin/perl

use strict;
use warnings;

#The sum of the squares of the first ten natural numbers is,
#1² + 2² + ... + 10² = 385
#
#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)² = 55² = 3025
#
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 385 = 2640.
#
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

my $sumofsq = 0;
my $sqofsum = 0;
my $i;

for ( $i = 1 ; $i <= 100 ; $i++ ) {
  $sumofsq += $i**2;
  $sqofsum += $i;
}

$sqofsum = $sqofsum**2;

print abs( $sumofsq - $sqofsum );
