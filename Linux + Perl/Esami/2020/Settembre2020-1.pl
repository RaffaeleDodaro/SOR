#!/usr/bin/perl
die $! if($#ARGV<0 or $#ARGV>1);
$risorsa = shift or die $!;
die $! if($risorsa ne "-c" or $risorsa ne "-m");
$utente=shift or die $!;
%hash;
foreach(qx{top -n1 -b})
{
    if($risorsa eq "-c")
    {
        $hash{$1}+=$2 if(m/\d+\s(\S+).+\w\s+(\d+\.\d)\s+(\d+\.\d)\s/);
    }
    else
    {
        $hash{$1}+=$3 if(m/\d+\s(\S+).+\w\s+(\d+\.\d)\s+(\d+\.\d)\s/);        
    }
}
open($fh,">","stat.log") or die $!;
print $fh "$utente --> $hash{$utente}\n";
foreach(sort{$hash{$b}<=>$hash{$a}} keys %hash)
{
    print $fh "$_ --> $hash{$_}\n";
    last;
}
close $fh or die $!;
