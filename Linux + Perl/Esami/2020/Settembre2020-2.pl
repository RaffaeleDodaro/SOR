#!/usr/bin/perl
die $! if($#ARGV>0 or $#ARGV<0);
$formati=shift or die $!;
$path = ".";
$path = shift or die $! if ($#ARGV >=0);
$f=$1 if($formati =~ m/--formats=(.+)/);
%hash;
$somma=0;
foreach(split(',', $f))
{
    foreach(qx(du -ka $path))
    {
        if(m/(\d+)\s+.+\.($_)/)
        {
            $hash{$_}+=$1;
            $somma+=$1;
        }
    }
}
foreach(sort{$hash{$b}<=>$hash{$a} or $a cmp $b} keys % hash;)
{
    print "Estensione: $_    $hash{$_}Kb\n";
}
open($fh,">","du.out") or die $!;
print $fh "$path $somma";
close($fh) or die $!;