#!/usr/bin/perl

use strict;
use warnings;

#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
#Find the sum of all the primes below two million.

my @primes = (3);
my $working = 5;
my $sum = 5;
my $limit = shift || 2000000;

while ( $working <= $limit ) {
  my $i;
  my $composite = 0;
  for ( $i = 0; ( $primes[$i] <= sqrt $working ) && !$composite ; $i++ ) {
    $composite = 1 if ( $working % $primes[$i] == 0 );
  }
  if (!$composite) {
    push ( @primes, $working );
    $sum += $working;
  }
  $working += 2;
}

print "\n$sum\n";
