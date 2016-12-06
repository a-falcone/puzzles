#!/usr/bin/perl

use strict;
use warnings;

#The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. In fact, there are exactly four numbers below fifty that can be expressed in such a way:
#
#28 = 2^2 + 2^3 + 2^4
#33 = 3^2 + 2^3 + 2^4
#49 = 5^2 + 2^3 + 2^4
#47 = 2^2 + 3^3 + 2^4
#
#How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?

my $answer = 0;
my %seen;

my $limit = shift || 50_000_000;

my @prime = (my $working = 3);

CANDIDATE: while ( $working <= sqrt($limit) + 500 ) {
    $working += 2;
    for ( my $i = 0; $prime[$i] <= sqrt $working ; $i++ ) {
        next CANDIDATE if ( $working % $prime[$i] == 0 );
    }
    push ( @prime, $working );
}
unshift ( @prime, 2 );

for ( my $c = 0; $prime[$c] ** 4 < $limit; $c++ ) {
    my $c4 = $prime[$c] ** 4;
    for ( my $b = 0; $c4 + $prime[$b] ** 3 < $limit; $b++ ) {
        my $b3 = $prime[$b] ** 3;
        for ( my $a = 0; $c4 + $b3 + $prime[$a] ** 2 < $limit; $a++ ) {
            if ( !$seen{$c4 + $b3 + $prime[$a] ** 2}++ ) {
                $answer++;
#                print "$prime[$c] ** 4 + $prime[$b] ** 3 + $prime[$a] ** 2 = ", $c4 + $b3 + $prime[$a] ** 2, "\n";
            }
        }
    }
}

print "$answer\n";
