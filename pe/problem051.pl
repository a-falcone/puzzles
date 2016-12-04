#!/usr/bin/perl

use strict;
use warnings;

#By replacing the 1st digit of *57, it turns out that six of the possible values: 157, 257, 457, 557, 757, and 857, are all prime.
#
#By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.
#
#Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

sub is_prime {
  return 0 if $_[0] % 3 == 0;
  my $limit = sqrt $_[0];
  for ( my $i = 5; $i < $limit; $i += 2 ) {
    return 0 if $_[0] % $i == 0;
    $i += 2;
    return 0 if $_[0] % $i == 0;
    $i += 2;
  }
  return 1;
}

my $seed = 1;

CANDIDATE: while( 1 ) {
  $seed += 2;
  next unless $seed =~ /([0123]).*\1.*\1./ && is_prime( $seed );
  my $found = 0;
  for ( my $i = 0; $i < 10; $i++ ) {
    my $tmp = $seed;
    $tmp =~ s/$1/$i/g;
    next if $tmp =~ /^0+/;
    $found++ if is_prime( $tmp );
  }
  if ( $found > 7 ) {
    print "$seed\n";
    last CANDIDATE;
  }
}

