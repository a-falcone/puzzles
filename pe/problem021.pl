#!/usr/bin/perl

use strict;
use warnings;

#Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
#If d(a) = b and d(b) = a, where a b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#
#For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
#Evaluate the sum of all the amicable numbers under 10000.

sub sumfactors {
  return 0 if $_[0] == 1;
  my $sum = 0;
  my $i;
  for ( $i = 1; $i <= sqrt $_[0] ; $i++ ) {
    $sum += ( $i + $_[0] / $i ) if $_[0] % $i == 0;
    $sum -= $i if $i == sqrt $_[0];
  }
  return $sum - $_[0];
}

my $answer = 0;
my @sums = ( 0, 0 );

for ( my $j = 2; $j < 10000; $j++ ) {
  next if defined( $sums[ $j ] );
  $sums[ $j ] = &sumfactors( $j );
  next if $sums[ $j ] == $j || defined $sums[ $sums[ $j ] ];
  $sums[ $sums[ $j ] ] = &sumfactors( $sums[ $j ] );
  if ( $sums[ $sums[ $j ] ] == $j ) {
    $answer += $j + $sums[ $j ];
  }

}

print "$answer\n";
