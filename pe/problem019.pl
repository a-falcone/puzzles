#!/usr/bin/perl

use strict;
use warnings;

#You are given the following information, but you may prefer to do some research for yourself.
#
#  * 1 Jan 1900 was a Monday.
#  * Thirty days has September,
#    April, June and November.
#    All the rest have thirty-one,
#    Saving February alone,
#    Which has twenty-eight, rain or shine.
#    And on leap years, twenty-nine.
#  * A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#
#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

my @days = ( 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 );
my $dow = 2;
my $month = 0;
my $year = 1901;
my $answer = 0;

while ( $year < 2001 ) {
  $dow++ if ( $year % 4 == 0 || $month == 2 );
  $dow = ( $dow + $days[ $month ] ) % 7;
  $answer++ if $dow == 0;
  $month = ( $month + 1 ) % 12;
  $year++ if $month == 0;
}

print "$answer\n";
