#!/usr/bin/perl

use strict;
use warnings;
use bigint;

#2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
#What is the sum of the digits of the number 2^1000?

my @a = split //, 2 ** 1000;
my $answer = 0;
for (@a) {
  $answer += $_;
}

print "$answer\n";
