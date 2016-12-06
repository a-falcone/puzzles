#!/usr/bin/perl

use warnings;
use strict;

#The points P (x1, y1) and Q (x2, y2) are plotted at integer co-ordinates and are joined to the origin, O(0,0), to form ΔOPQ.
#
#There are exactly fourteen triangles containing a right angle that can be formed when each co-ordinate lies between 0 and 2 inclusive; that is,
#0 ≤ x1, y1, x2, y2 ≤ 2.
#
#Given that 0 ≤ x1, y1, x2, y2 ≤ 50, how many right triangles can be formed?

sub dotprod {
    my ($x11, $y11, $x12, $y12, $x21, $y21, $x22, $y22) = @_;
    return ($x12 - $x11) * ($x22 - $x21) + ($y12 - $y11) * ($y22 - $y21);
}

my $answer = 0;

my $xlimit = shift || 50;
my $ylimit = shift || 50;

my %seen = ( 0, 0 );

for (my $x1 = 0; $x1 <= $xlimit; $x1++ ) {
    for (my $y1 = 0; $y1 <= $ylimit; $y1++ ) {
        next unless $x1 * $y1;
        $seen{"$x1,$y1"}++;
        for (my $x2 = 0; $x2 <= $xlimit; $x2++ ) {
            for (my $y2 = 0; $y2 <= $ylimit; $y2++ ) {
                next if $seen{"$x2,$y2"};
                $answer++ unless dotprod( 0, 0, $x1, $y1, 0, 0, $x2, $y2 ) *
                                 dotprod( $x1, $y1, $x2, $y2, 0, 0, $x2, $y2 ) *
                                 dotprod( 0, 0, $x1, $y1, $x1, $y1, $x2, $y2 );
            }
        }
    }
}

print "$answer\n";
