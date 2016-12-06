#!/usr/bin/perl

use strict;
use warnings;
use bigint;

#The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.
#
#Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

my $answer = 0;
#for ( my $i = 1; $i < 1000; $i++ ) {
for my $i ( 1 .. 999 ) {
  print "$i: $answer\n";
  $answer += $i ** $i;
}

$answer %= 10 ** 10;

print "$answer\n";
