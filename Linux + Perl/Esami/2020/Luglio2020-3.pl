#!/bin/bash/perl
@pid;
$input=<STDIN>;
while($input ne "-1")
{
    push @pid,$input;
    $input=<STDIN>;
}
%nomeVmPeak;
foreach(@pid)
{
    chomp;
    open($fh,"<","/proc/$_/status") or die $!;
    $nome;
    while(<$fh>){
        $nome=$1 if(m/(?i)NAME:\s+(\w+)/);
        $nomeVmPeak{$nome}+=$1 if(m/(?i)VmPeAK:\s+(\d+)/);
    }
    close $fh or die $!;
}
@sorted=sort{$nomeVmPeak{$b} <=> $nomeVmPeak{$a}} keys %nomeVmPeak;
print "max: $sorted[$0] --> $nomeVmPeak{$sorted[$0]}\n";
print "min: $sorted[@sorted-1] --> $nomeVmPeak{$sorted[@sorted-1]}\n";
qx(kill -9 $pid[0]);