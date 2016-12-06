#!/usr/bin/perl

use strict;
use warnings;

#The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.
#
#Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

#tools

sub is_prime {
  return 1 if $_[0] > 1 && $_[0] < 4;
  return 0 if $_[0] % 2 == 0;
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

sub makes_primes {
  return is_prime( "$_[0]$_[1]" ) && is_prime( "$_[1]$_[0]" );
}

#main
my $working = 3;
my @primea = (3);
my $limit = 10000;

CANDIDATE: while ( $working < $limit ) {
  $working += 2;
  my $i;
  for ( $i = 0; $primea[$i] <= sqrt $working ; $i++ ) {
    next CANDIDATE if ( $working % $primea[$i] == 0 );
  }
  push ( @primea, $working );
}

foreach my $modreject (2, 1) {
  for ( my $a = 0; $a <= $#primea - 4; $a++ ) {
    next if $primea[$a] % 3 == $modreject;

    for ( my $b = $a + 1; $b <= $#primea - 3; $b++ ) {
      next if $primea[$b] % 3 == $modreject;
      next unless makes_primes( $primea[$b], $primea[$a] );

      for ( my $c = $b + 1; $c <= $#primea - 2; $c++ ) {
        next if $primea[$c] % 3 == $modreject;
        next unless makes_primes( $primea[$c], $primea[$a] ) &&
                    makes_primes( $primea[$c], $primea[$b] );

        for ( my $d = $c + 1; $d <= $#primea - 1; $d++ ) {
          next if $primea[$d] % 3 == $modreject;
          next unless makes_primes( $primea[$d], $primea[$a] ) &&
                      makes_primes( $primea[$d], $primea[$b] ) &&
                      makes_primes( $primea[$d], $primea[$c] );

          for ( my $e = $d + 1; $e <= $#primea; $e++ ) {
            next if $primea[$e] % 3 == $modreject;
            next unless makes_primes( $primea[$e], $primea[$a] ) &&
                        makes_primes( $primea[$e], $primea[$b] ) &&
                        makes_primes( $primea[$e], $primea[$c] ) &&
                        makes_primes( $primea[$e], $primea[$d] );
            
            print $primea[$a] + $primea[$b] + $primea[$c] + $primea[$d] + $primea[$e];
            print ": $primea[$a] + $primea[$b] + $primea[$c] + $primea[$d] + $primea[$e]";
            print "\n";
          }
        }
      }
    }
  }
}
