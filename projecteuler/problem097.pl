#!/usr/bin/perl

use warnings;
use strict;

#The first known prime found to exceed one million digits was discovered in 1999, and is a Mersenne prime of the form 2^6972593-1; it contains exactly 2,098,960 digits. Subsequently other Mersenne primes, of the form 2^p-1, have been found which contain more digits.
#
#However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433*2^7830457+1.
#
#Find the last ten digits of this prime number.

use bigint;

my $t = 1;
my $e = 7830457;
my @e;

while ($e) {
    if ( $e % 2 ) {
        $e--;
        push @e, 0;
    } else {
        $e /= 2;
        push @e, 1;
    }
}

while (@e) {
    my $pow = pop @e;
    if ( $pow ) {
        $t **= 2;
    } else {
        $t *= 2;
    }
    $t %= 10_000_000_000;
}
$t = 28433 * $t + 1;

$t %= 10_000_000_000;

print "$t\n";
