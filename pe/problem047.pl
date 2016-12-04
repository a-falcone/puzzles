#!/usr/bin/perl

use strict;
use warnings;

#The first two consecutive numbers to have two distinct prime factors are:
#
#14 = 2*7
#15 = 3*5
#
#The first three consecutive numbers to have three distinct prime factors are:
#
#644 = 2²*7*23
#645 = 3*5*43
#646 = 2*17*19.
#
#Find the first four consecutive integers to have four distinct primes factors. What is the first of these numbers?

sub distinct_factors {
  my $tmp = $_[0];
  my $count = 0;
  my $max = 1;
  $count = 1 if $tmp % 2 == 0;
  while ( $tmp % 2 == 0) {
    $tmp /= 2;
  }
  for ( my $i = 3; $i <= sqrt($tmp); $i+=2) {
    if ( $tmp % $i == 0 ) {
      $tmp /= $i;
      $count++;
      while ( $tmp % $i == 0) {
        $tmp /= $i;
      }
    }
  }
  return $tmp == 1 ? $count : $count + 1;
}

my ( $count, $answer ) = ( 0, 1 );

while ( $count < 4 ) {
  $answer++;
  $count = distinct_factors( $answer ) >= 4 ? $count + 1 : 0;
}

printf "%d\n", $answer - 3;
