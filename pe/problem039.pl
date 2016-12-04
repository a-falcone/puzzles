#!/usr/bin/perl

use strict;
use warnings;

#If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
#
#{20,48,52}, {24,45,51}, {30,40,50}
#
#For which value of p 1000, is the number of solutions maximised?

my ($m, $n) = (2, 1);
my %seen;
my %count;
my ( $max, $maxcount ) = ( 0, 0 );

while ( $m < 100 ) {
  for ( $n = 1; $n < $m; $n++ ) {
    my $mult = 1;
    my ($a, $b, $c) = ($m ** 2 - $n ** 2, 2 * $m * $n, $m ** 2 + $n ** 2);
    while ( $mult * ( $a + $b + $c ) <= 1000 ) {
      my $tmp = join ':', sort ( $mult * $a, $mult * $b, $mult * $c );  
      if ( !defined $seen{ $tmp } ) {
        $seen{ $tmp }++;
        $count{ $mult * ( $a + $b + $c ) }++;
        if ( $count{ $mult * ( $a + $b + $c ) } > $maxcount ) {
          $max = $mult * ( $a + $b + $c );
          $maxcount = $count{ $mult * ( $a + $b + $c ) };
        }
      }
      $mult++;
    }
  }
  $m++;
}

print "$max\n";
