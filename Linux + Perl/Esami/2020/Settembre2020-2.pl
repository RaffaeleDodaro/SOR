#!/usr/bin/perl
die $! if($#ARGV>0 or $#ARGV>1);
$formati=shift or die $!;
$formati=$1 if($formati =~ m/--formats=(.+)/);
$path = ".";
$path = shift or die $! if ($#ARGV ==0);
%hash;
$somma=0;
foreach(split(',', $f))
{
    $ext=$_;
    foreach(qx(du -ka $path))
    {
        $hash{$ext}+=$1 if(m/(\d+)\s+.+\.$_/)
    }
}
foreach(sort{$hash{$b}<=>$hash{$a} or $a cmp $b} keys % hash)
{
    print "Estensione: $_    $hash{$_}Kb\n";
    $somma+=$hash{$_};
}
open($fh,">","du.out") or die $!;
print $fh "$path $somma";
close($fh) or die $!;