#!/usr/bin/perl

use strict;
use warnings;

#All square roots are periodic when written as continued fractions and can be written in the form:
#It can be seen that the sequence is repeating. For conciseness, we use the notation √23 = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats indefinitely.
#
#The first ten continued fraction representations of (irrational) square roots are:
#
#√2=[1;(2)], period=1
#√3=[1;(1,2)], period=2
#√5=[2;(4)], period=1
#√6=[2;(2,4)], period=2
#√7=[2;(1,1,1,4)], period=4
#√8=[2;(1,4)], period=2
#√10=[3;(6)], period=1
#√11=[3;(3,6)], period=2
#√12= [3;(2,6)], period=2
#√13=[3;(1,1,1,1,6)], period=5
#
#Exactly four continued fractions, for N ≤ 13, have an odd period.
#
#How many continued fractions for N ≤ 10000 have an odd period?

my $answer = 0;
#my $ulimit = 10_000;
my $ulimit = 23;

for( my $i = 23; $i <= $ulimit; $i++ ) {
    next if int sqrt($i) == sqrt($i);
    if ( calc_period($i) % 2 == 1 ) {
        $answer++;
    }
}

#print "$answer\n";

sub calc_period {
    my %seen;
    my $i = shift;
    my( $a, $b ) = ( -int(sqrt $i), 1 );
    my $frac = -$a;
    print "√$i=\n";
    while( !defined $seen{"$a,$b"} ) {
        print "a=$a b=$b frac=$frac i=$i\n";
        $seen{"$a,$b"}++;
        $frac = int( $b / (sqrt($i) + $a) );
        ($a,$b) = ( ... , ($i - $a**2)/$b );
    }
    return scalar keys %seen;
}
