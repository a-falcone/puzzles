#!/usr/bin/perl

use warnings;
use strict;

#The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:
#
#1! + 4! + 5! = 1 + 24 + 120 = 145
#
#Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:
#
#169 → 363601 → 1454 → 169
#871 → 45361 → 871
#872 → 45362 → 872
#
#It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,
#
#69 → 363600 → 1454 → 169 → 363601 (→ 1454)
#78 → 45360 → 871 → 45361 (→ 871)
#540 → 145 (→ 145)
#
#Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.
#
#How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?

sub f {
    my $t = shift;
    my $f = 1;
    while($t) {
        $f *= $t--;
    }
    return $f;
}

sub fs {
    my $sum = 0;
    $sum += f($_) for split //, shift;
    return $sum;
}

my $limit = shift || 1e6;
my $answer = 0;
for ( my $i = 1; $i < $limit; $i++ ) {
    my %seen;
    my $counter = 0;
    my $t = $i;
    while ( !$seen{$t}++ ) {
        $counter++;
        $t = fs $t;
    }
    if ( 60 == $counter ) {
        $answer++;
    }
}
print "$answer\n";
