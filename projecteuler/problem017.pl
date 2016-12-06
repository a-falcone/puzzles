#!/usr/bin/perl

use strict;
use warnings;

#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

my @ones = qw( a one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen );
my @tens = qw( a b twenty thirty forty fifty sixty seventy eighty ninety );

sub spellit {
  my $number = $_[0];
  my $name = "";

  return $name if ( $number < 1 || $number > 19999 );

  if ( $number >= 1000 ) {
    $name = $ones[$number / 1000]." thousand ";
    $number %= 1000;
  }

  if ( $number >= 100 ) {
    $name .= $ones[$number / 100]." hundred";
    $number %= 100;
    $name .= " and " if $number > 0;
  }

  if ( $number >= 20 ) {
    $name .= $tens[$number / 10];
    $name .= " ".$ones[$number % 10] if $number % 10 > 0;
  } else {
    $name .= " ".$ones[$number % 20] if $number % 20 > 0;
  }

  $name =~ s/ +/ /g;
  $name =~ s/^ +| +$//;

  return $name;
}

my ($i, $word);
my $answer = 0;
for ($i = 1; $i <= 1000; $i++) {
  $word = &spellit( $i );
  $word =~ s/ //g;
  $answer += length( $word ); 
}

print "$answer\n";
