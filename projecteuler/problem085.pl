#!/usr/bin/perl

use warnings;
use strict;

#By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:
#
# xoo xxo xxx
# ooo ooo ooo
#  6   4   2
#
# xoo xxo xxx
# xoo xxo xxx
#  3   2   1
#
#Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.

sub calc_rectangles {
    my $sum = 0;
    for ( my $r = 1; $r <= $_[0]; $r++ ) {
        for ( my $c = 1; $c <= $_[1]; $c++ ) {
            $sum += $r * $c;
        }
    }
    return $sum;
}

my $closest = 0;
my $answer = "";
my $limit = shift || 2_000_000;

THING:
for ( my $br = 1; ; $br++ ) {
    for ( my $bc = 1; $bc <= $br; $bc++ ) {
        my $total = calc_rectangles $br, $bc;
        last THING if $total > 5 * $limit;
        if ( abs( $total - $limit ) < abs( $closest - $limit ) ) {
            $closest = $total;
            $answer = $bc * $br;
            next;
        }
    }
}

print "$answer\n";
