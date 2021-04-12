#!/usr/bin/perl

# NON FUNZIONA

open($fh,"<","./SOR-Traccia-GENNAIO-2016/auth.log") or die $!;
%hash;
%ipUtente;
while(<$fh>)
{
    if(m/Failed password for invalid user (\S+) from (\d+.\d+.\d+.\d+)/)
    {
        $hash{$2}+=1;
        $ipUtente{$2}=$1;
    }
}
close $fh or die $!;
open($fh2,">","nuovo.txt") or die $!;
foreach(keys %ipUtente)
{
    print $fh2 "$ipUtente{$_} --> $hash{$_}\n";
    #print "$hash{$_}\n";
}
foreach(keys %hash)
{
    print "$_ --> $hash{$_}\n";
}
close $fh2 or die $!;