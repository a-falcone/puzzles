#!/usr/bin/perl

use strict;
use warnings;

#The prime 41, can be written as the sum of six consecutive primes:
#41 = 2 + 3 + 5 + 7 + 11 + 13
#
#This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#
#The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
#
#Which prime, below one-million, can be written as the sum of the most consecutive primes?

my $working = 3;
my %primeh;
$primeh{ 2 } = 1;
my @primea = (3);
my $limit = 1000000;

CANDIDATE: while ( $working < $limit ) {
  $working += 2;
  my $i;
  for ( $i = 0; $primea[$i] <= sqrt $working ; $i++ ) {
    next CANDIDATE if ( $working % $primea[$i] == 0 );
  }
  push ( @primea, $working );
  $primeh{ $working } = 1;
}
unshift ( @primea, 2 );

#main
my ( $start, $index, $maxcount ) = ( 0, 0, 1 );
my $upper = $limit / $maxcount;

while ( $primea[ $start ] < $upper ) {
  my $count = 1;
  my $sum = $primea[ $start ];
  while ( $sum < $limit ) {
    $sum += $primea[ $start + $count ];
    if ( defined $primeh{ $sum } && $count > $maxcount ) {
      print "SUM: $sum -- COUNT: $count\n";
      $maxcount = $count;
    }
    $count++;
  }
  $start++;
  $upper = $limit / $maxcount;
}
