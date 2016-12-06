#!/usr/bin/perl

use strict;
use warnings;

#A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.
#
#For example,
#
#44 → 32 → 13 → 10 → 1 → 1
#85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89
#
#Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.
#
#How many starting numbers below ten million will arrive at 89?

sub sss {
    my $thing = shift;
    my $sum = 0;
    while ($thing) {
        my $t = $thing % 10;
        $sum += $t * $t;
        $thing = int($thing / 10);
    }
    return $sum;
}

my @a;
$a[1] = 1;
$a[89] = 89;
my $total = 0;
my $limit = shift || 10_000_000;

for ( my $i = 2; $i < $limit; $i++ ) {
    my $c = $i;
    while ( !$a[$c] ) {
        $c = sss $c;
    }
    $a[$i] = $a[$c];
    $total++ if $a[$i] == 89;
}

print "$total\n";

