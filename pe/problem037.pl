#!/usr/bin/perl

use strict;
use warnings;

#The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
#
#Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
#
#NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

my $answer = 0;
my $found = 0;
my $working = 9;
my @primea = ( 3, 5, 7 );
my %primeh = ( 2=>1, 3=>1, 5=>1, 7=>1 );

CANDIDATE: while ( $found < 11 ) {
  $working += 2;
  my $i;
  for ( $i = 0; $primea[$i] <= sqrt $working ; $i++ ) {
    next CANDIDATE if ( $working % $primea[$i] == 0 );
  }
  push ( @primea, $working );
  $primeh{ $working }++;
  if ( prime_left( $working ) && prime_right( $working ) ) {
    $answer += $working;
    $found++;
  }
}

print "$answer\n";

sub prime_left {
  my $tmp = $_[0];
  return 1 if length $tmp == 1 && defined( $primeh{ $_[0] } );
  $tmp =~ s/^(.*).$/$1/;
  return defined( $primeh{ $_[0] } ) && prime_left( $tmp );
}

sub prime_right {
  my $tmp = $_[0];
  return 1 if length $tmp == 1 && defined( $primeh{ $_[0] } );
  $tmp =~ s/^.(.*)$/$1/;
  return defined( $primeh{ $_[0] } ) && prime_right( $tmp );
}

