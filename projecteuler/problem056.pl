#!/usr/bin/perl

use strict;
use warnings;
use bigint;

#A googol (10 ** 100) is a massive number: one followed by one-hundred zeros; 100 ** 100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.
#
#Considering natural numbers of the form, a ** b, where a, b < 100, what is the maximum digital sum?

#tools
sub sum_digits {
  my $sum = 0;
  map( $sum += ord( $_ ) - ord( '0' ), split( //, $_[0] ) );
  return $sum;
}

#main

my $answer = 0;

for ( my $a = 2; $a < 100; $a++ ) {
  for ( my $b = 2; $b < 100; $b++ ) {
    my $sum = sum_digits( $a ** $b );
    $answer = $sum if $sum > $answer;
  }
}

print "$answer\n";
