#!/bin/bash/perl
# Dato in input una stringa X ed una lettera Y, contare il numero di
# occorrenze di Y nella stringa X.
use strict; 
print"inserisci stringa\n";
my $stringa=<STDIN>;
chomp($stringa);

print"inserisci lettera\n";
my $lettera=<STDIN>;
chomp($lettera);

my $conto=0;
my @chars=split '',$stringa;
while(@chars)
{    
    if ($chars[0] eq $lettera)
    {
        $conto=$conto+1;
    }  
    shift @chars;
}
print "\nil numero di occorrenze di ". $lettera . " è: " . $conto."\n";