#!/usr/bin/perl

use warnings;
use strict;

sub add {
    my ($f1, $f2) = @_;
    my $max = @$f1 > @$f2 ? @$f1 : @$f2;
    my $c = 0;
    for ( my $i = 0; $i < $max; $i++ ) {
        my $s = ($f1->[$i] || 0) + ($f2->[$i] || 0) + $c;
        $f1->[$i] = $s % 10;
        $c = $s > 9 ? 1 : 0;
    }
    $f1->[$max] = 1 if $c;
}

sub panfront {
    return pan( map{$_[0][$_]}(0..8) );
}

sub panback {
    return pan( map{$_[0][$_]}(-9..-1) );
}

sub pan {
    my %seen;
    for ( @_ ) {
        return 0 unless $_;
        return 0 if $seen{$_}++;
    }
    return 1;
}

my ($f1, $f2, $fib) = ([1], [1], 2);

$SIG{'INT'} = sub { print "\nf1: ",scalar(@$f1),"\nf2: ", scalar(@$f2), "\n" };

while (1) {
    $fib++;
    add($f1, $f2);
    last if panfront($f1) && panback($f1);
    $fib++;
    add($f2, $f1);
    last if panfront($f2) && panback($f2);
}

print "$fib\n";
