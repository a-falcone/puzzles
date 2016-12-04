#!/usr/bin/perl

use strict;
use warnings;
use bigint;

#The 5-digit number, 16807=7^(5), is also a fifth power. Similarly, the 9-digit number, 134217728=8^(9), is a ninth power.

#How many n-digit positive integers exist which are also an nth power?

my ($p, $a) = (1, 0);

while( $p < 50 ) {
  my $b = 0;
  while ( length $b**$p <= $p ) {
    $b++;
    if ( length $b**$p == $p ) {
      print "$b^$p=", $b**$p, "\n";
      $a++;
    }
  }
  $p++;
}

print "$a\n";
