#!/usr/bin/perl

use strict;
use warnings;

#It is possible to write five as a sum in exactly six different ways:
#
#4 + 1
#3 + 2
#3 + 1 + 1
#2 + 2 + 1
#2 + 1 + 1 + 1
#1 + 1 + 1 + 1 + 1
#
#How many different ways can one hundred be written as a sum of at least two positive integers?

my %p = (1,{1,1});

sub p {
    my $p = shift;
    return $p{$p} if exists $p{$p};
    my %part = ($p,1);
    for ( my $i = $p - 1; $i >= 1 ; $i-- ) {
        for ( keys %{p($p-$i)} ) {
            $part{ join(",", (sort{$b<=>$a}( $i, split(/,/, $_) ) ) ) }++;
        }
    }
    $p{$p} = \%part;
    return \%part;
}

use Data::Dumper;
my $stuff = shift;
print scalar( keys %{p($stuff)}) - 1, "\n";
