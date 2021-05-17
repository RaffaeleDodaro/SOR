#!/usr/bin/perl
die $! if($#ARGV<0 or $#ARGV>2);
$path=shift or die $!;
$intero=shift or die $!;
$stringa=shift or die $!;
%hash;
$somma=0;
foreach(qx{ls -lR $path})
{
    if(m/.+\s\d+\s\w+\s\w+\s+(\d+)\s\w+\s+\d+\s\d+\:\d+\s(\N+)/)
    {
        $dim=$1;
        $nome=$2;
        if($2 =~ m/$stringa/)
        {
            if($dim>=$intero)
            {
                $somma+=$dim;
                $hash{$nome} = $dim;
            }
        }
    }
}
open($fh,">","results.out") or die $!;
foreach(sort{$hash{$b}<=>$hash{$a} or $a cmp $b} keys %hash)
{print $fh "$_ --> $hash{$_}\n";}
print $fh "------------------------------\nDimensione totale: $somma\n";
close $fh or die "non lo chiudo";