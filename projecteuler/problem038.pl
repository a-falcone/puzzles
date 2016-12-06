#!/usr/bin/perl

use strict;
use warnings;

#Take the number 192 and multiply it by each of 1, 2, and 3:
#
#  192 * 1 = 192
#  192 * 2 = 384
#  192 * 3 = 576
#
#  By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
#
#  The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
#
#  What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

my $answer = 123456789;

for ( my $i = 9; $i < 10; $i++ ) {
  my ( $tmp, $j ) = ( "", 1 );
  while ( length $tmp < 9 ) {
    $tmp .= $i * $j;
    $j++;
  }
  if ( length $tmp == 9 && $tmp !~ /(.).*\1|0/ ) {
    $answer = $tmp > $answer ? $tmp : $answer;
  }
}

for ( my $i = 90; $i < 99; $i++ ) {
  my ( $tmp, $j ) = ( "", 1 );
  while ( length $tmp < 9 ) {
    $tmp .= $i * $j;
    $j++;
  }
  if ( length $tmp == 9 && $tmp !~ /(.).*\1|0/ ) {
    $answer = $tmp > $answer ? $tmp : $answer;
  }
}

for ( my $i = 901; $i < 988; $i++ ) {
  next if $i =~ /(.).*\1/;
  my ( $tmp, $j ) = ( "", 1 );
  while ( length $tmp < 9 ) {
    $tmp .= $i * $j;
    $j++;
  }
  if ( length $tmp == 9 && $tmp !~ /(.).*\1|0/ ) {
    $answer = $tmp > $answer ? $tmp : $answer;
  }
}

for ( my $i = 9012; $i < 9877; $i++ ) {
  next if $i =~ /(.).*\1/;
  my ( $tmp, $j ) = ( "", 1 );
  while ( length $tmp < 9 ) {
    $tmp .= $i * $j;
    $j++;
  }
  if ( length $tmp == 9 && $tmp !~ /(.).*\1|0/ ) {
    $answer = $tmp > $answer ? $tmp : $answer;
  }
}

print "$answer\n";
