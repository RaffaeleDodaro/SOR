#!/usr/bin/perl
$path=shift or die("manca path");
$intero=shift or die("manca intero");
$stringa=shift or die("manca la stringa");
die "troppi parametri" if($#ARGV>=0);
@risultato=qx(ls -l -R $path|egrep '$stringa');
my $somma=0;
%hash;
open(my $fh,">","results.out") or die "non lo apro";

for(my $i=0;$i<@risultato;$i++){
    if(@risultato[$i] =~ m/\w+\s+(\d+\d+)\s+\w+/)
    {
        if($1 >= $intero)
        {
            $hash{@risultato[$i]}=$1;
            $somma+=$1;
        }
    }
}
foreach $size (sort{$hash{$a}<=>$hash{$b} or $a cmp $b} keys %hash)
{
    print $fh "$size --> $hash{$size}.\n";
}
print $fh "------------------------------";
print $fh "Dimensione totale: $somma\n";
close $fh;