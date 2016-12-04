#!/usr/bin/perl

use strict;
use warnings;

#A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
#a^2 + b^2 = c^2
#
#For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

my ($m, $n) = (2, 1);

while ( $m < 100 ) {
  for ( $n = 1; $n < $m; $n++ ) {
    my $mult = 1;
    my ($a, $b, $c) = ($m ** 2 - $n ** 2, 2 * $m * $n, $m ** 2 + $n ** 2);
    while ( $mult * ( $a + $b + $c ) <= 1000 ) {
      if ( $mult * ( $a + $b + $c ) == 1000 ) {
        print $mult **3 * $a * $b * $c."\n";
        exit;
      }
      $mult++;
    }
  }
  $m++;
}

print "Triple not found\n";
print "\n";
