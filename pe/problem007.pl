#!/usr/bin/perl

use strict;
use warnings;

#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
#What is the 10001st prime number?

my @primes = (3);
my $working = $primes[-1];

my $limit = shift || 10000;

while ( scalar @primes < $limit ) {
  $working += 2;
  my $composite = 0;
  for ( my $i = 0; ( $primes[$i] <= sqrt $working) && !$composite ; $i++ ) {
    if ( $working % $primes[$i] == 0 ) {
        $composite = 1;
    }
  }
  push ( @primes, $working ) unless $composite;
}

print $primes[-1]."\n";
