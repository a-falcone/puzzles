#!/usr/bin/perl

use strict;
use warnings;

#The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
#
#Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#
#(Please note that the palindromic number, in either base, may not include leading zeros.)

my $answer = 0;

for ( my $i = 1; $i < 1000000; $i += 2 ) {
  if ( $i == reverse $i ) {
    my $tmp = sprintf "%b", $i;
    $answer += $i if $tmp == reverse $tmp;
  }
}

print "$answer\n";
