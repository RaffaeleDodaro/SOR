#!/usr/bin/perl
$formati=shift or die $!;
$path = ".";
$path = shift or die $! if ($#ARGV >=0);
$f=$1 if($formati =~ m/--format=(.+)/);
@array=split(',', $f);
@file=qx(du -ka $path);
%hash;
$somma=0;
foreach($i=0;$i<@array;$i++)
{
    foreach(@file)
    {
        if(m/(\d+)\s+.+\.($array[$i])/)
        {
            $hash{$array[$i]}+=$1;
            $somma+=$1;
        }
    }
}

@sorted=sort{$hash{$b}<=>$hash{$a} or $a cmp $b} keys % hash;
foreach(@sorted)
{
    print "Estensione: $_    $hash{$_}Kb\n";
}
open($fh,">","du.out");
print $fh "$path $somma";
close($fh);