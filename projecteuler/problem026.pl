#!/usr/bin/perl

use strict;
use warnings;
use bigint;
#Description goes here

my ($period, $max, $target) = (0, 0, 1000);

while ( $target > $period ) {
  int (10**2000 / $target) =~ /(.+?)\1/;
  if ( length $1 > $period ) {
    $period = length $1;
    $max = $target;
  } 
  $target--;
}

print "$max\n";
