#!/bin/bash/perl
#open(my $file, "<" , "i_promes.txt");
my @righe = <STDIN>;
open(my $final,">","final.txt") or die "$!";

my $stringa = "@righe";
$stringa =~ s/Renzo/Lucia/;
$stringa =~ s/Renzo/Innominato/g;
print $final $stringa."\n";
close $final;