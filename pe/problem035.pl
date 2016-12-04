#!/usr/bin/perl

use strict;
use warnings;

#The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
#
#There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
#How many circular primes are there below one million?

sub rotate {
  my $tmp = $_[0];
  $tmp =~ s/(.)(.*)/$2$1/g;
  return $tmp;
}

my $working = 3;
my @primea = (3);
my %primeh = ( 2=>1, 3=>1 );
my $limit = 1000000;

CANDIDATE: while ( $working <= $limit ) {
  $working += 2;
  my $i;
  for ( $i = 0; $primea[$i] <= sqrt $working ; $i++ ) {
    next CANDIDATE if ( $working % $primea[$i] == 0 );
  }
  push ( @primea, $working );
  $primeh{ $working }++;
}
unshift ( @primea, 2 );

my %circular = ( 2 => 1, 5 => 1 );

foreach my $root ( @primea ) {
  next if $root =~ /[024568]/;
  my $shifting = $root;
  my $isprime = 1;
  for ( my $j = 1; $j < length $root; $j++ ) {
    $shifting = rotate $shifting;
    $isprime &= defined( $primeh{ $shifting } );
  }
  if ( $isprime ) {
    for ( my $j = 0; $j < length $root; $j++ ) {
      $shifting = rotate $shifting;
      $circular{ $shifting } = 1;
    }
  }
}

printf "%d\n", scalar keys %circular;
