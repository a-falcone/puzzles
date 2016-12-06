#!/usr/bin/perl

use strict;
use warnings;

#It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
#
#9 = 7 + 2*1^2
#15 = 7 + 2*2^2
#21 = 3 + 2*3^2
#25 = 7 + 2*3^2
#27 = 19 + 2*2^2
#33 = 31 + 2*1^2
#
#It turns out that the conjecture was false.
#
#What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

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

my $answer = 7;

CANDIDATE: while ( 1 ) {
  $answer += 2;
  next CANDIDATE if is_prime $answer;
  my $i = 1;
  while ( 2 * $i * $i < $answer ) {
    next CANDIDATE if is_prime( $answer - 2 * $i * $i );
    $i++;
  }
  last CANDIDATE;
}

print "$answer\n";
