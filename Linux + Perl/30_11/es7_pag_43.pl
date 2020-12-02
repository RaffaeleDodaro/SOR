#!/bin/bash/perl

# (1) Creare un array associativo composto dai seguenti valori: 
#       A => 1, B => 45, C => 5

# (2) Ordinare in maniera crescente i valori dell’array associativo
# utilizzando prima l’operatore compare per il contesto numeric e
# successivamente quello per il contesto string.

# (3) Quali sono le differenze nell’output ? E perchè ?

# (4)Aggiungere all’array associativo i valori: D => 45, E => 10, F => 1

# (5)Ordinare e stampare prima in ordine crescente i valori contenuti
# nell’array associativo e a parità di valore ordinare
# lessicograficamente sulle chiavi

#(1)array associativo=struttura dati che associa una chiave ad una variabile scalare
my %array = (
     A => '1',
     B => '45',
     C => '5');

#2.1 ordinare in maniera crescente i valori dell’array associativo
# utilizzando prima l’operatore compare per il contesto numeric
print("array ordinato numericamente\n");
foreach $number(sort{$array{$a}<=>$array{$b}} keys %array)
{
    print "$number - $array{$number}.\n"
}
#risposta viene sempre stampato in ordine corretto(penso):
# A - 1.
# C - 5.
# B - 45.



#2.2 ordinare in maniera crescente i valori dell’array associativo per il contesto string.
print("array ordinato secondo string\n");
foreach $letter(sort{$array{a}<=>$array{$b}} keys %array)
{
   print("$letter - $array{$letter}.\n");
}
#risposta: non sempre stampa abc penso in base a come vengono gestiti in memoria dato che è viene usato l'algoritmo hash?
# C - 5.
# A - 1.
# B - 45.



# (4)Aggiungere all’array associativo i valori: 
#D => 45, 
#E => 10, 
#F => 1
$array{D} = '45';
$array{F} = '1';
$array{E} = '10';
print("\naggiungo e riordino numericamente\n");
push %array(D=>'45',E=>'10',F=>'1');
foreach $number(sort{$array{$a}<=>$array{$b}} keys %array)
{
    print "$number - $array{$number}.\n"
}

print "stampo array finale: \n";
my @chiavi = keys %array;
my @valori = values %array;

for(my $i=0; $i<@chiavi; $i++)
{
    print @chiavi[$i]." => ".@valori[$i]."\n";
}