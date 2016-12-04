#!/usr/bin/perl

use warnings;
use strict;

#Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
#The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.
#
#Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.
#
#Find the value of n, 1 < n < 10^7, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.

my $limit = shift || 10**7;

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
my $quotient = 2 / phi( 2 );
for ( my $i = 2; $i < $limit; $i++ ) {
    my $phi = phi($i);
    if ( sorted($i) eq sorted($phi) ) {
        if ( $i / $phi < $quotient ) {
            print "new answer is $i (phi = $phi)\n"; 
            $answer = $i;
            $quotient = $i / $phi;
        }
    }
}

print "$answer\n";
