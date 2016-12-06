#!/usr/bin/perl

use strict;
use warnings;

#145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
#Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
#Note: as 1! = 1 and 2! = 2 are not sums they are not included.

sub fact {
  return 1 if $_[0] == 0;
  return $_[0] * fact( $_[0] - 1 );
}

my $answer = 0;
my $limit = fact( 9 ) + 10;

for ( my $i = 3; $i < $limit; $i++ ) {
  my $sum = 0;
  foreach ( split //, $i ) {
    $sum += fact( $_ );
  }
  $answer += $i if $sum == $i;
}

print "$answer\n";
