#!/usr/bin/perl

use strict;
use warnings;

#There are exactly ten ways of selecting three from five, 12345:
#123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
#
#In combinatorics, we use the notation, 5C3 = 10.
#
#In general, nCr = n!/(r!(nr)!) ,where r n, n! = n * (n - 1) * ... * 3 * 2 * 1, and 0! = 1.
#
#It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.
#
#How many, not necessarily distinct, values of  nCr, for 1 <= n <= 100, are greater than one-million?

#tools

sub fact {
  return perm( $_[0], $_[0] );
}

sub perm {
  my $ans = 1;
  for ( my $n = $_[0]; $n > ( $_[0] - $_[1] ); $n-- ) {
    $ans *= $n;
  }
  return $ans;
}

sub combo {
  return perm( $_[0], $_[1] ) / fact( $_[1] );
}

#main

my $answer = 0;

for ( my $i = 1; $i <= 100; $i++ ) {
  for ( my $j = 1; $j < $i; $j++ ) {
    $answer++ if combo( $i, $j ) > 1000000;
  }
}

print "$answer\n";
