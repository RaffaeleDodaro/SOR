#!/usr/bin/perl
die "pochi parametri" if($#ARGV<0);
$path=shift or die("manca path");
$intero=shift or die("manca intero");
$stringa=shift or die("manca la stringa");
die "troppi parametri" if($#ARGV>=0);
@risultato=qx(ls -lR $path|egrep '$stringa');
my $somma=0;
%hash;

foreach(@risultato){
    if(m/\w+\s+(\d+\d+)\s+\w+/)
    {
        if($1 >= $intero)
        {
            $hash{$_}=$1;
            $somma+=$1;
        }
    }
}
open(my $fh,">","results.out") or die "non lo apro";
foreach $size (sort{$hash{$a}<=>$hash{$b} or $a cmp $b} keys %hash)
{
    print $fh "$size --> $hash{$size}.\n";
}
print $fh "------------------------------\nDimensione totale: $somma\n";
close $fh or die "non lo chiuso";