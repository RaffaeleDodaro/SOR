#!/bin/bash/perl

##############################
#           ES1              #
##############################
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


##############################
#           ES2              #
##############################
# Aprire in modalità solo lettura il file /etc/passwd

# Stampare su un file output.txt (aperto in modalità solo scrittura)
# tutte le righe che contengono come nome utente "root"
# (NB.: Si può utilizzare la funziona split con delimitatore il carattere
# ":" oppure una espressione regolare)

# open(my $fh,"<","/etc/passwd") or die "non posso aprire passwd";
# qx(`rm output.txt`);
# open(my $fh1,">>","output.txt") or die "$!";

# while(my $line = <$fh>)
# {
#     chomp $line;
#     my @t = split /:/,$line;
#     for(my $i=0; $i<@t;$i++)
#     {
#         if(@t[$i] eq "root"){
#             print $fh1 "$line\n";
#             $i=@t;
#         }
#     }
# }
# close $fh;
# close $fh1;



##############################
#           ES3              #
##############################
# Creare uno script che prende come argomenti i nomi di almeno 2
# file di testo (es: perl script.pl file1 file2) e produca in
# output un unico file di testo chiamato merge.txt che contiene il
# contenuto di tutti i file passati precedentemente
open(my $file1,"<",$ARGV[0]) or die "$!";
open(my $file2,"<",$ARGV[1]) or die "$!";
open(my $file3,">","merge.txt") or die "$!";

while(my $line = <$file1>)
{
    chomp $line;
    print $file3 $line. "\n";
}

while(my $line = <$file2>)
{
    chomp $line;
    print $file3 $line . "\n";
}

close $file1;
close $file2;
close $file3;