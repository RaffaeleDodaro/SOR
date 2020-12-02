#Creare uno script che modelli il funzionamento di una rubrica
#telefonica
#Ad ogni persona, identificata tramite nome e cognome, è attribuito
#un unico numero di telefonica
#Stampare in output per ogni persona il proprio numero di telefono
#e la lista univoca delle persone in rubrica

#!/bin/bash/perl
use List::MoreUtils qw(uniq);
my %persone =('A Cognome'=> '1',
              'B Cognome'=> '2',
              'C Cognome'=> '3');
my @nomeCognome = keys %persone;
my @nCUniq= uniq @nomeCognome;

my @numeroTelefono = values %persone;

for(my $i=0; $i<@nomeCognome; $i++)
{
    print "nome: ".@nomeCognome[$i]." numero: ".@numeroTelefono[$i]."\n";
}