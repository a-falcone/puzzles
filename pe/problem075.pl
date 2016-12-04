#!/usr/bin/perl

use warnings;
use strict;

#It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle in exactly one way, but there are many more examples.
#
#12 cm: (3,4,5)
#24 cm: (6,8,10)
#30 cm: (5,12,13)
#36 cm: (9,12,15)
#40 cm: (8,15,17)
#48 cm: (12,16,20)
#
#In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle, and other lengths allow more than one solution to be found; for example, using 120 cm it is possible to form exactly three different integer sided right angle triangles.
#
#120 cm: (30,40,50), (20,48,52), (24,45,51)
#
#Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one integer sided right angle triangle be formed?

sub gcd {
    my ($i, $j) = @_;
    while ($i) {
        ($i,$j) = ($j%$i,$i);
    }
    return $j;
}

sub rp {
    return gcd(@_) == 1;
}

my $limit = shift || 1500000;
my $mlimit = sqrt($limit/2);
my %count;
my %seen;

for ( my $m = 2; $m <= $mlimit; $m++ ) {
    for ( my $n = 1; $n < $m; $n++ ) {
        next unless ( $n + $m ) % 2;
        next unless rp($n, $m);
        for ( my $k = 1; 2 * $k * $m * ( $m + $n ) <= $limit; $k++ ) {
            my $c = $k * ( $m**2 + $n**2 );
            my $d = $k * ( 2 * $n * $m );
            my $e = $k * ( $m**2 - $n**2 );
            if( !$seen{join ",", sort ($c,$d,$e)} ++ ) {
                $count{2 * $k * $m * ( $m + $n )}++;
            }
        }
    }
}

my $answer = grep {$_ == 1} values %count;
print "Answer: $answer\n";
