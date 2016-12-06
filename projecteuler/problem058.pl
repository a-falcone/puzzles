#!/usr/bin/perl

use strict;
use warnings;

#Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.
#
#37 36 35 34 33 32 31
#38 17 16 15 14 13 30
#39 18  5  4  3 12 29
#40 19  6  1  2 11 28
#41 20  7  8  9 10 27
#42 21 22 23 24 25 26
#43 44 45 46 47 48 49
#
#It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ~ 62%.
#
#If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?

#tools

sub is_prime {
  return 1 if $_[0] == 2;
  return 1 if $_[0] == 3;
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

#main

my $answer = 1;
my $primes = 0;

while ( 1 ) {
  $answer += 2;
  $primes++ if is_prime( $answer ** 2 - $answer + 1 );
  $primes++ if is_prime( $answer ** 2 - 2 * $answer + 2 );
  $primes++ if is_prime( $answer ** 2 - 3 * $answer + 3 );
  last if $primes / ( 2 * $answer - 1 ) < 0.1;
}

print "\n$answer\n";
