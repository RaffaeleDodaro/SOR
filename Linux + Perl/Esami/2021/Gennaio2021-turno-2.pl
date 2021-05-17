#!/usr/bin/perl
die $! if($#ARGV<0 or $#ARGV>2);
$path=shift or die $!;
$par=shift or die $!;
$stringa=shift or die $!;
%hash;
$somma=0;
if($par =~ m/-g/)
{
    foreach(qx{ls -lR $path})
    {

        if(m/.+\s\d\s\S+\s(\S+)+\s+(\d+)\s\w+\s\d+\s\d+\:\d+\s+(\N+)/)
        {
            $user=$1;
            $dim=$2;
            $perc=$3;
            if($perc=~m/$stringa/)
            {
                $hash{$user}+=$dim;
                $somma+=$dim;
            }
        }
    }
}
elsif($par =~ m/-u/)
{
    foreach(qx{ls -lR $path})
    {
        if(m/.+\s\d\s(\S+)\s\S+\s+(\d+)\s\w+\s\d+\s\d+\:\d+\s+(\N+)/)
        {
            $user=$1;
            $dim=$2;
            $perc=$3;
            if($perc=~m/$stringa/)
            {
                $hash{$user}+=$dim;
                $somma+=$dim;
            }
        }
    }
}
else {die $!;}
open($fh,">","results.out")or die $!;
foreach(sort{$hash{$b}<=>$hash{$a} or $a cmp $b} keys %hash )
{
    print $fh "$_ --> $hash{$_}\n";
}
print $fh "Dimensione totale: $somma\n";
close $fh or die $!;