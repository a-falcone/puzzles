#!/usr/bin/perl

use strict;
use warnings;

#The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
#
#There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
#
#What 12-digit number do you form by concatenating the three terms in this sequence?

my $working = 3;
my @primea = (3);
my $limit = 10000;
my %patterns;

CANDIDATE: while ( $working < $limit ) {
  $working += 2;
  for ( my $i = 0; $primea[$i] <= sqrt $working ; $i++ ) {
    next CANDIDATE if ( $working % $primea[$i] == 0 );
  }
  push ( @primea, $working );
  if ($working > 1000) {
    my $sorted = join "", sort split //, $working ;
    if ( defined $patterns{ $sorted } ) {
      push @{ $patterns{ $sorted } }, $working;
    } else {
      $patterns{ $sorted } = [ $working ];
    }
  }
}

FOUND: foreach ( sort keys %patterns ) {
  my @a = @{ $patterns{ $_ } };
  next if scalar @a < 3;
  my %possible;
  for ( my $i = 0; $i < scalar @a; $i++ ) {
    for ( my $j = $i + 1; $j < scalar @a; $j++ ) {
      if ( defined $possible{ $a[ $j ] } ) {
        printf "%d%d%d\n", $a[ $i ], ( $a[ $i ] + $a[ $j ] ) / 2, $a[ $j ];
        next FOUND;
      }
      $possible{ 2 * $a[$j] - $a[$i] } = 1;
    }
  }
}
