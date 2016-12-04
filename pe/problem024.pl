#!/usr/bin/perl

use strict;
use warnings;

#A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
#
#012   021   102   120   201   210
#
#What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

sub fact {
  return 1 if $_[0] == 0;
  return $_[0] * fact( $_[0] - 1 );
}

my $num = 999999;
my @digits = ( 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 );

for ( my $i = 9; $i > 0; $i-- ) { #output is the zero indexed place of the remaining numbers
  print splice @digits, int ( $num / fact( $i ) ) , 1;
  $num %= fact( $i );
}

print $digits[0]."\n";
