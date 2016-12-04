#!/usr/bin/perl

use strict;
use warnings;

#The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
#
#Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
#HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

my %products;

my %digits;

for ( 1 .. 9 ) {
  $digits{ $_ } = 1;
}

foreach my $a ( keys %digits ) {
  delete $digits{ $a };
  foreach my $b ( keys %digits ) {
    delete $digits{ $b };
    foreach my $c ( keys %digits ) {
      delete $digits{ $c };
      foreach my $d ( keys %digits ) {
        delete $digits{ $d };
        foreach my $e ( keys %digits ) {
          delete $digits{ $e };
          my $tmp1 = eval "$a * $b$c$d$e";
          my $tmp2 = eval "$a$b * $c$d$e";
          my ( $good1, $good2 ) = ( length $tmp1 == 4, length $tmp2 == 4 );
          foreach my $check ( keys %digits ) {
            $good1 &= 0 if $tmp1 !~ /$check/;
            $good2 &= 0 if $tmp2 !~ /$check/;
          }
            $products{ $tmp1 } = 1 if $good1;
            $products{ $tmp2 } = 1 if $good2;
          $digits{ $e } = 1;  
        }
        $digits{ $d } = 1;
      }
      $digits{ $c } = 1;
    }
    $digits{ $b } = 1;
  }
  $digits{ $a } = 1;
}

my $answer = 0;
$answer += $_ foreach keys %products;
printf "$answer\n";
