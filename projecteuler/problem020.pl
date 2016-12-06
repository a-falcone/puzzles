#!/usr/bin/perl

use strict;
use warnings;
use bigint;

#n! means n * (n + 1) *  ... * 3 * 2 * 1
#
#Find the sum of the digits in the number 100!

sub fact {
  return 1 if $_[0] == 0;
  return $_[0] * &fact( $_[0] - 1 );
}

my $answer = 0;

for ( split //, fact(100) ) {
  $answer += $_;
}

print "$answer\n";
