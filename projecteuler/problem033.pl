#!/usr/bin/perl

use strict;
use warnings;

#The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
#
#We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
#There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
#
#If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

for my $u1 ( 1 .. 9 ) {
  for my $u2 ( 1 .. 9 ) {
    for my $t1 ( 1 .. 9 ) {
      print "$t1$u1 / $u1$u2\n" if ( 10 * $t1 * $u1 + $t1 * $u2 == 10 * $t1 * $u2 + $u1 * $u2 && $u1 != $u2 );
    }
  }
}
