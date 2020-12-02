#!/bin/bash/perl
# Creare un array associativo ed inizializzarlo con i seguenti valori:
# A => 1, B => 2
use strict;
my %array=(A => '1',
           B => '2',
           C => '3');
           
# Stampare il valore associato alla chiave A
print "valore di a: ".$array{A} ."\n";

# Aggiungere altre 4 nuove coppie di chiave/valore nell’hash

# Cambiare il valore di A e settarlo a 0
$array{A} = '0';
print "nuovo valore di a: ".$array{A} ."\n";

# Controllare se esiste un elemento con chiave C
if($array{C})
    {print "chiave presente";}
else
    {print "chiave non presente";}

# Estrarre una sezione a scelta dei valori dell’hash
my @arrayEstratto=$array{B};
push @arrayEstratto, $array{A};

for(my $i=0;$i<@arrayEstratto;$i++)
{
    print "\narray estratto: ".%arrayEstratto[$i];
}
print"\n";

# Estrarre e salvare in un array tutte le chiavi e successivamente
# tutti i valori dell’hash
my @chiavi = keys %array;
my @valori = values %array;

# Stampare in output la dimensione dell’hash
print "dimensione hash prima dell'eliminazione: ".@chiavi."\n";

# Rimuovere dall’hash gli elementi con chiave A e B
delete $array{A};
delete $array{B};

print "stampo array finale: \n";
my @chiavi = keys %array;
my @valori = values %array;

for(my $i=0; $i<@chiavi; $i++)
{
    print @chiavi[$i]." => ".@valori[$i]."\n";
}