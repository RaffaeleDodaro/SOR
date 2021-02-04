#!/usr/bin/perl
print "inserisci opzione";
$opzione=<STDIN>;

die $! if($#ARGV >=0);

%rubrica;
$nome;
$cognome;
$telefono;
$check=0;
while($opzione ne "-k"){
    if($opzione eq "-a")
    {
        print "inserisci nome,cognome,telefono";
        $informazioni = <STDIN>;
        if($informazioni=~m/\s(\w+),(\w+),(\d+)/)
        {
            $nome=$1;
            $cognome=$2;
            $telefono=$3;
            while(length($telefono)<10)
            {
                print "inserisci numero telefono";
                $telefono=<STDIN>;
            }
        }
        while(my($n,$c)=each %rubrica)
        {
            if($n eq $nome and $c eq $cognome)
            {
                $check=1;
            }
        }
    }
    elsif($opzione eq "-d")
    {

    }
    elsif($opzione eq "-s")
    {

    }
    elsif($opzione eq "-e")
    {

    }
    elsif($opzione eq "-k")
    {

    }
    $opzione=<STDIN>;
}