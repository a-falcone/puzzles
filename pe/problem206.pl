#!/usr/bin/perl

use strict;
use warnings;

#Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
#where each “_” is a single digit.

for ( my $i = int sqrt 19293949596979899; $i >= sqrt 10203040506070809; $i-- ) {
    if ( $i**2 =~ /1.2.3.4.5.6.7.8.9/ ) {
        print "${i}0\n";
        last;
    }
}
