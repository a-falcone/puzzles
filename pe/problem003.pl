#!/usr/bin/perl

use strict;
use warnings;

#The prime factors of 13195 are 5, 7, 13 and 29.
#
#What is the largest prime factor of the number 600851475143 ?

my $sum = shift || 600851475143;
my $max = 1;
while ( $sum % 2 == 0) {
    $sum /= 2;
    $max = 2;
    print "2 is a factor. $sum is the new target.\n";
}
for ( my $i = 3; $i <= sqrt($sum); $i+=2) {
  if ( $sum % $i == 0 ) {
    $sum /= $i;
    $max = $i;
    print "$i is a factor. $sum is the new target.\n";
    $i = 1;
  }
}
print "$sum\n";
