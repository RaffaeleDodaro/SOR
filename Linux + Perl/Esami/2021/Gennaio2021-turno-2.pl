#!/usr/bin/perl
$path=shift or die $!;
$parametro=shift or die $!;
$stringa=shift or die $!;
die $! if($#ARGV>0);

open($fh,">","results.out");
$sommaTotale=0;
if($parametro eq "-g"){
    @file=qx(ls -lR $path | egrep "$stringa"|awk '{print $4}' | sort);
    %gruppoSize;
    
    foreach(@file)
    {
        if(m/-\w+\s?\d\s?\w+\s+(\w+)\s+(\d+)\s+/)
        {
            $gruppoSize{$1}+=$2;
            $sommaTotale+=$2;
        }
    }
    @sorted=sort{ $gruppoSize{$b}<=>$gruppoSize{$a} or {$a}cmp{$b}} keys %gruppoSize;
    foreach(@sorted)
    {
        print $fh "$_ --> $gruppoSize{$_}";
    }
}
elsif($parametro eq "-u"){
    %utenteSize;
    @file=qx(ls -lR $path | egrep "$stringa"|awk '{print $3}' | sort);
    foreach(@file)
    {
        if(m/-\w+\s?\d\s?(\w+)\s+\w+\s+(\d+)\s+/)
        {
            $utenteSize{$1}+=$2;
            $sommaTotale+=$2;
        }
    }
    @sorted=sort{ $utenteSize{$b}<=>$utenteSize{$a} or {$a}cmp{$b}} keys %utenteSize;
    foreach(@sorted)
    {
        print $fh "$_ --> $utenteSize{$_}";
    }
}
print $fh "\nsomma totale --> $sommaTotale";
close $fh;