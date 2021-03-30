#!/bin/bash/perl
@pid;
print("inserisci pid: \n");
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
    while(my $line=<$fh>){
        
        if($line=~m/(?i)NAME:\s+(\w+)/)
        {
            $nome=$1;
        }
        if($line=~m/(?i)VmPeAK:\s+(\d+)/)
        {
            $nomeVmPeak{$nome}+=$1;
        }
    }
    close $fh;
}

@sorted=sort{$nomeVmPeak{$b} <=> $nomeVmPeak{$a}} keys %nomeVmPeak;
print "max: $sorted[$0] --> $nomeVmPeak{$sorted[$0]}\n";
print "min: $sorted[@sorted-1] --> $nomeVmPeak{$sorted[@sorted-1]}\n";
qx(kill -9 $pid[0]);