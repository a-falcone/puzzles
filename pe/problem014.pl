#!/usr/bin/perl

use strict;
use warnings;

#The following iterative sequence is defined for the set of positive integers:
#
#n -> n/2 (n is even)
#n -> 3n + 1 (n is odd)
#
#Using the rule above and starting with 13, we generate the following sequence:
#13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
#
#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
#Which starting number, under one million, produces the longest chain?
#
#NOTE: Once the chain starts the terms are allowed to go above one million.

my %depths = (1 => 1);

sub depth {
  my $i = $_[0];
  return $depths{$i} if defined $depths{$i};

  my @stack = ();

  while ( !defined $depths{$i} && $i > 1 ) {
    unshift @stack, $i;
    $i = ( $i % 2 == 0 ) ? $i / 2 : 3 * $i + 1;
  }

  my $j = $depths{$i} + 1;
  for (@stack) {
    $depths{$_} = $j;
    $j++;
  }

  return $depths{$_[0]};
}

my $maxdepth = 1;
my $answer = 1;

for ( my $target = 1; $target < 1000000; $target++ ) {
  my $howdeep = depth( $target );
  if ( $howdeep > $maxdepth ) {
    $answer = $target;
    $maxdepth = $howdeep;
  }
}

print "$answer\n";
