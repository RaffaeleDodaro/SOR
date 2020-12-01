#!/bin/bash/perl

#Creare uno script che presi 2 interi in input ne 
#mostri la somma, la differenza, il prodotto e il quoziente
print"inserisci n1:";
my $n1=<STDIN>;
print"inserisci n2:";
my $n2=<STDIN>;

print "operazioni senza uso subroutine\n";
my $somma=$n1+$n2;
my $sottr=$n1-$n2;
my $prod=$n1*$n2;
my $quoz=$n1/$n2;
print "somma: $somma\n";
print "sottr: $sottr\n";
print "prod:  $prod\n";
print "quoz:  $quoz\n";

print "\n\noperazioni con uso subroutine\n";
my $somma2=somma($n1,$n2);
print "somma: $somma2\n";

my $sottr2=sottrazione($n1,$n2);
print "sottrazione: $sottr2\n";

my $prod2=prodotto($n1,$n2);
print "prodotto: $prod2\n";

my $quoz2=quoziente($n1,$n2);
print "quoziente: $quoz2\n";


#Rimodellare lo stesso programma facendo però uso delle
#subroutine. Creare quindi una subroutine che prende come
#parametri 2 variabili per ogni operazione matematica da eseguire
sub somma(my $n1, my $n2)
{
    my $somma=$n1+$n2;
    return $somma;
}

sub sottrazione(my $n1, my $n2)
{
    my $sottrazione=$n1-$n2;
    return $sottrazione;
}

sub quoziente(my $n1, my $n2)
{
    my $quoziente=$n1/$n2;
    return $quoziente;
}

sub prodotto(my $n1, my $n2)
{
    my $prodotto=$n1*$n2;
    return $prodotto;
}




#Creare uno script che presi in input una sequenza di numeri
#positivi terminati da tappo "-1", li inserisca in un array e
#successivamente ne calcoli la somma
print "\n\ninserisci input parte 3\n";
my $input=<STDIN>;
my @array;
while($input != "-1")
{
    push @array,($input);
    print "inserisci input parte 3\n";
    $input=<STDIN>;
}

my $somma=0;
while(@array)
    $somma+=shift @array;

print "\nla somma dell'array è: ". $somma;
