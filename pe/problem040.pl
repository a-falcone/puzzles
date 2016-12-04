#!/usr/bin/perl

use strict;
use warnings;

#An irrational decimal fraction is created by concatenating the positive integers:
#
#0.123456789101112131415161718192021...
#             ^
#
#It can be seen that the 12th digit of the fractional part is 1.
#
#If dn represents the nth digit of the fractional part, find the value of the following expression.
#
#d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000

my $answer = 1;
my @indices = ( 1, 10, 100, 1000, 10000, 100000, 1000000 );
my $position = 0;
my $i = 1;

foreach my $next_i ( @indices ) {
  while ( $next_i > $position + length $i ) {
    $position += length $i;
    $i++;
  }
  $answer *= substr( $i, ( $next_i - $position - 1 ), 1 );
  $position += length $i;
  $i++;
}

print "$answer\n";
