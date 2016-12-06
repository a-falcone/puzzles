#!/usr/bin/perl

use strict;
use warnings;

#Starting in the top left corner of a 2 x 2 grid, there are 6 routes (without backtracking) to the bottom right corner.
#
#How many routes are there through a 20 x 20 grid?

#to get from the top left to the bottom right, you must go right 20 times and down 20 times in any order. This is just 40 choose 20

sub fact {
  return 1 unless $_[0];
  my $f = 1;
  $f *= $_ for (2..shift);
  return $f;
}

my $answer = fact( 40 ) / ( fact( 20 ) ** 2 );

print "$answer\n";
