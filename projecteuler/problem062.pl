#!/usr/bin/perl

use strict;
use warnings;

#The cube, 41063625 (345^(3)), can be permuted to produce two other cubes: 56623104 (384^(3)) and 66430125 (405^(3)). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.
#
#Find the smallest cube for which exactly five permutations of its digits are cube.

my $exponent = 3;
my $break = 13;
my $i = 0;
my $curlen = length( $i ** $exponent );
my $lastlen = $curlen;
my %sorted;

while ( $break > $curlen ) {
  $curlen = length( $i ** $exponent );
  if ( $curlen > $lastlen ) {
#    compSorted;
    $lastlen = $curlen;
  }

  my $s = join( "", sort( split( //, $i ** $exponent ) ) );
  $sorted{ $s }++;
  printf "%s\n", $i ** $exponent if ( $s == "012334566789" );
  printf "%s\n", $i ** $exponent if ( $s == "012334556789" );

  $i++;
}
