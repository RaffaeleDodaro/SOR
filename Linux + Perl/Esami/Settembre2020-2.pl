#!/usr/bin/perl
$formato=shift or die $!;
$percorso=".";
if($#ARGV >= 0)
{
    $percorso=shift or die $!;
}
# die $! if($#ARGV >= 0);
$formato=~m/=(.+)+/;
$formato=$1;

@listaFormati=split(/,/, $formato);

@daFiltrare=qx(du -ka $percorso);

%fileFiltrati;

for(my $i=0;$i<@listaFormati;$i++)
{
    $f=@listaFormati[$i];
    $somma=0;
    for(@daFiltrare)
    {
        if($_ =~ m/(\d+).+(\.$f)/)
        {
           $somma+=$1;
        }
    }
    $fileFiltrati{$f}=$somma;
}

open(my $fh,">","du.out");
$somma=0;
foreach $values(sort {$fileFiltrati{$b}<=>$fileFiltrati{$a} or ($a cmp $b)} keys %fileFiltrati )#or {$a cmp $b}
{
    $somma+=$fileFiltrati{$values};
    print "$values --> $fileFiltrati{$values}\n";
}
print $fh "$somma\n";
close $fh;