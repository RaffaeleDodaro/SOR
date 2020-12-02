#!/usr/bin/perl

#Data una stringa in input, creare una subroutine che calcoli il suo
#complemento inverso.
use strict;
my $stringa=<STDIN>;
chomp $stringa;
calcolaInverso($stringa);

sub calcolaInverso( my $s)
{
    my @chars = split '',$stringa;
    for (my $i=$#chars;$i>=0;$i--)
    {
        print @chars[$i];
    }
    print "\n";
}