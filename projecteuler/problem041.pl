#!/usr/bin/perl

use strict;
use warnings;

#We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
#
#What is the largest n-digit pandigital prime that exists?

sub is_prime {
  return 0 if $_[0] % 2 == 0;
  return 0 if $_[0] % 3 == 0;
  my $limit = sqrt $_[0];
  for ( my $i = 5; $i < $limit; $i += 2 ) {
    return 0 if $_[0] % $i == 0;
    $i += 2;
    return 0 if $_[0] % $i == 0;
    $i += 2;
  }
  return 1;
}

my $possible = 7654323;
while ( $possible > 1234567 ) {
  $possible -= 2;
  next if $possible =~ /(.).*\1|0|9|8/;
  last if is_prime $possible;
}
print "$possible\n";
