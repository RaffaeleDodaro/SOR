#!/usr/bin/perl
$path=shift or die $!;
$par=shift or die $!;
die $! if($par ne "-g" and $par ne "-u");
$str=shift or die $!;
@file=qx(ls -laR | grep "$str");
%hash;
$somma=0;
foreach(@file){
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
    else {
        die $!;
    }
}
open(my $fh,">","results.out");
@sorted=sort{$hash{$b}<=>$hash{$a} or $a cmp$ b} keys %hash;
foreach(@sorted)
{
    print $fh "$_ $hash{$_}\n";
}
print $fh "---------------\n";
print $fh "Spazio totale occupato: $somma\n";
close $fh;