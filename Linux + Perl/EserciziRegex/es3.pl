#!/bin/bash/perl
my @righe=<STDIN>;
my $stringa = "@righe";
$stringa =~ tr/a-z/A-Z/;
print $stringa."\n";