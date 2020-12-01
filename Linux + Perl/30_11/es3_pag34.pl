#!/bin/bash/perl

print"inserisci stringa 1\n";
my $s1=<>;
chomp($s1);

print"inserisci stringa 2\n";
my $s2=<>;
chomp($s2);

my $sConc=$s1.$s2;

print "concatenata: ".$sConc;
print "\nlunghezza: ".length $sConc;
my $secondaMeta = (length $sConc)/2;
print "\nseconda metà: " . substr($sConc,$secondaMeta,$secondaMeta) . "\n";