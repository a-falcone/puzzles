#!/usr/bin/perl

use strict;
use warnings;

#A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
#A number whose proper divisors are less than the number is called deficient and a number whose proper divisors exceed the number is called abundant.
#
#As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
#
#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

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

my %found;
my %abundant;

for ( my $j = 1; $j <= 28123; $j++ ) {
  my $sum = &sumfactors( $j );
  if ( $sum > $j ) {
    $abundant{$j}++;
    foreach ( keys %abundant ) {
        $found{ $_ + $j }++;
    }
  }
}

my $answer = 0;

for ( my $j = 1; $j <= 28123; $j++ ) {
  $answer += $j unless defined $found{ $j };
} 
print "$answer\n";
