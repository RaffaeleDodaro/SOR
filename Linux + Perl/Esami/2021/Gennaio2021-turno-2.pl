#!/usr/bin/perl
die $! if (($#ARGV<0)or ($#ARGV>2));
$path=shift or die $!;
$par=shift or die $!;
$str=shift or die $!;
die $! if($par ne "-g" and $par ne "-u");
%hash;
$somma=0;
foreach(qx(ls -laR | grep "$str")){
    if($par =~m/-u/)
    {
        if(m/\d+\s+(\S+)\s+\S+\s+(\d+)\s+\w+\s+/)
        {
            $somma+=$2;
            $hash{$1}+=$2;
        }
    }
    elsif($par =~m/-g/)
    {
        if(m/\d+\s+\S+\s+(\S+)\s+(\d+)\s+\w+\s+/)
        {
            $somma+=$2;
            $hash{$1}+=$2;
        }
    }
}
open(my $fh,">","results.out") or die $!;
foreach(sort{$hash{$b}<=>$hash{$a} or $a cmp $b} keys %hash)
{
    print $fh "$_ $hash{$_}\n";
}
print $fh "---------------\nSpazio totale occupato: $somma\n";
close $fh or die $!;