#!/usr/bin/perl

use strict;
use warnings;

#Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.
#
#Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.
#
#We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.
#
#Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.
#
#Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.
#
#Find the least number for which the proportion of bouncy numbers is exactly 99%.

sub bouncy {
    my $num = shift;
    return 0 if $num < 100;
    my $last = chop $num;
    my $direction = 0;
    while ( $num ne "" ) {
        my $current = chop $num;
        my $diff = $last <=> $current;;
        if ( $direction && $diff ) {
            return 1 if $diff != $direction;
        } else {
            $direction ||= $diff;
        }
        $last = $current;
    }
    return 0;
}

#print bouncy(shift), "\n";
#exit;

my $proportion = shift || 99;

$proportion /= 100;
my ( $max, $bouncy ) = (1, 0);

while ( $bouncy / $max < $proportion ) {
    $max++;
    $bouncy++ if bouncy $max;
#    print "$bouncy/$max=", $bouncy / $max, "\n";
#    last if $max == 21780;
}

print "$max\n";
