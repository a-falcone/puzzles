#!/usr/bin/perl

use strict;
use warnings;

#Some positive integers n have the property that the sum [ n + reverse(n) ] consists entirely of odd (decimal) digits. For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and 904 are reversible. Leading zeroes are not allowed in either n or reverse(n).
#
#There are 120 reversible numbers below one-thousand.
#
#How many reversible numbers are there below one-billion (10^9)?

my $limit = shift || 1e9;

my $answer = 0;

sub reversible {
    return ( $_[0] + scalar reverse $_[0] ) !~ /[02468]/;
}

for ( my $i = 2; $i < $limit; $i += 2 ) {
    if ( $i =~ /^[2468]/ ) {
        $i += 10**(length($i) - 1);
    }
    $i += 2 if $i =~ /0$/;
    $answer += 2 if reversible( $i );
}

print "$answer\n";
