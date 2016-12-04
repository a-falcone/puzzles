#!/usr/bin/perl

use strict;
use warnings;

#In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
#
#  1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
#
#  It is possible to make £2 in the following way:
#
#  1x£1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
#
#  How many different ways can £2 be made using any number of coins?

my $answer = 0;
my $total = 200;

for ( my $L2 = int ($total / 200); $L2 >= 0; $L2-- ) {
  for ( my $L1 = int ( ($total - 200 * $L2) / 100 ); $L1 >= 0; $L1-- ) {
    for ( my $p50 = int ( ($total - 200 * $L2 - 100 * $L1) / 50 ); $p50 >= 0; $p50-- ) {
      for ( my $p20 = int ( ($total - 200 * $L2 - 100 * $L1 - 50 * $p50) / 20 ); $p20 >= 0; $p20-- ) {
        for ( my $p10 = int ( ($total - 200 * $L2 - 100 * $L1 - 50 * $p50 - 20 * $p20) / 10 ); $p10 >= 0; $p10-- ) {
          for ( my $p5 = int ( ($total - 200 * $L2 - 100 * $L1 - 50 * $p50 - 20 * $p20 - 10 * $p10) / 5 ); $p5 >= 0; $p5-- ) {
            for ( my $p2 = int ( ($total - 200 * $L2 - 100 * $L1 - 50 * $p50 - 20 * $p20 - 10 * $p10 - 5 * $p5) / 2 ); $p2 >= 0; $p2-- ) {
              $answer++;
            }
          }
        }
      }
    }
  }
}

print "$answer\n";
