#!/usr/bin/perl

use strict;
use warnings;

#Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.
#
#       4
#        \
#         3
#        / \
#       1---2--6
#      /
#     5
#
#Working clockwise, and starting from the group of three with the numerically lowest external node (4,3,2 in this example), each solution can be described uniquely. For example, the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.
#
#It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.
#
#Total   Solution Set
#9   4,2,3; 5,3,1; 6,1,2
#9   4,3,2; 6,2,1; 5,1,3
#10  2,3,5; 4,5,1; 6,1,3
#10  2,5,3; 6,3,1; 4,1,5
#11  1,4,6; 3,6,2; 5,2,4
#11  1,6,4; 5,4,2; 3,2,6
#12  1,5,6; 2,6,4; 3,4,5
#12  1,6,5; 3,5,4; 2,4,6
#By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.
#
#Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings. What is the maximum 16-digit string for a "magic" 5-gon ring?
#
# Positions:
#        0
#         \
#          1
#         / \   3
#        /   \ /
#       8     2
#      /|    /
#     9 6---4--5
#       |
#       7 
#

{
    my @o;
    sub new {
        @o = (0) x shift; 
    }
    
    sub inc {
        return unless @o;
        my $index = 0;
        while ( $index < @o ) {
            if ( $o[$index] == @o - $index - 1 ) {
                $o[$index++] = 0;
            } else {
                $o[$index]++;
                last;
            }
        }
        @o = () if $index == @o;
        return @o;
    }
    
    sub permute {
        return () unless @o;
        my @set = @_;
        my @new;
        for (@o) {
            push @new, splice( @set, $_, 1 );
        }
        inc;
        return @new;
    }
    
    sub print_it {
        print "@o\n";
    }
}

sub min {
    my $min = shift;
    while ( defined( my $new = shift ) ) {
        $new =~ s/^1(.*)/9$1/;
        $min = $min lt $new ? $min : $new;
    }
    return $min;
}

my $largest = 0;

new( 10 );
my @thing = (1..10);
while ( my @a = permute( @thing ) ) {
    next if (10 == $a[0] || 10 == $a[1] || 10 == $a[2] || 10 == $a[4] || 10 == $a[6] || 10 == $a[8]);
    if ( $a[0] + $a[1] == $a[3] + $a[4] ) {
        if ( $a[3] + $a[2] == $a[5] + $a[6] ) {
            if ( $a[5] + $a[4] == $a[7] + $a[8] ) {
                if ( $a[7] + $a[6] == $a[9] + $a[1] ) {
                    my $s1 = join '', @a[0, 1, 2, 3, 2, 4, 5, 4, 6, 7, 6, 8, 9, 8, 1];
                    my $s2 = join '', @a[3, 2, 4, 5, 4, 6, 7, 6, 8, 9, 8, 1, 0, 1, 2];
                    my $s3 = join '', @a[5, 4, 6, 7, 6, 8, 9, 8, 1, 0, 1, 2, 3, 2, 4];
                    my $s4 = join '', @a[7, 6, 8, 9, 8, 1, 0, 1, 2, 3, 2, 4, 5, 4, 6];
                    my $s5 = join '', @a[9, 8, 1, 0, 1, 2, 3, 2, 4, 5, 4, 6, 7, 6, 8];
                    my $s = min( $s1, $s2, $s3, $s4, $s5 );
                    $largest = $s gt $largest ? $s : $largest;
                }
            }
        }
    }
}

print "$largest\n";
