#!/bin/bash/perl
print "Inserisci il numero: ";
my $numero = <>;
chomp $numero;


if($numero =~ /^[a-fA-F\d]+$/) # "([a-fA-F]*|[0-9]*)")\da-fA-F
{
    print "il numero $numero e' esadecimale\n";
}
else
{
    print "il numero $numero non e' esadecimale\n";
}