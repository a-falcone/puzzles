#!/usr/bin/perl

use strict;
use warnings;

#In the game, Monopoly, the standard board is set up in the following way:
#00 01 02  03 04 05 06 07  08 09 10
#GO A1 CC1 A2 T1 R1 B1 CH1 B2 B3 JAIL
#39                              11
#H2                              C1
#38                              12
#T2                              U1
#37                              13
#H1                              C2
#36                              14
#CH3                             C3
#35                              15
#R4                              R2
#34                              16
#G3                              D1
#33                              17
#CC3                             CC2
#32                              18
#G2                              D2
#31                              19
#G1                              D3
#30  29 28 27 26 25 24 23 22  21 20
#G2J F3 U2 F2 F1 R3 E3 E2 CH2 E1 FP
#
#A player starts on the GO square and adds the scores on two 6-sided dice to determine the number of squares they advance in a clockwise direction. Without any further rules we would expect to visit each square with equal probability: 2.5%. However, landing on G2J (Go To Jail), CC (community chest), and CH (chance) changes this distribution.
#
#In addition to G2J, and one card from each of CC and CH, that orders the player to go directly to jail, if a player rolls three consecutive doubles, they do not advance the result of their 3rd roll. Instead they proceed directly to jail.
#
#At the beginning of the game, the CC and CH cards are shuffled. When a player lands on CC or CH they take a card from the top of the respective pile and, after following the instructions, it is returned to the bottom of the pile. There are sixteen cards in each pile, but for the purpose of this problem we are only concerned with cards that order a movement; any instruction not concerned with movement will be ignored and the player will remain on the CC/CH square.
#
#Community Chest (2/16 cards):
#   Advance to GO
#   Go to JAIL
#Chance (10/16 cards):
#   Advance to GO
#   Go to JAIL
#   Go to C1
#   Go to E3
#   Go to H2
#   Go to R1
#   Go to next R (railway company)
#   Go to next R
#   Go to next U (utility company)
#   Go back 3 squares.
#
#The heart of this problem concerns the likelihood of visiting a particular square. That is, the probability of finishing at that square after a roll. For this reason it should be clear that, with the exception of G2J for which the probability of finishing on it is zero, the CH squares will have the lowest probabilities, as 5/8 request a movement to another square, and it is the final square that the player finishes at on each roll that we are interested in. We shall make no distinction between "Just Visiting" and being sent to JAIL, and we shall also ignore the rule about requiring a double to "get out of jail", assuming that they pay to get out on their next turn.
#
#By starting at GO and numbering the squares sequentially from 00 to 39 we can concatenate these two-digit numbers to produce strings that correspond with sets of squares.
#
#Statistically it can be shown that the three most popular squares, in order, are JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and GO (3.09%) = Square 00. So these three most popular squares can be listed with the six-digit modal string: 102400.
#
#If, instead of using two 6-sided dice, two 4-sided dice are used, find the six-digit modal string.

my %special = ( 2 => \&cc, 7 => \&ch, 17 => \&cc, 22 => \&ch, 30 => \&jail, 33 => \&cc, 36 => \&ch );

sub jail { return 10; }
sub go { return 0; }
sub c1 { return 11; }
sub e3 { return 24; }
sub h2 { return 39; }
sub r1 { return 5; }
sub r { return $_[0] < 5  ? 5 :
               $_[0] < 15 ? 15 :
               $_[0] < 25 ? 25 :
                            35 }
sub u { return $_[0] < 12 ? 12 : 28 }
sub back3 { return ( ( $_[0] - 3 ) % 40 )}
sub noop { return $_[0] }

{
    my @cc = ( ( \&noop ) x 14, \&go, \&jail );
    sub ccinit {
        my $i = @cc;
        while ( $i-- ) {
            my $j = int rand ($i+1);
            @cc[$i,$j] = @cc[$j,$i];
        }
    }

    my $i = 0;
    sub cc {
        my $pos = shift;
        my $sub = $cc[$i++ % 16];
        return $sub->($pos);
    }
}

{
    my @ch = ( ( \&noop ) x 6, \&go, \&jail, \&c1, \&e3, \&h2, \&r1, \&r, \&r, \&u, \&back3 );
    sub chinit {
        my $i = @ch;
        while ( $i-- ) {
            my $j = int rand ($i+1);
            @ch[$i,$j] = @ch[$j,$i];
        }
    }

    my $i = 0;
    sub ch {
        my $pos = shift;
        my $sub = $ch[$i++ % 16];
        return $sub->($pos);
    }
}

sub roll {
    my $sides = $ARGV[0] || 4;
    my $d1 = int rand( $sides ) + 1;
    my $d2 = int rand( $sides ) + 1;
    return ($d1 + $d2, $d1 == $d2);
}

my ( $doubles, $pos, @spaces ) = ( 0, 0 );
$spaces[30] = 1;
for (1..10) {
    print "game $_ started\n";
    ccinit;
    chinit;
    for ( my $turn = 1; $turn <= 5e6; $turn++ ) {
        my ($r, $d) = roll;
        if ($d) {
            if ( $doubles == 2 ) {
                $doubles = 0;
                $pos = jail;
            } else {
                $doubles++;
                $pos += $r;
            }
        } else {
            $doubles = 0;
            $pos += $r;
        }
        $pos %= 40;
    
        if (exists $special{$pos}) {
            my $sub = $special{$pos}->($pos);
            if ( ref $sub ) {
                $pos = $sub->($pos);
            } else {
                $pos = $special{$pos}->($pos);
            }
        }
    
        $pos %= 40;
        print "30\n" if $pos == 30;
        $spaces[$pos]++;
    }
    print "game $_ ended\n";
}
print "$_: $spaces[$_]\n" for sort {$spaces[$b] <=> $spaces[$a]} (0 .. $#spaces);
