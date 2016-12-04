#!/usr/bin/perl

use strict;
use warnings;

#Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.
#
#If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:
#
#1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
#
#It can be seen that there are 21 elements in this set.
#
#How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?


my $limit = shift || 1e6;

my @primes = (2, 3);
my $candidate = 3;

CANDIDATE:
while ( $candidate + 2 < sqrt $limit ) {
    $candidate += 2;
    my $found = 0;
    for (my $i = 0; $primes[$i] <= sqrt( $candidate ) && !$found; $i++) {
        if ( $candidate % $primes[$i] == 0 ) {
            next CANDIDATE;
        }
    }
    push @primes, $candidate;
}

sub phi {
    my $t = shift;
    my $phi = $t;
    my $i = 0;
    for ( my $i = 0; $i < @primes && $primes[$i] <= sqrt $t; $i++ ) {
        if ( $t % $primes[$i] == 0 ) {
            $phi = $phi / $primes[$i] * ( $primes[$i] - 1 );
            $t /= $primes[$i] while ( $t % $primes[$i] == 0 );
        }
    }
    if ( $t > 1 ) {
        $phi = $phi / $t * ( $t - 1 );
    }

    return $phi;
}

sub sorted {
    return join "", sort split //, shift;
}

my $answer = 0;
for ( my $i = 2; $i <= $limit; $i++ ) {
    $answer += phi($i);
}

print "$answer\n";
