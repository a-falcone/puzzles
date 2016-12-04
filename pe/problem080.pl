#!/usr/bin/perl

use strict;
use warnings;
use Math::BigFloat;

#It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite without any repeating pattern at all.
#
#The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.
#
#For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.

my $limit = shift || 100;
my $sum = 0;
for my $base ( 2..$limit ) {
    next if ( sqrt $base == int sqrt $base );
    my ($a,$b) = split /\./, Math::BigFloat->new( $base )->bsqrt(105);
    $b = substr $b, 0, 100 - length $a;
    map { $sum += $_ } split //, "$a$b";
}

print "$sum\n";
