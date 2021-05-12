#!/usr/bin/perl
die $! if ($#ARGV < 0 or $#ARGV > 0);
$path = shift || die $!;
%utenteConto;
%utenteIpPorta;
foreach(qx{cat $path})
{
    if(m/Invalid user (.+) from (\d+\.\d+\.\d+\.\d+) port (\d+)/)
    {
        $utenteConto{$1}+=1;
        $utenteIpPorta{$1} = "$2:$3\n       $utenteIpPorta{$1}";
    }
}
open(my $fileNuovo,">","filenuovo.txt") || die "non creato";
foreach(sort{$utenteConto{$b}<=> $utenteConto{$a} || $a cmp $b} keys %utenteConto){
    print $fileNuovo "$_ --> $utenteConto{$_}\n       $utenteIpPorta{$_}";
}
close $fileNuovo || die $!;