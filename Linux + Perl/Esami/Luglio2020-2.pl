#!/usr/bin/perl
$path=shift || die $!;
@file=qx(cat $path);

%utenteConto;
%utenteIpPorta;
foreach(@file)
{
    if(m/ Invalid user (.+) from (\d+\.\d+\.\d+\.\d+) port (\d+)/)
    {
        $utenteConto{$1}+=1;
        %utenteIpPorta{$1}="$2.':'.$3 \n %utenteIpPorta{$1}";
    }
}
open(my $fileNuovo,">","filenuovo.txt") || die $!;
@sorted = sort($utenteConto{$b}<=> $utenteConto{a} || $a cmp $b} keys %utenteConto);
foreach(@sorted){
    print $fileNuovo "$_ --> $utenteConto{$_}\n";
    print $fileNuovo "$_  $utenteIpPorta{$_}";
}
close $fileNuovo;