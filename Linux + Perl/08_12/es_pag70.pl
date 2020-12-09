#!/bin/bash/perl

####    ES1    ####
#Aprire in modalità solo lettura il file /etc/passwd
#Scorrere il file e stampare tutte le righe pari

# @output = `cat /etc/passwd`;
# for(my $i=0; $i<@output;$i++)
# {
#     if($i % 2 == 0)
#     {
#         print ("riga $i: ". @output[$i]);
#     }
# }




####    ES2    ####
# Aprire in modalità solo lettura il file /etc/passwd

# Stampare su un file output.txt (aperto in modalità solo scrittura)
# tutte le righe che contengono come nome utente "root"
# (NB.: Si può utilizzare la funziona split con delimitatore il carattere
# ":" oppure una espressione regolare)

#MODO 1 PIU COMPLESSO
open(my $fh,"<","/etc/passwd") or die "non posso aprire passwd";
qx(`rm output.txt`);
open(my $fh1,">>","output.txt") or die "$!";

while(my $line = <$fh>)
{
    chomp $line;
    my @t = split /:/,$line;
    for(my $i=0; $i<@t;$i++)
    {
        if(@t[$i] eq "root"){
            print $fh1 "$line\n";
            $i=@t;
        }
    }
}
close $fh;
close $fh1;
